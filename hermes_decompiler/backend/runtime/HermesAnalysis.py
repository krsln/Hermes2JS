import re
from typing import Any

from hermes_decompiler.backend.analysis.cfg import CFG
from hermes_decompiler.backend.emit import JSEmitter
from hermes_decompiler.backend.transforms import StructuralAnalyzer
from hermes_decompiler.backend.transforms.shared import may_alias, read_members, stored_member
from hermes_decompiler.backend.transforms.cfg_passes import (
    ArrayDestructuringCfgPass, EnvArrayDestructuringCfgPass, GeneratorStateDispatchCfgPass,
    SharedReturnDuplicationCfgPass, generator_dispatch,
)
from hermes_decompiler.backend.transforms.structurers import SequenceStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.frontend.batch_pipeline.tables import CreatorFacts
from hermes_decompiler.ir.expressions import (
    AwaitExpression, CallExpression, Identifier, MemberExpression, NewExpression, YieldExpression,
)
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
        # Instruction currently being handled (see `current_instruction_overwrites`).
        self.current_entry = None
        # Addresses where each register is written inside a loop.
        self.loop_carried_writes: dict[str, list[int]] = {}
        # Forward-jump spans `(jump address, target address)`: an instruction
        # strictly inside one is skipped on the path that takes the jump, so
        # a write there is conditional (see `_is_phi_write`).
        self.skip_ranges: list[tuple[int, int]] = []
        # Every definition of each register, in order. `RegisterState.version`
        # is the index into this list, so `history[name][v + 1:]` is exactly
        # what redefined version `v` (see `stale_kind`).
        self.history: dict[str, list[RegisterState]] = {}
        # Memory stores (`Put*`, `Store*`, `Del*` of a property, not a literal
        # being built), as the assigned member (None when unknown), in order. A
        # value that READS memory is stale once a store that may alias it
        # follows its load (see `stale_kind`).
        self.store_log: list[MemberExpression | None] = []

    _MEMORY_STORE_RE = re.compile(r"(Put|Store|Del)")

    def add_result(self, result: OpcodeResult) -> None:
        self.results.append(result)

        if self._MEMORY_STORE_RE.match(result.entry.opcode):
            self._log_store(result)

        if not result.name:
            return

        prev = self.registers.get(result.name)
        version = prev.version + 1 if prev else 0

        # Snapshot BEFORE the register table is updated: a self-referencing
        # value (`r3 = r3.a`) must record the OLD version of r3 so that it
        # reads as stale as soon as this very definition replaces it.
        operand_versions = self._capture_operand_versions(result)

        reads_memory = (
                result.value is not None
                and not result.entry.opcode.startswith("Put")
                and any(isinstance(node, MemberExpression) for node in result.value.walk())
        )

        state = RegisterState(
            definition=result, version=version, operand_versions=operand_versions,
            memory_epoch=len(self.store_log) if reads_memory else None,
            memory_reads=read_members(result.value) if reads_memory else (),
        )
        self.registers[result.name] = state
        self.history.setdefault(result.name, []).append(state)

    def _log_store(self, result: OpcodeResult) -> None:
        member = stored_member(result.value)
        if member is not False:
            self.store_log.append(member)

    _REGISTER_NAME_RE = re.compile(r"r\d+")

    def _capture_operand_versions(self, result: OpcodeResult) -> tuple[tuple[str, int], ...]:
        value = result.value
        if value is None:
            return ()

        captured: dict[str, int] = {}
        for node in value.walk():
            if isinstance(node, Identifier) and self._REGISTER_NAME_RE.fullmatch(node.name):
                state = self.registers.get(node.name)
                if state is not None:
                    captured[node.name] = state.version

        return tuple(captured.items())

    # Opcodes whose first register operand is a READ (or that have no
    # destination), so they never overwrite it.
    _NON_WRITING_OPCODE_RE = re.compile(
        r"(J|Put|Store|Switch|Throw$|Ret$|SaveGenerator|ResumeGenerator|CompleteGenerator"
        r"|StartGenerator|SelectObject|Debugger)"
    )
    _FIRST_REGISTER_RE = re.compile(r"\s*Reg(?:8|32):\s*(\d+)")

    def current_instruction_overwrites(self, register_name: str) -> bool:
        """True if the instruction being handled writes `register_name`
        (first register operand of a value-producing opcode)."""
        entry = self.current_entry
        if entry is None or self._NON_WRITING_OPCODE_RE.match(entry.opcode):
            return False

        match = self._FIRST_REGISTER_RE.match(entry.args)
        return match is not None and f"r{match.group(1)}" == register_name

    def stale_kind(self, state: RegisterState) -> str | None:
        """How `state.value` has gone stale, if at all.

        - "self": its only stale operand is its own destination
          (`r3 = r3.a`). The `rN` inside then means the value BEFORE this
          definition, which stays true only while the definition's
          statement is folded away and the consumer overwrites `rN` itself
          (`r1 = r1.f; r1 = r1(x)` -> `r1 = r1.f(x)`).
        - "other": the value is a bare register alias (`Mov r5, r4` ->
          `r4`) and r4 was redefined since. Inlining would read the NEW r4.
        - None: still valid.

        A computed expression that mentions some OTHER redefined register
        is deliberately NOT reported: the redefinition is usually a
        constant/argument load that is itself folded away (so the register
        never changes in the output), and blocking those inlines turned
        `r1.ifTest.call(r2, 7)` into `r5 = r1.ifTest; r1 = r5(7)` without
        catching a confirmed bug. See the residual list in the notes.
        """
        # Put*: pseudo-definition - `obj[k] = v` re-published as a definition
        # of `obj` so the printer can chain `(o[0] = a)[1] = b`. Its value
        # mentions `obj` by design; it does not compute a new `obj`.
        if state.handler.startswith("Put"):
            return None

        if state.memory_epoch is not None and self._stored_since(state):
            # `r0 = r3[25]; r3[25] = null; throw r0`: the load ran before the
            # store, so its value is not what `r3[25]` reads now.
            return "memory"

        kind = None
        own = state.definition.name

        for name, version in state.operand_versions:
            current = self.registers.get(name)
            if current is not None and current.version == version:
                continue

            if name == own and current is state:
                kind = "self"
            elif (
                    current is not None
                    and name != own
                    and not isinstance(state.value, Identifier)
                    and self._redefined_by_kept_write(name, version)
            ):
                # A computed expression over a register that was since
                # reassigned by a statement that STAYS in the output (a call
                # result: `r6 = r7.index` ... `r7 = r9.getItemCount(...)`),
                # or by a write on only one path into the join being read
                # (`r6 = r3[0]` ... `r3 = r2 && r2[k]`). Inlined, it would
                # read the new value.
                return "other"
            elif isinstance(state.value, Identifier) and self._REGISTER_NAME_RE.fullmatch(state.value.name):
                # A bare register alias (`Mov r5, r4` -> value `r4`): the
                # alias only means anything while r4 still holds what it
                # held at the Mov. Any later write to r4 makes inlining the
                # alias wrong (it would read the NEW r4), and unlike a
                # computed expression there is no folded-away consumer
                # that could still make it right.
                return "other"

        return kind

    def _stored_since(self, state: RegisterState) -> bool:
        """A store since `state`'s load may have written a location it read."""
        for store in self.store_log[state.memory_epoch:]:
            if any(may_alias(read, store) for read in state.memory_reads):
                return True
        return False

    def _redefined_by_kept_write(self, name: str, version: int) -> bool:
        """Some definition of `name` after `version` is certain to leave the
        register changed in the printed output - not just the latest one: an
        earlier call result stays printed even if a folded load overwrote it
        afterwards."""
        for later in self.history.get(name, ())[version + 1:]:
            if self._redefinition_prints(later) or self._is_phi_write(later):
                return True

        return False

    def _is_phi_write(self, state: RegisterState) -> bool:
        """The definition ran on only one path into the join the current
        instruction reads after: it sits inside a forward jump's skipped span
        whose target is already behind us. The register then holds different
        values per path, so no single folded expression can stand for it -
        it is printed (as an `if` arm write or a folded `&&`/`||`/`?:`
        assignment), and a value computed from the older one is stale."""
        current = self.current_address
        if current is None:
            return False

        address = state.definition.address
        return any(start < address < end <= current for start, end in self.skip_ranges)

    def is_join_value(self, state: RegisterState) -> bool:
        """The register's current definition is a one-path write into the join
        being read AND an earlier definition reaches the same join on the
        skipping path (`r0 = a; if (!r0) { r0 = b }; <read r0>`): the read sees
        a merge of the two, so the arm's value alone is not what it holds."""
        return state.version > 0 and self._is_phi_write(state)

    @staticmethod
    def _redefinition_prints(state: RegisterState) -> bool:
        """The definition is kept as a statement of its own: a call/construct
        result is never folded into a reader, and a pinned one prints too."""
        return state.definition.definition_pinned or isinstance(
            state.value, (CallExpression, NewExpression, AwaitExpression, YieldExpression),
        )

    def may_inline(self, state: RegisterState) -> bool:
        """Whether `state.value` can be substituted at the read being handled."""
        kind = self.stale_kind(state)

        if kind is None:
            return True

        return (
                kind == "self"
                and not state.definition.definition_pinned
                and self.current_instruction_overwrites(state.definition.name)
        )

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
        lines, reason = self._generate_js(verbose, raw, creator_facts, duplicate_returns=False)

        if not raw and self._has_goto(lines):
            # A `return` block shared between early exits in different `if`
            # arms can leave a test without its exit (a raw `goto`). Only
            # then are the shared returns copied per jumper - doing it
            # always would restyle every function that merely has one.
            retry, retry_reason = self._generate_js(verbose, raw, creator_facts, duplicate_returns=True)
            if not self._has_goto(retry):
                lines, reason = retry, retry_reason

        if raw:
            return lines

        return self._warn_if_invalid_js(lines, reason)

    @staticmethod
    def _has_goto(lines: list[str]) -> bool:
        return any("goto label_" in line for line in lines)

    def _generate_js(
            self,
            verbose: bool,
            raw: bool,
            creator_facts: CreatorFacts | None,
            duplicate_returns: bool,
    ) -> tuple[list[str], tuple[str, bool] | None]:
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

        # `[a, b] = src` as one statement instead of the iterator-protocol
        # diamonds. Needs to see the final block order, after the generator
        # rewrite above, and before any analysis is computed.
        ArrayDestructuringCfgPass(cfg).run()
        EnvArrayDestructuringCfgPass(cfg).run()
        if duplicate_returns:
            SharedReturnDuplicationCfgPass(cfg).run()

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
            return lines, unresolved_dispatch_reason

        return lines, unresolved_dispatch_reason

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
