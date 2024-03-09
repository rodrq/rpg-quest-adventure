from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from src.auth.dependencies import authenticate_character
from fastapi import HTTPException, status
from datetime import timedelta
from src.auth.jwt import create_access_token


def login_for_access_token_handler(form_data: OAuth2PasswordRequestForm, db: Session) -> JSONResponse:
    try:
        user = authenticate_character(
            form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=180)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        response = JSONResponse(
            content={"message": "Login succesfull"}, status_code=200)

        response.set_cookie(key="access_token",
                            value=f"Bearer {access_token}",
                            httponly=True)
        return response

    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
