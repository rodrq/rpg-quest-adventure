from sqlalchemy.orm import Session
from src.models.models import Character
from src.models.schemas import CharacterName
import random
from sqlalchemy.sql.expression import update

def roll_success_handler(honor_gained, current_character: CharacterName, db: Session):
        db.query(Character).filter(Character.username == current_character.username).update(
        {
            Character.map_level: Character.map_level + 1,
            Character.honor_points: Character.honor_points + honor_gained
        }
    )
        db.commit()
        return {'message':'success'}
    
def roll_failure_handler(current_character: CharacterName, db: Session):
    db.query(Character).filter(Character.username == current_character.username).update({Character.is_dead: True})
    db.commit()
    return {'message': 'You are dead.'}