from pydantic.v1 import BaseModel


class BookRequest(BaseModel):
  id: int
  title: str
  description: str
  rating: int