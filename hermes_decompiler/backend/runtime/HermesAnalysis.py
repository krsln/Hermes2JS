from typing import Any

from hermes_decompiler.backend.analysis.cfg import CFG
from hermes_decompiler.backend.emit import JSEmitter
from hermes_decompiler.backend.transforms import StructuralAnalyzer
from hermes_decompiler.backend.transforms.cfg_passes import GeneratorStateDispatchCfgPass, generator_dispatch
from hermes_decompiler.backend.transforms.structurers import SequenceStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.frontend.parsing import CreatorFacts
from .RegisterState import RegisterState

logger = get_logger(__name__)


class HermesAnalysis:
    metadata_list: list[dict[str, Any]]
    metadata: dict[str, Any]

    def __init__(self, metadata: dict[str, Any] | None = None) -> None:
        """
        Initialize the Hermes analysis context.

        This object is created fresh per `Decompiler.build_context()` call and is
        the sole owner of state for one conversion pass (registers, results,
        string/function tables). It should never be reused or shared across
        conversions. There is no cross-section state here: each section's
        function name is resolved independently from that section's own
        metadata (see `SignatureStage`), not shared or looked up across
        sections.
        """
        self.registers: dict[str, RegisterState] = {}
        self.metadata_list = []
        self.metadata = metadata if metadata is not None else {}

        self.global_objects: int | None = None
        self.goto_list: list[int] = []

        self.results: list[OpcodeResult] = []

        # Loop intervals containing instruction addresses.
        self.loop_ranges: list[tuple[int, int]] = []
        # Address of the instruction currently being handled.
        self.current_address: int | None = None
        # Addresses where each register is written inside a loop.
        self.loop_carried_writes: dict[str, list[int]] = {}

    def add_result(self, result: OpcodeResult) -> None:
        self.results.append(result)

        if not result.name:
            return

        prev = self.registers.get(result.name)
        version = prev.version + 1 if prev else 0

        self.registers[result.name] = RegisterState(definition=result, version=version)

    def get_register_state(self, reg: int) -> RegisterState | None:
        return self.registers.get(f"r{reg}")

    def is_unsafe_loop_register(self, reg: int, definition_address: int) -> bool:
        """
        True if a read of `reg` at the instruction currently being
        handled (`self.current_address`) is unsafe to inline, because
        `reg` is redefined per-iteration within some loop range that
        also contains this read. Two ways that can happen:

        1. `reg`'s CURRENT definition (`definition_address`) is itself
           inside the same loop range as the read (e.g., a `Mov` aliasing
           a loop-body value, read again later in that same body).

        2. `reg` has ANY OTHER `write` (from `self.loop_carried_writes`,
           harvested in a first dispatch pass - see
           `OpcodeDispatcher.dispatch_all`) inside a loop range that also
           contains the read - even if that `write` comes LATER in address
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

    def generate_js(
            self,
            verbose: bool = False,
            raw: bool = False,
            creator_facts: CreatorFacts | None = None,
    ) -> list[str]:
        # Clone every result before handing it to the CFG/structuring
        # passes below: those passes routinely reassign an OpcodeResult's
        # `.value`/`.statement`/`.terminator`/`.definition_used` in place
        # (see `OpcodeResult.clone`'s docstring for why that's otherwise
        # unsafe). Building the CFG from clones means those reassignments
        # land on throwaway wrappers instead of `self.results`, so this
        # method stays safe to call more than once against the same
        # `HermesAnalysis` - e.g. `Decompiler.render()` called for both
        # `raw=True` and `raw=False` output from one `build_context()`.
        results = [result.clone() for result in self.results]

        cfg = CFG.from_results(results, self.metadata.get("exception_handlers", []))

        if creator_facts is not None and creator_facts.is_generator:
            # Must run before verify()/compute_dominators()/compute_loops()
            # below: it can replace cfg.entry and cfg.blocks outright, and
            # every one of those would otherwise be computed against a CFG
            # shape this rewrite is about to discard. See
            # GeneratorStateDispatchCfgPass's module docstring for why this
            # has to happen at the CFG level at all, rather than as an
            # ordinary StructuralAnalyzer pass - the short version is that
            # unlike every other pass there, this one is gated on a fact
            # (`creator_facts`) no single CFG can determine about itself on
            # hbc97+ (see CreatorTable).
            dispatch = generator_dispatch.detect(cfg)

            if dispatch is not None:
                applied = GeneratorStateDispatchCfgPass(
                    cfg, dispatch, is_async=creator_facts.is_async,
                ).run()

                if applied:
                    logger.debug(
                        "Generator dispatch on env[%d] rewritten: %d suspend site(s).",
                        dispatch.resume_slot, len(dispatch.suspend_sites),
                    )
            else:
                # A resolved generator/async body with no recognized
                # dispatch - most likely a shape `generator_dispatch`
                # doesn't cover yet (`yield*`, an async generator, or
                # something else entirely). Left as the raw goto form;
                # worth knowing about rather than silently accepting.
                logger.debug(
                    "Function is a resolved generator/async body but no state-dispatch "
                    "machine was recognized in it; rendering the raw goto form.",
                )

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
