from sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import Settings

metadata = MetaData()
Base = declarative_base()
async_engine = create_async_engine(DATABASE_URL, pool_size=20)
async_session = AsyncSession(async_engine)