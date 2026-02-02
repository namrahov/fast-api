from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(120))
    hashed_password = Column(String)
    active = Column(Boolean, default=False)
    nurlan = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")   # ⭐ THIS ENABLES NESTED RETURN

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', active={self.active},  nurlan={self.nurlan}, role='{self.role}')>"
