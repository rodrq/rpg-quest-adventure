from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

from src.auth.exceptions import FieldsAreEmpty


class UserForm(BaseModel):
    username: str
    password: str

    @field_validator("*")
    def valid_user_fields(cls, value: str):
        if not value or value.isspace():
            raise FieldsAreEmpty
        return value


class UserResponse(BaseModel):
    id: int
    username: str
    is_admin: bool
    selected_character: Optional[str] = None

    class Config:
        from_attributes = True


class UserFullData(UserResponse):
    created_characters: List[str] | None = None


class JWTData(BaseModel):
    user_id: int = Field(alias="sub")


class AccessTokenResponse(BaseModel):
    access_token: str
