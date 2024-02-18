from fastapi import APIRouter, Depends, HTTPException
from src.utils.auth import get_current_admin_user
from src.config.database import get_db
from src.models.models import Character, Quest
from src.models.schemas import CharacterName
from sqlalchemy.orm import Session

router = APIRouter(prefix='/admin',
                   tags=['Admin'])

@router.get("/get_quests")
async def admin_resource(
    current_admin_user: Character = Depends(get_current_admin_user),
    db: Session = Depends(get_db)):
    quests = db.query(Quest).all()
    return quests


@router.get("/get_quest/{quest_id}")
async def get_quest(quest_id: int, 
                    current_admin_user: Character = Depends(get_current_admin_user),
                    db: Session = Depends(get_db)):
    quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
    if not quest:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return quest
    
@router.get('/get_character/{character_name}')
async def get_character(character_name: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.username == character_name).first()
    return character

@router.get('/get_characters')
async def get_characters(current_admin_user: Character = Depends(get_current_admin_user), 
                         db: Session = Depends(get_db)):
    
    characters = db.query(Character).all()
    return characters