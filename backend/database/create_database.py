from sqlalchemy import create_engine
from models.post import Base as PostBase
from models.user import Base as UserBase
from models.blog import Base as BlogBase  # 新增
from database.connection import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# 创建所有表
PostBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)
BlogBase.metadata.create_all(bind=engine)  # 新增