from dataclasses import dataclass
from typing import Dict, Any, Optional, List

from hermes_decompiler.transforms.structurers import SequenceStructurer
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir import Expression


@dataclass(slots=True)
class RegisterState:
    definition: OpcodeResult
    version: int = 0
    reads: int = 0

    @property
    def value(self) -> Optional[Expression]:
        return self.definition.value

    @property
    def handler(self) -> str:
        return self.definition.handler

    def mark_read(self) -> None:
        self.reads += 1

    def mark_used(self) -> None:
        self.definition.definition_used = True


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
        self.registers: dict[str, RegisterState] = {}
        self.metadataList = []
        self.metadata = metadata if metadata is not None else {}

        self.globalObjects: Optional[int] = None
        self.gotoList: List[int] = []

        self.results: List[OpcodeResult] = []

    def add_result(self, result: OpcodeResult) -> None:
        self.results.append(result)

        if not result.name:
            return

        prev = self.registers.get(result.name)
        version = prev.version + 1 if prev else 0

        self.registers[result.name] = RegisterState(definition=result, version=version)

    def get_register_state(self, reg: int) -> Optional[RegisterState]:
        return self.registers.get(f"r{reg}")

    def generate_js(self, verbose: bool = False, raw: bool = False) -> list[str]:
        return self.generate_js_v1(verbose, raw)

    def generate_js_v1(self, verbose: bool = False, raw: bool = False) -> list[str]:
        from hermes_decompiler.analysis.cfg import CFG
        from hermes_decompiler.transforms import StructuralAnalyzer
        from hermes_decompiler.backend.emit import JSEmitter

        cfg = CFG.from_results(self.results, self.metadata.get("exception_handlers", []))

        cfg.verify()
        cfg.compute_dominators()
        cfg.compute_post_dominators()

        # ShortCircuitConditionCfgPass (stage 1 of StructuralAnalyzer.build())
        # requires cfg.loop_analysis to distinguish ordinary short-circuit
        # conditions from loop rotation artifacts.
        #
        # A rotated loop may duplicate the same guard or continue condition at
        # different points in the loop. Both tests can jump forward to the same
        # exit, which could otherwise be incorrectly folded into `a || b`.
        #
        # Therefore, loop analysis must be computed before build() runs.
        cfg.compute_loops()

        if raw:
            root = SequenceStructurer(cfg).run()
        else:
            root = StructuralAnalyzer(cfg).build()

        return JSEmitter(verbose).emit(root)
