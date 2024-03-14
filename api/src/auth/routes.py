from fastapi import APIRouter, Depends, status
from fastapi.responses import Response

from src.auth import service
from src.auth.dependencies import valid_username_create
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import UserBase, UserForm, UserInDb

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(response: Response, user_form: UserForm = Depends(valid_username_create)) -> UserBase:
    user = await service.create_user(user_form)
    await service.set_cookie_handler(user, response)
    return user


@router.post("/login")
async def login(auth_data: UserForm, response: Response) -> UserBase:
    user = await service.authenticate_user(auth_data)
    await service.set_cookie_handler(user, response)
    return user


@router.get("/user/me")
async def get_user_joined_data(user_id: int = Depends(parse_jwt_user_data)) -> UserBase:
    # Joined load all characters with FK user_id.
    user = await service.get_user_rel_joined_data(user_id)
    created_characters = [char["name"] for char in user if char["name"] is not None]
    return UserBase(**user[0], created_characters=created_characters)


@router.post("/logout")
async def logout(response: Response) -> dict[str, str]:
    response.delete_cookie(key="access_token")
    return {"message": "success logout"}
