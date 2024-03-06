from pydantic import BaseModel, validator
from typing import Optional


# Sent approach validation
class ChosenApproach(BaseModel):
    approach_number: int
    
    @validator("approach_number")
    def validate_approach_number(cls, value):
        if value < 1 or value > 3:
            raise ValueError("Approach number must be between 1 and 3")
        return value


# Quest serialization to avoid exposing model's cost, success_chance for each approach, and unnecesary data.
class ApproachGameResponse(BaseModel):
    choice_description: str

class NestedApproaches(BaseModel):
    approach_1: ApproachGameResponse
    approach_2: ApproachGameResponse
    approach_3: ApproachGameResponse

class QuestResponse(BaseModel):
    class Config:
        populate_by_name = True
    quest_id: int
    title: str
    description: str
    character_username: str
    approaches: NestedApproaches
    selected_approach: Optional[int]