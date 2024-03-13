from src.constants import ErrorCode
from src.exceptions import BadRequest, NotFound


class EmptySelectedCharacter(BadRequest):
    DETAIL = ErrorCode.EMPTY_SELECTED_CHARACTER


class CharacterStateWinner(BadRequest):
    DETAIL = ErrorCode.CHARACTER_STATE_WINNER


class CharacterStateDead(BadRequest):
    DETAIL = ErrorCode.CHARACTER_STATE_DEAD


class LastQuestNotCompleted(BadRequest):
    DETAIL = ErrorCode.LAST_QUEST_NOT_COMPLETED


class QuestBelongsToAnotherCharacter(BadRequest):
    DETAIL = ErrorCode.QUEST_NOT_OF_CURR_CHARACTER


class QuestNotFound(NotFound):
    DETAIL = ErrorCode.QUEST_NOT_FOUND
