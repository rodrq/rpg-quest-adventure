from fastapi import HTTPException, status
from pydantic import BaseModel, validator
from src.character.schemas import CharacterClassEnum, CharacterVirtueEnum, CharacterFlawEnum


def form_validator(key: str, value: str) -> str:
    if key in ('username', 'password'):
        if not value or value.isspace():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"{key} can't be empty.")
        return value

    enum_mapping = {
        'class_': CharacterClassEnum,
        'virtue': CharacterVirtueEnum,
        'flaw': CharacterFlawEnum,
    }

    enum_member = enum_mapping.get(key)

    if value and value not in enum_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"{value} is not a valid {key}")
    return value


def approach_number_validator(approach_number) -> int:
    if approach_number < 1 or approach_number > 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Approach number must be between 1 and 3")
    return approach_number


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



