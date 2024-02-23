from sqlalchemy.orm import Session
from src.config.database import get_db
from sqlalchemy import func
from src.models.models import Character
from fastapi import Depends, HTTPException, status
            
def get_character_query(username: str, db: Session):
    
    queried_character = db.query(Character).filter(func.lower(Character.username) == username.lower()).first()
    return queried_character