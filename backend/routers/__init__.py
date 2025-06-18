from .auth import auth_router
from .user import user_router
from .blog import blog_router
from .future import future_router

# 整合所有路由
all_routers = [
    auth_router,
    user_router,
    blog_router,
    future_router,
    # 这里可以添加其他路由，如 posts_router
]