# 📚 Books Information API

A clean and beginner-friendly **REST API built with FastAPI** for retrieving book information.

---

## ✨ Features

- 📖 List all available books  
- 🔍 Filter books by author  
- 🆔 Retrieve book details using ID  

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**

---

## ▶️ Run Locally

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Start the server

```bash
uvicorn main:app --reload
```

### 3. Open in browser

```
http://127.0.0.1:8000
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| GET | / | API status |
| GET | /books | Get all books |
| GET | /books?author=Author%20C | Filter books by author |
| GET | /books/{id} | Get book by ID |

---

## 📘 API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs  
- **ReDoc:** http://127.0.0.1:8000/redoc  

---

## 🧠 Notes

- Author filtering is case-sensitive  
- Data is stored in-memory  
- Restarting the server resets the data  

---

## 👤 Author

**Abhinav Ajay**  
_B.Tech Student | Backend & API Enthusiast_

---

⭐ If you like this project, consider giving it a star!
