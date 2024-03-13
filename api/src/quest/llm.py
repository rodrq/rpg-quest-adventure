def create_quest_prompt(name: str, class_: str, quest_map: str, virtue: str, flaw: str):
    system_prompt = """Respond with a string to be parsed to JSON, strings enclosed with double quotes and
    without any markdown formatting (just plain text.).
        You are the gamemaster of a RPG game, and your task is to create a quest for the player.
        The quest should include a challenge and three possible ways the player could overcome it.
        Each approach will have a chance of success, where the higher the risk of failing, the more daring the feat.
        Please structure the output as follows:
            'title': a string representing the quest's title,
            'description': a string describing the quest,
            With 'approaches' as parent dictionary, for each of the three approaches:
                'approach_(number)': a nested dictionary number variable from 1 to 3, with the following keys:
                    'choice_description': a string describing a way the player could overcome the quest,

                    'success_description': a string describing how the player succeeded the challenge and his
                        adventure continues,

                    'failure_description': a string describing how the player failed the challenge and died
                        in the process,

                    'chance_of_success': an integer representing the chance % of success.

            Additionally, the player will provide information about themselves, which should be used to make
            the quest more personalized. Remember: the bolder the approach, the lesser the 'chance_of_success'.
            I'd prefer to start with calmer quests and gradually face tougher challenges as I progress.
            Try to keep a balance between creativity and using the context provided."""

    user_prompt = f"""Hello gamemaster, My name is {name} and I'm a {class_}.
                    My virtue is {virtue}, and my flaw is {flaw}. I'm currently in the {quest_map}.
                    With that in mind create a fantasy setting RPG quest for me"""

    return system_prompt, user_prompt


prompt_maps_dict = {
    1: "village",
    2: "abandoned castle",
    3: "catacombs",
    4: "hills",
    5: "snowy mountain",
    6: "dwarf city",
    7: "dwarf king's hall. The last step before the end of my adventure.",
}
