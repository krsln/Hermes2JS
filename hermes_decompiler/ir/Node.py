from __future__ import annotations

from abc import ABC, abstractmethod

from abc import ABC
from dataclasses import fields, is_dataclass


class Node(ABC):

    @property
    def children(self) -> tuple["Node", ...]:
        if not is_dataclass(self):
            return ()

        children: list[Node] = []

        for field in fields(type(self)):
            value = getattr(self, field.name)

            if isinstance(value, Node):
                children.append(value)

            elif isinstance(value, tuple):
                children.extend(
                    child
                    for child in value
                    if isinstance(child, Node)
                )

        return tuple(children)


class Node_(ABC):
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


class Value(Node_, ABC):
    """
    Represents a JavaScript value.
    """
    pass


class Expression(Value, ABC):
    """
    Represents an expression producing a value.
    """
    pass


class Statement(Node_, ABC):
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
