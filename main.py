from fastapi import FastAPI
from alembic.config import Config
from alembic import command
from dotenv import load_dotenv
# ✅ Load environment variables
load_dotenv("application-local.env")
from db.database import DATABASE_URL
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
# def setup_database():
#     Base.metadata.create_all(bind=engine)
def setup_database():
    """Run Alembic migrations on startup"""
    try:
        alembic_cfg = Config("alembic.ini")
        # ⭐ Set the database URL BEFORE running upgrade
        alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
        command.upgrade(alembic_cfg, "head")
        print("✅ Database migrations applied successfully")
    except Exception as e:
        print(f"❌ Error running migrations: {e}")
        raise

# ✅ Run the server
def run_server():
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))
    uvicorn.run("main:app", host=host, port=port, reload=True)

# ✅ Main entry point
if __name__ == "__main__":
    setup_database()
    run_server()
