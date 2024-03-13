import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import List

import google.generativeai as genai
import orjson
from sqlalchemy import insert, select, update

from src.character.models import Character
from src.character.schemas import CharacterResponse
from src.config import settings
from src.database import execute, fetch_all, fetch_one
from src.quest.exceptions import QuestBelongsToAnotherCharacter, QuestNotFound
from src.quest.llm import create_quest_prompt, prompt_maps_dict
from src.quest.models import Quest


async def generate_quest(character: CharacterResponse) -> Quest:
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

    result = orjson.loads(response.text)
    insert_query = (
        insert(Quest)
        .values(
            character_name=character.name,
            title=result["title"],
            description=result["description"],
            approaches=result["approaches"],
            character_map_level=character.map_level,
        )
        .returning(Quest)
    )
    return await fetch_one(insert_query)


async def get_all_quests(current_character: str) -> List[Quest]:
    select_query = select(Quest).where(Quest.character_name == current_character)
    return await fetch_all(select_query)


async def update_characters_completed_last_quest(character_name: str, value: bool) -> None:
    update_query = (
        update(Character).where(Character.name == character_name).values(completed_last_quest=value)
    )
    return await execute(update_query)


async def get_quest(quest_id) -> Quest | None:
    select_query = select(Quest).where(Quest.id == quest_id)
    return await fetch_one(select_query)


async def get_selected_character_quest(selected_character: str, quest_id: int) -> Quest | None:
    quest = await get_quest(quest_id)
    if not quest:
        raise QuestNotFound()

    if quest["character_name"] != selected_character:
        raise QuestBelongsToAnotherCharacter()

    return quest


# async def create_quest_handler(selected_character: Character, db: Session):
#     try:
#         if selected_character.char_state in ('dead', 'winner'):
#             raise DeadOrWinner(
#                 """Can't play anymore. Your character's either dead or yourjourney came
#               to an end after exploring the whole world and coming victorious."""
#             )
#         if selected_character.quests:
#             last_quest: Quest = (selected_character.quests
#                                  .options(joinedload(Quest.character))
#                                  .order_by(desc(Quest.created_at))
#                                  .first())

#             if last_quest and last_quest.selected_approach is None:
#                 raise LastQuestNotFinished(
#                     f"""Can't create quest. Please finish your last one called '{
#                         last_quest.title}' """
#                 )

#         quest_map = prompt_maps[selected_character.map_level]

#         system_prompt, user_prompt = create_quest_prompt(selected_character.username,
#                                                          selected_character.class_,
#                                                          quest_map,
#                                                          selected_character.virtue,
#                                                          selected_character.flaw)
#         completion = openai_client.chat.completions.create(
#             model="gpt-3.5-turbo-0125",
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_prompt}
#             ],
#             response_format={"type": "json_object"},
#             temperature=1.0
#         )
#         result = orjson.loads(completion.choices[0].message.content)

#         Cost calc
#         usage_tokens = completion.usage
#         cost = (usage_tokens.prompt_tokens * 0.00001) + \
#             (usage_tokens.completion_tokens * 0.00003)

#         quest = Quest(
#             title=result['title'],
#             description=result['description'],
#             character_username=current_character.username,
#             approaches=result['approaches'],
#             cost=cost
#         )
#         db.add(quest)
#         db.commit()

#         #serialize response to not expose game secret data
#         response = QuestResponse.model_validate(quest, from_attributes=True)
#         serialized_quest = response.model_dump()
#         return JSONResponse(status_code=status.HTTP_201_CREATED,
#                             content={"quest": serialized_quest})

#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


# async def get_self_quests_handler(current_character_username: str, db: Session):
#     try:
#         quests = db.query(Quest).filter(
#             Quest.character_username == current_character_username).all()
#         if not quests:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail=f"{current_character_username} didn't generate any quest yet.")

#         If quest hasn't been completed, hide quest success chance, and choices descriptions.
#         serialized_quests = []
#         for quest in quests:
#             if quest.selected_approach is None:
#                 quest = QuestResponse.model_validate(
#                     quest, from_attributes=True)
#                 quest = quest.model_dump()
#                 serialized_quests.append(quest)
#             else:
#                 serialized_quests.append(quest)
#         return serialized_quests
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


# async def get_quest_handler(quest_id: int, db: Session):
#     try:
#         quest: Quest = db.query(Quest).filter(
#             Quest.quest_id == quest_id).first()

#         if not quest:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail="Quest doesn't exist")
#         If quest hasn't been completed, hide quest success chance, and choices descriptions.
#         if quest.selected_approach is None:
#             quest = QuestResponse.model_validate(quest, from_attributes=True)
#             return quest.model_dump()
#         return quest
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


# async def get_character_quests_handler(character_username: str, db: Session):
#     try:
#         quests = db.query(Quest).filter(
#             Quest.character_username == character_username).all()
#         if not quests:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail=f"{character_username} didn't generate any quest yet.")

#         If quest hasn't been completed, hide quest success chance, and choices descriptions.
#         serialized_quests = []
#         for quest in quests:
#             if quest.selected_approach is None:
#                 quest = QuestResponse.model_validate(
#                     quest, from_attributes=True)
#                 quest = quest.model_dump()
#                 serialized_quests.append(quest)
#             else:
#                 serialized_quests.append(quest)
#         return serialized_quests
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
