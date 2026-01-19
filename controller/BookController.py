from main import app
from starlette import status
from starlette.exceptions import HTTPException
from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Dict
import re
from pathlib import Path
from dao.entity.Book import Book
from model.BookRequest import BookRequest

LOG_FILE_PATH = Path(r"C:\tms.log")  # adjust path

TIMESTAMP_PATTERN = re.compile(
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+) Z\]"
)
USER_ID_PATTERN = re.compile(
    r"(?:userID=|wsSession\.userID=)([a-zA-Z0-9]+)"
)


Books = [
    Book(1, "Fizika", "Fizika kitabi", 3),
    Book(2, "Math", "Riyaziyyat kitabi", 4)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    return Books

@app.post("/create-book",status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    book = Book(**book_request.dict())
    Books.append(book)
    return Books

@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def get_book(id: int):
    for book in Books:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Not Found")

@app.get("/logs/users/latest")
def get_distinct_users_with_last_activity():
    try:
        data = parse_log_file(LOG_FILE_PATH)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file not found")

    return [
        {
            "userId": user_id,
            "lastSeen": ts.isoformat() + "Z"
        }
        for user_id, ts in data.items()
    ]

def parse_log_file(file_path: Path) -> Dict[str, datetime]:
    if not file_path.exists():
        raise FileNotFoundError("Log file not found")

    result: Dict[str, datetime] = {}

    with file_path.open("r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            ts_match = TIMESTAMP_PATTERN.search(line)
            user_match = USER_ID_PATTERN.search(line)

            if not ts_match or not user_match:
                continue

            timestamp = datetime.strptime(
                ts_match.group(1),
                "%Y-%m-%d %H:%M:%S.%f"
            )
            user_id = user_match.group(1)

            if user_id not in result or timestamp > result[user_id]:
                result[user_id] = timestamp

    return result
