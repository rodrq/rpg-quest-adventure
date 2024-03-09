from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.character.service import get_character_query
from .security import verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")





def authenticate_character(username: str, password: str, db: Session):
    character = get_character_query(username, db)
    if not character or not verify_password(password, character.hashed_password):
        return None
    return character
