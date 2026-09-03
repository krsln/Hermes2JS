from typing import Dict, Any, Optional, List, Tuple

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.transforms.structurers import SequenceStructurer
from .RegisterState import RegisterState


class HermesAnalysis:
    metadataList: List[Dict[str, Any]]
    metadata: Dict[str, Any]

    def __init__(self, metadata: Optional[dict[str, Any]] = None) -> None:
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

        # TODO: shorter desc
        # Populated once by `OpcodeDispatcher.dispatch_all()` before the
        # main opcode walk starts; `current_address` is advanced by the
        # dispatcher before each `handler.handle(ctx)` call. Both default
        # to "no loop info yet" / "unknown position" so any code that
        # reads them before the dispatcher runs (e.g. tests constructing
        # a bare HermesAnalysis by hand) degrades to "never unsafe",
        # matching prior behavior exactly.
        self.loop_ranges: List[Tuple[int, int]] = []
        self.current_address: Optional[int] = None

        # TODO: shorter desc
        # Populated by `OpcodeDispatcher.dispatch_all()`'s first (scratch)
        # pass: for every register, every address (inside some loop
        # range) where it gets WRITTEN - not just the single "most
        # recent definition" `defined_and_used_in_same_loop` alone can
        # see. This is what catches the self-referencing-accumulator
        # shape (a register read early in a loop body, but ALSO
        # rewritten later in that same body via a back-edge-carried
        # `Inc`/`AddN`/etc. - e.g. a rest-parameter copy loop's index
        # register) - the same shape `Binary.AddN`/`Binary.SubN`
        # originally special-cased by hand, generalized here to any
        # opcode/register.
        self.loop_carried_writes: Dict[str, List[int]] = {}

    def add_result(self, result: OpcodeResult) -> None:
        self.results.append(result)

        if not result.name:
            return

        prev = self.registers.get(result.name)
        version = prev.version + 1 if prev else 0

        self.registers[result.name] = RegisterState(definition=result, version=version)

    def get_register_state(self, reg: int) -> Optional[RegisterState]:
        return self.registers.get(f"r{reg}")

    # TODO: rename?
    def defined_and_used_in_same_loop(self, reg: int, definition_address: int) -> bool:
        """
        True if a read of `reg` at the instruction currently being
        handled (`self.current_address`) is unsafe to inline, because
        `reg` is redefined per-iteration within some loop range that
        also contains this read. Two ways that can happen:

        1. `reg`'s CURRENT definition (`definition_address`) is itself
           inside the same loop range as the read (e.g. a `Mov` aliasing
           a loop-body value, read again later in that same body).

        2. `reg` has ANY OTHER write (from `self.loop_carried_writes`,
           harvested in a first dispatch pass - see
           `OpcodeDispatcher.dispatch_all`) inside a loop range that also
           contains the read - even if that write comes LATER in address
           order than this read. This catches the self-referencing
           accumulator shape: a loop-carried register read near the top
           of the body but rewritten near the bottom (via the back-edge),
           where the "current definition" at read-time is still the
           pre-loop initial value.
        """
        if self.current_address is None:
            return False

        for start, end in self.loop_ranges:
            if not (start <= self.current_address <= end):
                continue

            if start <= definition_address <= end:
                return True

            for write_address in self.loop_carried_writes.get(f"r{reg}", ()):
                if start <= write_address <= end:
                    return True

        return False

    def generate_js(self, verbose: bool = False, raw: bool = False) -> list[str]:
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
