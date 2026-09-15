from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class BytecodeExtractionStage(PipelineStage):
    """Slices out the lines following the 'Bytecode listing' marker, if any."""

    def run(self, context: PipelineContext) -> PipelineContext:
        start = next((i for i, line in enumerate(context.lines) if "Bytecode listing" in line), -1)
        context.bytecode_lines = context.lines[start + 1:] if start >= 0 else []
        return context
