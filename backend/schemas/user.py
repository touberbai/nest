# backend/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Union
from datetime import datetime


class UserBase(BaseModel):
    # username: str | None
    username: Union[str, None]
    email: Union[EmailStr, str]

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[str]
    is_active: Optional[int]
    # role: str

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
    
class LoginResponse(BaseModel):
    token: Token
    user: User