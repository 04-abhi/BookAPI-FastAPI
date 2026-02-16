# 🔐 Assignment 4 – Authentication & Authorization (JWT) with FastAPI

This assignment is part of **Session 4** of the FastAPI training program.  
It focuses on implementing **JWT-based authentication**, **role-based authorization**, and securing CRUD operations using FastAPI dependencies.

---

## 🎯 Objectives Covered

- JWT authentication concepts
- OAuth2 Password flow with Bearer tokens
- Password hashing using Passlib
- Access token generation and validation
- Securing routes using `Depends`
- Role-based access control (Admin vs User)
- Protecting CRUD operations

---

## 🛠️ Tech Stack

- Python 3.9+
- FastAPI
- SQLModel
- SQLite
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Uvicorn

---

## 📁 Project Structure

```
.
├── main.py
├── models.py
├── auth.py
├── database.db
└── README.md
```

---

## 👤 Authentication Features

### User Registration
- Allows new users to register
- Passwords are securely hashed using Passlib
- Default role assigned: `user`

### User Login
- Authenticates users using OAuth2 Password flow
- Returns a JWT access token
- Token type: Bearer

---

## 🔑 Authorization & Security

- JWT Bearer token authentication
- Protected routes using FastAPI dependencies
- Role-based access:
  - **User** → Can create books
  - **Admin** → Can update and delete books

---

## 🔒 Protected Routes

| Method | Endpoint | Access Level |
|------|--------|--------------|
| POST | /books | Authenticated user |
| PUT | /books/{id} | Admin only |
| DELETE | /books/{id} | Admin only |

---

## ▶️ Run the Application

### Install dependencies

```bash
pip install fastapi uvicorn sqlmodel passlib[bcrypt] python-jose
```

### Start the server

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🧪 How to Test Authentication

1. Open Swagger UI: `/docs`
2. Register a user using `/register`
3. Login using `/login` to get JWT token
4. Click **Authorize** and paste the token
5. Access protected endpoints

---

## 📘 API Documentation

- Swagger UI: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc  

---

## 🧠 Notes

- JWT tokens expire after a configured time
- Database persists data across restarts
- Admin role can be assigned manually in the database if needed
- Passwords are never stored in plain text

---

## 👤 Author

**Abhinav Ajay**  
B.Tech Student | FastAPI Learner

---

⭐ This README documents the completion of **Session 4 – Assignment (Authentication & Authorization using JWT)**.
