from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from crud.post import get_posts, create_post
from schemas.post import Post, PostCreate
from database.connection import get_db

app = FastAPI()


@app.get("/posts/", response_model=list[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts


@app.post("/posts/", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db=db, post=post)
