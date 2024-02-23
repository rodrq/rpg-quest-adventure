from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response, JSONResponse
from src.handlers.auth import login_for_access_token_handler
from src.utils.auth import check_token
from typing import Annotated
from src.config.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/auth",
                   tags=["Authorization"])


@router.post("/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: Session = Depends(get_db)):
    return login_for_access_token_handler(form_data, db)
    
@router.get("/logout")
async def logout(response: Response):
    response = JSONResponse(content={"message": "Logout succesfull"})
    response.delete_cookie("token")
    return response

    
