from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from schemas.user import UserCreate, User, Token, TokenData, VerificationCodeRequest, VerificationCodeVerify
from models.user import User as UserModel
from database.connection import get_db
from utils.email import generate_verification_code, send_verification_email

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key"  # 替换为你的密钥
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(username=user.username, hashed_password=hashed_password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/send-verification-code")
def send_verification_code(request: VerificationCodeRequest, db: Session = Depends(get_db)):
    code = generate_verification_code()
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if user:
        user.verification_code = code
        user.code_expiration_time = datetime.utcnow() + timedelta(minutes=5)  # 设置验证码 5 分钟有效期
        db.commit()
    else:
        new_user = UserModel(
            email=request.email,
            verification_code=code,
            code_expiration_time=datetime.utcnow() + timedelta(minutes=5)  # 设置验证码 5 分钟有效期
        )
        db.add(new_user)
        db.commit()
    if send_verification_email(request.email, code):
        return {"message": "Verification code sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send verification code")
    

@router.post("/verify-verification-code")
def verify_verification_code(request: VerificationCodeVerify, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if not user or user.verification_code != request.code:
        raise HTTPException(status_code=400, detail="Invalid verification code")
    return {"message": "Verification code verified successfully"}

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    print(form_data)
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    print(form_data)
    return {"access_token": access_token, "token_type": "bearer"}

auth_router = router