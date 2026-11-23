from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from ._base import Expression

__all__ = [
    "AwaitExpression",
    "YieldExpression",
]


@dataclass(frozen=True, slots=True, eq=False)
class AwaitExpression(Expression):
    """
    Await expression.

    Example:
        await value
    """

    argument: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


@dataclass(frozen=True, slots=True, eq=False)
class YieldExpression(Expression):
    """
    Yield expression.

    Examples:
        yield value
        yield* iterable
    """

    argument: Expression | None = None
    delegate: bool = False
    # The address of the `ResumeGenerator` this is the placeholder of (None for a real `yield`): two
    # placeholders of one function differ by it, so a copy of one (an object literal built from the
    # resumed value) is told from the placeholder of the NEXT resume point.
    resume_at: int | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.argument is None else (self.argument,)