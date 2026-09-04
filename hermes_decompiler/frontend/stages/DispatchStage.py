from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.OpcodeDispatcher import OpcodeDispatcher
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class DispatchStage(PipelineStage):
    """Runs every bytecode line through its opcode handler."""

    def __init__(self, strict: bool = False):
        self._strict = strict

    def run(self, context: PipelineContext) -> PipelineContext:
        if not context.bytecode_lines:
            return context

        OpcodeDispatcher.dispatch_all(context.entries, context.analysis, strict=self._strict)

        return context
