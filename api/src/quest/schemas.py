from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ApproachBase(BaseModel):
    choice_description: str


class ApproachSchema(BaseModel):
    choice_description: str
    success_description: str
    failure_description: str
    chance_of_success: int


class ApproachesBase(BaseModel):
    approach_1: ApproachBase
    approach_2: ApproachBase
    approach_3: ApproachBase


class Approaches(BaseModel):
    approach_1: ApproachSchema
    approach_2: ApproachSchema
    approach_3: ApproachSchema


class QuestBase(BaseModel):
    id: int
    title: str
    description: str
    approaches: ApproachesBase
    character_name: Optional[str] = None
    selected_approach: Optional[int]


class QuestSchema(QuestBase):
    approaches: Approaches  # type: ignore
    survived: Optional[bool]
    created_at: datetime


class QuestSummary(BaseModel):
    title: str
    description: str
    action: str
    consequence: str
    survived: bool
