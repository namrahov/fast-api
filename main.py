from fastapi import FastAPI
from TodoApp.database import engine, Base
from controller import UserController

# Initialize FastAPI app
app = FastAPI()

# Initialize database tables
def setup_database():
    Base.metadata.create_all(bind=engine)

# Run the server
def run_server():
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# Main entry point
if __name__ == "__main__":
    setup_database()
    run_server()
