from dao.entity.User import User
from sqlalchemy.orm import Session


def save_all_users(users, db: Session):
    try:
        user_objects = [User(name=u["name"], email=u["email"]) for u in users]
        db.add_all(user_objects)
        db.commit()
        print(f"✅ Saved {len(user_objects)} users.")
        return user_objects
    except Exception as e:
        db.rollback()
        print(f"❌ Error saving users: {e}")
        raise

#
# def save_user(name, email):
#     session = SessionLocal()
#     try:
#         user = User(name=name, email=email)
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         print(f"✅ Saved user: {user}")
#     except Exception as e:
#         session.rollback()
#         print(f"❌ Error: {e}")
#     finally:
#         session.close()
