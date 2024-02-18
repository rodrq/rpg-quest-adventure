from sqlalchemy.orm import Session
from src.models.models import Character
from src.models.schemas import CharacterRollData

def roll_success_handler(current_character: CharacterRollData, honor_gained, game_success_description, db: Session):
    character = db.query(Character).filter(Character.username == current_character.username).first()
    if character:
        new_map_level = character.map_level + 1
        new_honor_points = character.honor_points + honor_gained
        update_values = {
            Character.map_level: new_map_level,
            Character.honor_points: new_honor_points
        }

        if new_map_level >= 10:
            update_values[Character.char_state] = 'winner'
            return {'message':f'{game_success_description} You are a champion and your adventure ends here.'}

        db.query(Character).filter(Character.username == current_character.username).update(update_values)
        db.commit()
        return {'message':f'{game_success_description} You can continue your adventure'}
    
def roll_failure_handler(current_character: CharacterRollData, game_failure_description, db: Session):
    db.query(Character).filter(Character.username == current_character.username).update({Character.char_state: 'dead'})
    db.commit()
    return {'message': f'{game_failure_description} You died.' }