from dao.entity.User import User
from sqlalchemy.orm import Session
from model.exception.UserAlreadyExistsException import UserAlreadyExistsException
from sqlalchemy.exc import IntegrityError


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
            raise e

    def save_user(self, user):
        try:
            self.db.add(user)
            self.db.commit()
            return user
        except IntegrityError:
            self.db.rollback()
            raise UserAlreadyExistsException(user.email)
        except Exception as e:
            self.db.rollback()
            raise e

