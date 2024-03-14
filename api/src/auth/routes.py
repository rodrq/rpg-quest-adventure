from fastapi import APIRouter, Depends
from fastapi.responses import Response

from src.auth import jwt, service
from src.auth.dependencies import valid_username_create
from src.auth.jwt import parse_jwt_user_data
from src.auth.models import User
from src.auth.schemas import AccessTokenResponse, UserForm, UserFullData

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/user")
async def create_user(
    response: Response, user_form: UserForm = Depends(valid_username_create)
) -> dict[str, str]:
    user = await service.create_user(user_form)
    access_token_value = jwt.create_access_token(user_id=user["id"])
    response.set_cookie(key="access_token", value=access_token_value, httponly=True)
    return {"message": "success", "created": user["username"]}


@router.get("/user/me")
async def get_user_joined_data(user_id: int = Depends(parse_jwt_user_data)) -> UserFullData:
    # Joined load all characters with FK user_id.
    user: User = await service.get_user_rel_joined_data(user_id)
    created_characters = [char["name"] for char in user if char["name"] is not None]
    return UserFullData(**user[0], created_characters=created_characters)


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
