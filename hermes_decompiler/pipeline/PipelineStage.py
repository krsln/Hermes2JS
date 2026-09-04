from abc import ABC, abstractmethod

from .PipelineContext import PipelineContext


class PipelineStage(ABC):
    """
    Base class for pipeline stages.

    Using an ABC with an explicit base class (rather than a structural
    typing.Protocol) is deliberate here: some type checkers/IDEs (PyCharm's
    inspector included) don't reliably infer structural Protocol
    conformance for a `list[Stage]` literal containing several concrete
    classes - they end up widening the inferred type to a Union of the
    concrete classes instead of `Stage`, which then doesn't match the
    `Pipeline.__init__(stages: List[Stage])` parameter. Explicit
    inheritance sidesteps that: every concrete stage IS-A Stage, nominally
    and structurally, so `list[Stage]` type-checks cleanly everywhere.
    """

    @abstractmethod
    def run(self, context: PipelineContext) -> PipelineContext:
        ...
