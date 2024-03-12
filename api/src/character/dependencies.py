from fastapi import Depends, Path

from src.auth import jwt
from src.character import exceptions, service
from src.character.schemas import CharacterBase


async def valid_character_create(character: CharacterBase):
    if await service.get_character_by_name(character.name):
        raise exceptions.CharacterNameTaken
    return character


async def valid_user_character_fetch(
    character_name: str = Path(), user_id: int = Depends(jwt.parse_jwt_user_data)
):
    if await service.get_user_character_by_name(character_name, user_id):
        return character_name
    raise exceptions.CharacterNotYours


async def valid_user_character_delete(
    character_name: str = Path(), user_id: int = Depends(jwt.parse_jwt_user_data)
):
    if await service.get_user_character_by_name(character_name, user_id):
        return character_name
    raise exceptions.CharacterCantBeDeleted
