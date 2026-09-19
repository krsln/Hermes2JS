from abc import ABC, abstractmethod

from .BatchContext import BatchContext


class BatchStage(ABC):
    """
    Base class for batch stages - the cross-section counterpart of
    PipelineStage (see that class's own docstring for why an explicit
    ABC rather than a structural Protocol).

    Where a PipelineStage sees one function's own bytecode, a BatchStage
    sees every section in the batch at once (BatchContext.sections) -
    it's where CreatorTable, EnvironmentOriginTable, PrivateNameTable,
    ClassEnvironmentTable and any future table of the same shape get
    built, once, before any individual section's own PipelineContext is
    constructed. See BatchPipeline's docstring for how these compose and
    why the order stages run in matters here in a way it mostly doesn't
    for PipelineStage.
    """

    @abstractmethod
    def run(self, context: BatchContext) -> BatchContext:
        ...