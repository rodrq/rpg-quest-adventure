from fastapi import Depends, Path

from src.character.dependencies import get_selected_character
from src.character.exceptions import EmptySelectedCharacter
from src.character.schemas import CharacterSchema
from src.quest import service
from src.quest.exceptions import (
    CharacterStateDead,
    CharacterStateWinner,
    LastQuestNotCompleted,
)
from src.quest.schemas import QuestResponse


async def valid_quest_post(
    selected_character: CharacterSchema = Depends(get_selected_character)
) -> CharacterSchema:
    if not selected_character:
        raise EmptySelectedCharacter()

    if selected_character.state == "winner":
        raise CharacterStateWinner()

    if selected_character.state == "dead":
        raise CharacterStateDead()

    if selected_character.completed_last_quest is False:
        raise LastQuestNotCompleted()

    return selected_character


async def fetch_quest_from_path_id(
    selected_character: CharacterSchema = Depends(get_selected_character), quest_id: int = Path()
) -> QuestResponse:
    return await service.get_selected_character_quest(selected_character, quest_id)
