from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, field_validator

from src.auth.exceptions import FieldsAreEmpty


class UserForm(BaseModel):
    username: str
    password: str

    @field_validator("*")
    def valid_user_fields(cls, value: str):
        if not value or value.isspace():
            raise FieldsAreEmpty
        return value


class UserBase(BaseModel):
    id: int
    username: str
    is_admin: bool
    selected_character: Optional[str] = None
    created_characters: Optional[List[Optional[str]]] = None


class UserSchema(UserBase):
    hashed_password: bytes
    created_at: datetime
    updated_at: Optional[datetime] = None
