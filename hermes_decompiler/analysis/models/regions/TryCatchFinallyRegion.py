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
