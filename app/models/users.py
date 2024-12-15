"""imported modules"""
from pydantic import BaseModel, EmailStr

class UsersBase(BaseModel):
    """base user class"""
    name: str
    email: EmailStr
    is_active: bool = True

class UsersCreate(UsersBase):
    """user create class"""

class Users(UsersBase):
    """users class"""
    id: int
