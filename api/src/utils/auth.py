from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from src.utils.query import get_character_query
from src.utils.pw_hash import verify_password
from src.config.settings import Settings
from src.models.models import Character
from src.models.enums import UserRoles
from src.config.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


def create_access_token(data: dict, expires_delta=timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Settings().HASH_SECRET_KEY, "HS256")
    return encoded_jwt


credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


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


def get_current_character_username(token: str = Depends(oauth2_scheme)):
    character_name = decode_jwt_token_sub(token)
    return character_name


def get_current_character(character_name: str = Depends(get_current_character_username),
                          db: Session = Depends(get_db)):
    character = get_character_query(username=character_name, db=db)
    if character is None:
        raise credentials_exception
    return character


def authenticate_character(username: str, password: str, db: Session):
    character = get_character_query(username, db)
    if not character or not verify_password(password, character.hashed_password):
        return None
    return character


def get_current_admin_user(current_user: Character = Depends(get_current_character)):
    if current_user.role != UserRoles.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this resource",
        )
    return current_user
