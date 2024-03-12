from fastapi import APIRouter, Depends

router = APIRouter(prefix='/quest', tags=['Quests'])


# @router.post("/create")
# async def create_quest(current_character: str = Depends(valid_create_quest)):

