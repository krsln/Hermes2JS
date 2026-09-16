from dataclasses import dataclass, field

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.frontend.parsing import FunctionKindFacts, FunctionKindIndex


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
    # 'generator' | 'async' | 'normal' - the disassembler's own FuncKind for
    # *this* Function-table entry (absent/always 'normal' under LAYOUT_V96,
    # which has no Kind bits - see FunctionMetadataParser). Deliberately
    # NOT used to override `is_generator` above: FuncKind is a *source-level*
    # tag (e.g. an outer `function*` stub that only calls CreateGenerator
    # and returns still carries header_kind='generator', even though that
    # stub's own bytecode has no <StartGenerator> and must print as a plain
    # `function`, not `function*` - see SignatureStage.run()). Superseded by
    # `kind_facts` below whenever a batch index is available; kept as the
    # single-section fallback.
    header_kind: str = "normal"
    # Batch-resolved generator/async facts for this function, or None when
    # decompiling a lone section with no batch index to consult.
    #
    # This is the *fact* layer and is deliberately kept separate from
    # `is_generator` above, which is the *render-affecting* flag. The two
    # disagree by design on v97+, where a generator body carries no
    # suspend/resume opcodes at all: `kind_facts.is_generator_body` is
    # True (the batch proved it via the CreateGenerator edge) while
    # `is_generator` stays False, so rendering keeps emitting the literal
    # state-machine the bytecode actually contains instead of a `function*`
    # header over a body full of raw `return {value, done}` objects. Wiring
    # these together is the job of the generator state-dispatch structuring
    # work, not of the index that merely identifies the bodies.
    kind_facts: "FunctionKindFacts | None" = None
    # The batch index `kind_facts` is looked up in, carried here only so
    # SignatureStage can resolve it against MetadataStage's function id
    # rather than the filename-derived section_index. None when decompiling
    # a lone section.
    kind_index: "FunctionKindIndex | None" = None
