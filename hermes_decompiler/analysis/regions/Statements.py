from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hermes_decompiler.opcode import OpcodeResult


@dataclass(slots=True)
class State:
    parent: Any = field(default=None, kw_only=True)


@dataclass(slots=True)
class InstructionState(State):
    block: Any  # BasicBlock; left untyped here to avoid a hard import cycle
    index: int
    result: OpcodeResult
