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
    characters_ids: list[int] | None
    current_character: str | None
    is_admin: bool


class JWTData(BaseModel):
    user_id: int = Field(alias="sub")


class AccessTokenResponse(BaseModel):
    access_token: str
