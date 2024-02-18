from fastapi import APIRouter, Depends
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.schemas import ChosenApproach, CharacterGameData
from src.utils.auth import get_current_character
from typing import Annotated
from src.handlers.play import roll_handler


router = APIRouter(prefix='/play', tags=['Play'])


@router.post('/roll')
async def roll_and_game(current_character_game_data: Annotated[CharacterGameData, Depends(get_current_character)],
                         chosen_approach: ChosenApproach, db: Session = Depends(get_db)):

    return roll_handler(current_character_game_data, chosen_approach, db)
    
    


