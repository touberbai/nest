# main.py
from fastapi import FastAPI
from routers import all_routers
import logging

app = FastAPI()

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 注册所有路由
for router in all_routers:
    app.include_router(router)