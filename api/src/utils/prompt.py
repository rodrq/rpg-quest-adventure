def create_quest_prompt(username: str, class_: str, map: str, virtue:str, flaw:str):
    system_prompt = f"""You are the gamemaster of a RPG game, and you will create a creative quest for the player in JSON format.
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
                        which should be used to make the quest more personalized."""
                    
    user_prompt = f""""Hello gamemaster, My name is {username} and I'm a {class_}. I'm currently in the {map}. 
                        My virtue is {virtue}, and my flaw is {flaw}"""
    return system_prompt, user_prompt 

prompt_maps = {
    1:'Farm village',
    2:'River',
    3:'Abandoned castle',
    4:'Catacombs',
    5:'Sewage',
    6:'Plage-ridden town',
    7:'Hills',
    8:'Snowy mountain',
    9:'Dwarf city',
    10:"Dwarf king's hall. The last step before the end of my adventure.",
  }