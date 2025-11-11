from fastapi import FastAPI
from TodoApp.database import engine, Base
import dao.entity.User  # 👈 make sure to import your model module
from controller import UserController  # 👈 import after app is created

app = FastAPI()

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
