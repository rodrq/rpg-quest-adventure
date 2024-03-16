from fastapi import APIRouter, Depends

from src.auth import jwt
from src.character import service as character_service
from src.character.dependencies import get_selected_character
from src.character.schemas import CharacterSchema
from src.quest import game, service
from src.quest.dependencies import (
    get_quest_from_id_in_path,
    get_valid_character_for_quest,
)
from src.quest.exceptions import CharacterStateDead, CharacterStateWinner, QuestAlreadyCompleted
from src.quest.schemas import QuestBase, QuestSchema

router = APIRouter(prefix="/quest", tags=["Quest endpoints"])


@router.post("/create")
async def create_quest(
    character: CharacterSchema = Depends(get_valid_character_for_quest),
    user_id: int = Depends(jwt.parse_jwt_user_data),
):
    quest = await service.generate_quest(character)

    """Updates Character.completed_last_quest to False since we just created a quest.
    Updates characters created_quests with the new quest data."""
    await character_service.after_quest_update_character_data(character.name, user_id)  # type: ignore
    return quest


@router.get("/")
async def get_quests(selected_character: CharacterSchema = Depends(get_selected_character)):
    return await service.get_all_quests(selected_character)


@router.get("/{quest_id}")
async def get_quest(quest: QuestSchema = Depends(get_quest_from_id_in_path)):
    if not quest.selected_approach:
        # if quest not finished, hide important game data
        return QuestBase(**quest.model_dump())
    return quest


@router.post("/play/{quest_id}/{approach_number}")
async def play_quest_approach(
    approach_number: int,
    quest: QuestSchema = Depends(get_quest_from_id_in_path),
    character: CharacterSchema = Depends(get_selected_character),
):
    if character.state == "dead":
        raise CharacterStateDead
    if character.state == "winner":
        raise CharacterStateWinner
    # true or false means quest already done (default is None)
    if isinstance(quest.survived, bool):
        raise QuestAlreadyCompleted
    return await game.roll_approach(approach_number, quest, character)
