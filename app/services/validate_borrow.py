from schemas.users import users
from schemas.books import books
from schemas.borrows import borrows


def validate_borrow(borrow_in):
    """Validates a borrowing transaction."""
    user_id = borrow_in.user_id
    book_id = borrow_in.book_id

    # Check if user exists and is active
    user = next((user for user in users if user["id"] == user_id and user["is_active"]), None)
    if not user:
        return False

    # Check if book exists and is available
    book = next((book for book in books if book["id"] == book_id and book["is_available"]), None)
    if not book:
        return False

    # Check if user has already borrowed the book
    has_borrowed = any(borrow for borrow in borrows if borrow["user_id"] == user_id and borrow["book_id"] == book_id)
    if has_borrowed:
        return False

    return True