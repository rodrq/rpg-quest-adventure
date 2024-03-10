from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func, Boolean, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from src.models import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password = Column(LargeBinary, nullable=False)
    is_admin = Column(Boolean, server_default="false", nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

