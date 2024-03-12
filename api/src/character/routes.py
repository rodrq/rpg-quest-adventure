from typing import Any
from fastapi import APIRouter, Depends
from src.auth import jwt
from src.character.schemas import CharacterBase, CharacterResponse
from src.character.dependencies import valid_character_create, valid_user_character_delete, valid_user_character_fetch
from src.character import service


router = APIRouter(prefix="/characters", tags=['Character creation'])

@router.post("/")
async def create_character(character_form: CharacterBase = Depends(valid_character_create),
                           user_id: str = Depends(jwt.parse_jwt_user_data)):
    
    character = await service.create_character(character_form, user_id)
    return CharacterResponse(**character)


@router.get("/")
async def get_characters(user_id: str = Depends(jwt.parse_jwt_user_data)):
    characters = await service.get_characters_by_user_id(user_id)
    return [CharacterResponse(**character) for character in characters]
    

@router.get("/{character_name}")
async def get_own_character(character_name: str = Depends(valid_user_character_fetch)):
    character = await service.get_character_by_name(character_name)
    return CharacterResponse(**character)


@router.put("/{character_name}")
async def reset_own_character(character_name: str = Depends(valid_user_character_fetch)):
    character = await service.update_character_by_name(character_name)
    return CharacterResponse(**character)


@router.delete("/{character_name}")
async def delete_own_character(character_name: str = Depends(valid_user_character_delete)):
    await service.delete_character_by_name(character_name)
    return {"message": f"successfuly deleted character '{character_name}'"} #TODO better response


