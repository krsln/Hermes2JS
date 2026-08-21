from enum import Enum


class LoopKind(Enum):
    UNKNOWN = "unknown"
    WHILE = "while"
    DO_WHILE = "do_while"
    FOR = "for"
    FOR_OF = "for_of"
    FOR_IN = "for_in"
    ENDLESS = "endless"
