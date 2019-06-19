from enum import Enum
class ReviewState( Enum ):
    READY_FOR_ANSWER = 0
    ANSWER_SHOWN = 1
    ANSWER_GIVEN = 2
    WAITING_FOR_INCORRECT_DELAY = 3
