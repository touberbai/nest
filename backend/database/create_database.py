# from sqlalchemy import create_engine
# from models.post import Base
# from database.connection import SQLALCHEMY_DATABASE_URL
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Base.metadata.create_all(bind=engine)

# backend/database/create_database.py
from sqlalchemy import create_engine
from models.post import Base as PostBase
from models.user import Base as UserBase
from database.connection import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# 创建所有表
PostBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)