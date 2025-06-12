from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from crud.blog import get_blog_categories, create_blog_category, get_blog_posts, create_blog_post, get_blog_post_comments, create_blog_post_comment, get_blog_post_likes, create_blog_post_like
from schemas.blog import BlogCategoryCreate, BlogPostCreate, BlogCommentCreate, BlogLikeCreate
from database.connection import get_db
from schemas.blog import BlogCategory, BlogPost, BlogComment, BlogLike

router = APIRouter()

# 获取所有分类
@router.post("/categories/", response_model=list[BlogCategory])
def read_blog_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = get_blog_categories(db, skip=skip, limit=limit)
    return categories

# 创建分类
@router.post("/categories/create", response_model=BlogCategory)
def create_new_blog_category(category: BlogCategoryCreate, db: Session = Depends(get_db)):
    return create_blog_category(db=db, category=category)

# 获取所有文章
@router.post("/posts/", response_model=list[BlogPost])
def read_blog_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = get_blog_posts(db, skip=skip, limit=limit)
    return posts

# 创建文章
@router.post("/posts/create", response_model=BlogPost)
def create_new_blog_post(
    # post: BlogPostCreate,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    print(title, content)
    post=BlogPostCreate(title=title, content=content)
    return create_blog_post(db=db, post=post)

# 获取文章的评论
@router.post("/posts/{post_id}/comments/", response_model=list[BlogComment])
def read_blog_post_comments(post_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = get_blog_post_comments(db, post_id=post_id, skip=skip, limit=limit)
    return comments

# 创建文章的评论
@router.post("/posts/{post_id}/comments/create", response_model=BlogComment)
def create_new_blog_post_comment(post_id: int, comment: BlogCommentCreate, db: Session = Depends(get_db)):
    comment.post_id = post_id
    return create_blog_post_comment(db=db, comment=comment)

# 获取文章的点赞
@router.post("/posts/{post_id}/likes/", response_model=list[BlogLike])
def read_blog_post_likes(post_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    likes = get_blog_post_likes(db, post_id=post_id, skip=skip, limit=limit)
    return likes

# 创建文章的点赞
@router.post("/posts/{post_id}/likes/create", response_model=BlogLike)
def create_new_blog_post_like(post_id: int, like: BlogLikeCreate, db: Session = Depends(get_db)):
    like.post_id = post_id
    return create_blog_post_like(db=db, like=like)

blog_router = router