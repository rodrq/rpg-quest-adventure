from sqlalchemy import delete, func, insert, select, update
from sqlalchemy.sql import text

from src.auth.models import User
from src.character.models import Character
from src.character.schemas import CharacterBase
from src.database import execute, fetch_all, fetch_one


async def create_character(character_form: CharacterBase, user_id: int) -> Character:
    insert_query = (
        insert(Character)
        .values(
            user_id=user_id,
            name=character_form.name,
            class_=character_form.class_,
            virtue=character_form.virtue,
            flaw=character_form.flaw,
        )
        .returning(Character)
    )
    return await fetch_one(insert_query)


async def add_to_users_character_list(character_name, user_id):
    update_query = (
        update(User).where(User.id == user_id).values(characters=User.characters + [character_name])
    )
    await execute(update_query)


async def delete_from_users_character_list(character_name, user_id):
    update_query = (
        update(User)
        .where(User.id == user_id)
        .values(characters=func.array_remove(User.characters, character_name))
    )
    await execute(update_query)


async def get_all_user_characters(user_id: int):
    select_query = select(Character).where(Character.user_id == user_id)
    return await fetch_all(select_query)


async def get_character(name: str) -> Character | None:
    select_query = select(Character).where(Character.name == name)

    return await fetch_one(select_query)


async def get_user_character(character_name: str, user_id: int):
    select_query = select(Character).where(
        (Character.name == character_name) & (Character.user_id == user_id)
    )
    return await fetch_one(select_query)


async def delete_character(character_name: str):
    delete_query = delete(Character).where(Character.name == character_name)
    return await execute(delete_query)


async def reset_character_by_name(character_name: str):
    update_query = (
        update(Character)
        .where(Character.name == character_name)
        .values(
            state="adventuring",
            valor_points=0,
            map_level=1,
            times_reset=text("times_reset + 1"),
            completed_last_quest=False,
        )
        .returning(Character)
    )

    return await fetch_one(update_query)


async def update_user_selected_character(character_name: str | None, user_id: int):
    update_query = (
        update(User).where(User.id == user_id).values(selected_character=character_name).returning(User)
    ).returning(User)

    return await fetch_one(update_query)
