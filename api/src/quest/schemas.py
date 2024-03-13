from pydantic import BaseModel


class ApproachGameResponse(BaseModel):
    choice_description: str


class NestedApproaches(BaseModel):
    approach_1: ApproachGameResponse
    approach_2: ApproachGameResponse
    approach_3: ApproachGameResponse


class QuestResponse(BaseModel):
    id: int
    title: str
    description: str
    approaches: NestedApproaches
    character_name: str
    character_map_level: int
    selected_approach: int | None


class Approach(BaseModel):
    choice_description: str
    success_description: str
    failure_description: str
    chance_of_success: int
