"""imported modules"""
from fastapi import APIRouter, HTTPException
from schemas.users import users
from models.users import (User, UserCreate, UserUpdate)

user_router = APIRouter()

@user_router.get("", response_model=list[User], status_code=200)
async def read_users():
    """returns all users from the schema"""
    return users

@user_router.get("/{user_id}", response_model=User, status_code=200)
async def read_user(user_id: int):
    """returns a single user from the schema"""
    for user in users.copy():
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found!")

@user_router.post("", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """creates a new user"""
    user_id = len(users) + 1
    user = User(**user.model_dump(), id=user_id)
    users.append(user.model_dump())
    return user

@user_router.put("/{user_id}", response_model=User, status_code=200)
async def update_user(user_id: int, user_in: UserUpdate):
    """updates a user"""
    for user in users.copy():
        if user["id"] == user_id:
            user.update(user_in.model_dump())
            return user
    raise HTTPException(status_code=404, detail="User not found!")

@user_router.patch("/{user_id}", response_model=User, status_code=200)
async def patch_user(user_id: int, user_in: UserUpdate):
    """partially updates a user"""
    for user in users.copy():
        if user["id"] == user_id:
            updated_user = user.copy()
            updated_user.update(user_in.model_dump(exclude_unset=True))
            user.update(updated_user)
            return updated_user
    raise HTTPException(status_code=404, detail="User not found!")

@user_router.patch("/{user_id}/deactivate", response_model=User, status_code=200)
async def deactivate_user(user_id: int):
    """Endpoint to deactivate a user, setting is_active to False"""
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i]["is_active"] = False
            return User(**users[i])
            # return {"message": "User deactivated successfully!"}
    raise HTTPException(status_code=404, detail="User not found!")

@user_router.delete("/{user_id}", response_model=dict, status_code=200)
async def delete_user(user_id: int):
    """deletes a user"""
    for user in users.copy():
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted successfully!"}
    raise HTTPException(status_code=404, detail="User not found!")
