from fastapi import APIRouter, Depends
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.schemas import ChosenApproach
from src.models.models import Approach, Quest
from src.utils.auth import get_current_character_id
from typing import Annotated
from src.handlers.play import roll_success_handler, roll_failure_handler
import random

router = APIRouter(prefix='/play', tags=['Play'])


@router.post('/roll')
async def roll_and_game(current_character: Annotated[str, Depends(get_current_character_id)],
                         chosen_approach: ChosenApproach, db: Session = Depends(get_db)):
    dice_roll = random.randint(1, 100)
    approach = db.query(Approach).filter(Approach.approach_id == chosen_approach.approach_id).first()
    chance_of_success = approach.chance_of_success
    if dice_roll < chance_of_success:
        honor_gained = (100 - chance_of_success) * 10
        return roll_success_handler(honor_gained, current_character, db)
    else:
        return roll_failure_handler(current_character, db)
    
    
# @router.get('/approach/{quest_id}')
# async def get_approaches(quest_id: int, current_character: str = Depends(get_current_character_id), db: Session = Depends(get_db)):
#     approaches = db.query(Approach).filter(Approach.quest_id == quest_id).all()
#     return approaches