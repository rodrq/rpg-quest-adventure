# from src.character.schemas import CharacterInDb
# from src.character import service
# from src.exceptions import 
# async def valid_character_create(character_form: CharacterInDb) -> CharacterInDb:
#     if await service.get_character_by_name(character_form.username):
#         raise EmailTaken()

#     return user

# def get_current_character_username(token: str = Depends(oauth2_scheme)):
#     character_name = decode_jwt_token_sub(token)
#     return character_name


# def get_current_character(character_name: str = Depends(get_current_character_username)):
#     character = get_character_query(username=character_name)
#     if character is None:
#         raise credentials_exception
#     return character