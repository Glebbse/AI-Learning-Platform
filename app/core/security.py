from datetime import datetime, timedelta, timezone
import hashlib
from jose import jwt

from bcrypt import hashpw, gensalt, checkpw

from hashlib import sha256 

from secrets import token_urlsafe

from cryptography import fernet
from base64 import urlsafe_b64encode

from app.core.config import settings


class Security:
    def __init__(self):
        key_bytes = settings.SECRET_KEY.encode("utf-8")
        key_digest = sha256(key_bytes).digest()
        fernet_key = urlsafe_b64encode(key_digest)
        self._fernet_instance = fernet.Fernet(fernet_key)


    @staticmethod
    def hash_password(password: str) -> str:
        return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
     
    def encrypt(self, encrypted_data: str) -> str:
        return self._fernet_instance.encrypt(encrypted_data.encode("utf-8")).decode("utf-8")
    
    def decrypt(self, encrypted_data: str) -> str:
        return self._fernet_instance.decrypt(encrypted_data.encode("utf-8")).decode("utf-8")


class TokenManager():

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    @staticmethod
    def create_refresh_token() -> str:
        return token_urlsafe(64)

    @staticmethod
    def hash_refresh_token(token: str) -> str:
        return hashlib.sha256(token.encode("utf-8")).hexdigest()

    @staticmethod
    def get_refresh_token_expires_at() -> datetime:
        return datetime.now(timezone.utc) + timedelta(days=30)

secure = Security()
manage_tokens = TokenManager()

