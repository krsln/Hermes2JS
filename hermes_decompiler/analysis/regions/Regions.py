from __future__ import annotations

from abc import ABC
from enum import Enum

from hermes_decompiler.ir import Expression
from hermes_decompiler.analysis.cfg import BasicBlock


class Region(ABC):
    """
    Base class for every node in the region tree.

    `covered_blocks` is the set of every raw BasicBlock reachable
    anywhere under this region. It's lazily computed and cached;
    `invalidate_coverage()` must be called whenever the subtree
    changes shape and propagates up through `.parent` so an ancestor
    never serves a stale answer.
    """

    def __init__(self):
        self.parent: Region | None = None
        self._covered_blocks: set[BasicBlock] | None = None

    @property
    def covered_blocks(self) -> set[BasicBlock]:
        if self._covered_blocks is None:
            self._covered_blocks = self._compute_covered_blocks()

        return self._covered_blocks

    def invalidate_coverage(self) -> None:
        if self._covered_blocks is None and self.parent is None:
            return
        self._covered_blocks = None
        if self.parent is not None:
            self.parent.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        raise NotImplementedError


class LoopKind(Enum):
    WHILE = "while"
    DO_WHILE = "do_while"
    FOR = "for"
    ENDLESS = "endless"
    FOR_OF = "for_of"
    FOR_IN = "for_in"


class SequenceRegion(Region):

    def __init__(self):
        super().__init__()

        self.children: list[BasicBlock | Region] = []
        self.items = []

    def append(self, node):
        if isinstance(node, Region):
            node.parent = self

        self.children.append(node)
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        covered: set[BasicBlock] = set()

        for child in self.children:
            if isinstance(child, BasicBlock):
                covered.add(child)
            else:
                covered |= child.covered_blocks

        return covered


class SwitchCase:
    """
    One `case` label group in a `SwitchRegion`.

    `tests` holds one Expression per label sharing this body - more
    than one entry means fallthrough labels with no code between them
    (`case 3: case 4: body`), which share a single `body` SequenceRegion
    rather than being duplicated.
    """

    def __init__(self, tests: list, body: "SequenceRegion"):
        self.tests = tests
        self.body = body


class SwitchRegion(Region):

    def __init__(self, discriminant):
        super().__init__()

        self.discriminant = discriminant
        self.cases: list[SwitchCase] = []

        self._default_body: SequenceRegion | None = None

    @property
    def default_body(self) -> "SequenceRegion | None":
        return self._default_body

    @default_body.setter
    def default_body(self, value: "SequenceRegion | None") -> None:
        self._default_body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    def add_case(self, case: SwitchCase) -> None:
        case.body.parent = self
        self.cases.append(case)
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        covered: set[BasicBlock] = set()

        for case in self.cases:
            covered |= case.body.covered_blocks

        if self._default_body is not None:
            covered |= self._default_body.covered_blocks

        return covered


class LoopRegion(Region):
    """
    NOTE: `body` is a property. Assigning `loop_region.body = x`
    (as opposed to mutating `loop_region.body.children` in place, which
    `LoopStructurer` does) automatically reparents `x` and invalidates
    coverage - this is what makes the earlier bug (structurers
    silently overwriting a subregion without fixing its `.parent`)
    structurally impossible instead of a discipline problem.
    """

    def __init__(self, loop):
        super().__init__()
        self.header_block = loop.header

        self.condition = None
        self.loop_kind = LoopKind.WHILE
        self.iterable = None  # for-of: arrays, for-in: objects
        self.loop_binding = None  # dest_reg

        self._body = SequenceRegion()
        self._body.parent = self

        self.exits = list(loop.exits)
        self.latches = list(loop.latches)

    @property
    def header(self):
        return self.header_block

    @property
    def body(self) -> SequenceRegion:
        return self._body

    @body.setter
    def body(self, value: SequenceRegion) -> None:
        self._body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        return set(self._body.covered_blocks)


class IfRegion(Region):

    def __init__(self):
        super().__init__()

        self.condition: Expression | None = None

        self._then_body = SequenceRegion()
        self._then_body.parent = self

        self._else_body: SequenceRegion | None = None

    @property
    def then_body(self) -> SequenceRegion:
        return self._then_body

    @then_body.setter
    def then_body(self, value: SequenceRegion) -> None:
        self._then_body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    @property
    def else_body(self) -> SequenceRegion | None:
        return self._else_body

    @else_body.setter
    def else_body(self, value: SequenceRegion | None) -> None:
        self._else_body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        covered = set(self._then_body.covered_blocks)

        if self._else_body is not None:
            covered |= self._else_body.covered_blocks

        return covered


class TryRegion(Region):

    def __init__(self):
        super().__init__()

        self._try_body = SequenceRegion()
        self._try_body.parent = self

        self._catch: CatchRegion | None = None
        self._finally: FinallyRegion | None = None

    @property
    def try_body(self) -> SequenceRegion:
        return self._try_body

    @try_body.setter
    def try_body(self, value: SequenceRegion) -> None:
        self._try_body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    @property
    def catch(self) -> "CatchRegion | None":
        return self._catch

    @catch.setter
    def catch(self, value: "CatchRegion | None") -> None:
        self._catch = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    @property
    def finally_(self) -> "FinallyRegion | None":
        return self._finally

    @finally_.setter
    def finally_(self, value: "FinallyRegion | None") -> None:
        self._finally = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        covered = set(self._try_body.covered_blocks)

        if self._catch is not None:
            covered |= self._catch.covered_blocks

        if self._finally is not None:
            covered |= self._finally.covered_blocks

        return covered


class CatchRegion(Region):

    def __init__(self):
        super().__init__()

        self.exception: str | None = None

        self._body = SequenceRegion()
        self._body.parent = self

    @property
    def body(self) -> SequenceRegion:
        return self._body

    @body.setter
    def body(self, value: SequenceRegion) -> None:
        self._body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        return set(self._body.covered_blocks)


class FinallyRegion(Region):

    def __init__(self):
        super().__init__()

        self._body = SequenceRegion()
        self._body.parent = self

    @property
    def body(self) -> SequenceRegion:
        return self._body

    @body.setter
    def body(self, value: SequenceRegion) -> None:
        self._body = value
        if value is not None:
            value.parent = self
        self.invalidate_coverage()

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        return set(self._body.covered_blocks)
