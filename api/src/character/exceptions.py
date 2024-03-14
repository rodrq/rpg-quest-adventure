from src.constants import ErrorCode
from src.exceptions import BadRequest, NotFound


class FieldsAreEmpty(BadRequest):
    DETAIL = ErrorCode.FIELDS_ARE_EMPTY


class CharacterNameTaken(BadRequest):
    DETAIL = ErrorCode.CHARACTER_NAME_TAKEN


class CharacterCantBeDeleted(BadRequest):
    DETAIL = ErrorCode.CHARACTER_CANT_BE_DELETED


class CharacterNotFound(NotFound):
    DETAIL = ErrorCode.CHARACTER_NOT_FOUND


class EmptySelectedCharacter(BadRequest):
    DETAIL = ErrorCode.EMPTY_SELECTED_CHARACTER


class NotYourCurrentSelectedCharacter(BadRequest):
    DETAIL = ErrorCode.NOT_YOUR_SELECTED_CHARACTER
