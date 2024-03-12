from typing import Any
from sqlalchemy import (CursorResult, Select, Insert, Update, Delete)
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings
from src.models import Base
DATABASE_URL = str(settings.DB_URL)

engine = create_async_engine(DATABASE_URL)

async def init_db():  
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def fetch_one(select_query: Select | Insert | Update) -> dict[str, Any] | None:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query)
        return cursor.first()._asdict() if cursor.rowcount > 0 else None


async def fetch_all(select_query: Select | Insert | Update) -> list[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query)
        return [r._asdict() for r in cursor.all()]


async def execute(select_query: Insert | Update | Delete) -> None:
    async with engine.begin() as conn:
        await conn.execute(select_query)