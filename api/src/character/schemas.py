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


class CharacterResponse(CharacterBase):
    id: int
    user_id: int
    state: CharacterStateEnum
    honor_points: int
    map_level: int
    times_reset: int
