from fastapi import APIRouter, Depends

from src.auth import jwt
from src.auth.schemas import UserResponse
from src.character import service
from src.character.dependencies import valid_character_create, valid_user_character_fetch
from src.character.schemas import CharacterBase, CharacterResponse

router = APIRouter(prefix="/character", tags=["Character endpoints"])


@router.post("/")
async def create_character(
    character_form: CharacterBase = Depends(valid_character_create),
    user_id: str = Depends(jwt.parse_jwt_user_data),
):
    created_character = await service.create_character(character_form, user_id)
    await service.add_to_users_character_list(created_character["name"], user_id)
    return CharacterResponse(**created_character)


@router.get("/")
async def get_characters(user_id: int = Depends(jwt.parse_jwt_user_data)):
    characters = await service.get_all_user_characters(user_id)
    return [CharacterResponse(**character) for character in characters]


@router.get("/{character_name}")
async def get_own_character(character: CharacterResponse = Depends(valid_user_character_fetch)):
    return CharacterResponse(**character)


@router.put("/reset/{character_name}")
async def reset_own_character(character: CharacterResponse = Depends(valid_user_character_fetch)):
    character = await service.reset_character_by_name(character["name"])
    return CharacterResponse(**character)


@router.delete("/delete/{character_name}")
async def delete_own_character(
    character: CharacterResponse = Depends(valid_user_character_fetch),
    user_id: int = Depends(jwt.parse_jwt_user_data),
):
    await service.delete_character(character["name"])
    await service.delete_from_users_character_list(character["name"], user_id)
    return {"message": f"successfuly deleted character '{character["name"]}'"}  # TODO better response


@router.put("/select/{character_name}")
async def update_user_selected_character(
    character: CharacterResponse = Depends(valid_user_character_fetch),
    user_id: int = Depends(jwt.parse_jwt_user_data),
):
    updated_user = await service.update_user_selected_character(character["name"], user_id)
    return UserResponse(**updated_user)


# TODO GET_JOURNEY FOR RANKING AND STUFF
@router.get("/journey/{character_name}")
async def get_character_journey(character_name: str):
    pass
