from typing import Any
from src.database import fetch_one
from sqlalchemy import select, insert
from src.auth.models import User
from src.auth.schemas import UserForm
from src.auth.security import hash_password, check_password
from src.auth.exceptions import InvalidCredentials


async def create_user(user_form: UserForm):
    insert_query = (
        insert(User)
        .values(
            username = user_form.username,
            hashed_password = hash_password(user_form.password)
        )
        .returning(User)
    )
    
    return await fetch_one(insert_query)


async def authenticate_user(user_form: UserForm):
    user = await get_user_by_username(user_form.username)
    if not user:
        raise InvalidCredentials()
    if not check_password(user_form.password, user["hashed_password"]):
        raise InvalidCredentials()

    return User(**user)


async def get_user_by_username(username: str):
    select_query = select(User).where(User.username == username)
    
    return await fetch_one(select_query)


async def get_user_by_id(user_id: int) -> dict[str, Any] | None:
    select_query = select(User).where(User.id == user_id)

    return await fetch_one(select_query)


