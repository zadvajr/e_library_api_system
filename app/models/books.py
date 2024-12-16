from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

class BookUpdate(BookBase):
    title: str = None
    author: str = None
    is_available: bool = None