from starlette.exceptions import HTTPException
import io
from fastapi import UploadFile
from dao.repository.UserRepository import *
import openpyxl


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.userRepo = UserRepository(db)

    async def upload_excel_file(self, file: UploadFile):
        if not file.filename.endswith((".xlsx", ".xls")):
            raise HTTPException(status_code=403, detail="Invalid file type. Only .xlsx or .xls allowed.")

        content = await file.read()
        workbook = openpyxl.load_workbook(io.BytesIO(content))

        users = []

        for sheet in workbook.sheetnames:
            ws = workbook[sheet]
        print(f"📄 Reading sheet: {sheet}")

        for row in ws.iter_rows(values_only=True):
            if row and len(row) >= 2:  # ensure at least two columns
                name, email = row[0], row[1]
                if name and email:  # skip empty rows
                    users.append({"name": name, "email": email})

        self.userRepo.save_all_users(users)
