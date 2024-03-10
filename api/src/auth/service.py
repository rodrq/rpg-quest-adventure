from typing import Any
import uuid as uuid_lib
from datetime import datetime, timedelta
from pydantic import UUID4
from src.database import fetch_one, execute
from sqlalchemy import select, insert
from src.auth.models import User, RefreshToken
from src.auth.schemas import UserSchema
from src.auth.security import hash_password, check_password
from src.auth.exceptions import InvalidCredentials
from src.auth import utils
from src.auth.config import auth_config


async def create_user(user_form: UserSchema):
    insert_query = (
        insert(User)
        .values(
            username = user_form.username,
            hashed_password = hash_password(user_form.password)
        )
        .returning(User)
    )
    
    return await fetch_one(insert_query)


async def get_user_by_username(username: str):
    select_query = select(User).where(User.username == username)
    
    return await fetch_one(select_query)


async def get_user_by_id(user_id: int) -> dict[str, Any] | None:
    select_query = select(User).where(User.id == user_id)

    return await fetch_one(select_query)


async def authenticate_user(user_form: UserSchema):
    user = await get_user_by_username(user_form.username)
    print(user)
    if not user:
        raise InvalidCredentials()
    if not check_password(user_form.password, user["hashed_password"]):
        raise InvalidCredentials()

    return user


async def create_refresh_token(user_id: int, refresh_token: str | None = None):
    if not refresh_token:
        new_refresh_token = utils.generate_random_alphanum(64)

    insert_query = insert(RefreshToken).values(
        uuid = uuid_lib.uuid4(),
        refresh_token = new_refresh_token,
        expires_at = datetime.utcnow() + timedelta(seconds=auth_config.REFRESH_TOKEN_EXP),
        user_id = user_id
        )
    await execute(insert_query)
    
    return new_refresh_token


    # RefreshToken.uuid = uuid.uuid4(), 
    #              RefreshToken.refresh_token: refresh_token, 
    #              RefreshToken.expires_at=datetime.utcnow() + timedelta(seconds=auth_config.REFRESH_TOKEN_EXP),
    #             RefreshToken.user_id=user_id)
    await execute(insert_query)

    return refresh_token

# def login_for_access_token_handler(form_data: OAuth2PasswordRequestForm, db: Session) -> JSONResponse:
#     try:
#         user = authenticate_character(
#             form_data.username, form_data.password, db)
#         if not user:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Incorrect username or password",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#         access_token_expires = timedelta(minutes=180)
#         access_token = create_access_token(
#             data={"sub": user.username}, expires_delta=access_token_expires
#         )

#         response = JSONResponse(
#             content={"message": "Login succesfull"}, status_code=200)

#         response.set_cookie(key="access_token",
#                             value=f"Bearer {access_token}",
#                             httponly=True)
#         return response

#     except Exception as e:
#         raise HTTPException(
#             status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
