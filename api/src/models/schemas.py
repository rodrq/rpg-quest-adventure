from pydantic import BaseModel


    
class CharacterParams(BaseModel):
    username: str
    class_: str
    virtue: str
    flaw: str
    
class CharacterInDb(CharacterParams):
    password: str

class CharacterName(BaseModel):
    username: str

class ChosenApproach(BaseModel):
    approach_number: int

class Approach(BaseModel):
    choice_description: str
    success_description: str
    failure_description: str
    chance_of_success: int

    
class CharacterGameData(BaseModel):
    username: str
    class_: str
    virtue: str
    flaw: str
    honor_points: int
    map_level: int
    char_state: str