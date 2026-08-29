from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import Region, SequenceRegion


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

        # Raw register number the handler's own `Catch` instruction
        # bound the exception to - kept alongside `exception` (the
        # friendly display name) because later passes (see
        # `_FinallyAttacher.maybe_reinterpret_as_finally`) need to
        # recognize a rethrow of THIS SAME exception by register
        # identity, not by name: `Throw`'s own value is deliberately
        # kept as a bare `r{N}` reference (never inlined - see
        # Throw.py's own docstring), so it can never be expected to
        # already read as the friendly name.
        self.exception_reg: int | None = None

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
