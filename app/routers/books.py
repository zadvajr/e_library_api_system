"""This module contains the routers for the books endpoints"""
from fastapi import APIRouter, HTTPException
from models.books import (Book, BookCreate, BookUpdate)
from schemas.books import books


book_router = APIRouter()

@book_router.get("", response_model=list[Book])
async def read_books():
    """returns all books from the schema"""
    return books

@book_router.get("/{book_id}", response_model=Book, status_code=200)
async def read_book(book_id: int):
    """returns a single book from the schema"""
    for book in books.copy():
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.post("", response_model=Book, status_code=201)
async def create_book(book_in: BookCreate):
    """creates a new book"""
    book_id = len(books) + 1
    new_book = Book(**book_in.model_dump(), id=book_id)
    books.append(new_book.model_dump())
    return new_book

@book_router.put("/{book_id}", response_model=Book, status_code=200)
async def update_book(book_id: int, book_in: BookUpdate):
    """updates a book"""
    for book in books:
        if book["id"] == book_id:
            book.update(book_in.model_dump())
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.patch("/{book_id}")
async def patch_book(book_id: int, book_in: BookUpdate):
    """partially updates a book"""
    for book in books:
        if book["id"] == book_id:
            updated_book = book.copy()
            updated_book = book_in.model_dump(exclude_unset=True)
            book.update(updated_book)
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.patch("/{book_id}/unavailable", response_model=Book)
async def mark_book_unavailable(book_id: int):
    """Endpoint to mark a book as unavailable"""
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i]["is_available"] = False
            # return {"message": "Book marked unavailable!"}
            return Book(**books[i])
    raise HTTPException(status_code=404, detail="Book not found!")

@book_router.delete("/{book_id}")
async def delete_book(book_id: int):
    """deletes a book"""
    for book in books.copy():
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully!"}
    raise HTTPException(status_code=404, detail="Book not found!")
