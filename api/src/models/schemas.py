from pydantic import BaseModel
from typing import Union


class TokenData(BaseModel):
    username: Union[str, None] = None
    
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
    approach_id: int
  
class CharacterResponse(BaseModel):
    username: str
    class_: str
    virtue: str
    flaw: str
    honor_points: str
    map_level: str
    is_dead: bool
    is_winner: bool