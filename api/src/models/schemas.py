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
    quest_id: int
    approach_number: int

class Approach(BaseModel):
    choice_description: str
    success_description: str
    failure_description: str
    chance_of_success: int

    
class CharacterRollData(BaseModel):
    username: str
    class_: str
    honor_points: int
    map_level: int
    char_state: str