"""This module contains the Borrow router."""
from fastapi import APIRouter, HTTPException
from schemas.borrows import borrows
from schemas.books import books
from schemas.users import users
from models.borrows import (Borrow, BorrowCreate, BorrowUpdate)
from services.validate_borrow import validate_borrow

borrow_router = APIRouter()

@borrow_router.get("", response_model=list[Borrow], status_code=200)
async def read_borrows():
    """returns all borrowing transactions from the schema"""
    return borrows

@borrow_router.get("/{borrow_id}", response_model=Borrow, status_code=200)
async def read_borrow(borrow_id: int):
    """returns a single borrowing transaction from the schema"""
    for borrow in borrows.copy():
        if borrow["id"] == borrow_id:
            return borrow
    raise HTTPException(status_code=404, detail="Borrow not found!")

@borrow_router.post("", response_model=Borrow, status_code=201)
async def borrow_book(borrow_in: BorrowCreate):
    """creates a new borrowing transaction"""
    if validate_borrow(borrow_in):
        borrow_id = len(borrows) + 1
        new_borrow = Borrow(**borrow_in.model_dump(), id=borrow_id)
        borrows.append(new_borrow.model_dump())
        book_id = borrow_in.book_id
        for book in books:
            if book["id"] == book_id:
                book["is_available"] = False
                break
        return new_borrow
    raise HTTPException(status_code=400, detail="Invalid borrowing transaction!")

@borrow_router.put("/{borrow_id}", response_model=Borrow, status_code=200)
async def update_borrow(borrow_id: int, borrow_in: BorrowUpdate):
    """updates a borrowing transaction"""
    for borrow in borrows.copy():
        if borrow["id"] == borrow_id:
            borrow.update(borrow_in.model_dump())
            return borrow
    raise HTTPException(status_code=404, detail="Borrow not found!")

@borrow_router.patch("/{borrow_id}", response_model=Borrow, status_code=200)
async def partial_update_borrow(borrow_id: int, borrow_in: BorrowUpdate):
    """partially updates a borrowing transaction"""
    for borrow in borrows.copy():
        if borrow["id"] == borrow_id:
            borrow.update(borrow_in.model_dump())
            return borrow
    raise HTTPException(status_code=404, detail="Borrow not found!")

@borrow_router.delete("/{borrow_id}", status_code=204)
async def delete_borrow(borrow_id: int):
    """deletes a borrowing transaction"""
    for borrow in borrows.copy():
        if borrow["id"] == borrow_id:
            borrows.remove(borrow)
            return
    raise HTTPException(status_code=404, detail="Borrow not found!")
