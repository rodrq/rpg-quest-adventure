from fastapi import Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.character.exceptions import credentials_exception
from src.character.service import get_character_query
from src.auth.dependencies import oauth2_scheme
from src.auth.jwt import decode_jwt_token_sub


def get_current_character_username(token: str = Depends(oauth2_scheme)):
    character_name = decode_jwt_token_sub(token)
    return character_name


def get_current_character(character_name: str = Depends(get_current_character_username),
                          db: Session = Depends(get_db)):
    character = get_character_query(username=character_name, db=db)
    if character is None:
        raise credentials_exception
    return character