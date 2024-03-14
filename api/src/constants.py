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
    CHARACTER_NOT_FOUND = "Character not found."
    EMPTY_SELECTED_CHARACTER = "No selected character to handle quests for."
    CHARACTER_STATE_WINNER = "Can't play anymore. Your characters has retired after becoming a champion."
    CHARACTER_STATE_DEAD = "Can't play anymore. Your character is dead."
    LAST_QUEST_NOT_COMPLETED = "You need to complete your previous quest before generating a new one"
    QUEST_NOT_FOUND = "Quest not found"
    QUEST_NOT_OF_CURR_CHARACTER = "Quest doesn't belong to your selected character"
    INVALID_CHOSEN_APPROACH = "Invalid approach number"
    NOT_YOUR_SELECTED_CHARACTER = "Not your selected character"
    QUEST_ALREADY_COMPLETED = "This quest is already completed"
