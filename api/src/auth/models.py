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

    
class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    
    uuid = Column(UUID, primary_key=True)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

