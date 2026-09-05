from .PipelineContext import PipelineContext
from .PipelineStage import PipelineStage


class Pipeline:
    """
    Minimal pipeline scaffolding.

    Each Stage receives and returns the same `PipelineContext`, mutating it and
    handing it to the next stage. This turns `Decompiler.build_context()` from one
    monolithic method (metadata parsing + string table + function table +
    dispatch + codegen, all inline) into named, independently testable steps -
    without pulling in a dependency for something this small.
    """

    def __init__(self, stages: list[PipelineStage]):
        self._stages = stages

    def run(self, context: PipelineContext) -> PipelineContext:
        for stage in self._stages:
            context = stage.run(context)

        return context
