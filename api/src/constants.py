from enum import Enum


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

class Environment(str, Enum):
    LOCAL = "LOCAL"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

class ErrorCode:
    AUTHENTICATION_REQUIRED = "Authentication required."
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    FIELDS_ARE_EMPTY = "One or all required fields are empty"
    USERNAME_TAKEN = "Username is already taken."
    CHARACTER_NAME_TAKEN = "Character name is already taken."
    REFRESH_TOKEN_NOT_VALID = "Refresh token is not valid."
    REFRESH_TOKEN_REQUIRED = "Refresh token is required either in the body or cookie."
    CHARACTER_CANT_BE_DELETED = "Character either doesn't exist or isn't yours"
    CHARACTER_NOT_YOURS = "Character isn't yours"