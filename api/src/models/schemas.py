from pydantic import BaseModel, validator, field_validator, ValidationInfo
from .validators import form_validator, approach_number_validator

# pylint:disable=no-self-argument

# Char creation schemas


class CharacterParams(BaseModel):
    username: str
    class_: str
    virtue: str
    flaw: str


class CharacterInDb(CharacterParams):
    password: str

    @field_validator("*")
    def validate_form(cls, value: str, info: ValidationInfo) -> str:
        key = info.field_name
        return form_validator(key, value)


# Game logic schemas
class Approach(BaseModel):
    choice_description: str
    success_description: str
    failure_description: str
    chance_of_success: int


class ChosenApproach(BaseModel):
    """Sent approach number schema and validation"""
    approach_number: int

    @validator("approach_number")
    def validate_approach_number(cls, value):
        return approach_number_validator(value)


class CharacterGameData(BaseModel):
    username: str
    class_: str
    virtue: str
    flaw: str
    honor_points: int
    map_level: int
    char_state: str
    times_reset: int
