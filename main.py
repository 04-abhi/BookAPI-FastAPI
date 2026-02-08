from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from contextlib import asynccontextmanager

from models import Book, engine, create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
def root():
    return {"message": "Books Information API"}


@app.get("/books")
def get_books(
    author: str | None = None,
    session: Session = Depends(get_session)
):
    statement = select(Book)
    if author:
        statement = statement.where(Book.author == author)

    books = session.exec(statement).all()
    return {"books details": books}


@app.get("/books/{id}")
def get_book_by_id(
    id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, id)
    if not book:
        return {"message": "Book not found"}
    return {"book details": book}
