# routers/auth.py
from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/test")
def test_route():
    return {"message": "Test route is working!"}