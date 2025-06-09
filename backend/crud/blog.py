from sqlalchemy.orm import Session
from models.blog import BlogCategory, BlogPost, BlogComment, BlogLike
from schemas.blog import BlogCategoryCreate, BlogPostCreate, BlogCommentCreate, BlogLikeCreate

# 获取所有分类
def get_blog_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BlogCategory).offset(skip).limit(limit).all()

# 创建分类
def create_blog_category(db: Session, category: BlogCategoryCreate):
    db_category = BlogCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# 获取所有文章
def get_blog_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BlogPost).offset(skip).limit(limit).all()

# 创建文章
def create_blog_post(db: Session, post: BlogPostCreate):
    db_post = BlogPost(title=post.title, content=post.content, category_id=post.category_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# 获取文章的评论
def get_blog_post_comments(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.query(BlogComment).filter(BlogComment.post_id == post_id).offset(skip).limit(limit).all()

# 创建文章的评论
def create_blog_post_comment(db: Session, comment: BlogCommentCreate):
    db_comment = BlogComment(post_id=comment.post_id, user_id=comment.user_id, content=comment.content)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# 获取文章的点赞
def get_blog_post_likes(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.query(BlogLike).filter(BlogLike.post_id == post_id).offset(skip).limit(limit).all()

# 创建文章的点赞
def create_blog_post_like(db: Session, like: BlogLikeCreate):
    db_like = BlogLike(post_id=like.post_id, user_id=like.user_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like