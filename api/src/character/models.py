from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from sqlalchemy.orm import relationship
from src.database import Base
from .schemas import CharacterClassEnum, CharacterVirtueEnum, CharacterFlawEnum, CharacterStateEnum, UserRoleEnum

class Character(Base):
    __tablename__ = 'characters'

    username = Column(String, primary_key=True,
                      nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    class_ = Column(Enum(CharacterClassEnum), nullable=False)
    virtue = Column(Enum(CharacterVirtueEnum), nullable=False)
    flaw = Column(Enum(CharacterFlawEnum), nullable=False)

    quests = relationship('Quest', back_populates='character', lazy='dynamic')

    honor_points = Column(Integer, default=0)
    char_state = Column(Enum(CharacterStateEnum),
                        default=CharacterStateEnum.adventuring)
    map_level = Column(Integer, default=1)
    times_reset = Column(Integer, default=0)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    role = Column(Enum(UserRoleEnum), default=UserRoleEnum.user)

    # TODO: SPLIT GAMEDATA
