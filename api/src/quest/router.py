from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.quest.service import (create_quest_handler,
                                get_self_quests_handler,
                                get_quest_handler,
                                get_character_quests_handler)
from src.character.models import Character
from src.character.dependencies import get_current_character, get_current_character_username
from src.database import get_db


quest_router = APIRouter(prefix='/quest', tags=['Quests'])


@quest_router.post("/create")
async def create_quest(current_character: Annotated[Character, Depends(get_current_character)],
                       db: Session = Depends(get_db)):

    return await create_quest_handler(current_character, db)


@quest_router.get("/all/self")
async def get_quests(current_character_username: Annotated[str, Depends(get_current_character_username)],
                     db: Session = Depends(get_db)):

    return await get_self_quests_handler(current_character_username, db)


@quest_router.get("/id/{quest_id}")
async def get_quest(quest_id: int,
                    db: Session = Depends(get_db)):
    return await get_quest_handler(quest_id, db)


@quest_router.get("/all/{character_username}")
async def get_character_quests(character_username: str,
                               db: Session = Depends(get_db)):

    return await get_character_quests_handler(character_username, db)
