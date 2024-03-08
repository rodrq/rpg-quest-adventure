from typing import Optional
from pydantic import BaseModel, ConfigDict
# pylint: disable=no-self-argument


# Quest serialization to hide non completed quest sensitive data.
class ApproachGameResponse(BaseModel):
    choice_description: str


class NestedApproaches(BaseModel):
    approach_1: ApproachGameResponse
    approach_2: ApproachGameResponse
    approach_3: ApproachGameResponse


class QuestResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    quest_id: int
    title: str
    description: str
    character_username: str
    approaches: NestedApproaches
    selected_approach: Optional[int]
