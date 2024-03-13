from fastapi import APIRouter, Depends, Path

from src.character.schemas import CharacterResponse
from src.quest import service
from src.quest.dependencies import get_user_selected_character, valid_approach_number, valid_game_character
from src.quest.schemas import QuestResponse

router = APIRouter(prefix="/quest", tags=["Quest endpoints"])


@router.post("/create")
async def create_quest(character: CharacterResponse = Depends(valid_game_character)):
    quest = await service.generate_quest(character)
    # updates characters completed_last_quest to False.
    # updates character quests = Column(ARRAY(String, ForeignKey("quests.id"))
    await service.post_quest_creation_updates(character.name, quest)
    return QuestResponse(**quest)


@router.get("/")
async def get_quests(selected_character: str = Depends(get_user_selected_character)):
    quests = await service.get_all_quests(selected_character)
    # if quest not finished, hide important game data
    return [QuestResponse(**quest) if quest["selected_approach"] is None else quest for quest in quests]


@router.get("/{quest_id}")
async def get_quest(selected_character: str = Depends(get_user_selected_character), quest_id: int = Path()):
    quest = await service.get_selected_character_quest(selected_character, quest_id)
    if not quest["selected_approach"]:
        # if quest not finished, hide important game data
        return QuestResponse(**quest)
    return quest


# @router.post("/play/{quest_id}/{approach_number}")
# async def choose_approach(quest=Depends(), approach_number: int = Depends(valid_approach_number)):
#     pass
