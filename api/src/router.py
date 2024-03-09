from fastapi import APIRouter

from .character.router import character_router
from .quest.router import quest_router
from .auth.router import auth_router
from .admin.router import admin_router
from .game.router import game_router

router = APIRouter(prefix='/api')

router.include_router(
    character_router)

router.include_router(
    quest_router)

router.include_router(
    auth_router)

router.include_router(
    game_router )

router.include_router(
    admin_router)
