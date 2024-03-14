from datetime import datetime, timedelta, timezone

from fastapi import Cookie
from jose import JWTError, jwt

from src.auth.config import auth_config
from src.auth.exceptions import AuthRequired, InvalidToken
from src.config import settings


def create_access_token(user_id: int, expires_delta=timedelta(hours=auth_config.JWT_EXP)):
    jwt_data = {"sub": str(user_id), "exp": datetime.now(timezone.utc) + expires_delta}
    access_token = jwt.encode(jwt_data, settings.JWT_SECRET, auth_config.JWT_ALG)
    return access_token


async def parse_jwt_user_data(access_token: str = Cookie(default=None)):
    if not access_token:
        raise AuthRequired()

    try:
        payload = jwt.decode(access_token, auth_config.JWT_SECRET, algorithms=[auth_config.JWT_ALG])

    except JWTError:
        raise InvalidToken()

    return int(payload["sub"])
