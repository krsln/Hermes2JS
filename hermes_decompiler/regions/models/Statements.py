from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hermes_decompiler.ir import Expression, Node, Statement
from hermes_decompiler.models.OpcodeResult import OpcodeResult


@dataclass(slots=True)
class State:
    parent: Any = field(default=None, kw_only=True)


@dataclass(slots=True)
class InstructionState(State):
    block: Any  # BasicBlock; left untyped here to avoid a hard import cycle
    index: int
    result: OpcodeResult


# ============================================================================
# Pre-structural control flow
# ============================================================================
#
# JS has no `goto`. These two nodes are CFG-level IR only: the raw
# output of jump opcodes (Jmp*, JCompareX, ...) before
# StructuralAnalyzer/Structurers replace them with real `while`/`if`/
# `break`/`continue` nodes from `ir.statements`. They live here, not in
# `ir/`, because `ir/` models the *final* JS AST and these have no JS
# equivalent - they should not survive past the structuring pass into
# rendered output outside verbose/debug mode.
#
# They still subclass `ir.Statement` (rather than being a wholly
# separate hierarchy) so they can be carried on `JSVariable.statement`
# and printed by `Printer` like any other statement during this
# transitional, pre-structuring stage.
# ============================================================================


@dataclass(frozen=True, slots=True, eq=False)
class GotoStatement(Statement):
    """Unconditional jump to another basic block, pre-structuring."""

    target: int

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


@dataclass(frozen=True, slots=True, eq=False)
class IfGotoStatement(Statement):
    """Conditional jump to another basic block, pre-structuring."""

    condition: Expression
    target: int

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.condition,)