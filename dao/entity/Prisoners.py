from sqlalchemy import Column, Integer, String, Date, Boolean, TIMESTAMP
from db.database import Base


class Prisoners(Base):
    __tablename__ = "prisoners"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255), nullable=False)
    organization_id = Column(Integer, nullable=True)
    module_id = Column(Integer, nullable=True)
    sub_module_id = Column(Integer, nullable=True)
    division = Column(Integer, nullable=True)
    personal_number = Column(Integer, nullable=True)

    last_meet_date = Column(Date, nullable=True)

    photo_id = Column(Integer, nullable=True)

    short_term_permit = Column(Integer, nullable=True)
    long_term_permit = Column(Integer, nullable=True)

    visit_item = Column(Integer, nullable=True)
    parcel = Column(Integer, nullable=True)

    article = Column(String(255), nullable=True)
    pin = Column(String(255), nullable=True)

    serial_type_id = Column(Integer, nullable=True)
    serial_number = Column(String(255), nullable=True)
    penalty_period_days = Column(Integer, nullable=True)

    birth_date = Column(Date, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    # Audit columns
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)

    deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Prisoner(id={self.id}, full_name='{self.full_name}', personal_number={self.personal_number}, deleted={self.deleted})>"
