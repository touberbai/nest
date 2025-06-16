from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime

# 博客分类表
class BlogCategory(Base):
    __tablename__ = "blog_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    # 关联文章
    # posts = relationship("BlogPost", back_populates="category")

# 博客文章表
class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)

    # 关联分类
    category_id = Column(Integer, ForeignKey("blog_categories.id"), nullable=True)
    category = relationship("BlogCategory", back_populates="posts")
    #
    # # 关联评论
    comments = relationship("BlogComment", back_populates="post")
    #
    # # 关联点赞
    likes = relationship("BlogLike", back_populates="post")
    #
    # # 创建者
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    #
    # # 关联用户
    created_user = relationship("User", back_populates="posts")

# 博客评论表
class BlogComment(Base):
    __tablename__ = "blog_comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("blog_posts.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

    # # 关联文章
    post = relationship("BlogPost", back_populates="comments")
    #
    # # 关联用户
    user = relationship("User", backref="blog_comments")
    

# 博客点赞表
class BlogLike(Base):
    __tablename__ = "blog_likes"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("blog_posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)

    # # 关联文章
    post = relationship("BlogPost", back_populates="likes")
    #
    # # 关联用户
    user = relationship("User", backref="blog_likes")