from fastapi import APIRouter

from src.auth.routes import router as auth_router
from src.character.routes import router as character_router

router = APIRouter(prefix='/api')

router.include_router(auth_router)
router.include_router(character_router)

