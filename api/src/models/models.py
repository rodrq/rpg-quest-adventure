from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum, JSON
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from src.config.database import Base
from src.models.enums import CharacterClassesEnum, CharacterStateEnum, UserRole
from src.models.validators import validate_enum, validate_not_empty

class Character(Base):
    __tablename__ = 'characters'
     
    username = Column(String, primary_key=True, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    class_ = Column(Enum(CharacterClassesEnum), nullable=False)
    quests = relationship('Quest', back_populates='character')
    honor_points = Column(Integer, default=0)
    virtue = Column(String, nullable=False)
    flaw = Column(String, nullable=False)
    char_state = Column(Enum(CharacterStateEnum), default=CharacterStateEnum.adventuring)
    map_level = Column(Integer, name='map level', default=1)
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user)
    
    @validates('username', 'password')
    def non_empty_validator(self, key, value):
        return validate_not_empty(key, value)

    @validates('class_', 'virtue', 'flaw')
    def enum_validator(self, key, value):
        return validate_enum(key, value)
    

class Quest(Base):
    __tablename__ = 'quests'
    
    quest_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, name='title')
    description = Column(String, name='description')
    character_username = Column(String, ForeignKey('characters.username'))
    character = relationship('Character', back_populates='quests')
    cost = Column(Float, name="cost")
    approaches = Column(JSON, name='approaches')
    selected_approach = Column(Integer, name='selected_approach', default=None)


    
    
