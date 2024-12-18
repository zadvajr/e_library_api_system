"""This module contains the Borrow model."""
from pydantic import BaseModel

class BorrowBase(BaseModel):
    """Borrow model."""
    user_id: int
    book_id: int
    borrow_date: str
    return_date: str

class Borrow(BorrowBase):
    """Borrow model."""
    id: int

class BorrowCreate(BorrowBase):
    """Borrow create model."""

class BorrowUpdate(BorrowBase):
    """Borrow update model."""
    user_id: int = None
    book_id: int = None
    borrow_date: str = None
    return_date: str = None
