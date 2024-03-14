from sqlalchemy import Boolean, Column, DateTime, Integer, LargeBinary, String, func
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password = Column(LargeBinary, nullable=False)
    is_admin = Column(Boolean, server_default="false", nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    characters = relationship("Character", back_populates="user")
    selected_character = Column(String, default=None)
