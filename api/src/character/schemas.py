from typing import Any, List

from pydantic import BaseModel, field_validator

from src.character.enum import CharacterClassEnum, CharacterFlawEnum, CharacterStateEnum, CharacterVirtueEnum
from src.character.exceptions import FieldsAreEmpty


class CharacterBase(BaseModel):
    name: str
    class_: CharacterClassEnum
    virtue: CharacterVirtueEnum
    flaw: CharacterFlawEnum

    @field_validator("name")
    def name_validator(cls, value: str):
        if value.isspace() or value is None:
            raise FieldsAreEmpty()
        return value


class CharacterSchema(CharacterBase):
    user_id: int
    state: CharacterStateEnum
    valor_points: int
    map_level: int
    times_reset: int
    completed_last_quest: bool

    class Config:
        use_enum_values = True


class CharacterWithQuests(CharacterSchema):
    quests: List[dict[str, Any]] | None = None
