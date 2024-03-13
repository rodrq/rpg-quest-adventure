from fastapi import Depends, Path

from src.auth import jwt
from src.character import exceptions, service
from src.character.schemas import CharacterBase


async def valid_character_create(character: CharacterBase):
    # Checks if character name is taken
    if await service.get_character(character.name):
        raise exceptions.CharacterNameTaken
    return character


async def valid_user_character_fetch(
    character_name: str = Path(), user_id: int = Depends(jwt.parse_jwt_user_data)
):
    # Checks if character exists and if it's owned by the requester
    character = await service.get_user_character(character_name, user_id)
    if not character:
        raise exceptions.CharacterNotFound
    return character
