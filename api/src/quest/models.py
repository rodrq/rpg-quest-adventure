from sqlalchemy import JSON, Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from src.database import Base


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True)
    character_name = Column(String, ForeignKey("characters.name", ondelete="CASCADE"))
    character = relationship("Character", back_populates="quests")
    title = Column(String)
    description = Column(String)
    approaches = Column(JSON)
    selected_approach = Column(Integer, default=None)
    survived = Column(Boolean, default=None)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
