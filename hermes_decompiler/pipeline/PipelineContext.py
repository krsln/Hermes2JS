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

    # 'generator' | 'async' | 'normal' - the disassembler's own FuncKind for
    # *this* Function-table entry (absent/always 'normal' under LAYOUT_V96,
    # which has no Kind bits - see FunctionMetadataParser). Deliberately
    # NOT used to override `is_generator` above: FuncKind is a *source-level*
    # tag (e.g., an outer `function*` stub that only calls CreateGenerator
    # and returns still carries header_kind='generator', even though that
    # stub's own bytecode has no <StartGenerator> and must print as a plain
    # `function`, not `function*` - see SignatureStage.run()). Superseded by
    # `kind_facts` below whenever a batch index is available; kept as the
    # single-section fallback.
    header_kind: str = "normal"
