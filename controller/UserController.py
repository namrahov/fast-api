from typing import Annotated
from fastapi import UploadFile, File, Depends, status
from sqlalchemy.orm import Session
from main import app
from db.database import get_session
from service.UserService import upload_excel_file


@app.post("/upload-excel", status_code=status.HTTP_201_CREATED)
async def upload_excel(
        file: UploadFile = File(...),
        db: Annotated[Session, Depends(get_session)] = None
):
    await upload_excel_file(file, db)
