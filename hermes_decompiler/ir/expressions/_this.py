from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from ._base import Expression

__all__ = [
    "ThisPlaceholder",
]


@dataclass(frozen=True, slots=True, eq=False)
class ThisPlaceholder(Expression):
    """
    TEMPORARY bridge sentinel for the uninitialized `this` object produced
    by CreateThis / CreateThisForNew / CreateThisForSuper. Has no JS
    surface syntax of its own -- it exists solely to be consumed by the
    following Construct/ConstructLong (or super-call) opcode handler,
    which strips it out of the collected argument list before building
    the final expression.

    Unlike RawExpression, this value must NEVER survive into a rendered
    AST node. If it does, that's a bug in whichever handler failed to
    consume it -- the pretty-printer should treat encountering one as a
    hard failure, not print it as source text.

    `origin` identifies which opcode created it (debug-only).
    `source_reg` is the constructor/new_target register it derives from
    (debug-only).
    """

    origin: str
    source_reg: int

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
