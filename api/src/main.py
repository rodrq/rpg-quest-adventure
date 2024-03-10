from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import router
from src.config import app_configs, settings, get_conn_str
from psycopg_pool import AsyncConnectionPool
from src.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    app.async_pool = AsyncConnectionPool(conninfo=get_conn_str())
    yield
    await app.async_pool.close()

app = FastAPI(**app_configs, lifespan=lifespan)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
)


