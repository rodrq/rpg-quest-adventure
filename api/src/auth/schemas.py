from pydantic import BaseModel, Field, field_validator, Extra
from src.auth.exceptions import FieldsAreEmpty

class UserSchema(BaseModel):
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
    

class JWTData(BaseModel):
    user_id: int = Field(alias="sub")
    is_admin: bool = False


class AccessTokenResponse(BaseModel):
    access_token: str
    refresh_token: str


