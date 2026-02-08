from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Lord of the Rings",
        "author": "Author A",
        "year": 1954
    },
    {    
        "id": 2,
        "title": "The Hobbit",
        "author": "Author B",
        "year": 1937
    },
    {    
        "id": 3,
        "title": "The Silmarillion",
        "author": "Author C",
        "year": 1977
    }
]

@app.get("/")
async def root():
    return {"message": "Books Information API"}

@app.get("/books")
async def get_books(author: str = None):
    if author:
        filtered_books = [book for book in books if book["author"] == author]
        return {"books details": filtered_books}
    return {"books details": books}

@app.get("/books/{id}")
async def get_book_by_id(id: int):
    for book in books:
        if book["id"] == id:
            return {"book details": book}
    return {"message": "Book not found"}