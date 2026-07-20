from enum import Enum, auto


class BlockType(Enum):
    ENTRY = auto()

    NORMAL = auto()

    IF = auto()

    LOOP_HEADER = auto()

    LOOP_BODY = auto()

    SWITCH = auto()

    TRY = auto()

    CATCH = auto()

    FINALLY = auto()

    EXIT = auto()
