from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.utils.query import get_character
from src.utils.pw_hash import verify_password
from datetime import datetime, timedelta
from src.config.settings import SECRET_KEY, ALGORITHM
from typing import Annotated
from src.models.schemas import CharacterName


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

def create_access_token(data: dict, expires_delta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_character_username(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        jwt_character_username: str = payload.get("sub")
        if jwt_character_username is None:
            raise credentials_exception
        token_data = CharacterName(username=jwt_character_username)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_character(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        jwt_character_username: str = payload.get("sub")
        if jwt_character_username is None:
            raise credentials_exception
        character_name = CharacterName(username=jwt_character_username)
    except JWTError:
        raise credentials_exception
    character = get_character(username=character_name.username)
    if character is None:
        raise credentials_exception
    return character

def authenticate_character(username: str, password: str):
    character = get_character(username)
    if not character or not verify_password(password, character.password):
        return None
    return character


def check_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        if jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]):
            return {'message': 'Token is correct'}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token is incorrect',
            headers={"WWW-Authenticate": "Bearer"},
        )