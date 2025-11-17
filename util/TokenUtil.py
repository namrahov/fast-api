from datetime import timedelta, datetime
from jose import jwt

SECRET_KEY = 'sfsf23sd2312dfdfs'
ALGORITHM = 'HS256'


class TokenUtil:
    def __init__(self):
        pass

    def generate_token(self, email: str, user_id: int, expires_delta: timedelta):
        encode = {'sub': email, 'id': user_id}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
