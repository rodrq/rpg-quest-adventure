from fastapi import Depends
from src.auth.jwt import parse_jwt_user_data


# def get_current_character(user_id: int = Depends(parse_jwt_user_data)):
#     current_character = 
#     pass


# def valid_create_quest(current_character: str = Depends(get_current_character)):
#     pass

