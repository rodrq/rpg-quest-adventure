# from typing import Any
# from src.auth.jwt import create_access_token
# from src.auth.security import get_hashed_password
# from src.database import character, fetch_one
# from src.character.schemas import CharacterInDb
# from fastapi.responses import JSONResponse
# from fastapi import HTTPException, status
# from sqlalchemy.orm import Session
# from sqlalchemy import func, insert

# async def create_character(character_form: CharacterInDb) -> dict[str, Any] | None:
#     insert_query = (
#         insert(character)
#         .values(
#             {
#                 "username": character_form.username,
#                 "hashed_password": character_form.password,
#                 "class_": character_form.class_,
#                 "virtue": character_form.virtue,
#                 "flaw": character_form.flaw,
#             }
#         )
#         .returning(character)
#     )

#     return await fetch_one(insert_query)

# # def get_character_query(username: str, db: Session):
# #     queried_character = db.query(Character).filter(
# #         func.lower(Character.username) == username.lower()).first()
# #     return queried_character


# # async def create_character_handler(create_character_params: CharacterInDb, db: Session):
# #     try:
# #         if get_character_query(create_character_params.username, db):
# #             raise HTTPException(status.HTTP_409_CONFLICT,
# #                                 detail="Character username already exists")
# #         character = Character(
# #             username=create_character_params.username,
# #             hashed_password=get_hashed_password(
# #                 create_character_params.password),

# #             class_=create_character_params.class_,
# #             virtue=create_character_params.virtue,
# #             flaw=create_character_params.flaw
# #         )

# #         db.add(character)
# #         db.commit()

# #         token_data = {"sub": create_character_params.username}
# #         access_token = create_access_token(token_data)

# #         response = JSONResponse(content={"message": "Created character"})
# #         response.set_cookie(key="access_token",
# #                             value=f"Bearer {access_token}",
# #                             httponly=True)
# #         return response

# #     except Exception as e:
# #         raise HTTPException(
# #             status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
