from src.constants import ErrorCode
from src.exceptions import BadRequest, NotFound, PermissionDenied


class CharacterStateWinner(BadRequest):
    DETAIL = ErrorCode.CHARACTER_STATE_WINNER


class CharacterStateDead(BadRequest):
    DETAIL = ErrorCode.CHARACTER_STATE_DEAD


class LastQuestNotCompleted(BadRequest):
    DETAIL = ErrorCode.LAST_QUEST_NOT_COMPLETED


class QuestUnauthorized(PermissionDenied):
    DETAIL = ErrorCode.QUEST_UNAUTHORIZED


class QuestNotFound(NotFound):
    DETAIL = ErrorCode.QUEST_NOT_FOUND


class InvalidApproachChoice(BadRequest):
    DETAIL = ErrorCode.INVALID_CHOSEN_APPROACH


class QuestAlreadyCompleted(BadRequest):
    DETAIL = ErrorCode.QUEST_ALREADY_COMPLETED
