from typing import Any, List

from sqlalchemy import func, insert, select, update
from sqlalchemy.orm import joinedload

from src.auth.exceptions import InvalidCredentials
from src.auth.models import User
from src.auth.schemas import UserForm
from src.auth.security import check_password, hash_password
from src.database import execute, fetch_all, fetch_one


async def create_user(user_form: UserForm):
    insert_query = (
        insert(User)
        .values(username=user_form.username, hashed_password=hash_password(user_form.password))
        .returning(User)
    )

    return await fetch_one(insert_query)


async def authenticate_user(user_form: UserForm):
    user = await get_user_by_username(user_form.username)
    if not user:
        raise InvalidCredentials()
    if not check_password(user_form.password, user["hashed_password"]):
        raise InvalidCredentials()
    print(user)
    return User(**user)


async def get_user_by_username(username: str):
    select_query = select(User).where(User.username == username)

    return await fetch_one(select_query)


async def get_user_by_id(user_id: int) -> User | None:
    select_query = select(User).where(User.id == user_id)
    return await fetch_one(select_query)


async def get_user_rel_joined_data(user_id: int) -> List[dict]:
    select_query = select(User).options(joinedload(User.characters)).where(User.id == user_id)
    return await fetch_all(select_query)


async def update_value(user_id: int, column_name: str, column_key: Any):
    to_update = {column_name: column_key}
    update_query = update(User).where(User.id == user_id).values(to_update)

    return await execute(update_query)


async def delete_value(user_id: int, column_name: str, column_key: Any, from_list: bool = False):
    if from_list:
        to_update = {column_name: func.array_remove(column_name, column_key)}
    else:
        to_update = {column_name: column_key}
    update_query = update(User).where(User.id == user_id).values(to_update)
    await execute(update_query)
