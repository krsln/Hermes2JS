from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields, is_dataclass

from hermes_decompiler.ir.Location import SourceLocation

__all__ = [
    "Node",
]


@dataclass(frozen=True, slots=True, eq=False)
class Node(ABC):
    """
    Abstract base class for all IR nodes.

    Equality is identity-based (`eq=False`) rather than structural, since
    structural equality is expensive on large trees and rarely what
    callers want. Use `structurally_equal` when a deep comparison is
    actually needed.

    Subclasses must:
        - Declare `@dataclass(frozen=True, slots=True, eq=False)`.
          `eq=False` does not inherit automatically; omitting it
          silently restores structural `__eq__`/`__hash__`.
        - Implement `children` explicitly, listing only the fields
          that are semantically child nodes (e.g. excluding raw
          operands or register indices).
    """

    loc: SourceLocation | None = field(default=None, kw_only=True, compare=False, repr=False)

    @property
    @abstractmethod
    def children(self) -> tuple["Node", ...]:
        """Direct child nodes, in evaluation order."""

        raise NotImplementedError

    def structurally_equal(self, other: object) -> bool:
        """Deep, position-independent comparison of two nodes."""

        if type(self) is not type(other):
            return False

        if not is_dataclass(self):
            return self is other

        for f in fields(self):
            if f.name == "loc":
                continue

            self_value = getattr(self, f.name)
            other_value = getattr(other, f.name)

            if isinstance(self_value, Node):
                if not self_value.structurally_equal(other_value):
                    return False

            elif isinstance(self_value, tuple):
                if len(self_value) != len(other_value):
                    return False

                for a, b in zip(self_value, other_value):
                    if isinstance(a, Node):
                        if not a.structurally_equal(b):
                            return False
                    elif a != b:
                        return False

            elif self_value != other_value:
                return False

        return True

    def walk(self):
        """Pre-order traversal of this node and its full subtree."""

        yield self

        for child in self.children:
            yield from child.walk()
