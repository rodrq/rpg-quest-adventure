from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import app_configs, settings
from src.router import router

app = FastAPI(**app_configs)  # type: ignore
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
)
