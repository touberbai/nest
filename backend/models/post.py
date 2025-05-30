from sqlalchemy import Column, Integer, String, Text
from database.connection import Base


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)
