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

        # A generator/async body is wrapped in one synthetic `try` by its state machine
        # (every handler targets the same dispatcher); see `HermesAnalysis.crosses_try_boundary`.
        facts = context.creator_facts
        context.analysis.generator_body = (
                context.is_generator
                or context.header_kind != "normal"
                or (facts is not None and (facts.is_generator or facts.is_async))
        )

        OpcodeDispatcher.dispatch_all(
            context.entries, context.analysis, strict=self._strict,
            function_id=context.function_id, batch_tables=context.batch_tables,
        )

        return context
