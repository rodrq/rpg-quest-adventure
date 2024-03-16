from fastapi import APIRouter, Depends

from src.auth import jwt
from src.auth import service as auth_service
from src.character import service
from src.character.dependencies import (
    get_valid_auth_character,
    valid_character_create,
)
from src.character.schemas import CharacterBase, CharacterSchema

router = APIRouter(prefix="/character", tags=["Character endpoints"])


@router.post("/")
async def create_character(
    character_form: CharacterBase = Depends(valid_character_create),
    user_id: int = Depends(jwt.parse_jwt_user_data),
):
    created_character = await service.create_character(character_form, user_id)
    await auth_service.update_user_data(user_id)
    return created_character


@router.get("/")
async def get_characters(user_id: int = Depends(jwt.parse_jwt_user_data)):
    characters = await service.get_all_user_characters(user_id)
    return [CharacterSchema(**character) for character in characters]


@router.get("/{character_name}")
async def get_own_character(character: CharacterSchema = Depends(get_valid_auth_character)):
    return character


@router.put("/reset/{character_name}")
async def reset_own_character(character: CharacterSchema = Depends(get_valid_auth_character)):
    await service.reset_character(character)
    return {"status": 200, "message": "success", "times_reset": character.times_reset + 1}


@router.delete("/delete/{character_name}")
async def delete_own_character(
    character: CharacterSchema = Depends(get_valid_auth_character),
    user_id: int = Depends(jwt.parse_jwt_user_data),
):
    await service.delete_character(character.name)
    await auth_service.update_user_data(user_id, char_delete=character.name)
    return {"message": f"successfuly deleted character '{character.name}'"}


@router.put("/select/{character_name}")
async def update_user_selected_character(
    user_id: int = Depends(jwt.parse_jwt_user_data),
    character: CharacterSchema = Depends(get_valid_auth_character),
):
    await auth_service.update_value(user_id, "selected_character", character.name)
    return {"status": 200, "message": "success"}


# TODO GET_JOURNEY FOR RANKING AND STUFF
@router.get("/journey/{character_name}")
async def get_character_journey(character_name: str):
    pass
