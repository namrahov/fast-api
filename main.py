from fastapi import FastAPI
from TodoApp.database import engine, Base
import importlib
import pkgutil
import controller

# Initialize FastAPI app
app = FastAPI()

# Dynamically import all controller modules
def load_controllers(package):
    package_path = package.__path__
    for _, name, _ in pkgutil.iter_modules(package_path):
        importlib.import_module(f"{package.__name__}.{name}")

load_controllers(controller)

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
