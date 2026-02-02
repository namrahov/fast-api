from sqlalchemy import Column, BigInteger, String
from db.database import Base


class Inquiry(Base):
    __tablename__ = "inquiry"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255))

    def __repr__(self):
        return f"<Inquiry(id={self.id}, name='{self.name}')>"