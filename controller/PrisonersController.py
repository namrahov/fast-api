from fastapi import File

from db.database import db_dependency as db_depenceny
from main import app
from service.PrisonersService import *


@app.post("/upload-real-excel-stream")
async def upload_excel_stream(
        file: UploadFile = File(...),
        db: db_depenceny = None
):
    result = await PrisonersService(db).save_real_excel_stream(file)
    return result