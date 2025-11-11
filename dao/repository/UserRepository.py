from dao.entity.User import User
from TodoApp.database import SessionLocal

def save_all_users(users):
    """
    users: list of dicts or tuples, e.g.
    [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]
    """
    session = SessionLocal()
    try:
        user_objects = [User(name=u["name"], email=u["email"]) for u in users]
        session.add_all(user_objects)
        session.commit()
        print(f"✅ Saved {len(user_objects)} users.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error saving users: {e}")
    finally:
        session.close()

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
