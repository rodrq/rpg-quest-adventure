# from fastapi import APIRouter, Depends
# from fastapi.responses import JSONResponse
# from sqlalchemy.orm import Session
# from src.character.models import Character
# from src.quest.models import Quest
# from src.admin.dependencies import get_current_admin_user

# router = APIRouter(prefix='/admin', tags=['Admin'])


# @router.get("/get_quests", dependencies=[Depends(get_current_admin_user)])
# async def get_quests():
#     quests = db.query(Quest).all()
#     return quests


# @router.get("/get_quest/{quest_id}", dependencies=[Depends(get_current_admin_user)])
# async def get_quest(quest_id: int):
#     quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
#     return quest


# @router.get(
#     "/get_character/{character_name}", dependencies=[Depends(get_current_admin_user)]
# )
# async def get_character(character_name: str):
#     character = db.query(Character).filter(Character.username == character_name).first()
#     return character


# @router.get("/get_characters", dependencies=[Depends(get_current_admin_user)])
# async def get_characters():
#     characters = db.query(Character).all()
#     return characters


# @router.delete("/delete_character", dependencies=[Depends(get_current_admin_user)])
# async def delete_character(username: str):
#     character = db.query(Character).filter(Character.username == username).first()
#     if character:
#         db.delete(character)
#         db.commit()
#         return JSONResponse(content="Character deleted")

