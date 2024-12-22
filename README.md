# Backend Python Second Semester Examination Project
## BY
## DANIEL ZADVA JNR - ALT/SOE/024/1026
AltSchool Backend Engineering Karatu 2024 Second Semester (Python).

## Project Title: E-Library API System

### About:
E-Library API System is a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books. To view full specification of the project click [here](./srs.md).


### Code Structure
```bash
    e_library_api_system
    |   |
    │   │   README.md
    │   │   .gitignore
    │   │   srs.md
    │   └───requirements.txt
    |
    └───app
        │   main.py
        │   __init__.py
        |
        ├───models
        │   │   books.py
        │   │   borrows.py
        │   │   users.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │
        ├───routers
        │   │   books.py
        │   │   borrows.py
        │   │   users.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │
        ├───schemas
        │   │   books.py
        │   │   borrows.py
        │   │   users.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │
        ├───services
        │   │   validate_borrow.py
        │   │
        │   └───__pycache__
        │
        └───__pycache__
```

### How to Run the App
1. Copy the repo URL [here](https://github.com/zadvajr/e_library_api_system.git)
2. Navigate to your desired location to save the repo locally (e.g Desktop)
3. Right click and select `Git bash here` and `git clone <repo-url>`
4. Navigate into `e_library_api_system` by running `cd e_library_api_system`
5. Navigate into `app` folder by running `cd app`
6. To run the app run `uvicorn main:app --reload` You will see:
    ```bash 
    C:\Users\danie\OneDrive\Desktop\altschool_exam\e_library_api_system\app>uvicorn main:app --reload
    INFO:     Will watch for changes in these directories: ['C:\\Users\\danie\\OneDrive\\Desktop\\altschool_exam\\e_library_api_system\\app']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [7156] using WatchFiles
    INFO:     Started server process [6508]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```
7.  Press CTRL + Click on the URL: ` http://127.0.0.1:8000` or ` http://127.0.0.1:8000/docs` for interractive docs.
8.  You need to create at least 1 user, 1 book, before you will be able to create borrow transactions. All the databases are empty until user decide to create them at run time.


Thank you
Daniel Zadva Jnr