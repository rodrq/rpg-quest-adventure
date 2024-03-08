from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response, JSONResponse
from sqlalchemy.orm import Session
from src.handlers.auth import login_for_access_token_handler
from src.config.database import get_db


router = APIRouter(prefix="/auth",
                   tags=["Authorization"])


@router.post("/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: Session = Depends(get_db)) -> JSONResponse:
    return login_for_access_token_handler(form_data, db)


@router.post("/logout")
async def logout(response: Response) -> JSONResponse:
    response = JSONResponse(content={"message": "Logout succesful"})
    response.delete_cookie("token")
    return response
