# Smart Learning Platform API

## Overview

Smart Learning Platform API is a backend learning management system built using FastAPI, Pydantic, SQLAlchemy, and SQLite.

The primary objective of this project is to learn modern backend development concepts such as API development, request validation, database integration, authentication, authorization, and scalable application architecture.

The project is being developed incrementally, starting with core backend fundamentals.

---

## Features

### Authentication & Security

* User Registration
* User Login
* Password Hashing with bcrypt
* JWT Authentication
* Protected Routes
* User Profile Endpoint

### User Management

* Create Users
* View Users
* Email Validation
* Password Validation
* Response Serialization


### Data Validation

* Email Validation
* Password Validation
* Field Constraints
* Custom Validators
* Request Models
* Response Models

---

## Tech Stack

### Backend Framework

* FastAPI

### Programming Language

* Python

### Validation

* Pydantic

### Database

* SQLite

### ORM

* SQLAlchemy

### Authentication

* JWT (JSON Web Tokens)
* Passlib
* bcrypt

### Server

* Uvicorn

---

## Project Structure

```text
smart-learning-platform-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│   ├── auth.py
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

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd smart-learning-platform-api
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows CMD

```cmd
venv\Scripts\activate
```

#### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Database

This project currently uses SQLite for local development.

Database file:

```text
learning.db
```

The database is automatically created when the application starts.

Current tables:

* users
* courses
* quizzes

---

## Authentication Flow

### Registration

Users register with:

* Name
* Email
* Password

Passwords are never stored in plain text.

### Password Hashing

Passwords are securely hashed using bcrypt before being stored in the database.

### Login

Users authenticate using their email and password.

Successful authentication returns a JWT access token.

### Protected Routes

Protected endpoints require a valid JWT token.

Example:

```text
Authorization: Bearer <access_token>
```

---

## Validation Features

The project demonstrates several Pydantic validation techniques:

### Email Validation
### Password Validation
### Field Constraints
### Custom Validators


## Learning Objectives

This project is intended to provide hands-on experience with:

* FastAPI Application Development
* APIRouter Architecture
* Request Validation
* Response Validation
* Pydantic Models
* Custom Validators
* Dependency Injection
* SQLAlchemy ORM
* SQLite Integration
* CRUD Operations
* Password Hashing
* JWT Authentication
* Protected Endpoints
* Backend Project Organization

---


## Development Commands

### Run the Application

```bash
uvicorn app.main:app --reload
```

### Generate Requirements File

```bash
pip freeze > requirements.txt
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Author

**Pogula Chandra Kanth**
