from typing import Annotated, Optional
from datetime import datetime, timedelta
from fastapi import Depends, Cookie
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError
from src.config import settings
from src.auth.config import auth_config
from src.auth.exceptions import AuthorizationFailed, AuthRequired, InvalidToken
from src.auth.schemas import JWTData


def create_token(*, user: dict, expires_delta=timedelta(minutes=auth_config.JWT_EXP)):
    jwt_data = {
        "sub": str(user["id"]),
        "exp": datetime.utcnow() + expires_delta,
        "is_admin": user["is_admin"],
    }
    return jwt.encode(jwt_data, settings.JWT_SECRET, auth_config.JWT_ALG)


async def parse_jwt_user_data(access_token: str = Cookie(default=None),
                              refresh_token: str = Cookie(default=None)):
    
    if not access_token:
        raise AuthRequired()
    
    try:
        payload = jwt.decode(access_token, 
                             auth_config.JWT_SECRET, 
                             algorithms=[auth_config.JWT_ALG])
        
    except ExpiredSignatureError:
        #refresh token
        raise InvalidToken()
    return JWTData(**payload)

async def refresh_expired_access_token(refresh_token: str = Cookie(default=None)):
    if not refresh_token:
        raise AuthRequired()
    
    return