from src.constants import ErrorCode
from src.exceptions import BadRequest, NotAuthenticated, PermissionDenied


class FieldsAreEmpty(BadRequest):
    DETAIL = ErrorCode.FIELDS_ARE_EMPTY


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class AuthorizationFailed(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class UsernameTaken(BadRequest):
    DETAIL = ErrorCode.USERNAME_TAKEN
