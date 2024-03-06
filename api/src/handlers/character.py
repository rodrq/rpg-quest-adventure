from src.models.schemas import CharacterInDb
from src.models.models import Character, Quest
from src.utils.pw_hash import get_hashed_password
from src.utils.query import get_character_query
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.utils.auth import create_access_token


async def create_character_handler(create_character_params: CharacterInDb, db: Session):
    try:    
        if get_character_query(create_character_params.username, db):
                raise ValueError("Character username already exists")
        character = Character(
            username=create_character_params.username,
            password=get_hashed_password(create_character_params.password),
            class_=create_character_params.class_,
            virtue = create_character_params.virtue,
            flaw = create_character_params.flaw
        )
          
        db.add(character)
        db.commit()

        token_data = {"sub": create_character_params.username}
        access_token = create_access_token(token_data)
        
        response = JSONResponse(content={"message": "Created character"})
        response.set_cookie(key="token", value=access_token, max_age=7200, samesite='none', secure=True, httponly=True)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def reset_character_handler(current_character: Character, db:Session):
    try:
        if current_character:
            current_character.map_level = 1
            current_character.honor_points = 0
            current_character.char_state = 'adventuring'
            current_character.times_reset +=  1
            db.query(Quest).filter(Quest.character_username == current_character.username).delete()
            db.commit()
            return {'message': 'Character reset.' }
    except Exception as e:
        HTTPException(status_code=500, detail=str(e, 'error on reset_character_handler'))