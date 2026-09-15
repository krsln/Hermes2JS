from hermes_decompiler.core.Exceptions import OpcodeConstructionError
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.frontend.parsing import OpcodeParser
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class ParsingStage(PipelineStage):
    def run(self, context: PipelineContext) -> PipelineContext:
        entries = []

        for i, raw_line in enumerate(context.bytecode_lines):
            line = raw_line.strip()

            if not line:
                continue

            try:
                parsed = OpcodeParser.parse(line)
            except OpcodeConstructionError as e:
                # Grammar matched but construction failed: a parser bug, not
                # a plain non-opcode line. Log it distinctly and fall back to
                # the same placeholder used for non-matching lines, matching
                # prior runtime behavior.
                logger.warning(str(e))
                parsed = None

            if parsed is None:
                parsed = OpcodeEntry(bytecode=line, hex_address="", opcode="", args="", comment="")

            # parsed.index = i # starts from 1
            parsed.index = len(entries)  # starts from 0
            entries.append(parsed)

        context.entries = entries

        return context
