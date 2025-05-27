# backend/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    is_active: int
    role: str

    class Config:
        from_attributes = True
    
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    
class VerificationCodeRequest(BaseModel):
    email: EmailStr
    
class VerificationCodeVerify(BaseModel):
    email: EmailStr
    code: str