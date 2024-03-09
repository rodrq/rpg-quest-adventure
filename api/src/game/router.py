from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from src.character.models import Character
from src.character.dependencies import get_current_character
from src.game.schemas import ChosenApproach
from src.game.service import roll_handler
from src.database import get_db

game_router = APIRouter(prefix='/game', tags=['Game'])


@game_router.post('/roll')
async def roll_dice(current_character: Annotated[Character, Depends(get_current_character)],
                    chosen_approach: ChosenApproach,
                    db: Session = Depends(get_db)):

    return roll_handler(current_character, chosen_approach, db)
