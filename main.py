from fastapi import FastAPI, Depends, Request
from sqlmodel import Session, select
from contextlib import asynccontextmanager
import time
import logging

from models import Book, engine, create_db_and_tables

# LOGGING CONFIGURATION
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# APPLICATION LIFECYCLE (LIFESPAN)
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup: creating database tables")
    create_db_and_tables()
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

# MIDDLEWARE: LOGGING + REQUEST TIMING
@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    execution_time = (time.perf_counter() - start_time) * 1000

    logger.info(
        f"Method={request.method} | "
        f"Path={request.url.path} | "
        f"Status={response.status_code} | "
        f"Time={execution_time:.2f}ms"
    )

    return response


# DEPENDENCY: DATABASE SESSION
def get_session():
    with Session(engine) as session:
        yield session


# ROUTES
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