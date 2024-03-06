from fastapi import APIRouter, Depends
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.models import Character
from src.models.serializers import ChosenApproach
from src.utils.auth import get_current_character
from typing import Annotated
from src.handlers.play import roll_handler


router = APIRouter(prefix='/play', tags=['Play'])


@router.post('/roll')
async def roll_dice(current_character: Annotated[Character, Depends(get_current_character)],
                         chosen_approach: ChosenApproach, 
                         db: Session = Depends(get_db)):
    
    return roll_handler(current_character, chosen_approach, db)
    
    
