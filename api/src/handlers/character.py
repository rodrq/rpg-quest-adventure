from src.models.schemas import CharacterInDb
from src.models.models import Character
from src.utils.pw_hash import get_hashed_password
from src.utils.query import get_character
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.utils.auth import create_access_token


async def create_character_handler(params: CharacterInDb, db: Session):
    try:
        if get_character(params.username):
                raise HTTPException(status_code=400, detail="Character username already exists")
        character = Character(
            username=params.username,
            password=get_hashed_password(params.password),
            class_=params.class_
        )
          
        db.add(character)
        db.commit()

        token_data = {"sub": params.username}
        access_token = create_access_token(token_data)
        
        response = JSONResponse(content={"message": "Created character"})
        response.set_cookie(key="token", value=access_token, max_age=1800, samesite='none', secure=True, httponly=True)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
    
