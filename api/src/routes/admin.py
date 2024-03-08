from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.utils.auth import get_current_admin_user
from src.config.database import get_db
from src.models.models import Character, Quest


router = APIRouter(prefix='/admin',
                   tags=['Admin'])


@router.get("/get_quests", dependencies=[Depends(get_current_admin_user)])
async def get_quests(db: Session = Depends(get_db)):
    quests = db.query(Quest).all()
    return quests


@router.get("/get_quest/{quest_id}", dependencies=[Depends(get_current_admin_user)])
async def get_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
    return quest


@router.get("/get_character/{character_name}", dependencies=[Depends(get_current_admin_user)])
async def get_character(character_name: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(
        Character.username == character_name).first()
    return character


@router.get("/get_characters", dependencies=[Depends(get_current_admin_user)])
async def get_characters(db: Session = Depends(get_db)):
    characters = db.query(Character).all()
    return characters


@router.delete('/delete_character', dependencies=[Depends(get_current_admin_user)])
async def delete_character(username: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(
        Character.username == username).first()
    if character:
        db.delete(character)
        db.commit()
        return JSONResponse(content="Character deleted")
