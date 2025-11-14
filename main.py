from fastapi import FastAPI

from dotenv import load_dotenv
# ✅ Load environment variables
load_dotenv("application-local.env")

from db.database import engine, Base
import importlib
import pkgutil
import controller
import uvicorn
import os
import dao.entity as entity

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Dynamically import all controller modules
def load_controllers(package):
    package_path = package.__path__
    for _, name, _ in pkgutil.iter_modules(package_path):
        importlib.import_module(f"{package.__name__}.{name}")

# Load all controllers so routes are registered
load_controllers(controller)

def load_models(package):
    for _, module, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package.__name__}.{module}")

load_models(entity)

# ✅ Initialize database tables
def setup_database():
    Base.metadata.create_all(bind=engine)

# ✅ Run the server
def run_server():
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))
    uvicorn.run("main:app", host=host, port=port, reload=True)

# ✅ Main entry point
if __name__ == "__main__":
    setup_database()
    run_server()
