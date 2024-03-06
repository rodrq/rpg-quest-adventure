from fastapi import APIRouter, Depends, status
from src.handlers.quest import create_quest_handler, get_self_quests_handler, get_quest_handler, get_character_quests_handler
from src.models.models import Character
from typing import Annotated
from src.utils.auth import get_current_character, get_current_character_username
from src.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/quest',
                   tags=['Quests'])


@router.post("/create")
async def create_quest(current_character: Annotated[Character, Depends(get_current_character)],
                       db: Session = Depends(get_db)):
    
    return await create_quest_handler(current_character, db)


@router.get("/all/self")
async def get_quests(current_character_username: Annotated[str, Depends(get_current_character_username)],
                     db: Session = Depends(get_db)):
    
    return await get_self_quests_handler(current_character_username, db)


@router.get("/id/{quest_id}")
async def get_quest(quest_id: int,
                    db: Session = Depends(get_db)):
    return await get_quest_handler(quest_id, db)
    

@router.get("/all/{character_username}")
async def get_character_quests(character_username: str,
                               db: Session = Depends(get_db)):
    
    return await get_character_quests_handler(character_username, db)

