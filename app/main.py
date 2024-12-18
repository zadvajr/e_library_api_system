"""imported modules"""
from fastapi import FastAPI
from routers.users import user_router
from routers.books import book_router
from routers.borrows import borrow_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_router, prefix="/borrows", tags=["Borrows"])
