from datetime import datetime, timedelta
from fastapi import Cookie
from jose import jwt, JWTError
from src.config import settings
from src.auth.config import auth_config
from src.auth.exceptions import InvalidToken, AuthRequired

def create_access_token(user_id: int, expires_delta=timedelta(hours=auth_config.JWT_EXP)):
    jwt_data = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + expires_delta
    }
    access_token = jwt.encode(jwt_data, settings.JWT_SECRET, auth_config.JWT_ALG)
    return access_token


async def parse_jwt_user_data(access_token: str = Cookie(default=None)):
    if not access_token:
        raise AuthRequired()
    
    try:
        payload = jwt.decode(access_token, 
                             auth_config.JWT_SECRET, 
                             algorithms=[auth_config.JWT_ALG])
            
    except JWTError:
        raise InvalidToken()
    
    return int(payload["sub"])
