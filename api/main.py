from fastapi import FastAPI
from src.routes import api
from src.config.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import CORS_ORIGINS
from src.utils.middlewares import TokenToAuthorizationMiddleware

def get_app() -> FastAPI:

    app = FastAPI()

    Base.metadata.create_all(bind=engine)
    
    app.include_router(api.router)

    app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])
    
    app.add_middleware(TokenToAuthorizationMiddleware)


    

    return app

app = get_app()



