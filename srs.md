# Backend Python Second Semester Examination Project
AltSchool Backend Engineering Karatu 2024 Second Semester (Python).

## Project Title: E-Library API System

### Description:
The goal of this project is to create a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books.

The system includes the following entities:

1. **User**: Represents a user of the library.
    - id: Unique identifier for the user.
    - name: Name of the user.
    - email: Email address of the user.
    - is_active: Indicates if the user account is active (defaults to True).
2. **Book**: Represents a book in the library.
    - id: Unique identifier for the book.
    - title: Title of the book.
    - author: Author of the book.
    - is_available: Indicates if the book is available for borrowing (defaults to True).
3. **BorrowRecord**: Represents a borrowing record.
    - id: Unique identifier for the record.
    - user_id: ID of the user who borrowed the book.
    - book_id: ID of the borrowed book.
    - borrow_date: Date the book was borrowed.
    - return_date: Date the book was returned (if applicable).
<hr>

### Requirements:
#### API Endpoints:
You are required to create the following endpoints:

1. **User Endpoints**:
    - CRUD operations for User.
    - Endpoint to deactivate a user, setting is_active to False.
2. **Book Endpoints**:
    - CRUD operations for Book.
    - Endpoint to mark a book as unavailable (e.g., if it’s lost or under maintenance).
3. **Borrow Operations**:
    - **Borrow a book**:
        - Allows an active user to borrow an available book.
        - A user cannot borrow a book if it’s unavailable or if they have already borrowed the same book.
        - If the book is successfully borrowed, update its is_available status to False.
        - If the book cannot be borrowed, return an appropriate response and status code.
    - **Return a book**:
        - Marks a borrowed book as returned by updating the return_date in the BorrowRecord and setting the book’s is_available status to True.
4. **Borrow Record Management**:
    - Endpoint to view borrowing records for a specific user.
    - Endpoint to view all borrowing records.
<hr>

### Additional Requirements:
1. **Database**:
    - Use in-memory data structures (list or dict) for storage.
2. **Validation**:
    - Use Pydantic models to validate inputs for all endpoints.
3. **Code Structure**:
    - Follow a modular structure for better readability and maintainability.
    - Use separate files for models, routes, and application configuration.
4. **Status Codes**:
    - Use appropriate HTTP status codes for success and error scenarios.
<hr>

### Constraints:
1. Users must be active to perform any operations.
2. Books must be available to be borrowed.
3. Each borrowing operation should have a unique BorrowRecord.
<hr>

### Submission Instructions:
1. Develop the project using FastAPI.
2. Add a README.md file with instructions on how to run the application.
3. Push your code to a **public GitHub repository**.
4. Include test cases to validate your API endpoints (optional for extra credit).
<hr>

Submission Link: [AltSchool of Backend Engineering Python Karatu 2nd ’24 Semester Exam Submission Link](https://forms.gle/7vpvT2qUAUrivvuU9)