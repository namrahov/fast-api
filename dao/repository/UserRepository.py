from dao.entity.User import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from model.exception.NotFoundException import NotFoundException
from model.exception.UserAlreadyExistsException import UserAlreadyExistsException
from sqlalchemy.orm import joinedload

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

    def get_user_by_id(self, user_id: int):
        user = (
            self.db.query(User)
            .options(joinedload(User.role))   # ⭐ Auto join
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            not_found_message = f"User with id={user_id} not found"
            raise NotFoundException(not_found_message)

        return user
