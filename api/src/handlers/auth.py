from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.utils.auth import authenticate_character, create_access_token
from fastapi.responses import JSONResponse
from datetime import timedelta
from src.config.settings import TOKEN_LIFETIME_MINUTES

def login_for_access_token_handler(form_data: OAuth2PasswordRequestForm):
    try:
        user = authenticate_character(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=int(TOKEN_LIFETIME_MINUTES))
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        response = JSONResponse(content={"message": "Login succesfull"})
        response.set_cookie(key="token", value=access_token, max_age=1800, samesite='none', secure=True, httponly=True)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
