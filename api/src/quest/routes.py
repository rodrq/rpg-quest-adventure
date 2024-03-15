from fastapi import APIRouter, Depends

from src.character import service as character_service
from src.character.dependencies import get_selected_character
from src.character.schemas import CharacterSchema
from src.quest import game, service
from src.quest.dependencies import (
    fetch_quest_from_path_id,
    valid_quest_post,
)
from src.quest.exceptions import CharacterStateDead, CharacterStateWinner, QuestAlreadyCompleted
from src.quest.schemas import QuestBase, QuestSchema

router = APIRouter(prefix="/quest", tags=["Quest endpoints"])


@router.post("/create")
async def create_quest(character: CharacterSchema = Depends(valid_quest_post)):
    quest = await service.generate_quest(character)
    # updates characters completed_last_quest to False.
    await character_service.update_character_multiple(character.name, {"completed_last_quest": False})
    return quest


@router.get("/")
async def get_quests(selected_character: CharacterSchema = Depends(get_selected_character)):
    return await service.get_all_quests(selected_character)


@router.get("/{quest_id}")
async def get_quest(quest: QuestSchema = Depends(fetch_quest_from_path_id)):
    if not quest.selected_approach:
        # if quest not finished, hide important game data
        return QuestBase(**quest.model_dump())
    return quest


@router.post("/play/{quest_id}/{approach_number}")
async def play_quest_approach(
    approach_number: int,
    quest: QuestSchema = Depends(fetch_quest_from_path_id),
    character: CharacterSchema = Depends(get_selected_character),
):
    if character.state == "dead":
        raise CharacterStateDead
    if character.state == "winner":
        raise CharacterStateWinner
    if isinstance(quest.survived, bool):
        raise QuestAlreadyCompleted
    return await game.roll_approach(approach_number, quest, character)
