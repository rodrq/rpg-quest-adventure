from fastapi import Depends, Path

from src.auth import jwt
from src.auth import service as auth_service
from src.character import service as character_service
from src.character.schemas import CharacterResponse
from src.quest import service
from src.quest.exceptions import (
    CharacterStateDead,
    CharacterStateWinner,
    EmptySelectedCharacter,
    LastQuestNotCompleted,
)


async def get_user_selected_character(user_id: int = Depends(jwt.parse_jwt_user_data)):
    user = await auth_service.get_user_by_id(user_id)
    return user["selected_character"]


async def valid_game_character(character: str = Depends(get_user_selected_character)) -> CharacterResponse:
    character = await character_service.get_character(character["name"])
    if not character:
        raise EmptySelectedCharacter()

    if character["state"] == "winner":
        raise CharacterStateWinner()

    if character["state"] == "dead":
        raise CharacterStateDead()

    if character["completed_last_quest"] is False:
        raise LastQuestNotCompleted()

    return CharacterResponse(**character)
