"""This module contains the Borrow model."""
from pydantic import BaseModel

class BorrowBase(BaseModel):
    """Borrow model."""
    user_id: int
    book_id: int
    borrow_date: str
    # return_date: str

class Borrow(BorrowBase):
    """Borrow model."""
    id: int
    returned: bool = False

class BorrowCreate(BorrowBase):
    """Borrow create model."""

class BorrowUpdate(BorrowBase):
    """Borrow update model."""
    borrow_date: str = None
    return_date: str = None
    returned: bool = None
    

class ReturnBorrow(BorrowBase):
    """Return borrow model."""
    return_date: str
