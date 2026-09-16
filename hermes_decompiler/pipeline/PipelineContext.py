from dataclasses import dataclass, field

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.frontend.opcode import OpcodeEntry


@dataclass
class PipelineContext:
    section_index: int
    lines: list[str]
    entries: list[OpcodeEntry] = field(default_factory=list)

    analysis: HermesAnalysis = field(default_factory=HermesAnalysis)
    function_name: str = ""
    params: list[str] = field(default_factory=list)
    bytecode_lines: list[str] = field(default_factory=list)
    js_lines: list[str] = field(default_factory=list)
    # True iff the bytecode contains <StartGenerator> - i.e., the function
    # is *some* flavor of generator. Hermes lowers both plain `function*`
    # generators and async functions/generators through the exact same
    # suspend/resume opcodes (see SignatureStage.run()'s note below), so
    # this flag alone cannot tell those two cases apart - CodeGenerationStage
    # combines it with a separate async signal derived from the dispatched
    # IR to decide the actual printed header.
    is_generator: bool = False
