from openai import OpenAI
from src.config import Settings


openai_client = OpenAI(api_key=Settings().OPENAI_API_KEY,
                       organization=Settings().OPENAI_ORG_ID)


def create_quest_prompt(username: str, class_: str, quest_map: str, virtue: str, flaw: str):
    system_prompt = """You are the gamemaster of a RPG game, and you will create a creative quest for the player in JSON format.
                        The quest should include a challenge and three possible ways the player could overcome it. 
                        Each approach will have a chance of success, where the higher the risk of failing, the more daring the feat.

                        Please provide the following details in the output:

                            'title': a string representing the quest's title,
                            'description': a string describing the quest,
                        
                        With 'approaches' as parent dictionary, for each of the three approaches:
                            'approach_(number)': a nested dictionary number variable from 1 to 3, with the following keys:
                                'choice_description': a string describing a way the player could overcome the quest,
                                'success_description': a string describing how the player succeeded the challenge and his adventure continues,
                                'failure_description': a string describing how the player failed the challenge and died in the process,
                                'chance_of_success': an integer representing the chance % of success.

                        Additionally, the player will provide information about themselves,
                        which should be used to make the quest more personalized.
                        The bolder the approach, the lesser the 'chance_of_success'"""

    user_prompt = f""""Hello gamemaster, My name is {username} and I'm a {class_}.
                    My virtue is {virtue}, and my flaw is {flaw}. I'm currently in the {quest_map}.
                    Generate a fun quest for me using as much of the given context as possible. """

    return system_prompt, user_prompt


prompt_maps = {
    1: 'village',
    2: 'abandoned castle',
    3: 'catacombs',
    4: 'hills',
    5: 'snowy mountain',
    6: 'dwarf city',
    7: "dwarf king's hall. The last step before the end of my adventure.",
}
