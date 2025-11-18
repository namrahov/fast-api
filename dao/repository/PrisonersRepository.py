from sqlalchemy.orm import Session
from dao.entity.Prisoners import Prisoners


class PrisonersRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_all_prisoners(self, prisoners_list):
        objects = [Prisoners(**p) for p in prisoners_list]
        self.db.bulk_save_objects(objects)
        self.db.commit()
