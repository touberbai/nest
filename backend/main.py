from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from crud.post import get_posts, create_post
# from schemas.post import Post, PostCreate
# from database.connection import get_db
from routers import all_routers
import logging
app = FastAPI()

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 注册所有路由
for router in all_routers:
    app.include_router(router)
# @app.get("/posts/", response_model=list[Post])
# def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     posts = get_posts(db, skip=skip, limit=limit)
#     return posts
#
#
# @app.post("/posts/", response_model=Post)
# def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     return create_post(db=db, post=post)
