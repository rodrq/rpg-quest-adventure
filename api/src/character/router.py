# from typing import Any
# from fastapi import APIRouter, Depends
# from sqlalchemy import insert
# from src.database import character, fetch_one
# from src.character.schemas import CharacterInDb

# router = APIRouter(tags=['Character creation'])

# @router.post("/character")
# async def create_character(character_form: CharacterInDb = Depends(valid_character_create)) -> dict[str, Any] | None:
   


# @router.get('/data')
# async def self_character_gamedata(
#     current_character: Annotated[Character, Depends(get_current_character)]
# ):
#     character_gamedata = convert_character_to_gamedata(current_character)
#     return character_gamedata


# @router.post('/reset')
# async def reset_character(
#     current_character: Annotated[Character, Depends(get_current_character)]):
#     return reset_character_gamedata(current_character)
