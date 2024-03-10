# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from src.character.service import get_character_query
# from .security import verify_password
from src.auth.schemas import UserSchema
from src.auth import service
from src.auth.exceptions import UsernameTaken
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")



async def valid_username_create(user: UserSchema):
    if await service.get_user_by_username(user.username):
        raise UsernameTaken
    return user

# def authenticate_character(username: str, password: str, db: Session):
#     character = get_character_query(username, db)
#     if not character or not verify_password(password, character.hashed_password):
#         return None
#     return character
