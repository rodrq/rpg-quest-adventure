from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response, JSONResponse
from src.handlers.auth import login_for_access_token_handler
from src.utils.auth import check_token
from typing import Annotated

router = APIRouter(prefix="/auth",
                   tags=["Authorization"])


@router.post("/")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return login_for_access_token_handler(form_data)
    
@router.get("/logout")
async def logout(response: Response):
    response = JSONResponse(content={"message": "Logout succesfull"})
    response.delete_cookie("token")
    return response

@router.get("/is_logged")
async def check_login(token_check: Annotated[bool, Depends(check_token)]):
    return token_check
    
