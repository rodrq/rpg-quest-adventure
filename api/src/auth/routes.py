from fastapi import APIRouter, Depends, status
from fastapi.responses import Response

from src.auth import service
from src.auth.dependencies import valid_username_create
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import UserBase, UserForm

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(response: Response, user_form: UserForm = Depends(valid_username_create)) -> UserBase:
    user = await service.create_user(user_form)
    await service.set_cookie_handler(user, response)
    return user


@router.post("/login")
async def login(auth_data: UserForm, response: Response) -> UserBase:
    user = await service.authenticate_user(auth_data)
    user = UserBase.model_validate(user)
    await service.set_cookie_handler(user, response)
    return user


@router.get("/user/me")
async def get_user_data(user_id: int = Depends(parse_jwt_user_data)) -> UserBase:
    return await service.get_user_by_id(user_id)


@router.post("/logout")
async def logout(response: Response) -> dict[str, str]:
    response.delete_cookie(key="access_token")
    return {"message": "success logout"}
