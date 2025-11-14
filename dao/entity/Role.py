from sqlalchemy import Column, Integer, String
from db.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))


    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"

