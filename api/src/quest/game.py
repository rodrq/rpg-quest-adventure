import random

from src.character.models import Character
from src.character.schemas import CharacterSchema
from src.quest import llm, service
from src.quest.exceptions import InvalidApproachChoice
from src.quest.schemas import ApproachSchema, QuestSchema


async def roll_approach(approach_number, quest: QuestSchema, character: CharacterSchema):
    quest_approaches = {
        1: quest.approaches.approach_1,
        2: quest.approaches.approach_2,
        3: quest.approaches.approach_3,
    }
    # if approach_number 1,2 or 3. chosen_approach = quest.approaches.approach_N
    if approach_number in quest_approaches:
        chosen_approach = quest_approaches[approach_number]
    else:
        raise InvalidApproachChoice()
    # game mechanic. every 20 valor points 1% easier quest
    enhance_chance = character.valor_points // 20
    composed_chance_success = chosen_approach.chance_of_success + enhance_chance
    rolled_chance = random.randint(0, 100)
    # if rolled number smaller or equal than composed chance of success, user wins
    print(composed_chance_success)
    if composed_chance_success >= rolled_chance:
        return await success_roll(character, quest, chosen_approach, approach_number)
    return await failure_roll(character, quest, chosen_approach, approach_number)


async def success_roll(
    character: CharacterSchema, quest: QuestSchema, chosen_approach: ApproachSchema, approach_number: int
):
    character_updates = {
        "valor_points": Character.valor_points + (100 - chosen_approach.chance_of_success),
        "map_level": Character.map_level + 1,
        "completed_last_quest": True,
    }

    # check if next map_level greater than max numbers of maps
    if character.map_level + 1 >= len(llm.prompt_maps_dict + 1):
        character_updates["state"] = "winner"

    quest_updates = {
        "selected_approach": approach_number,
        "survived": True,
    }
    await service.update_game_variables(character, character_updates, quest, quest_updates)
    return {"status": "success", "message": chosen_approach.success_description}


async def failure_roll(
    character: CharacterSchema, quest: QuestSchema, chosen_approach: ApproachSchema, approach_number: int
):
    character_updates = {
        "valor_points": Character.valor_points + (100 - chosen_approach.chance_of_success),
        "completed_last_quest": True,
        "state": "dead",
    }
    quest_updates = {
        "selected_approach": approach_number,
        "survived": False,
    }

    await service.update_game_variables(character, character_updates, quest, quest_updates)
    return {"status": "failure", "message": chosen_approach.failure_description}
