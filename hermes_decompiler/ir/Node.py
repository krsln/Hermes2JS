from __future__ import annotations

from abc import ABC, abstractmethod


class Node(ABC):
    """
    Base class for every IR node.
    """

    @abstractmethod
    def render(self) -> str:
        """
        Temporary compatibility layer.

        Rendering will eventually be moved to JSRenderer.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.render()


class Value(Node, ABC):
    """
    Represents a JavaScript value.
    """
    pass


class Expression(Value, ABC):
    """
    Represents an expression producing a value.
    """
    pass


class Statement(Node, ABC):
    """
    Represents an executable statement.
    """
    pass

#                 Node
#               /      \
#          Statement   Value
#                       |
#                  Expression
#                       |
#          -------------------------
#          |           |          |
#      Binary      Call       Identifier

#                 Node
#                /    \
#               /      \
#      Statement      Expression
