from dataclasses import dataclass, field

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.frontend.parsing import BatchTables, CreatorFacts


@dataclass
class PipelineContext:
    section_index: int
    lines: list[str]
    entries: list[OpcodeEntry] = field(default_factory=list)

    analysis: HermesAnalysis = field(default_factory=HermesAnalysis)
    function_name: str = ""
    # The function id MetadataStage parses from this section's own
    # header - authoritative; section_index above is only a
    # filename-derived fallback and the two can disagree. Every
    # batch_tables lookup keys off this, not section_index.
    function_id: int | None = None
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
    # function, from `batch_tables.creator_table` - None when decompiling
    # a lone section with no batch at all, or when the batch never
    # mentions this function id. Where this and `is_generator` disagree,
    # `creator_facts.is_generator` is the one hbc97+ needs: hbc97 dropped
    # every opcode `is_generator` looks for, so it is always False there
    # regardless of the truth, and this is the only signal that survives -
    # see CreatorTable's docstring for how it's derived.
    creator_facts: "CreatorFacts | None" = None
    # Every optional batch-level (cross-section) table this function's
    # own decompilation can consult - see BatchTables. A single bundle
    # rather than one field per table (creator_table, private_name_table,
    # ...): adding a new table only ever grows BatchTables itself, never
    # this dataclass's own field list. None when decompiling a lone
    # section with no batch at all - every stage/handler that reads a
    # specific table through this falls back to that table's own
    # `.empty()` in that case, same as everywhere else these tables
    # degrade.
    batch_tables: "BatchTables | None" = None
