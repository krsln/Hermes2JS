from __future__ import annotations

from abc import ABC
from dataclasses import fields, is_dataclass, dataclass


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

#                 Node
#                /    \
#               /      \
#      Statement      Expression
