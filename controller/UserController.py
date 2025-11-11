from main import app   # import the SAME app

from starlette import status
from fastapi import File
from service.UserService import *


@app.post("/upload-excel", status_code=status.HTTP_201_CREATED)
async def upload_excel(file: UploadFile = File(...)):
   await upload_excel_file(file)
   return

