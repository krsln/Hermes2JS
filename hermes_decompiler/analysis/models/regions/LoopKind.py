from enum import Enum, auto


class LoopKind(Enum):
    UNKNOWN = "unknown"
    WHILE = "while"
    DO_WHILE = "do_while"
    FOR = "for"
    FOR_OF = "for_of"
    FOR_IN = "for_in"
    ENDLESS = "endless"


# class LoopKind(Enum):
#     UNKNOWN = auto()
#     WHILE = auto()
#     DO_WHILE = auto()
#     FOR = auto()
#     FOR_OF = auto()
#     FOR_IN = auto()
#     ENDLESS = auto()
