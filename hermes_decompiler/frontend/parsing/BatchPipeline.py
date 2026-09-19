from .BatchContext import BatchContext
from .BatchStage import BatchStage


class BatchPipeline:
    """
    Minimal scaffolding for the batch (cross-section) phase - same shape
    as Pipeline, one level up: where Pipeline turns per-function
    decompilation into named, independently testable steps, BatchPipeline
    does the same for building the tables every section's own
    PipelineContext optionally consults (CreatorTable,
    EnvironmentOriginTable, PrivateNameTable, ClassEnvironmentTable, and
    whatever else joins them later), instead of each one being built by
    its own bespoke method on FileOperations.

    Order matters here in a way it mostly doesn't for Pipeline's own
    stages: EnvironmentOriginTable has to run before PrivateNameTable and
    ClassEnvironmentTable, since both take it as a constructor argument
    (see their own `from_sections`). CreatorTable has no such dependency
    either way. FileOperations.build_batch_tables is the one place that
    orders the actual stage list - this class just runs whatever list
    it's given, in order, same as Pipeline.
    """

    def __init__(self, stages: list[BatchStage]):
        self._stages = stages

    def run(self, context: BatchContext) -> BatchContext:
        for stage in self._stages:
            context = stage.run(context)

        return context
