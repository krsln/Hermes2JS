from typing import Dict, Any, Optional, List

from hermes_decompiler.cfg import BasicBlockBuilder, ControlFlowGraphBuilder, CFGValidator
from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.emitter.JavaScriptEmitter import JavaScriptEmitter
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.Logger import get_logger
from hermes_decompiler.regions.building.RegionBuilder import RegionBuilder

logger = get_logger(__name__)


class Output:
    indent: int = 0
    content: str = ""

    used: Optional[bool] = None
    var: Optional[JSVariable] = None

    def __init__(self, lvl: int, content: str, used: Optional[bool] = False, var: Optional[JSVariable] = None) -> None:
        self.indent = lvl
        self.content = content
        self.used = used
        self.var = var


class HermesAnalysis:
    metadataList: List[Dict[str, Any]]
    metadata: Dict[str, Any]

    def __init__(
            self,
            metadata: Optional[dict[str, Any]] = None,
            stringTable: Optional[dict[str, str]] = None,
    ) -> None:
        """
        Initialize the Hermes analysis context.

        This object is created fresh per `JSConverter.convert()` call and is
        the sole owner of state for one conversion pass (registers, results,
        string/function tables). It should never be reused or shared across
        conversions - see core/registry.py for how cross-section data
        (function names) is shared explicitly instead.
        """
        self.registers: dict[str, JSVariable] = {}
        self.metadataList = []
        self.metadata = metadata if metadata is not None else {}

        self.globalObjects: Optional[int] = None
        self.gotoList: List[int] = []

        self.results: List[OpcodeResult] = []

    def add_result(
            self,
            entry: OpcodeEntry,
            variable: JSVariable,
            goto: Optional[int] = None,
            extra_gotos: Optional[List[int]] = None,
    ):
        """
        Add a variable, tracking multiple assignments.

        `extra_gotos` is for instructions with more than one possible
        jump target that isn't a plain fallthrough - today that's only
        SwitchImm (one target per case label). See OpcodeResult for
        why this is a separate parameter instead of making `goto` a
        list.
        """
        result = OpcodeResult(entry, variable, goto, extra_gotos)
        self.results.append(result)

        if variable.name:
            self.registers[variable.name] = variable

    def generate_js(self, verbose: bool = False) -> list[str]:
        #
        # CFG
        #

        blocks = BasicBlockBuilder.build(self.results)

        cfg = ControlFlowGraphBuilder.build(blocks, metadata=self.metadata)

        #
        # Analyses
        #

        analysis = CFGAnalysis(
            cfg=cfg,
            metadata=self.metadata,
        )

        #
        # Regions
        #

        region = RegionBuilder.build(analysis)

        #
        # Emit
        #

        emitter = JavaScriptEmitter(verbose)

        return emitter.emit(region)

    def __str__(self):
        return f"HermesAnalysis(globalObjects={self.globalObjects}, gotoList={self.gotoList}, results={[var.to_dict() for var in self.results]})"

    def to_dict(self):
        """Convert the HermesAnalysis object to a dictionary."""
        return {
            "metadata": self.metadata,
            "globalObjects": self.globalObjects,
            "gotoList": self.gotoList,
            "results": [var.to_dict() for var in self.results],
        }
