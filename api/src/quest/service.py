from typing import List

import json_repair
import orjson
from sqlalchemy import insert, select, update

from src.character.models import Character
from src.character.schemas import CharacterSchema
from src.database import execute, fetch_all, fetch_one
from src.quest import llm
from src.quest.exceptions import QuestNotFound, QuestUnauthorized
from src.quest.models import Quest
from src.quest.schemas import QuestBase, QuestSchema, QuestSummary


async def generate_quest(character: CharacterSchema) -> QuestBase | None:
    response = await llm.generate_quest(character)
    # LLMs sometimes generates markdown template or adds some unnecesary comma so we fix.
    decoded_result = json_repair.repair_json(response.text, skip_json_loads=True)
    result = orjson.loads(decoded_result)
    insert_query = (
        insert(Quest)
        .values(
            character_name=character.name,
            title=result["title"],
            description=result["description"],
            approaches=result["approaches"],
        )
        .returning(Quest)
    )
    created_quest = await fetch_one(insert_query)
    if not created_quest:
        return None
    # since quest is not finished, hide important game data
    return QuestBase(**created_quest)


async def get_all_quests(selected_character: CharacterSchema) -> List[QuestBase | QuestSchema]:
    select_query = select(Quest).where(Quest.character_name == selected_character.name)
    quests = await fetch_all(select_query)
    # if quest not finished, hide important game data
    return [
        QuestBase(**quest) if quest["selected_approach"] is None else QuestSchema(**quest) for quest in quests
    ]


async def get_quest(quest_id) -> QuestSchema | None:
    select_query = select(Quest).where(Quest.id == quest_id)
    quest = await fetch_one(select_query)
    if quest is None:
        raise QuestUnauthorized()
    return QuestSchema(**quest)


async def get_selected_character_quest(selected_character: CharacterSchema, quest_id: int) -> QuestSchema:
    quest = await get_quest(quest_id)
    if not quest:
        raise QuestNotFound()

    if quest.character_name != selected_character.name:
        raise QuestUnauthorized()
    return quest


async def update_game_variables(
    character: CharacterSchema, character_updates: dict, quest: QuestSchema, quest_updates: dict
) -> dict:
    character_query = (
        update(Character).where(Character.name == quest.character_name).values(character_updates)
    )
    quest_query = (
        update(Quest)
        .where((Quest.character_name == character.name) & (Quest.id == quest.id))
        .values(quest_updates)
    )
    await execute(character_query)
    await execute(quest_query)
    return {"message": "character states updated"}


async def orphan_quests(character_name: str) -> dict:
    orphan_quests = update(Quest).where(Quest.character_name == character_name).values(character_name=None)
    await execute(orphan_quests)
    return {"status": 200, "message": "success"}


async def get_character_journey(character_name) -> List[QuestSummary]:
    select_query = select(Quest).where(Quest.character_name == character_name)
    quests = await fetch_all(select_query)

    summarized_quests = [
        QuestSummary(
            title=quest["title"],
            description=quest["description"],
            action=quest["approaches"][f"approach_{quest['selected_approach']}"]["choice_description"],
            consequence=quest["approaches"][f"approach_{quest['selected_approach']}"]["success_description"],
            survived=quest["survived"],
        )
        for quest in quests
    ]
    return summarized_quests
