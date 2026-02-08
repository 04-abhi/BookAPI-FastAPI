# 📚 Books Information API (FastAPI + SQLModel)

A clean and modern **REST API built with FastAPI and SQLModel** to manage and retrieve book information.  
This project uses the **FastAPI lifespan event manager** (recommended approach) for database initialization.

---

## ✨ Features

- 📖 List all books  
- 🔍 Filter books by author  
- 🆔 Retrieve book details by ID  
- 🗄️ SQLite database using SQLModel  
- ⚡ Lifespan event manager (no deprecated startup events)

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **FastAPI**
- **SQLModel**
- **SQLite**
- **Uvicorn**

---

## 📁 Project Structure

```
.
├── main.py
├── models.py
├── database.db
└── README.md
```

---

## ▶️ Run Locally

### 1. Install dependencies

```bash
pip install fastapi uvicorn sqlmodel
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
|------|--------|------------|
| GET | / | API status |
| GET | /books | Get all books |
| GET | /books?author=Author%20C | Filter books by author |
| GET | /books/{id} | Get book by ID |

---

## 📘 API Documentation

FastAPI automatically generates interactive API docs:

- **Swagger UI:** http://127.0.0.1:8000/docs  
- **ReDoc:** http://127.0.0.1:8000/redoc  

---

## 🧠 Notes

- Tables are created automatically using the **lifespan event manager**
- Data is stored in an SQLite database
- Restarting the server does NOT delete data
- Database starts empty (use POST endpoints or DB tools to insert data)

---

## 🚀 Future Improvements

- Add POST / PUT / DELETE endpoints
- Pagination & sorting
- Database migrations (Alembic)
- Authentication & authorization

---

## 👤 Author

**Abhinav Ajay**  
_B.Tech Student | Backend & API Enthusiast_

---

⭐ If you find this project useful, consider giving it a star!
