# from src.models import Base
# from sqlalchemy import Column, Integer, String, ForeignKey, Float, JSON, Boolean, DateTime, func
# from sqlalchemy.orm import relationship

# class Quest(Base):
#     __tablename__ = 'quests'

#     quest_id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, name='title')
#     description = Column(String, name='description')
#     character_username = Column(String, ForeignKey('characters.username'))
#     character = relationship('Character', back_populates='quests')
#     cost = Column(Float, name="cost")
#     approaches = Column(JSON, name='approaches')
#     selected_approach = Column(Integer, name='selected_approach', default=None)
#     survived = Column(Boolean, default=None)
#     created_at = Column(DateTime, server_default=func.now(), nullable=False)
