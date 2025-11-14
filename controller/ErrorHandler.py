

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from model.exception.UserAlreadyExistsException import UserAlreadyExistsException
from model.exception.NotFoundException import NotFoundException
from main import app

@app.exception_handler(UserAlreadyExistsException)
async def user_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "UserAlreadyExists",
            "message": f"User with email '{exc.email}' already exists."
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "InternalServerError",
            "message": str(exc)
        }
    )


@app.exception_handler(NotFoundException)
async def user_not_found_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "NotFound",
            "message": f" not found."
        },
    )
