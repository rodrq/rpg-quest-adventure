from fastapi import APIRouter, Depends
from src.config.database import get_db
from src.models.schemas import CharacterInDb, CharacterName, CharacterResponse

from src.models.models import Character

from src.handlers.character import create_character_handler
from sqlalchemy.orm import Session

router = APIRouter(prefix='/character',
                   tags=['Character creation'])


@router.post('/')
async def create_character(params: CharacterInDb, db: Session = Depends(get_db)):
    return await create_character_handler(params, db)
    
@router.get('/', response_model=CharacterResponse)
async def get_character(username: CharacterName, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.username == username.username).first()
    #if admin:
    # return character
    #else:
    return CharacterResponse(username=character.username,
                             class_=character.class_,
                             map_level=character.map_level,
                             honor_points=character.honor_points,
                             virtue=character.virtue,
                             flaw=character.flaw,
                             is_dead=character.is_dead,
                             is_winner=character.is_winner
                            )