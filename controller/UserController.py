from fastapi import File, Depends, status
from main import app
from db.database import get_session, db_dependency as db_depenceny
from service.UserService import *


@app.post("/upload-excel", status_code=status.HTTP_201_CREATED)
async def upload_excel(file: UploadFile = File(...), db: db_depenceny = None):
    await UserService(db).upload_excel_file(file)
