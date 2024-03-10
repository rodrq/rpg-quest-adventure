from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import Response, JSONResponse
from src.auth.schemas import UserSchema, AccessTokenResponse, JWTData, UserResponse
from src.auth.dependencies import valid_username_create
from src.auth import service, jwt
from src.auth.jwt import parse_jwt_user_data

router = APIRouter(prefix="/auth", tags=["Authorization"])

@router.post("/user")
async def create_user(user_form: UserSchema = Depends(valid_username_create)):
    user = await service.create_user(user_form)
    return {
        "message": "success", "created": user['username']
    }


@router.get("/user/me")
async def get_my_user(jwt_data: Annotated[JWTData, Depends(parse_jwt_user_data)]) -> UserResponse:
    user = await service.get_user_by_id(jwt_data.user_id)
    return UserResponse(**user)


#LOGIN
@router.post("/tokens")
async def auth_user(auth_data: UserSchema, response: Response) -> AccessTokenResponse:
    user = await service.authenticate_user(auth_data)
    refresh_token_value = await service.create_refresh_token(user_id=user["id"])
    access_token_value = jwt.create_access_token(user=user)
    response.set_cookie(key="refresh_token", value=refresh_token_value, httponly=True)
    response.set_cookie(key="access_token", value=access_token_value, httponly=True)

    return AccessTokenResponse(
        access_token=access_token_value,
        refresh_token = refresh_token_value,
    )


# @router.post("/logout")
# async def logout(response: Response) -> JSONResponse:
#     response = JSONResponse(content={"message": "Logout succesful"})
#     response.delete_cookie("token")
#     return response
