from fastapi import HTTPException, status
from .enums import CharacterClasses, CharacterFlaws, CharacterVirtues


def form_validator(key: str, value: str) -> str:
    if key in ('username', 'password'):
        if not value or value.isspace():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"{key} can't be empty.")
        return value

    enum_mapping = {
        'class_': CharacterClasses,
        'virtue': CharacterVirtues,
        'flaw': CharacterFlaws,
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
