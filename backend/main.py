# main.py
from fastapi import FastAPI
from routers import all_routers
import logging
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 注册所有路由
for router in all_routers:
    app.include_router(router)
    
# 配置 CORS 中间件
origins = [
    "http://127.0.0.1:7776",  # 前端项目的地址
    # 可以添加更多允许的源
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)