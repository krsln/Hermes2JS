from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions.BaseRegion import Region, SequenceRegion
from hermes_decompiler.ir import Expression


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
