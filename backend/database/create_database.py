from sqlalchemy import create_engine
from models.base import Base
from models.post import Base as PostBase
from models.user import Base as UserBase
from models.blog import Base as BlogBase  # 新增
from database.connection import SQLALCHEMY_DATABASE_URL

print(f"数据库连接 URI: {SQLALCHEMY_DATABASE_URL}")  #
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 创建所有表
PostBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)
BlogBase.metadata.create_all(bind=engine)  # 新增

# 打印所有已注册的表
print("已注册的表:", Base.metadata.tables.keys())