from fastapi import APIRouter, Depends
from src.handlers.quest import create_quest_handler, get_quests_handler, get_quest_handler
from src.models.serializers import CharacterName, CharacterGameData
from typing import Annotated
from src.utils.auth import get_current_character, get_current_character_username
from src.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/quest',
                   tags=['Quests'])


@router.post("/create")
async def create_quest(current_character_game_data: Annotated[CharacterGameData, Depends(get_current_character)],
                       db: Session = Depends(get_db)):
    
    return await create_quest_handler(current_character_game_data, db=db)


@router.get("/all")
async def get_quests(current_character_username: Annotated[CharacterName, Depends(get_current_character_username)],
                     db: Session = Depends(get_db)):
    
    return await get_quests_handler(current_character_username, db)


@router.get("/{quest_id}")
async def get_quest(quest_id: int,
                    current_character_username: Annotated[CharacterName, Depends(get_current_character_username)],
                    db: Session = Depends(get_db)):
    
    return await get_quest_handler(current_character_username.username, quest_id, db)
    