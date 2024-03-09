import enum
from fastapi import HTTPException, status
from pydantic import BaseModel, field_validator, ValidationInfo

class CharacterStateEnum(str, enum.Enum):
    dead = 'dead'
    winner = 'winner'
    adventuring = 'adventuring'


class CharacterClassEnum(enum.Enum):
    warrior = 'warrior'
    mage = 'mage'
    barbarian = 'barbarian'
    cleric = 'cleric'
    warlock = 'warlock'
    druid = 'druid'
    paladin = 'paladin'
    rogue = 'rogue'
    knight = 'knight'
    archer = 'archer'


class CharacterVirtueEnum(enum.Enum):
    courage = "courage"
    honor = "honor"
    compassion = "compassion"
    wisdom = "wisdom"
    resilience = "resilience"
    generosity = "generosity"
    determination = "determination"
    humility = "humility"


class CharacterFlawEnum(enum.Enum):
    cowardice = "cowardice"
    greed = "greed"
    dishonesty = "dishonesty"
    cruelty = "cruelty"
    ignorance = "ignorance"
    selfishness = "selfishness"
    impulsiveness = "impulsiveness"
    arrogance = "arrogance"
    
class UserRoleEnum(str, enum.Enum):
    user = "user"
    admin = "admin"

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