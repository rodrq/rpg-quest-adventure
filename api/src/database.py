from typing import Any

from sqlalchemy import CursorResult, Delete, Insert, MetaData, Select, Update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from src.config import settings
from src.constants import POSTGRES_INDEXES_NAMING_CONVENTION
from src.utils import logger

metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)

Base = declarative_base(metadata=metadata)

DATABASE_URL = str(settings.DB_URL)

engine = create_async_engine(
    DATABASE_URL,
    future=True,
    # echo=True
)


# This db query approach saves us from dependency injecting dbs and managing sessions all around the app
# Its trade-off is serializing everything to dict and having to map it to a schema later.
async def fetch_one(select_query: Select | Insert | Update) -> dict[str, Any] | None:
    try:
        async with engine.begin() as conn:
            cursor: CursorResult = await conn.execute(select_query)
            row = cursor.first()
            return row._asdict() if row is not None else None
    except SQLAlchemyError as e:
        logger.error(f"Database error occurred on fetch_one {str(select_query)}: {e}")
        return None


async def fetch_all(select_query: Select | Insert | Update) -> list[dict[str, Any]]:
    try:
        async with engine.begin() as conn:
            cursor: CursorResult = await conn.execute(select_query)
            return [r._asdict() for r in cursor.all()]
    except SQLAlchemyError as e:
        logger.error(f"Database error occurred on fetch_all {str(select_query)}: {e}")
        return []


async def execute(select_query: Insert | Update | Delete) -> None:
    try:
        async with engine.begin() as conn:
            await conn.execute(select_query)
    except SQLAlchemyError as e:
        logger.error(f"Database error occurred on execute {str(select_query)}: {e}")
        return None
