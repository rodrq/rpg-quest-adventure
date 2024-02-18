from fastapi import APIRouter, Depends
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.schemas import ChosenApproach, CharacterRollData
from src.models.models import Quest, Character
from src.utils.auth import get_current_character
from typing import Annotated
from src.handlers.play import roll_handler


router = APIRouter(prefix='/play', tags=['Play'])


@router.post('/roll')
async def roll_and_game(current_character: Annotated[Character, Depends(get_current_character)],
                         chosen_approach: ChosenApproach, db: Session = Depends(get_db)):
    
    current_character_game_data = CharacterRollData(username=current_character.username,
                                                    class_= current_character.class_,
                                                    honor_points=current_character.honor_points,
                                                    map_level=current_character.map_level,
                                                    char_state=current_character.char_state
                                                    )
    
    return roll_handler(current_character_game_data, chosen_approach, db)
    
    


