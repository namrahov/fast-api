from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str
