from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .settings import DB_URL
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine(DB_URL)

Session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()