"""imported modules"""
from fastapi import APIRouter
from schemas.users import users
from models.users import User

user_router = APIRouter()

@user_router.get("/users")
async def read_users():
    """returns all users from the schema"""
    return {"users": users}

@user_router.get("/users/{user_id}")
async def read_user(user_id: int):
    """returns a single user from the schema"""
    return {"user": users[user_id]}
