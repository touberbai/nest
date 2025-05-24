from sqlalchemy import Column, Integer, String, DateTime
# from database.connection import Base
from models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    verification_code = Column(String(6))  # 用于存储验证码
    code_expiration_time = Column(DateTime)  # 用于存储验证码的过期时间
    is_active = Column(Integer, default=0)  # 是否激活
    