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
    sorcerer = 'sorcerer'
    monk = 'monk'
    bard = 'bard'
    necromancer = 'necromancer'
    wizard = 'wizard'
    knight = 'knight'
    archer = 'archer'
    assassin = 'assassin'
    priest = 'priest'
    shaman = 'shaman'
    samurai = 'samurai'
    summoner = 'summoner'
    artificer = 'artificer'
    warlord = 'warlord'
    engineer = 'engineer'
    juggernaut = 'juggernaut'
    sentinel = 'sentinel'
    elementalist = 'elementalist'
    geomancer = 'geomancer'
    brawler = 'brawler'