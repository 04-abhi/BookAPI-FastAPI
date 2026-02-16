from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from fastapi.security import OAuth2PasswordRequestForm

from models import Book, User, engine, create_db_and_tables
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user,
    admin_required
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


def get_session():
    with Session(engine) as session:
        yield session


# ---------------- AUTH ROUTES ----------------

@app.post("/register")
def register(username: str, password: str, session: Session = Depends(get_session)):
    user_exists = session.exec(
        select(User).where(User.username == username)
    ).first()

    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")

    user = User(
        username=username,
        hashed_password=hash_password(password),
        role="user"
    )
    session.add(user)
    session.commit()
    return {"message": "User registered successfully"}


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.username == form_data.username)
    ).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


# ---------------- BOOK ROUTES ----------------

@app.get("/books")
def get_books(session: Session = Depends(get_session)):
    return session.exec(select(Book)).all()


@app.post("/books")
def create_book(
    book: Book,
    _: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    session.add(book)
    session.commit()
    return book


@app.put("/books/{id}")
def update_book(
    id: int,
    book: Book,
    _: User = Depends(admin_required),
    session: Session = Depends(get_session)
):
    db_book = session.get(Book, id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_book.title = book.title
    db_book.author = book.author
    db_book.year = book.year
    session.commit()
    return db_book


@app.delete("/books/{id}")
def delete_book(
    id: int,
    _: User = Depends(admin_required),
    session: Session = Depends(get_session)
):
    book = session.get(Book, id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()
    return {"message": "Book deleted"}