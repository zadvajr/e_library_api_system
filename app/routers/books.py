from fastapi import APIRouter, HTTPException
from schemas.books import books
from models.books import Book, BookCreate

book_router = APIRouter()

@book_router.get("/")
async def read_books():
    """returns all books from the schema"""
    return books

@book_router.get("/{book_id}")
async def read_book(book_id: int):
    """returns a single book from the schema"""
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.post("/", response_model=Book)
async def create_book(book: BookCreate):
    """creates a new book"""
    book_id = len(books) + 1
    book = Book(**book.model_dump(), id=book_id)
    books.append(book.model_dump())
    return book

@book_router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book_in: BookCreate):
    """updates a book"""
    for book in books:
        if book["id"] == book_id:
            book.update(book_in.model_dump())
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.patch("/{book_id}")
async def patch_book(book_id: int, book_in: BookCreate):
    """patches a book"""
    for book in books:
        if book["id"] == book_id:
            book.update(book_in.model_dump())
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.delete("/{book_id}")
async def delete_book(book_id: int):
    """deletes a book"""
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully!"}
    raise HTTPException(status_code=404, detail="Book not found!")
