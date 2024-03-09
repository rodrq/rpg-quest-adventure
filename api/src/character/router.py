from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from .models import Character
from .schemas import CharacterInDb
from .service import create_character_handler
from .dependencies import get_current_character
from src.game.utils import convert_character_to_gamedata
from src.game.service import reset_character_gamedata

character_router = APIRouter(prefix='/character', tags=['Character creation'])

@character_router.post('/create')
async def create_character(
    character: CharacterInDb,
    db: Session = Depends(get_db)
):
    return await create_character_handler(character, db)


@character_router.get('/data')
async def self_character_gamedata(
    current_character: Annotated[Character, Depends(get_current_character)]
):
    character_gamedata = convert_character_to_gamedata(current_character)
    return character_gamedata


@character_router.post('/reset')
async def reset_character(
    current_character: Annotated[Character, Depends(get_current_character)],
    db: Session = Depends(get_db)
):
    return reset_character_gamedata(current_character, db)
