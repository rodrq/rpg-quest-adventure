from src.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, JSON, Boolean, DateTime, func

class Quest(Base):
    __tablename__ = 'quests'

    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(String, ForeignKey('characters.id'))
    title = Column(String)
    description = Column(String)
    cost = Column(Float)
    approaches = Column(JSON)
    selected_approach = Column(Integer, default=None)
    survived = Column(Boolean, default=None)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
