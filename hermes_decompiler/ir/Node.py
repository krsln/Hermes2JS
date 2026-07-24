from __future__ import annotations

from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def render(self) -> str:
        """
        Temporary compatibility layer.

        This method will be removed once the Visitor/Renderer
        infrastructure fully replaces node rendering.
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
