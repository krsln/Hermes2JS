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

            parsed = OpcodeParser.parse(line)

            if parsed is None:
                parsed = OpcodeEntry(bytecode=line, hex_address="", opcode="", args="", comment="")

            # parsed.index = i # starts from 1
            parsed.index = len(entries)  # starts from 0
            entries.append(parsed)

        context.entries = entries

        return context
