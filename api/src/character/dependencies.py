from fastapi import Depends, Path

from src.auth import jwt
from src.auth import service as auth_service
from src.character import service
from src.character.exceptions import (
    CharacterNameTaken,
    CharacterNotFound,
    EmptySelectedCharacter,
)
from src.character.schemas import CharacterBase, CharacterSchema


async def valid_character_create(character: CharacterBase):
    # Checks if character name is taken
    if await service.get_character(character.name):
        raise CharacterNameTaken
    return character


async def get_valid_auth_character(
    character_name: str = Path(), user_id: int = Depends(jwt.parse_jwt_user_data)
):
    # Checks if character exists and if it's owned by the requester
    character = await service.get_character_by_user_id(character_name, user_id)
    if not character:
        raise CharacterNotFound
    return CharacterSchema(**character)


async def get_selected_character(user_id: int = Depends(jwt.parse_jwt_user_data)) -> CharacterSchema:
    user = await auth_service.get_user_by_id(user_id)
    if user.selected_character is None:
        raise EmptySelectedCharacter()
    character = await service.get_character(user.selected_character)
    return CharacterSchema.model_validate(character)
