from typing import Any

from hermes_decompiler.backend.analysis.cfg import CFG
from hermes_decompiler.backend.emit import JSEmitter
from hermes_decompiler.backend.transforms import StructuralAnalyzer
from hermes_decompiler.backend.transforms.cfg_passes import GeneratorStateDispatchCfgPass, generator_dispatch
from hermes_decompiler.backend.transforms.structurers import SequenceStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.frontend.batch_pipeline.tables import CreatorFacts
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

        # Why this function's own suspend/resume dispatch might still be
        # left in its raw, unstructured `goto`/`if (...) goto` form by the
        # time `JSEmitter` runs below - tracked here (reason, confirmed)
        # so the invalid-JS check after `JSEmitter.emit` can explain
        # *why*, not just *that*. `confirmed=False` means this is only a
        # plausible explanation (batch_tables being absent also means we
        # don't even know whether this body is a generator/async at
        # all), not a definite diagnosis - the warning below has to word
        # those two cases differently rather than asserting a cause this
        # function was never actually able to verify.
        unresolved_dispatch_reason: tuple[str, bool] | None = None

        if creator_facts is None:
            unresolved_dispatch_reason = (
                "no batch_tables were provided (see FileOperations.build_batch_tables), "
                "so if this body is a generator/async function its suspend-resume dispatch "
                "could not be detected or resolved",
                False,
            )
        elif creator_facts.is_generator:
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
                    unresolved_dispatch_reason = (
                        "a generator/async dispatch chain was recognized but this "
                        "pass declined to fold it (see GeneratorStateDispatchCfgPass.run's "
                        "own all-or-nothing contract - logged above at DEBUG)",
                        True,
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
                unresolved_dispatch_reason = (
                    "this is a resolved generator/async body whose suspend-resume dispatch "
                    "shape isn't one generator_dispatch.detect recognizes yet "
                    "(e.g. `yield*`, an async generator)",
                    True,
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

        lines = JSEmitter(verbose).emit(root)

        if raw:
            # The raw renderer's whole point is the unstructured form -
            # `goto`/`if (...) goto` here is expected output, not a defect
            # to flag.
            return lines

        return self._warn_if_invalid_js(lines, unresolved_dispatch_reason)

    @staticmethod
    def _warn_if_invalid_js(
            lines: list[str],
            unresolved_dispatch_reason: tuple[str, bool] | None,
    ) -> list[str]:
        """
        `StatementPrinter.visit_TerminatorJump`/`visit_TerminatorConditionalBranch`
        are the Printer's own fallback for a terminator no structurer
        pass claimed - `goto label_N;` / `if (...) goto label_N;`. Both
        are real Python-side output but neither is valid JavaScript
        syntax at all (`goto` isn't a JS keyword), so a caller that
        writes this straight to a `.js` file or feeds it to a JS parser
        gets a hard syntax error with no hint why.

        This is checked here, on the final emitted lines, rather than by
        asking every individual structurer pass whether it fully
        succeeded: `goto`/`label_` never appear in genuine output (no
        real JS construct this printer emits contains either token), so
        a plain substring scan is exact, and it catches every route to
        this shape in one place - not just the generator/async
        no-batch-context case this method's own caller already tracks a
        reason for (`unresolved_dispatch_reason`), but any other
        genuinely irreducible control flow a structurer pass simply
        doesn't cover yet.
        """
        if not any("goto label_" in line for line in lines):
            return lines

        if unresolved_dispatch_reason is not None:
            reason, confirmed = unresolved_dispatch_reason
            cause = reason if confirmed else f"possibly because {reason}"
        else:
            cause = (
                "this function's control flow could not be fully structured "
                "by any recognized loop/if/switch/try shape"
            )

        warning = [
            "// ⚠ WARNING: this output is NOT valid JavaScript.",
            f"// Cause: {cause}.",
            "// It contains raw `goto label_N;` / `if (...) goto label_N;` statements -",
            "// `goto` is not a JavaScript keyword, so this will fail to parse as-is.",
            "// If this is a generator/async function, re-run decompilation with batch_tables",
            "// built from the full section directory (FileOperations.build_batch_tables) so",
            "// its suspend/resume dispatch can be recognized before structuring runs.",
        ]

        logger.warning(
            "Emitted output contains unstructured `goto` statements and is not valid "
            "JavaScript (cause: %s).",
            cause,
        )

        return warning + lines
