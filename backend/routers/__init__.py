from .auth import auth_router

# 整合所有路由
all_routers = [
    auth_router,
    # 这里可以添加其他路由，如 posts_router
]