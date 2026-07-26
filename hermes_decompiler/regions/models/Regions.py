from __future__ import annotations

from abc import ABC
from enum import Enum
from typing import TYPE_CHECKING

from hermes_decompiler.ir import Expression
from hermes_decompiler.regions.cfg.BasicBlock import BasicBlock

if TYPE_CHECKING:
    from hermes_decompiler.regions.models.Statements import State


class Region(ABC):

    def __init__(self):
        self.parent: Region | None = None


class LoopKind(Enum):
    WHILE = "while"
    DO_WHILE = "do_while"
    FOR = "for"
    ENDLESS = "endless"


class SequenceRegion(Region):

    def __init__(self):
        super().__init__()

        self.children: list[BasicBlock | Region] = []
        self.statements: list[State] = []
        self.items = []

    def append(self, node):
        if isinstance(node, Region):
            node.parent = self

        self.children.append(node)


class LoopRegion(Region):

    def __init__(self, loop):
        super().__init__()
        self.header_block = loop.header

        self.condition = None
        self.loop_kind = LoopKind.WHILE
        self.body = SequenceRegion()

        self.exits = list(loop.exits)
        self.latches = list(loop.latches)

    @property
    def header(self):
        return self.header_block


class IfRegion(Region):

    def __init__(self):
        super().__init__()

        # NOTE: an `ir.Expression`, not pre-rendered text - kept as real
        # IR through the structuring passes (e.g. `BooleanChainFolder`
        # needs to structurally compare conditions) and only turned into
        # a string by `JSRenderer`/`Printer` at output time.
        self.condition: Expression | None = None

        self.then_body = SequenceRegion()

        self.else_body: SequenceRegion | None = None


class CatchRegion(Region):

    def __init__(self):
        super().__init__()

        self.exception: str | None = None

        self.body = SequenceRegion()


class FinallyRegion(Region):

    def __init__(self):
        super().__init__()

        self.body = SequenceRegion()