from typing import Dict, Any, Optional, List

from hermes_decompiler.core import get_logger
from hermes_decompiler.opcode import OpcodeResult

logger = get_logger(__name__)


class HermesAnalysis:
    metadataList: List[Dict[str, Any]]
    metadata: Dict[str, Any]

    def __init__(
            self,
            metadata: Optional[dict[str, Any]] = None,
    ) -> None:
        """
        Initialize the Hermes analysis context.

        This object is created fresh per `JSConverter.convert()` call and is
        the sole owner of state for one conversion pass (registers, results,
        string/function tables). It should never be reused or shared across
        conversions - see core/registry.py for how cross-section data
        (function names) is shared explicitly instead.
        """
        self.registers: dict[str, OpcodeResult] = {}
        self.metadataList = []
        self.metadata = metadata if metadata is not None else {}

        self.globalObjects: Optional[int] = None
        self.gotoList: List[int] = []

        self.results: List[OpcodeResult] = []

    def add_result(self, result: OpcodeResult) -> None:
        """
        Register a single `OpcodeResult` produced by a handler.

        Handlers now construct exactly one `OpcodeResult` per opcode and
        pass that same instance both here and as their `handle()` return
        value. Previously `add_result(entry, variable, goto, extra_gotos)`
        built its own internal `OpcodeResult` while the handler
        separately constructed and returned a second, different
        `OpcodeResult` for the same opcode - the two were only kept in
        sync by convention.
        """

        self.results.append(result)

        if result.name:
            self.registers[result.name] = result

    def generate_js(self, verbose: bool = False) -> list[str]:
        return self.generate_js_v1(verbose)

    def generate_js_v1(self, verbose: bool = False) -> List[str]:
        from hermes_decompiler.analysis.cfg import CFG
        from hermes_decompiler.analysis.transforms import StructuralAnalyzer
        from hermes_decompiler.emit import JSEmitter

        cfg = CFG.from_results(self.results, self.metadata.get("exception_handlers", []))

        cfg.verify()
        cfg.compute_dominators()
        cfg.compute_post_dominators()
        cfg.compute_loops()

        root = StructuralAnalyzer(cfg).build()
        renderer = JSEmitter(verbose)

        return renderer.render(root)
