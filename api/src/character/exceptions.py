from src.exceptions import BadRequest
from src.constants import ErrorCode

class FieldsAreEmpty(BadRequest):
    DETAIL = ErrorCode.FIELDS_ARE_EMPTY
    
class CharacterNameTaken(BadRequest):
    DETAIL = ErrorCode.CHARACTER_NAME_TAKEN
    
class CharacterCantBeDeleted(BadRequest):
    DETAIL = ErrorCode.CHARACTER_CANT_BE_DELETED
    
class CharacterNotYours(BadRequest):
    DETAIL = ErrorCode.CHARACTER_NOT_YOURS