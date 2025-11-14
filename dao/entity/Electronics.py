from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base


class Electronics(Base):
    __tablename__ = "electronics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.id"))
