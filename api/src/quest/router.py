# from typing import Annotated
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from src.quest.service import (create_quest_handler,
#                                 get_self_quests_handler,
#                                 get_quest_handler,
#                                 get_character_quests_handler)
# from src.database import character
# from src.character.dependencies import get_current_character, get_current_character_username


# router = APIRouter(prefix='/quest', tags=['Quests'])


# @router.post("/create")
# async def create_quest(current_character: Annotated[character, Depends(get_current_character)]):

#     return await create_quest_handler(current_character)


# @router.get("/all/self")
# async def get_quests(current_character_username: Annotated[str, Depends(get_current_character_username)]):

#     return await get_self_quests_handler(current_character_username)


# @router.get("/id/{quest_id}")
# async def get_quest(quest_id: int):
#     return await get_quest_handler(quest_id)


# @router.get("/all/{character_username}")
# async def get_character_quests(character_username: str):

#     return await get_character_quests_handler(character_username, db)
