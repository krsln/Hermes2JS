from dataclasses import dataclass, field

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.frontend.parsing import CreatorFacts, CreatorTable


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
    # IR to decide the actual printed header. hbc97+ emits none of these
    # opcodes at all (see CreatorTable), so this stays False there
    # regardless of the function's real generator-ness - `creator_facts`
    # below is what covers that case.
    is_generator: bool = False
    # 'generator' | 'async' | 'normal' - the disassembler's own FuncKind for
    # *this* Function-table entry (absent/always 'normal' under LAYOUT_V96,
    # which has no Kind bits - see FunctionMetadataParser). Read directly
    # only as a CreatorTable input; SignatureStage does not use it to
    # override `is_generator` on its own function, for the same
    # stub-vs-body reason `creator_facts` exists.
    header_kind: str = "normal"
    # Batch-resolved CreatorFacts(is_generator, is_async) for this
    # function, from CreatorTable - None when decompiling a lone section
    # with no batch table to consult, or when the batch never mentions
    # this function id. Where this and `is_generator` disagree,
    # `creator_facts.is_generator` is the one hbc97+ needs: hbc97 dropped
    # every opcode `is_generator` looks for, so it is always False there
    # regardless of the truth, and this is the only signal that survives -
    # see CreatorTable's docstring for how it's derived.
    creator_facts: "CreatorFacts | None" = None
    # The batch table `creator_facts` is looked up in, carried here only
    # so SignatureStage can resolve it against MetadataStage's function id
    # rather than the filename-derived section_index. None when
    # decompiling a lone section.
    creator_table: "CreatorTable | None" = None
