from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from db.database import get_session
from dao.entity.User import User
import os

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login")  # or "token", but must match your login route


def get_current_user(
        token: Annotated[str, Depends(oauth2_bearer)],
        db: Annotated[Session, Depends(get_session)],
) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(
            token,
            os.getenv("SECRET_KEY"),
            algorithms=[os.getenv("ALGORITHM")],
        )
        user_id: int | None = payload.get("id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    from dao.repository.UserRepository import UserRepository  # local import to avoid circulars
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_id(user_id)

    return user
