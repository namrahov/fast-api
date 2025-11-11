from typing import Annotated
from fastapi import File, Depends, status
from main import app
from db.database import get_session
from service.UserService import *


@app.post("/upload-excel", status_code=status.HTTP_201_CREATED)
async def upload_excel(file: UploadFile = File(...), db: Annotated[Session, Depends(get_session)] = None):
    await UserService(db).upload_excel_file(file)
