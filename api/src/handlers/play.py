import random
from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
from src.models.models import Character, Quest
from src.models.schemas import ChosenApproach
from src.models.schemas import Approach
from src.utils.exceptions import DeadOrWinner
from src.utils.prompt import prompt_maps


def roll_handler(current_character: Character, chosen_approach: ChosenApproach, db: Session):
    try:
        # TODO make this a dependency
        if current_character.char_state in ('dead', 'winner'):
            raise DeadOrWinner(
                """Can't play anymore. Your character's either dead or your journey came
                    to an end after exploring the whole world and coming victorious."""
            )

        # get latest quest on db, meaning, the one just created.
        current_quest: Quest = (current_character.quests
                                .options(joinedload(Quest.character))
                                .order_by(desc(Quest.created_at))
                                .first())

        if current_quest and current_quest.selected_approach is None:

            approach = current_quest.approaches[f"approach_{
                chosen_approach.approach_number}"]

            approach = Approach(choice_description=approach['choice_description'],
                                success_description=approach['success_description'],
                                failure_description=approach['failure_description'],
                                chance_of_success=approach['chance_of_success'])

            # save chosen aproach to Quest table
            if approach:
                current_quest.selected_approach = chosen_approach.approach_number

            # Every 200 honor, +1% chance of success
            processed_chance_of_success = approach.chance_of_success + \
                (current_character.honor_points/200)
            dice_roll = random.randint(1, 100)
            if dice_roll >= processed_chance_of_success:
                # every 1% chance of failure = 10 honor
                honor_gained = (100 - approach.chance_of_success) * 10
                return roll_success_handler(current_character,
                                            current_quest,
                                            honor_gained,
                                            approach.success_description, db)

            return roll_failure_handler(current_character, current_quest, approach.failure_description, db)
        if current_quest is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No quest generated.")

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Last quest completed. Generate a new one")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


def roll_success_handler(current_character: Character, current_quest: Quest,
                         honor_gained, approach_success_description, db: Session):
    try:
        current_quest.survived = True
        current_character.map_level += 1
        current_character.honor_points += honor_gained
        # Game ends after last map, so we check.
        if current_character.map_level >= len(prompt_maps):
            current_character.char_state = 'winner'
            return {'message': f'{approach_success_description} Congratulations, you are a champion and your adventure ends here.'}
        db.commit()
        return {'message': f'{approach_success_description} You can continue your adventure'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e


def roll_failure_handler(current_character: Character,
                         current_quest: Quest, approach_failure_description,
                         db: Session):
    try:
        if current_quest:
            current_quest.survived = False
        current_character.char_state = 'dead'
        db.commit()
        return {'message': f'{approach_failure_description} You died.'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
