from sqlalchemy import Column, Integer, String
# from database.connection import Base
from models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    verification_code = Column(String(6))  # 用于存储验证码