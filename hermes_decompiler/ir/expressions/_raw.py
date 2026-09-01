from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from ._base import Expression

__all__ = [
    "RawExpression",
]


@dataclass(frozen=True, slots=True, eq=False)
class RawExpression(Expression):
    """
    TEMPORARY bridge for values that don't yet have a proper AST node
    (e.g., Hermes-specific concepts: closures, generators, builtins,
    caught exceptions). Carries pre-rendered source text verbatim.

    This is technical debt, not a permanent part of the IR surface.
    Every use site should eventually be replaced with a dedicated node
    once its JS semantics are fully modeled. Do not add new callers
    without a comment explaining why a proper node isn't possible yet.
    """

    source: str

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
