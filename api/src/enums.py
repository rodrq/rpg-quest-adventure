import enum

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