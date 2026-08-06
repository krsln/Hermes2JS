from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.core.PipelineContext import PipelineContext
from hermes_decompiler.core.PipelineStage import PipelineStage
from hermes_decompiler.frontend.dispatch import OpcodeDispatcher

logger = get_logger(__name__)


class DispatchStage(PipelineStage):
    """Runs every bytecode line through its opcode handler."""

    def __init__(self, strict: bool = False):
        self._strict = strict

    def run(self, context: PipelineContext) -> PipelineContext:
        if not context.bytecode_lines:
            return context

        OpcodeDispatcher.dispatch_all(context.entries, context.analysis, strict=self._strict)

        processed = sum(1 for e in context.entries if e.opcode)
        if len(context.analysis.results) < processed:
            logger.warning(
                "Section section_%s: analysis.results (%s) is fewer than processed entries (%s) — some opcode likely produced zero results",
                context.section_index, len(context.analysis.results), processed,
            )

        # if len(results) != len(context.analysis.results):
        #     logger.warning(
        #         "Section section_%s: Dispatcher returned %s results but analysis.results has %s",
        #         context.section_index, len(results), len(context.analysis.results)
        #     )

        return context
