from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from src.models.models import Character, Quest
from src.models.serializers import ChosenApproach
from src.models.schemas import CharacterGameData, Approach
import random
from src.utils.exceptions import DeadOrWinner

def roll_handler(current_character_gamedata: CharacterGameData, chosen_approach: ChosenApproach, db: Session):
    try:
        #TODO make this a dependency
        if current_character_gamedata.char_state == 'dead' or current_character_gamedata.char_state == 'winner':
            raise DeadOrWinner(
                    """Can't play anymore. Your character's either dead or your journey came
                    to an end after exploring the whole world and coming victorious."""
                    )
        

        #get latest quest on db, meaning, the one we just created
        current_quest = db.query(Quest).order_by(desc(Quest.quest_id)).first()

        if current_quest and current_quest.selected_approach==None:
            
            approach = current_quest.approaches[f'approach_{chosen_approach.approach_number}']
            
            approach = Approach(choice_description=approach['choice_description'],
                                success_description=approach['success_description'],
                                failure_description=approach['failure_description'],
                                chance_of_success=approach['chance_of_success'])
            
            #save aproach to quest table
            if approach:
                current_quest.selected_approach = chosen_approach.approach_number
            
            #Every 200 honor, 1% more chance per approach 
            gamey_chance_of_success = approach.chance_of_success + (current_character_gamedata.honor_points/200)
            dice_roll = random.randint(1, 100)
            if dice_roll < gamey_chance_of_success:
                # every 1% chance of failure = 10 honor
                honor_gained = (100 - approach.chance_of_success) * 10
                return roll_success_handler(current_character_gamedata, honor_gained, approach.success_description, db)
            else:
                return roll_failure_handler(current_character_gamedata, approach.failure_description, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def roll_success_handler(current_character: CharacterGameData, honor_gained, game_success_description, db: Session):
    try:
        if current_character:
            new_map_level = current_character.map_level + 1
            new_honor_points = current_character.honor_points + honor_gained
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def roll_failure_handler(current_character: CharacterGameData, game_failure_description, db: Session):
    try:
        db.query(Character).filter(Character.username == current_character.username).update({Character.char_state: 'dead'})
        db.commit()
        return {'message': f'{game_failure_description} You died.' }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def reset_character_handler(current_character_gamedata: CharacterGameData, db:Session):
    
    character = db.query(Character).filter(Character.username == current_character_gamedata.username).first()
    print(character.char_state)
    if character:
        new_map_level = 1
        new_honor_points = 0
        new_char_state = 'adventuring'
        update_values = {
            Character.map_level: new_map_level,
            Character.honor_points: new_honor_points,
            Character.char_state: new_char_state
        }
        db.query(Character).filter(Character.username == character.username).update(update_values)
        db.commit()
    character = db.query(Character).filter(Character.username == current_character_gamedata.username).first()
    print(character.char_state)
    
    return {'message': 'Character reset.' }