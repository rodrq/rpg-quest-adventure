from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from src.config.database import Base
from src.models.enums import CharacterClassesEnum, CharacterStateEnum
from src.models.validations import validate_class, validate_not_empty

class Character(Base):
    __tablename__ = 'characters'
     
    username = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    class_ = Column(Enum(CharacterClassesEnum,), nullable=False)
    quests = relationship('Quest', back_populates='character')
    honor_points = Column(Integer, default=0)
    virtue = Column(String)
    flaw = Column(String)
    char_state = Column(Enum(CharacterStateEnum), default=CharacterStateEnum.adventuring)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    map_level = Column(Integer, name='map level', default=1)
    
    @validates('username', 'password')
    def validate_not_empty(self, key, value):
        return validate_not_empty(key, value)

    @validates('class_')
    def validate_class(self, key, value):
        return validate_class(key, value)


class Quest(Base):
    __tablename__ = 'quests'
    
    quest_id = Column(Integer, primary_key=True)
    title = Column(String, name='title')
    description = Column(String, name='description')
    character_username = Column(String, ForeignKey('characters.username'))
    character = relationship('Character', back_populates='quests')
    cost = Column(Float, name="cost")
    approaches = relationship('Approach', back_populates='quest', lazy='select')
    selected_approach = Column(Integer, name='selected_approach', default=None)


class Approach(Base):
    __tablename__ = 'approaches'
    
    approach_id = Column(Integer, primary_key= True)
    choice_description = Column(String, name='choice description')
    success_description = Column(String, name='success description')
    failure_description = Column(String, name='failure description')
    chance_of_success = Column(Integer, name='chance of success')

    quest_id = Column(Integer, ForeignKey('quests.quest_id'))
    quest = relationship('Quest', back_populates='approaches')
    
    
