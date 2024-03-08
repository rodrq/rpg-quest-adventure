from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import Settings

Base = declarative_base()

engine = create_engine(Settings().DB_URL.unicode_string())

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    """db session dependency injection"""
    db = Session()
    try:
        yield db
    finally:
        db.close()
