from sqlalchemy import ARRAY, Boolean, Column, DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from src.character.enum import CharacterClassEnum, CharacterFlawEnum, CharacterStateEnum, CharacterVirtueEnum
from src.database import Base


class Character(Base):
    __tablename__ = "characters"

    name = Column(String, nullable=False, unique=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="characters")
    class_ = Column(Enum(CharacterClassEnum), nullable=False)
    virtue = Column(Enum(CharacterVirtueEnum), nullable=False)
    flaw = Column(Enum(CharacterFlawEnum), nullable=False)
    state = Column(Enum(CharacterStateEnum), default="adventuring")
    valor_points = Column(Integer, default=0)
    map_level = Column(Integer, default=1)
    times_reset = Column(Integer, default=0)

    quests = relationship("Quest", back_populates="character", cascade="all")
    created_quests = Column(ARRAY(Integer), default=None)

    # tracker to check if last generated quest was completed. Default True so you can generate the first one
    completed_last_quest = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
