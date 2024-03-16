import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import List

import google.generativeai as genai
import json_repair
import orjson
from sqlalchemy import insert, select, update

from src.character.models import Character
from src.character.schemas import CharacterSchema
from src.config import settings
from src.database import execute, fetch_all, fetch_one
from src.quest.exceptions import QuestBelongsToAnotherCharacter, QuestNotFound
from src.quest.llm import create_quest_prompt, prompt_maps_dict
from src.quest.models import Quest
from src.quest.schemas import QuestBase, QuestSchema


async def generate_quest(character: CharacterSchema) -> QuestBase | None:
    genai.configure(api_key=settings.GEMINI_API_KEY)

    model = genai.GenerativeModel("gemini-pro")

    quest_map = prompt_maps_dict[character.map_level]

    system_prompt, user_prompt = create_quest_prompt(
        character.name, character.class_, quest_map, character.virtue, character.flaw
    )

    def generate_content_sync():
        return model.generate_content(
            f"""System role: {system_prompt}.
                User role: {user_prompt}. """,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                temperature=1.0,
            ),
        )

    # execute llm in separate thread to not block I/O
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    response = await loop.run_in_executor(executor, generate_content_sync)

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
        raise QuestNotFound()
    return QuestSchema(**quest)


async def get_selected_character_quest(selected_character: CharacterSchema, quest_id: int) -> QuestSchema:
    quest = await get_quest(quest_id)
    if not quest:
        raise QuestNotFound()

    if quest.character_name != selected_character.name:
        raise QuestBelongsToAnotherCharacter()
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
