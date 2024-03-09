from src.character.models import Character
from src.game.schemas import CharacterGameData


def convert_character_to_gamedata(character: Character) -> CharacterGameData:
    return CharacterGameData(
        username=character.username,
        class_=character.class_,
        virtue=character.virtue,
        flaw=character.flaw,
        honor_points=character.honor_points,
        map_level=character.map_level,
        char_state=character.char_state,
        times_reset=character.times_reset,
    )
