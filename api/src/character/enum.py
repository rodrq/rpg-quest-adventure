from enum import Enum


class CharacterStateEnum(str, Enum):
    dead = "dead"
    winner = "winner"
    adventuring = "adventuring"


class CharacterClassEnum(str, Enum):
    warrior = "warrior"
    mage = "mage"
    barbarian = "barbarian"
    cleric = "cleric"
    warlock = "warlock"
    druid = "druid"
    paladin = "paladin"
    rogue = "rogue"
    knight = "knight"
    archer = "archer"


class CharacterVirtueEnum(str, Enum):
    courage = "courage"
    honor = "honor"
    compassion = "compassion"
    wisdom = "wisdom"
    resilience = "resilience"
    generosity = "generosity"
    determination = "determination"
    humility = "humility"


class CharacterFlawEnum(str, Enum):
    cowardice = "cowardice"
    greed = "greed"
    dishonesty = "dishonesty"
    cruelty = "cruelty"
    ignorance = "ignorance"
    selfishness = "selfishness"
    impulsiveness = "impulsiveness"
    arrogance = "arrogance"
