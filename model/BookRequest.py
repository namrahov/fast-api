from typing import Optional

from pydantic.v1 import BaseModel, Field


class BookRequest(BaseModel):
  id: Optional[int] = None
  title: str = Field(..., max_length=3)
  description: str
  rating: int