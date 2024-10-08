from typing import Any, List

from sqlalchemy import delete, func, insert, select, update
from sqlalchemy.orm import joinedload

from src.auth import service as auth_service
from src.auth.models import User
from src.character.exceptions import BadRequest
from src.character.models import Character
from src.character.schemas import CharacterBase, CharacterSchema
from src.database import execute, fetch_all, fetch_one
from src.quest import service as quest_service


async def create_character(character_form: CharacterBase, user_id: int) -> CharacterSchema:
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
    character = await fetch_one(insert_query)
    # set just created character as user's selected_character
    await auth_service.update_value(user_id, "selected_character", character["name"])
    return CharacterSchema.model_validate(character)


async def add_to_users_character_list(character_name, user_id):
    update_query = (
        update(User).where(User.id == user_id).values(characters=User.characters + [character_name])
    )
    await execute(update_query)


async def get_all_user_characters(user_id: int):
    select_query = select(Character).where(Character.user_id == user_id)
    return await fetch_all(select_query)


async def get_character(name: str) -> CharacterSchema:
    select_query = select(Character).where(Character.name == name)

    return await fetch_one(select_query)


async def get_character_by_user_id(character_name: str, user_id: int) -> Character:
    select_query = select(Character).where(
        (Character.name == character_name) & (Character.user_id == user_id)
    )
    return await fetch_one(select_query)


async def after_quest_update_character_data(character_name: str, user_id: int) -> None:
    select_query = (
        select(Character)
        .options(joinedload(Character.quests))
        .where((Character.name == character_name) & (Character.user_id == user_id))
    )
    character_with_quests = await fetch_all(select_query)
    character = CharacterSchema.model_validate(character_with_quests[0])
    quests = [
        {"title": quest["title"], "quest_id": quest["id"], "survived": quest["survived"]}
        for quest in character_with_quests
    ]
    character.created_quests = quests
    character.completed_last_quest = False
    update_query = update(Character).where(Character.name == character_name).values(character.model_dump())
    await execute(update_query)
    return None


async def delete_character(character_name: str):
    delete_query = delete(Character).where(Character.name == character_name)
    return await execute(delete_query)


async def reset_character(character: CharacterSchema):
    factory_settings_character = {
        "state": "adventuring",
        "valor_points": 0,
        "map_level": 1,
        "times_reset": Character.times_reset + 1,
        "completed_last_quest": True,
    }

    await update_character_multiple(character.name, factory_settings_character)
    return await quest_service.orphan_quests(character.name)


async def update_character_value(
    character_name: str, column_name: str, update_value: Any = None, append_value: Any = None
):
    if update_value is None and append_value is None:
        # shouldn't ever happen tbh
        raise BadRequest
    if update_value:
        to_update = {column_name: update_value}
        update_query = update(Character).where(Character.name == character_name).values(to_update)
    else:
        to_append = {column_name: func.array_append(getattr(Character, column_name), append_value)}
        update_query = update(Character).where(Character.name == character_name).values(to_append)
    return await execute(update_query)


async def update_character_multiple(character_name: str, update_values: dict[str, Any]):
    update_query = update(Character).where(Character.name == character_name).values(**update_values)
    await execute(update_query)

    return {"status": 200, "message": "success"}
