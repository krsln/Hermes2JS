from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.regions.cfg.BasicBlock import BasicBlock


@dataclass(slots=True)
class State:
    parent: Any = field(default=None, kw_only=True)


@dataclass(slots=True)
class InstructionState(State):
    block: BasicBlock
    index: int
    result: OpcodeResult

#
# @dataclass(slots=True)
# class BreakStatement(Statement):
#     pass
#
#
# @dataclass(slots=True)
# class ContinueStatement(Statement):
#     pass
#
#
# @dataclass(slots=True)
# class ReturnStatement(Statement):
#     expression: str | None = None
#
#
# @dataclass(slots=True)
# class ThrowStatement(Statement):
#     expression: str | None = None
#
#
# @dataclass(slots=True)
# class GotoStatement(Statement):
#     source: BasicBlock
#
#     target: BasicBlock
#
#
# @dataclass(slots=True)
# class IfGotoStatement(Statement):
#     source: BasicBlock
#
#     condition: str
#
#     target: BasicBlock

