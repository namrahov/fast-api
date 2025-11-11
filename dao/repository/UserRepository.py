from dao.entity.User import User
from TodoApp.database import SessionLocal

def save_all_users(users):
    with SessionLocal() as session:
        try:
            user_objects = [User(name=u["name"], email=u["email"]) for u in users]
            session.add_all(user_objects)
            session.commit()
            print(f"✅ Saved {len(user_objects)} users.")
        except Exception as e:
            session.rollback()
            print(f"❌ Error saving users: {e}")

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
