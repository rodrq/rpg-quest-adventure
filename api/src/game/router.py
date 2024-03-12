from fastapi import APIRouter, Depends
from src.character.dependencies import valid_user_character_fetch
from src.game import service

# from sqlalchemy.orm import Session
# from typing import Annotated
# from src.database import character
# from src.character.dependencies import get_current_character
# from src.game.schemas import ChosenApproach
# from src.game.service import roll_handler

router = APIRouter(prefix='/game', tags=['Game'])

# @router.post('/roll')
# async def roll_dice(current_character: Annotated[character, Depends(get_current_character)],
#                     chosen_approach: ChosenApproach):

#     return roll_handler(current_character, chosen_approach)
