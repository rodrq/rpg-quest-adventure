from sqlalchemy.orm import Session
from src.models.models import Character, Quest
from src.models.schemas import CharacterGameData, ChosenApproach, Approach
import random
from src.utils.exceptions import MaxMapLevelReached

def roll_handler(current_character_game_data: CharacterGameData, chosen_approach: ChosenApproach, db: Session):
    
    if current_character_game_data.map_level >= 10:
        raise MaxMapLevelReached(
            "Can't play anymore. Your character's journey came to an end after exploring the whole world and being victorious."
            )
    
    dice_roll = random.randint(1, 100)
    
    quest = db.query(Quest).filter(Quest.quest_id == chosen_approach.quest_id).first()

    if quest:
        try:
            #TODO: ADD APPROACH_NUMBER VALIDATION 1 TO 3
            approach = quest.approaches[f'approach_{chosen_approach.approach_number}']
        except:
            raise ValueError(f"Approach {chosen_approach.approach_number} not found for the quest.")
        
        approach = Approach(choice_description=approach['choice_description'],
                            success_description=approach['success_description'],
                            failure_description=approach['failure_description'],
                            chance_of_success=approach['chance_of_success'])
        
        chance_of_success = approach.chance_of_success
        
        if dice_roll < chance_of_success:
            honor_gained = (100 - chance_of_success) * 10
            return roll_success_handler(current_character_game_data, honor_gained, approach.success_description, db)
        else:
            return roll_failure_handler(current_character_game_data, approach.failure_description, db)


def roll_success_handler(current_character: CharacterGameData, honor_gained, game_success_description, db: Session):
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
    
def roll_failure_handler(current_character: CharacterGameData, game_failure_description, db: Session):
    db.query(Character).filter(Character.username == current_character.username).update({Character.char_state: 'dead'})
    db.commit()
    return {'message': f'{game_failure_description} You died.' }