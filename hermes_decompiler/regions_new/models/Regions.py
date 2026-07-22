from __future__ import annotations

from abc import ABC
from enum import Enum
from typing import TYPE_CHECKING

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock

if TYPE_CHECKING:
    from hermes_decompiler.regions_new.models.Statements import Statement


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
        self.statements: list[Statement] = []

    def append(self, node):
        if isinstance(node, Region):
            node.parent = self

        self.children.append(node)


class LoopRegion:

    def __init__(self, loop):
        self.header_block = loop.header

        self.condition = None
        self.loop_kind = None
        self.body = SequenceRegion()

        self.exits = list(loop.exits)
        self.latches = list(loop.latches)

    @property
    def header(self):
        return self.header_block


class IfRegion(Region):

    def __init__(self):
        super().__init__()

        self.condition: str = ""

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
