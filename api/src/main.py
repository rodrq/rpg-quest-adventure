from src.config import app_configs
from src.router import router
from .database import init_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


def init_app():

    app = FastAPI(**app_configs)

    init_db()
    
    app.include_router(router)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"])

    return app

app = init_app()