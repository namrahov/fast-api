from fastapi import FastAPI
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

