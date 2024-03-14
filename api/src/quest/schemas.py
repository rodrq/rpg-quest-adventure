from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SecretApproach(BaseModel):
    choice_description: str


class Approach(BaseModel):
    choice_description: str
    success_description: str
    failure_description: str
    chance_of_success: int


class SecretApproaches(BaseModel):
    approach_1: SecretApproach
    approach_2: SecretApproach
    approach_3: SecretApproach


class Approaches(BaseModel):
    approach_1: Approach
    approach_2: Approach
    approach_3: Approach


class SecretQuestResponse(BaseModel):
    id: int
    title: str
    description: str
    approaches: SecretApproaches
    character_name: str
    selected_approach: Optional[int]


class QuestResponse(SecretQuestResponse):
    approaches: Approaches
    survived: Optional[bool]
    created_at: datetime
