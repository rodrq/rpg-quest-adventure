from sqlalchemy import ARRAY, Boolean, Column, DateTime, ForeignKey, Integer, LargeBinary, String, func

from src.models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password = Column(LargeBinary, nullable=False)
    is_admin = Column(Boolean, server_default="false", nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    characters = Column(ARRAY(String, ForeignKey("characters.name")), default=None)
    selected_character = Column(String, default=None)  # TODO
