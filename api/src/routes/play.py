from fastapi import APIRouter, Depends
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.models import Character
from src.models.schemas import ChosenApproach
from src.utils.auth import get_current_character
from typing import Annotated
from src.handlers.play import roll_handler, reset_character_handler
from src.utils.game import convert_character_to_gamedata

router = APIRouter(prefix='/play', tags=['Play'])


@router.post('/roll')
async def roll_and_game(current_character: Annotated[Character, Depends(get_current_character)],
                         chosen_approach: ChosenApproach, 
                         db: Session = Depends(get_db)):
    
    current_character_gamedata = convert_character_to_gamedata(current_character)
    return roll_handler(current_character_gamedata, chosen_approach, db)
    
    
@router.post('/play_again')
async def reset_character(current_character: Annotated[Character, Depends(get_current_character)],
                          db: Session = Depends(get_db)):
    current_character_gamedata = convert_character_to_gamedata(current_character)

    return reset_character_handler(current_character_gamedata, db)