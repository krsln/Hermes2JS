from enum import Enum


class BlockType(Enum):
    NORMAL = "normal"

    IF = "if"
    LOOP = "loop"

    TRY = "try"
    CATCH = "catch"
    FINALLY = "finally"