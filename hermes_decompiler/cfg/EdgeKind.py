from enum import Enum, auto


class EdgeKind(Enum):
    """
    Semantic type of a Control Flow Graph edge.
    """

    FALLTHROUGH = auto()

    TRUE_BRANCH = auto()

    FALSE_BRANCH = auto()

    UNCONDITIONAL = auto()

    EXCEPTION = auto()