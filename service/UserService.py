from dao.entity.User import User
from TodoApp.database import SessionLocal
from starlette.exceptions import HTTPException
import io
from fastapi import UploadFile
import openpyxl


async def upload_excel_file(file: UploadFile):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=403, detail="Invalid file type. Only .xlsx or .xls allowed.")

    # Read uploaded file into memory
    content = await file.read()
    workbook = openpyxl.load_workbook(io.BytesIO(content))

    users = []  # collect all user rows

    for sheet in workbook.sheetnames:
        ws = workbook[sheet]
    print(f"📄 Reading sheet: {sheet}")

    for row in ws.iter_rows(values_only=True):
        if row and len(row) >= 2:  # ensure at least two columns
            name, email = row[0], row[1]
            if name and email:  # skip empty rows
                users.append({"name": name, "email": email})

    if users:
        save_all_users(users)
        return {"message": f"✅ {len(users)} users saved successfully!"}
    else:
        return {"warning": "⚠️ No valid rows found to save."}





def save_all_users(users):
    """
    users: list of dicts or tuples, e.g.
    [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]
    """
    session = SessionLocal()
    try:
        user_objects = [User(name=u["name"], email=u["email"]) for u in users]
        session.add_all(user_objects)
        session.commit()
        print(f"✅ Saved {len(user_objects)} users.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error saving users: {e}")
    finally:
        session.close()


#
# def save_user(name, email):
#     session = SessionLocal()
#     try:
#         user = User(name=name, email=email)
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         print(f"✅ Saved user: {user}")
#     except Exception as e:
#         session.rollback()
#         print(f"❌ Error: {e}")
#     finally:
#         session.close()
