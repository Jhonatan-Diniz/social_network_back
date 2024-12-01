from pwdlib import PasswordHash
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jwt import encode


SECRET_KEY = ''
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = PasswordHash.recommended()


# Hash a string
def get_password_hash(password):
    return pwd_context.hash(password)


# Check the passwords corresponds
def verify_password(given_password, hash_password):
    return pwd_context.verify(given_password, hash_password)


def create_access_token(data: dict):
    data_to_encode = data.copy()
    expire_time = \
        datetime.now(tz=ZoneInfo('UTC')) + \
        timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    data_to_encode.update({'exp': expire_time})
    jwt_token = encode(data_to_encode, SECRET_KEY, ALGORITHM)

    return jwt_token
