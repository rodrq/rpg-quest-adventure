from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String, func

from src.character.enum import CharacterClassEnum, CharacterFlawEnum, CharacterStateEnum, CharacterVirtueEnum
from src.models import Base


class Character(Base):
    __tablename__ = "characters"

    name = Column(String, nullable=False, unique=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    class_ = Column(Enum(CharacterClassEnum), nullable=False)
    virtue = Column(Enum(CharacterVirtueEnum), nullable=False)
    flaw = Column(Enum(CharacterFlawEnum), nullable=False)
    state = Column(Enum(CharacterStateEnum), default="adventuring")

    # TODO quests = Column()

    valor_points = Column(Integer, default=0)
    map_level = Column(Integer, default=1)
    times_reset = Column(Integer, default=0)

    # tracker to check if last generated quest was completed. Default True so you can generate the first one
    completed_last_quest = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
