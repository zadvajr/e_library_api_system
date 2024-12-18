"""This module contains the Pydantic models for the Book model."""
from pydantic import BaseModel

class BookBase(BaseModel):
    """Base model for the Book model."""
    title: str
    author: str
    is_available: bool = True

class BookCreate(BookBase):
    """Model for creating a new Book."""

class Book(BookBase):
    """Model for the Book model."""
    id: int

class BookUpdate(BookBase):
    """Model for updating an existing Book."""
    title: str = None
    author: str = None
    is_available: bool = None
