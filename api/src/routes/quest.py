from fastapi import APIRouter, Depends
from src.handlers.quest import create_quest_handler, get_quests_handler, get_quest_handler
from src.models.schemas import CharacterName, CharacterParams
from typing import Annotated
from src.utils.auth import get_current_character, get_current_character_id
from src.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/quest',
                   tags=['Quests'])


@router.post("/")
async def create_quest(current_character: Annotated[CharacterParams, Depends(get_current_character)],
                       db: Session = Depends(get_db)):
    
    return await create_quest_handler(username = current_character.username, 
                                         class_= current_character.class_,
                                         map_level = current_character.map_level,
                                         virtue = current_character.virtue,
                                         flaw= current_character.flaw,
                                         db=db)


@router.get("/all")
async def get_quests(current_character_id: Annotated[CharacterName, Depends(get_current_character_id)],
                     db: Session = Depends(get_db)):
    
    return await get_quests_handler(current_character_id, db)


@router.get("/{quest_id}")
async def get_quest(quest_id: int,
                    current_character_id: Annotated[CharacterName, Depends(get_current_character_id)],
                    db: Session = Depends(get_db)):
    
    return await get_quest_handler(current_character_id.username, quest_id, db)
    