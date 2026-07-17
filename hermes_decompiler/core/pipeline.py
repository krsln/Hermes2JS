"""
Minimal pipeline scaffolding.

Each Stage receives and returns the same `ConversionState`, mutating it and
handing it to the next stage. This turns JSConverter.convert() from one
monolithic method (metadata parsing + string table + function table +
dispatch + codegen, all inline) into named, independently testable steps -
without pulling in a dependency for something this small.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.FunctionTableRegistry import FunctionTableRegistry


@dataclass
class ConversionState:
    section_index: int
    lines: List[str]
    function_registry: Optional[FunctionTableRegistry] = None

    analysis: HermesAnalysis = field(default_factory=HermesAnalysis)
    function_name: str = ""
    params: List[str] = field(default_factory=list)
    is_async: bool = False
    bytecode_lines: List[str] = field(default_factory=list)
    js_lines: List[str] = field(default_factory=list)


class Stage(ABC):
    """
    Base class for pipeline stages.

    Using an ABC with an explicit base class (rather than a structural
    typing.Protocol) is deliberate here: some type checkers/IDEs (PyCharm's
    inspector included) don't reliably infer structural Protocol
    conformance for a `list[Stage]` literal containing several concrete
    classes - they end up widening the inferred type to a Union of the
    concrete classes instead of `Stage`, which then doesn't match the
    `Pipeline.__init__(stages: List[Stage])` parameter. Explicit
    inheritance sidesteps that: every concrete stage IS-A Stage, nominally
    and structurally, so `list[Stage]` type-checks cleanly everywhere.
    """

    @abstractmethod
    def run(self, state: ConversionState) -> ConversionState:
        ...


class Pipeline:
    def __init__(self, stages: List[Stage]):
        self._stages = stages

    def run(self, state: ConversionState) -> ConversionState:
        for stage in self._stages:
            state = stage.run(state)
        return state
