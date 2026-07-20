from enum import Enum, auto


class EdgeKind(Enum):
    """
    Type of control-flow transition between two basic blocks.
    """

    FALLTHROUGH = auto()

    JUMP = auto()

    TRUE = auto()

    FALSE = auto()

    EXCEPTION = auto()
