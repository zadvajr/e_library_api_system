"""This module contains the Pydantic models for the User model."""
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """base user class"""
    name: str
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    """user create class"""

class User(UserBase):
    """users class"""
    id: int

class UserUpdate(UserBase):
    """user update class"""
    name: str = None
    email: EmailStr = None
    is_active: bool = True
