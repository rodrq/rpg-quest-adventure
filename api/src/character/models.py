from sqlalchemy import Column, Integer, String, DateTime, func, Enum, ForeignKey
from src.models import Base
from src.character.enum import CharacterClassEnum, CharacterVirtueEnum, CharacterFlawEnum, CharacterStateEnum


class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    class_ = Column(Enum(CharacterClassEnum), nullable=False)
    virtue = Column(Enum(CharacterVirtueEnum), nullable=False)
    flaw = Column(Enum(CharacterFlawEnum), nullable=False)
    state = Column(Enum(CharacterStateEnum), default="adventuring")
    
    #TODO quests = Column()
    
    honor_points = Column(Integer, default = 0)
    map_level = Column(Integer, default = 1)
    times_reset = Column(Integer, default = 0)
    
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

