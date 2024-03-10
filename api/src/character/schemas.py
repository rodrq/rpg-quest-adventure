# from fastapi import HTTPException, status
# from pydantic import BaseModel



# class CharacterParams(BaseModel):
#     username: str
#     class_: str
#     virtue: str
#     flaw: str

# class CharacterInDb(CharacterParams):
#     password: str


# def form_validator(key: str, value: str) -> str:
#     if key in ('username', 'password'):
#         if not value or value.isspace():
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                                 detail=f"{key} can't be empty.")
#         return value

#     enum_mapping = {
#         'class_': CharacterClassEnum,
#         'virtue': CharacterVirtueEnum,
#         'flaw': CharacterFlawEnum,
#     }

#     enum_member = enum_mapping.get(key)

#     if value and value not in enum_member:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail=f"{value} is not a valid {key}")
#     return value