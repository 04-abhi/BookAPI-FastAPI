# 🧪 Session 5 – Testing & Documentation (FastAPI)

This assignment covers **industry-standard testing and API documentation practices** using FastAPI.

The focus of this session is writing complete test coverage for the Book API, including JWT-protected routes and negative testing scenarios.

---

## 🎯 Objectives Covered

- Swagger UI & ReDoc documentation
- Response models validation
- PyTest integration with FastAPI
- TestClient usage
- Dependency overrides for test database
- Validating response schema & status codes
- Testing JWT-protected routes
- Negative testing patterns

---

## 🛠️ Tech Stack

- Python 3.9+
- FastAPI
- PyTest
- HTTPX (TestClient dependency)
- SQLModel
- SQLite

---

## 📁 Project Structure

```
.
├── main.py
├── models.py
├── auth.py
├── tests/
│   ├── conftest.py
│   └── test_books.py
└── README.md
```

---

## 🧪 Testing Implementation

### ✅ TestClient
FastAPI’s `TestClient` is used to simulate HTTP requests without running a live server.

### ✅ Dependency Override
Database session dependency is overridden to use a **separate test database**, ensuring isolation from production data.

### ✅ JWT Testing
Tests include:
- Login to retrieve access token
- Passing Bearer token in headers
- Verifying protected route access
- Testing unauthorized access scenarios

### ✅ Negative Testing
- Invalid credentials
- Access without token
- Access with wrong role
- Resource not found (404)

---

## ▶️ Running Tests

### Install dependencies

```bash
pip install pytest httpx
```

### Run test suite

```bash
pytest -v
```

---

## 📊 What is Covered

| Test Area | Status |
|-----------|--------|
| Root endpoint | ✅ |
| CRUD operations | ✅ |
| JWT authentication | ✅ |
| Role-based authorization | ✅ |
| Status code validation | ✅ |
| Error handling | ✅ |

---

## 📘 API Documentation

FastAPI automatically generates interactive documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 🧠 Key Learning Outcomes

- Writing isolated and repeatable tests
- Securing APIs and testing authentication
- Validating responses and status codes
- Applying dependency injection in testing
- Implementing negative testing strategies

---

## 👤 Author

**Abhinav Ajay**  
B.Tech Student | FastAPI Learner

---

⭐ This README documents the completion of **Session 5 – Testing & Documentation Assignment**.
