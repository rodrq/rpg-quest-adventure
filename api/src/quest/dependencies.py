from fastapi import Depends, Path

from src.auth import jwt
from src.auth import service as auth_service
from src.character import service as character_service
from src.character.schemas import CharacterResponse
from src.quest.exceptions import (
    CharacterStateDead,
    CharacterStateWinner,
    EmptySelectedCharacter,
    LastQuestNotCompleted,
)
from src.quest.schemas import ApproachNumber


async def get_user_selected_character(user_id: int = Depends(jwt.parse_jwt_user_data)):
    user = await auth_service.get_user_by_id(user_id)
    if not user.get("selected_character"):
        raise EmptySelectedCharacter()
    return user.get("selected_character")


async def valid_game_character(
    selected_character: str = Depends(get_user_selected_character)
) -> CharacterResponse:
    character = await character_service.get_character(selected_character)
    if not character:
        raise EmptySelectedCharacter()

    if character["state"] == "winner":
        raise CharacterStateWinner()

    if character["state"] == "dead":
        raise CharacterStateDead()

    if character["completed_last_quest"] is False and character["quests"] is not None:
        raise LastQuestNotCompleted()

    return CharacterResponse(**character)


async def valid_approach_number(approach_number: int = Path()):
    return ApproachNumber(**approach_number)
