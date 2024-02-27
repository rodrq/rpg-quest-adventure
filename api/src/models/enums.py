import enum

class CharacterStateEnum(enum.Enum):
    dead = 'dead'
    winner = 'winner'
    adventuring = 'adventuring'

class UserRole(str, enum.Enum):
    user = "user"
    admin = "admin"   
    
class CharacterClassesEnum(enum.Enum):
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

class CharacterVirtuesEnum(enum.Enum):
    courage = "courage"
    honor = "honor"
    compassion = "compassion"
    wisdom = "wisdom"
    resilience = "resilience"
    generosity = "generosity"
    determination = "determination"
    humility = "humility"


class CharacterFlawsEnum(enum.Enum):
    cowardice = "cowardice"
    greed = "greed"
    dishonesty = "dishonesty"
    cruelty = "cruelty"
    ignorance = "ignorance"
    selfishness = "selfishness"
    impulsiveness = "impulsiveness"
    arrogance = "arrogance"
    
    
