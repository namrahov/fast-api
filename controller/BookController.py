from fastapi import FastAPI
from starlette.exceptions import HTTPException

from dao.entity.Book import Book
from model.BookRequest import BookRequest

app = FastAPI()

Books = [
    Book(1, "Fizika", "Fizika kitabi", 3),
    Book(2, "Math", "Riyaziyyat kitabi", 4)
]

@app.get("/books")
async def get_books():
    return Books

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    book = Book(**book_request.dict())
    Books.append(book)
    return Books

@app.get("/books/{id}", status_code=200)
async def get_book(id: int):
    for book in Books:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Not Found")

