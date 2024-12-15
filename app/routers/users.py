"""imported modules"""
from fastapi import APIRouter, HTTPException
from schemas.users import users
from models.users import Users, UsersCreate

user_router = APIRouter()

@user_router.get("/")
async def read_users():
    """returns all users from the schema"""
    return users

@user_router.get("/{user_id}")
async def read_user(user_id: int):
    """returns a single user from the schema"""
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found!")

@user_router.post("/", response_model=Users)
async def create_user(user: UsersCreate):
    """creates a new user"""
    user_id = len(users) + 1
    user = Users(**user.model_dump(), id=user_id)
    users.append(user.model_dump())
    return user

@user_router.put("/{user_id}", response_model=Users)
async def update_user(user_id: int, user_in: UsersCreate):
    """updates a user"""
    for user in users:
        if user["id"] == user_id:
            user.update(user_in.model_dump())
            return user
    raise HTTPException(status_code=404, detail="User not found!")

@user_router.patch("/{user_id}")
