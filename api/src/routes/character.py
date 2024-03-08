from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.models import Character
from src.models.schemas import CharacterInDb
from src.handlers.character import create_character_handler, reset_character_handler
from src.utils.auth import get_current_character
from src.utils.game import convert_character_to_gamedata


router = APIRouter(prefix='/character',
                   tags=['Character creation'])


@router.post('/create')
async def create_character(
    character: CharacterInDb,
    db: Session = Depends(get_db)
):
    return await create_character_handler(character, db)


@router.get('/data')
async def self_character_gamedata(
    current_character: Annotated[Character, Depends(get_current_character)]
):
    character_gamedata = convert_character_to_gamedata(current_character)
    return character_gamedata


@router.post('/reset')
async def reset_character(
    current_character: Annotated[Character, Depends(get_current_character)],
    db: Session = Depends(get_db)
):
    return reset_character_handler(current_character, db)
