from hermes_decompiler.core.Exceptions import MetadataParseError
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.parsing import FunctionMetadataParser
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class MetadataStage(PipelineStage):
    """Parses the .hbc header line (line 0) into analysis.metadata."""

    def run(self, context: PipelineContext) -> PipelineContext:
        if not context.lines:
            raise MetadataParseError("No lines to parse metadata from")

        try:
            metadata = FunctionMetadataParser.parse(context.lines[0])

            metadata["exception_handlers"] = []

            if len(context.lines) > 1 and context.lines[1].strip().startswith("[Exception handlers:"):
                metadata["exception_handlers"] = FunctionMetadataParser.parse_exception_handlers(context.lines[1])

            context.analysis.metadata = metadata
            context.analysis.metadataList.append(metadata)
        except Exception as e:
            raise MetadataParseError(f"Failed to parse metadata: {e}") from e

        return context
