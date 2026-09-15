from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions._base import Region, SequenceRegion
from hermes_decompiler.backend.regions.LoopKind import LoopKind


class LoopRegion(Region):
    """
    Structured representation of a loop.

    The region owns exactly one SequenceRegion as its body.

    `body` is a property rather than a public mutable field so that
    replacing the body automatically reparents the new region and
    invalidates cached coverage.

    Loop metadata is deliberately kept on the LoopRegion rather than
    inferred by the Printer. Structuring / region passes are responsible
    for determining:

        - Loop kind
        - Condition
        - Update
        - Continue target
        - Break target
        - For-of / for-in information
        - Labels

    The Printer only renders this already-recovered information.
    """

    def __init__(self, loop):
        super().__init__()

        self.header_block: BasicBlock = loop.header

        self.exits = list(loop.exits)
        self.latches = list(loop.latches)

        # Not yet classified.
        self.loop_kind: LoopKind = LoopKind.UNKNOWN

        self.condition = None
        self.condition_block: BasicBlock | None = None

        self.continue_target: BasicBlock | None = None
        self.break_target: BasicBlock | None = None

        self.update_block: BasicBlock | None = None

        # ---------------------------------------------------------
        # Classic `for (...)` metadata
        # ---------------------------------------------------------

        # Expression executed before the first iteration.
        #
        # Example:
        #
        #     let i = 0
        #
        self.initializer = None

        # Expression executed after every iteration.
        #
        # Example:
        #
        #     i++
        #
        self.update = None

        # Optional binding used by FOR_OF / FOR_IN.
        #
        # Example:
        #
        #     for (const x of iterable)
        #
        self.iterable = None
        self.loop_binding = None

        # ---------------------------------------------------------
        # Labels
        # ---------------------------------------------------------

        # Assigned only when an explicit label is actually required
        # by a break/continue targeting this loop.
        self.label: str | None = None

        # ---------------------------------------------------------
        # Body
        # ---------------------------------------------------------

        self._body = SequenceRegion()
        self._body.parent = self

    # -------------------------------------------------------------
    # Basic properties
    # -------------------------------------------------------------

    @property
    def header(self) -> BasicBlock:
        return self.header_block

    @property
    def body(self) -> SequenceRegion:
        return self._body

    @body.setter
    def body(self, value: SequenceRegion) -> None:
        if value is None:
            raise ValueError("LoopRegion.body cannot be None")

        if not isinstance(value, SequenceRegion):
            raise TypeError(
                f"LoopRegion.body must be SequenceRegion, "
                f"got {type(value).__name__}"
            )

        # Detach previous body if necessary.
        if self._body is not value and self._body.parent is self:
            self._body.parent = None

        self._body = value
        value.parent = self

        self.invalidate_coverage()

    # -------------------------------------------------------------
    # Coverage
    # -------------------------------------------------------------

    def _compute_covered_blocks(self) -> set[BasicBlock]:
        return set(self._body.covered_blocks)
