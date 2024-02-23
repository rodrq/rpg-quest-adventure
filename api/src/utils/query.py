from sqlalchemy.orm import Session
from sqlalchemy import func
from src.models.models import Character
            
def get_character_query(username: str, db: Session):
    
    queried_character = db.query(Character).filter(func.lower(Character.username) == username.lower()).first()
    return queried_character