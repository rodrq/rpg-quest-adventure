from fastapi import APIRouter, Depends
from fastapi.responses import Response

from src.auth import jwt, service
from src.auth.dependencies import valid_username_create
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import AccessTokenResponse, UserForm, UserResponse

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/user")
async def create_user(user_form: UserForm = Depends(valid_username_create)) -> dict[str, str]:
    user = await service.create_user(user_form)
    return {"message": "success", "created": user["username"]}


@router.get("/user/me")
async def get_my_user(user_id: int = Depends(parse_jwt_user_data)) -> UserResponse:
    user = await service.get_user_by_id(user_id)
    return UserResponse(**user)


@router.post("/login")
async def login(auth_data: UserForm, response: Response) -> AccessTokenResponse:
    user = await service.authenticate_user(auth_data)
    access_token_value = jwt.create_access_token(user_id=user.id)
    response.set_cookie(key="access_token", value=access_token_value, httponly=True)

    return AccessTokenResponse(access_token=access_token_value)


@router.post("/logout")
async def logout(response: Response) -> dict[str, str]:
    response.delete_cookie(key="access_token")
    return {"message": "success logout"}
