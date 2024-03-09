from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response, JSONResponse
from sqlalchemy.orm import Session
from src.auth.service import login_for_access_token_handler
from src.database import get_db


auth_router = APIRouter(prefix="/auth", tags=["Authorization"])


@auth_router.post("/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: Session = Depends(get_db)) -> JSONResponse:
    return login_for_access_token_handler(form_data, db)


@auth_router.post("/logout")
async def logout(response: Response) -> JSONResponse:
    response = JSONResponse(content={"message": "Logout succesful"})
    response.delete_cookie("token")
    return response
