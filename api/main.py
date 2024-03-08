from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import app_configs
from src.routes import api
from src.config.database import Base, engine


def get_app() -> FastAPI:

    init_app = FastAPI(**app_configs)

    Base.metadata.create_all(bind=engine)

    init_app.include_router(api.router)

    init_app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"])

    return init_app


app = get_app()
