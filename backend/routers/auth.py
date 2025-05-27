from fastapi import APIRouter, Depends, HTTPException, Form
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
ACCESS_TOKEN_EXPIRE_MINUTES = 5

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def create_user(db: Session, user: UserCreate):
    password = get_password_hash(user.password)
    db_user = UserModel(username=user.username, password=password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    print('email', email)
    user = get_user(db, email)
    print(user, 'login', user.email, user.password)
    if not user:
        return False
    if not verify_password(password, user.password):
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
def send_verification_code(email: str = Form(...), db: Session = Depends(get_db)):
    code = generate_verification_code()
    user = db.query(UserModel).filter(UserModel.email == email).first()
    # 验证码有效期5分钟
    code_expiration_time = datetime.now().astimezone() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if user:
        user.verification_code = code
        user.code_expiration_time = code_expiration_time
        db.commit()
    else:
        new_user = UserModel(email=email, verification_code=code)
        new_user.code_expiration_time = code_expiration_time
        db.add(new_user)
        db.commit()
    if send_verification_email(email, code):
        return {"message": "Verification code sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send verification code")

@router.post("/verify-verification-code")
def verify_verification_code(email: str = Form(...), code: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user or user.verification_code != code:
        raise HTTPException(status_code=400, detail="Invalid verification code")
    user.verification_code = None
    user.code_expiration_time = None
    db.commit()
    return {"message": "Verification code verified successfully"}

@router.post("/register")
def register(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    db_user = get_user(db, username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = UserCreate(username=username, email=email, password=password)
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    password1 = get_password_hash(password)
    print('p1', password1)
    user = authenticate_user(db, email, password)
    print(email, password, db, user, 'login')
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/refresh-token")
def refresh_token(refresh_token: str = Form(...), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        user = get_user(db, username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
auth_router = router