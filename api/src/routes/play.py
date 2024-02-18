from fastapi import APIRouter, Depends
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.schemas import ChosenApproach, Approach
from src.models.models import Quest
from src.utils.auth import get_current_character
from typing import Annotated
from src.handlers.play import roll_success_handler, roll_failure_handler
import random

router = APIRouter(prefix='/play', tags=['Play'])


@router.post('/roll')
async def roll_and_game(current_character: Annotated[str, Depends(get_current_character)],
                         chosen_approach: ChosenApproach, db: Session = Depends(get_db)):
    dice_roll = random.randint(1, 100)
    quest = db.query(Quest).filter(Quest.quest_id == chosen_approach.quest_id).first()
    if quest:
        try:
            #TODO: ADD APPROACH_NUMBER VALIDATION 1 TO 3
            approach = quest.approaches[f'approach_{chosen_approach.approach_number}']
        except:
            raise ValueError(f"Approach {chosen_approach.approach_number} not found for the quest.")
        
        approach = Approach(choice_description=approach['choice_description'],
                            success_description=approach['success_description'],
                            failure_description=approach['failure_description'],
                            chance_of_success=approach['chance_of_success'])
        
        chance_of_success = approach.chance_of_success
        if dice_roll < chance_of_success:
            honor_gained = (100 - chance_of_success) * 10
            return roll_success_handler(honor_gained, current_character, db)
        else:
            return roll_failure_handler(current_character, db)


