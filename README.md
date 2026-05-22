# Smart Learning API

A backend learning platform API built using FastAPI, Pydantic, and SQLAlchemy.

This project is designed to learn:

- FastAPI
- Pydantic validations
- SQLAlchemy ORM
- CRUD APIs
- Dependency Injection
- SQLite database integration
- Backend project structure

Later this project can be extended with:

- JWT Authentication
- Async APIs
- File uploads
- AI quiz generation
- AI tutor system
- Recommendation engine

---

# Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn

---

# Project Structure

```bash
smart-learning-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│   │
│   ├── routers/
│   │   ├── users.py
│   │   ├── courses.py
│   │   └── quizzes.py
│   │
│   └── utils/
│
├── requirements.txt
├── learning.db
└── README.md
```

---

# Features

## Users

- Create users
- View users
- Email validation
- Password validation

## Courses

- Create courses
- View courses

## Quizzes

- Create quizzes
- View quizzes

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd smart-learning-api
```

---

# Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

#### CMD

```bash
venv\Scripts\activate
```

#### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
uvicorn app.main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

# Swagger Documentation

FastAPI automatically generates API documentation.


# Database

This project uses SQLite.

Database file:

```text
learning.db
```

Tables are automatically created when server starts.

---


# Pydantic Validations

This project demonstrates:

- Email validation
- Password validation
- Field constraints
- Custom validators
- Nested models
- Response models


# Password Validation Rules

Password must:

- be at least 8 characters
- contain uppercase letter

---

# Concepts Covered

- FastAPI routing
- APIRouter
- Request models
- Response models
- SQLAlchemy ORM
- Dependency Injection
- SQLite integration
- CRUD operations
- Validation handling

---

# Future Improvements

## Backend Improvements

- JWT Authentication
- Password hashing
- Role-based access
- Async database
- Pagination
- Search/filter APIs

## AI Features

- AI Quiz Generator
- AI Tutor
- Personalized recommendations
- AI answer evaluation

---

# Useful Commands

## Run Server

```bash
uvicorn app.main:app --reload
```

## Freeze Requirements

```bash
pip freeze > requirements.txt
```

---

# Author

Pogula Chandra Kanth