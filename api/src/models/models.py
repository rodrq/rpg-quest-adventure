from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum, JSON, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.config.database import Base
from src.models.enums import (
    CharacterClasses, CharacterFlaws, CharacterVirtues, CharacterState, UserRoles)

# pylint: disable=not-callable


class Character(Base):
    __tablename__ = 'characters'

    username = Column(String, primary_key=True,
                      nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    class_ = Column(Enum(CharacterClasses), nullable=False)
    virtue = Column(Enum(CharacterVirtues), nullable=False)
    flaw = Column(Enum(CharacterFlaws), nullable=False)

    quests = relationship('Quest', back_populates='character', lazy='dynamic')

    honor_points = Column(Integer, default=0)
    char_state = Column(Enum(CharacterState),
                        default=CharacterState.adventuring)
    map_level = Column(Integer, default=1)
    times_reset = Column(Integer, default=0)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    role = Column(Enum(UserRoles), default=UserRoles.user)

    # TODO: SPLIT GAMEDATA


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
    survived = Column(Boolean, default=None)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
