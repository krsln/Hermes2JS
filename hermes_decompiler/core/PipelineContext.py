from dataclasses import dataclass, field
from typing import List

from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.runtime import HermesAnalysis


@dataclass
class PipelineContext:
    section_index: int
    lines: List[str]
    entries: List[OpcodeEntry] = field(default_factory=list)

    analysis: HermesAnalysis = field(default_factory=HermesAnalysis)
    function_name: str = ""
    params: List[str] = field(default_factory=list)
    is_async: bool = False
    bytecode_lines: List[str] = field(default_factory=list)
    js_lines: List[str] = field(default_factory=list)
