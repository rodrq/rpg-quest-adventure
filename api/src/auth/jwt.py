from datetime import datetime, timedelta
from jose import JWTError, jwt
from src.config import Settings
from .exceptions import credentials_exception

def create_access_token(data: dict, expires_delta=timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Settings().HASH_SECRET_KEY, "HS256")
    return encoded_jwt


def decode_jwt_token_sub(token: str):
    try:
        payload = jwt.decode(
            token, Settings().HASH_SECRET_KEY, algorithms="HS256")
        jwt_character_username: str = payload.get("sub")
        if jwt_character_username is None:
            raise credentials_exception
        return jwt_character_username

    except JWTError as exc:
        raise credentials_exception from exc
