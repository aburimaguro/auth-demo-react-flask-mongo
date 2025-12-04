import os
from datetime import datetime, timedelta
import bcrypt
import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
ACCESS_EXPIRES = int(os.getenv("JWT_ACCESS_EXPIRES_SECONDS", "300"))
REFRESH_EXPIRES = int(os.getenv("JWT_REFRESH_EXPIRES_SECONDS", "1209600"))

def hash_password(plain_password: str) -> bytes:
    return bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())

def check_password(plain_password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed)

def create_access_token(user_id: str):
    payload = {
        "sub": str(user_id),
        "type": "access",
        "exp": datetime.utcnow() + timedelta(seconds=ACCESS_EXPIRES),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def create_refresh_token(user_id: str):
    payload = {
        "sub": str(user_id),
        "type": "refresh",
        "exp": datetime.utcnow() + timedelta(seconds=REFRESH_EXPIRES),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except Exception:
        return None

