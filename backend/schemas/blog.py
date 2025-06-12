from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# 博客分类相关模型

# 博客分类创建时的请求体模型
class BlogCategoryCreate(BaseModel):
    name: str

# 博客分类返回给前端的响应模型
class BlogCategory(BlogCategoryCreate):
    id: int

    class Config:
        from_attributes = True

# 博客文章相关模型

# 博客文章创建时的请求体模型
class BlogPostCreate(BaseModel):
    title: str
    content: str
    # category_id: int

# 博客文章返回给前端的响应模型
class BlogPost(BlogPostCreate):
    id: int
    # created_at: Optional[datetime]

    class Config:
        from_attributes = True

# 博客评论相关模型

# 博客评论创建时的请求体模型
class BlogCommentCreate(BaseModel):
    post_id: int
    user_id: int
    content: str

# 博客评论返回给前端的响应模型
class BlogComment(BlogCommentCreate):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True

# 博客点赞相关模型

# 博客点赞创建时的请求体模型
class BlogLikeCreate(BaseModel):
    post_id: int
    user_id: int

# 博客点赞返回给前端的响应模型
class BlogLike(BlogLikeCreate):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True

# 包含分类、评论和点赞信息的完整博客文章响应模型
class BlogPostDetail(BlogPost):
    category: BlogCategory
    comments: List[BlogComment]
    likes: List[BlogLike]

    class Config:
        from_attributes = True