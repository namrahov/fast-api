from dao.entity.User import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_all_users(self, users):
        try:
            user_objects = [User(name=u["name"], email=u["email"]) for u in users]
            self.db.add_all(user_objects)
            self.db.commit()
            print(f"✅ Saved {len(user_objects)} users.")
            return user_objects
        except Exception as e:
            self.db.rollback()
        print(f"❌ Error saving users: {e}")
        raise
