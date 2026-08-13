from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import Region, SequenceRegion


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
