from __future__ import annotations

import dataclasses
from collections import deque

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, LoopKind, LoopRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import AssignmentOperator, Node
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.expressions import (
    Expression,
    UnaryExpression,
    BinaryExpression,
    AssignmentExpression,
    Identifier,
    NumericLiteral, NullLiteral,
    UndefinedLiteral, StringLiteral, BooleanLiteral,
)
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch
from ._base import RegionPass

logger = get_logger(__name__)

_SAFE_INIT_VALUE_TYPES = (
    NumericLiteral, StringLiteral, BooleanLiteral,
    NullLiteral, UndefinedLiteral, Identifier,  # Identifier = plain register/Mov copy
)


class LoopConditionRegionPass(RegionPass, RegionVisitor):
    """Extracts the loop condition and classifies the physical loop shape.

    Supported shapes:

        `while`:

            `header`
              |
              +-- condition false --> exit
              |
              v
             body
              |
              +--------------------> header


        `do-while`:

            `header`
              |
             body
              |
            condition
              |
              +-- true ------------> header
              |
              +-- false -----------> exit


        for:

            header
              |
             body
              |
             update
              |
            condition
              |
              +-- true ------------> header
              |
              +-- false -----------> exit

    The important distinction between `do-while` and `for` is that a
    source-level `for` has a distinct update phase immediately before
    the loop guard.

    The pass is deliberately conservative. If the CFG does not provide
    enough evidence to distinguish the shapes, it does not invent a
    `for` loop.

    Once a loop is classified as `FOR`, this pass also attempts to
    recover the `initializer` and `update` expressions (see
    `_extract_for_components`) so the Printer can render a proper
    `for (init; cond; update)` header instead of leaving those slots
    empty.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._extract(node)
        self.visit(node.body)

    # ------------------------------------------------------------------
    # Main extraction
    # ------------------------------------------------------------------

    def _extract(self, loop: LoopRegion) -> None:
        header = loop.header_block

        # Defensive reset. This matters if the pass is ever run twice
        # against the same region tree.
        loop.condition = None
        loop.condition_block = None
        loop.update_block = None
        loop.continue_target = None
        loop.break_target = None
        loop.initializer = None
        loop.update = None
        loop.loop_kind = LoopKind.WHILE

        # ------------------------------------------------------------------
        # 1. Self-loop
        # ------------------------------------------------------------------

        if header in loop.latches:
            if self._consume_guard(header, loop, LoopKind.DO_WHILE, update_block=None):
                loop.continue_target = header
                return

            logger.warning(
                "Loop header block %d (0x%x): self-loop with no valid "
                "guard; leaving loop unclassified.",
                header.id, header.address,
            )
            return

        # ------------------------------------------------------------------
        # 2. Bottom-tested loop, tried FIRST when the latch itself carries
        #    a conditional guard.
        # ------------------------------------------------------------------
        #
        # A single latch with its own TerminatorConditionalBranch is a
        # strong, unambiguous signal that the loop's real condition lives
        # there, not at the header - even when the header's own branch
        # ALSO happens to satisfy the top-tested edge-exits shape (e.g. an
        # ordinary early-`break`-style `if` sitting at the very start of
        # the loop body). Must stay in lockstep with
        # `_predicates.is_loop_guard_shaped`, which the structuring passes
        # (_DominanceIfBuilder / _CompoundConditionFolder /
        # LoopBreakStructurer) use to decide whether to leave the header's
        # branch untouched for this pass - if the two disagree about which
        # block holds the "real" guard, one pass ends up consuming what
        # the other was relying on staying intact.

        if (
                len(loop.latches) == 1
                and isinstance(next(iter(loop.latches)).terminator, TerminatorConditionalBranch)
        ):
            latch = next(iter(loop.latches))

            update_block = self._find_for_update_block(loop, latch)

            if self._classify_bottom_tested(loop, latch, update_block):
                return

            # Latch had a conditional branch but didn't parse as a valid
            # guard (both edges leave / both stay) - fall through to the
            # top-tested attempt below rather than giving up immediately;
            # a malformed bottom-tested guess shouldn't block a genuinely
            # valid top-tested reading of the header.

        # ------------------------------------------------------------------
        # 3. Top-tested loop: while (...)
        # ------------------------------------------------------------------

        if self._consume_guard(header, loop, LoopKind.WHILE, update_block=None):
            loop.continue_target = header
            return

        # ------------------------------------------------------------------
        # 4. Bottom-tested loop, generic fallback (multi-latch or a latch
        #    without its own conditional - already excluded by step 2's
        #    guard clause above, so this only runs for shapes step 2
        #    didn't even attempt).
        # ------------------------------------------------------------------

        if len(loop.latches) != 1:
            logger.warning(
                "Loop header block %d (0x%x): expected exactly one latch "
                "for bottom-tested loop classification, got %d.",
                header.id, header.address, len(loop.latches),
            )
            return

        latch = next(iter(loop.latches))

        if latch is header:
            return

        # The latch must carry the actual loop guard.
        if not isinstance(latch.terminator, TerminatorConditionalBranch):
            logger.debug(
                "Loop header block %d (0x%x): latch block %d (0x%x) "
                "does not contain a conditional guard.",
                header.id, header.address, latch.id, latch.address,
            )
            return

        # A bottom-tested loop can be either:
        #
        #     do { body } while (cond)
        #
        # or:
        #
        #     for (...; cond; update) { body }
        #
        # First determine whether this is the canonical `for` shape.
        update_block = self._find_for_update_block(loop, latch)

        if self._classify_bottom_tested(loop, latch, update_block):
            return

        logger.warning(
            "Loop header block %d (0x%x): no valid loop guard found.",
            header.id, header.address,
        )

    # ------------------------------------------------------------------
    # Bottom-tested classification (shared by both call sites above)
    # ------------------------------------------------------------------

    def _classify_bottom_tested(
            self,
            loop: LoopRegion,
            latch: BasicBlock,
            update_block: BasicBlock | None,
    ) -> bool:
        """Try `for` classification first (when `update_block` was
        found), falling back to `do-while` - either because
        `update_block` is `None` to begin with, because
        `_consume_guard` itself doesn't accept `latch` as a valid
        guard, or because the new soundness check below rejects a
        `for` reading that `_consume_guard` DID accept. Shared by both
        call sites in `_extract` (the bottom-tested-tried-first path
        and the generic bottom-tested fallback), which differ only in
        WHEN they attempt this, never in the classification logic
        itself.

        Returns True if EITHER classification succeeded (`loop.loop_kind`
        is now `FOR` or `DO_WHILE`) - the caller should return
        immediately in that case. False means `latch`'s own branch
        didn't parse as a valid guard for EITHER kind at all - genuinely
        unrelated to this method's own soundness check, so the caller
        should keep trying whatever fallback comes next.

        The soundness check runs in two parts, both guarding the exact
        same claim from two different angles - that `cond` is ALSO
        safe to check once before the very first iteration, using
        whatever value each register it reads happens to hold at that
        point:

        1. `_condition_boundary_registers_safe` - `cond`'s OTHER
           operand (the loop's boundary/limit, e.g. an `arr.length`
           re-read every iteration). Hermes' own `for`-loop lowering
           routinely reuses that same register for something else
           entirely (typically the ONE-TIME "is the array even
           non-empty" guard's own boolean result) in the code that
           runs right before falling into the loop, specifically
           BECAUSE that register's pre-loop value is never actually
           read by the real bytecode before the loop recomputes it in
           `update_block` on the first iteration - only this pass's
           OWN `for`-header rendering invents a new, non-existent read
           of it. Left unchecked, that reuse gets misread as the
           boundary's "initial" value, corrupting the very first
           condition check (confirmed bug in
           `loopBreakCrossesTryBoundaryTest`/9477: the guard's boolean
           got misread as the array length, so the printed `for`
           compared the counter against `true`/`false` instead,
           exiting after one iteration).

        2. The induction register itself, right below. Unlike the
           boundary register, this one's own pre-loop write (if any)
           is already found and inspected by `_extract_initializer` -
           but that method's own docstring is explicit that finding
           NOTHING is treated as "nothing to extract", leaving
           `loop.initializer` empty as a "strictly worse but still
           correct fallback". It isn't always correct: when the
           induction register genuinely has no reaching write outside
           the loop at all (confirmed bug in
           `loopBreakCrossesTryBoundaryTest`/15089, and independently
           in `tryFinallyLoopBreakTest`/15084 - a DIFFERENT register
           playing the induction role, so not something (1) above
           already catches there), an empty initializer slot leaves it
           JS `undefined`, so `undefined < boundary` is simply always
           `false` and the loop never runs even once - not "worse",
           wrong. The distinguishing case this still has to let through
           unmodified: the induction register IS a `LoadParam` (or
           anything else) whose value was already established well
           before `update_block`'s own single immediate predecessor -
           `_extract_initializer` deliberately never looks that far
           back (see its own docstring), so its blank result there
           does NOT mean "undefined", only "out of this method's own,
           narrower, reach". `_find_pre_loop_definition`'s wider
           backward search (used here, but not reused BY
           `_extract_initializer` itself, to keep that method's own
           narrow, already-proven-safe scope untouched) is what tells
           these two "blank" cases apart.

        `do-while` sidesteps all of this outright: its condition is
        only ever evaluated AFTER the first iteration already ran, by
        which point `update_block` has freshly (re)established every
        register it touches - which is exactly why falling back to it
        is always safe, never just "less bad".
        """
        if update_block is not None:
            if self._consume_guard(latch, loop, LoopKind.FOR, update_block=update_block):
                loop.update_block = update_block
                loop.continue_target = update_block

                induction_reg = self._infer_induction_register(
                    loop.condition, loop.update_block, loop.condition_block,
                )

                safe = (
                        induction_reg is not None
                        and self._condition_boundary_registers_safe(loop, induction_reg)
                )

                if safe:
                    # `_extract_initializer` BEFORE `_extract_update`,
                    # reversing `_extract_for_components`'s own order:
                    # `_extract_update` REMOVES the induction register's
                    # update instruction from `update_block` the moment
                    # it finds it, with nothing that would put it back
                    # were this to revert to `do-while` afterward - so
                    # the initializer check below has to happen, and
                    # potentially trigger that revert, BEFORE
                    # `_extract_update` ever touches `update_block`. The
                    # two are otherwise independent (different blocks),
                    # so swapping them is not a behavior change on its
                    # own for the case that stays `for`.
                    self._extract_initializer(loop)

                    if (
                            loop.initializer is None
                            and self._find_pre_loop_definition(loop, induction_reg) is None
                    ):
                        safe = False

                if safe:
                    self._extract_update(loop)
                    return True

                # `loop.condition`/`loop.condition_block` (already set by
                # `_consume_guard` above) stay exactly as they are - a
                # `do-while`'s condition is the same expression, just
                # checked at a different point - so nothing about them
                # needs undoing here. `loop.initializer` (if the
                # induction-register check above is what failed) is left
                # as whatever `_extract_initializer` produced - `None` in
                # the failing case, since a `do-while` has no header slot
                # for it anyway.
                loop.loop_kind = LoopKind.DO_WHILE
                loop.update_block = None
                loop.continue_target = latch
                return True

        if self._consume_guard(latch, loop, LoopKind.DO_WHILE, update_block=None):
            loop.continue_target = latch
            return True

        return False

    def _condition_boundary_registers_safe(self, loop: LoopRegion, induction_reg: int | None) -> bool:
        """True unless some register `loop.condition` reads - OTHER than
        `induction_reg`, already covered separately by
        `_extract_initializer` - is redefined inside `loop.update_block`
        with a value that DOESN'T match what that same register holds
        on the path INTO the loop from outside. See
        `_classify_bottom_tested`'s own docstring for why a mismatch
        here specifically means "unsafe to print as `for`", not just
        "unsafe to fill in a cosmetic slot".

        A register `loop.condition` reads that ISN'T touched anywhere
        in `update_block` at all needs no check: nothing about entering
        the loop changes its value between the first iteration's
        condition check and any later one, so wherever it originally
        came from is equally valid at both points.
        """
        if loop.condition is None or loop.update_block is None:
            return True

        other_registers = self._registers_read(loop.condition)

        if induction_reg is not None:
            other_registers = other_registers - {induction_reg}

        if not other_registers:
            return True

        inside_values = {
            instruction.dest_reg: instruction.value
            for instruction in loop.update_block.instructions
            if (
                    instruction.terminator is None
                    and instruction.dest_reg is not None
                    and instruction.value is not None
            )
        }

        for reg in other_registers:
            inside_value = inside_values.get(reg)

            if inside_value is None:
                continue

            outside_instruction = self._find_pre_loop_definition(loop, reg)

            if (
                    outside_instruction is None
                    or repr(outside_instruction.value) != repr(inside_value)
            ):
                return False

        return True

    @staticmethod
    def _find_pre_loop_definition(loop: LoopRegion, reg: int):
        """Backward BFS for `reg`'s reaching definition, confined
        entirely to blocks OUTSIDE the loop body.

        Deliberately NOT `_reaching_definition_block`: that method
        walks through ALL of `before_block`'s predecessors, including -
        for a block inside a loop - the back-edge from the loop's own
        latch. For a register redefined every iteration (exactly the
        shape this is checking), that back-edge path "finds" a second,
        different definition purely because the search wasn't confined
        to outside the loop in the first place, so the ambiguity check
        (`len(found_blocks) == 1`) trips and returns `None` even when
        there's a perfectly good, unambiguous OUTSIDE definition. This
        walk instead never crosses into `loop.body.covered_blocks` at
        all, so the loop's own per-iteration redefinition is never a
        candidate to begin with.

        Returns the single reaching-definition instruction (so the
        caller can inspect its VALUE, not just its location), or
        `None` when zero or more than one such instruction exists.
        """
        covered = loop.body.covered_blocks
        header = loop.header_block

        visited: set = set()
        queue = deque(
            predecessor
            for predecessor in header.predecessors
            if predecessor not in covered
        )

        found = []

        while queue:
            block = queue.popleft()

            if block in visited:
                continue
            visited.add(block)

            instruction = next(
                (
                    instr
                    for instr in reversed(block.instructions)
                    if instr.dest_reg == reg and instr.value is not None
                ),
                None,
            )

            if instruction is not None:
                found.append(instruction)
                continue

            queue.extend(
                predecessor
                for predecessor in block.predecessors
                if predecessor not in covered
            )

        if len(found) != 1:
            return None

        return found[0]

    @staticmethod
    def _consume_guard(block: BasicBlock, loop: LoopRegion, kind: LoopKind, update_block: BasicBlock | None) -> bool:
        """Consume a conditional branch with exactly one edge leaving the loop.

        The branch is removed from the BasicBlock, since its condition
        becomes loop.condition. update_block is metadata only - it is
        not used to determine the condition itself.
        """

        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return False

        exits = set(loop.exits)

        target_block = next(
            (
                successor
                for successor in block.successors
                if successor.address == branch.target
            ),
            None,
        )

        fallthrough_candidates = [
            successor
            for successor in block.successors
            if successor is not target_block
        ]

        if len(fallthrough_candidates) != 1:
            return False

        fallthrough_block = fallthrough_candidates[0]

        target_is_exit = (
                target_block is not None
                and target_block in exits
        )

        fallthrough_is_exit = fallthrough_block in exits

        if target_is_exit and not fallthrough_is_exit:
            # if (condition) goto exit
            #
            # Continue looping while !condition.
            condition: Expression = UnaryExpression(
                UnaryOperator.LOGICAL_NOT,
                branch.condition,
            )

        elif fallthrough_is_exit and not target_is_exit:
            # if (condition) goto body
            #
            # Continue looping while condition.
            condition = branch.condition

        else:
            # Both edges leave, or both edges stay inside.
            # This is not a loop guard.
            return False

        # ------------------------------------------------------------------
        # Consume the terminator.
        # ------------------------------------------------------------------

        block.terminator = None

        if (
                block.instructions
                and block.instructions[-1].terminator is branch
        ):
            block.instructions.pop()

        loop.condition = condition
        loop.condition_block = block
        loop.loop_kind = kind

        if update_block is not None:
            loop.update_block = update_block

        return True

    # ------------------------------------------------------------------
    # FOR detection
    # ------------------------------------------------------------------

    @staticmethod
    def _find_for_update_block(
            loop: LoopRegion,
            condition_block: BasicBlock,
    ) -> BasicBlock | None:
        """Locate the block holding the for loop's update instruction.

        For Hermes' canonical numeric-for lowering, the update
        operation and the loop guard can live in the same BasicBlock::

            Inc ...
            JLess ... -> header

        In that shape the condition block itself is the update block.
        For a separated update block, use the unique in-loop predecessor.
        """

        covered = loop.body.covered_blocks

        # Canonical Hermes:
        #
        #     update instruction
        #     conditional guard
        #
        # in the same block.
        if condition_block.instructions:
            non_terminator_instructions = [
                instruction
                for instruction in condition_block.instructions
                if instruction.terminator is None
            ]

            if non_terminator_instructions:
                return condition_block

        # Generic separated-update form:
        candidates = [
            predecessor
            for predecessor in condition_block.predecessors
            if predecessor in covered
               and predecessor is not condition_block
        ]

        if len(candidates) != 1:
            return None

        candidate = candidates[0]

        if candidate is loop.header_block:
            return None

        if condition_block not in candidate.successors:
            return None

        return candidate

    # ------------------------------------------------------------------
    # FOR component recovery (initializer / update)
    # ------------------------------------------------------------------

    def _extract_for_components(self, loop: LoopRegion) -> None:
        """Best-effort recovery of the `for(initializer; condition; update)` slots.

        Purely cosmetic: only affects what the Printer shows in the
        for(...) header. Never touches loop.condition or
        loop.loop_kind, which are already final by the time this runs.

        Two independent lookups happen here:

        1. update - the trailing register-defining instruction still
           sitting in loop.update_block (e.g. `Inc r5, r6` /
           `Mov r5, r6`). Removed from the block so it isn't also
           rendered as an ordinary statement inside the loop body - it
           now lives exclusively in the for header.
        2. `initializer` - the last assignment to the loop's induction
           register found in the loop header's single out-of-loop
           predecessor (e.g. `LoadConstZero r5` -> `let r5 = 0`).
           Likewise, removed from that block once captured.

        Both lookups are deliberately conservative and bail out
        (leaving loop.initializer / loop.update as None) whenever the
        shape isn't the simple, unambiguous case described above. A
        missing initializer or update is not an error - the Printer
        already renders an empty slot for either
        (`for (; cond; update)` etc.), a strictly worse but still
        correct fallback.
        """

        self._extract_update(loop)
        self._extract_initializer(loop)

    def _extract_update(self, loop: LoopRegion) -> None:
        """Pull the induction register's own update instruction into loop.update.

        Register-aware by design, mirroring `_extract_initializer`
        below (`_infer_induction_register` first, then search for
        that register's definition specifically) rather than blindly
        taking whichever dest_reg-bearing instruction sits last in the
        block.

        Filtering by `instruction.dest_reg == induction_reg` matters
        at three levels of loop nesting: `_find_for_update_block`'s
        generic fallback can then resolve to a block that also holds
        some deeper nested loop's own unrelated instruction (e.g., an
        alias Mov, or an unrelated counter Inc sitting at that address
        purely by CFG shape - see `tripleNestedLabeledTest`'s
        `Inc r4, r13` hit-counter, sharing a block with the innermost
        loop's real machinery). Taking the plain last instruction
        without this filter would grab that unrelated write instead,
        producing a for header with a self-referential-looking update
        (`r13 = r13 + 1`) that doesn't match the induction register at
        all. Filtering fails safe instead: if the real update
        instruction isn't in this block, loop.update simply stays None
        (Printer already renders an empty update slot) rather than a
        wrong one.

        One more shape the backward scan has to see through: Hermes
        sometimes persists the induction register to its backing
        environment slot (e.g. because the loop variable is captured -
        see `generatorWithLoopTest`, where suspending at a `yield`
        forces every live register out to the environment first) and
        then, in the very next instruction, reloads that exact same
        slot straight back into the exact same register - a `x = R;
        ...; R = x` round trip with no other write of `R` in between.
        That reload is real bytecode but is not itself the update - the
        genuine mutation (the `Inc`/`Add`/etc.) sits one instruction
        earlier, writing the very value the reload just reads back
        unchanged. Naively taking the LAST dest_reg match would grab
        the reload (`for (...; ...; r7 = r1[1][1])` - a plain re-read,
        not an increment) and leave the real `Inc` behind as an
        ordinary statement inside the loop body instead of the header.
        `_is_environment_roundtrip_reload` recognizes exactly this
        adjacent store-then-reload pair and skips it, so the scan
        continues backward onto the genuine update.
        """
        update_block = loop.update_block

        if update_block is None:
            return

        induction_reg = self._infer_induction_register(loop.condition, update_block, loop.condition_block)

        if induction_reg is None:
            return

        for index in range(len(update_block.instructions) - 1, -1, -1):
            instruction = update_block.instructions[index]

            if instruction.terminator is not None:
                continue

            if instruction.value is None or instruction.dest_reg is None:
                continue

            if instruction.dest_reg != induction_reg:
                # Some other register's instruction sharing this block
                # (see docstring above) - not the induction register's
                # own update. Keep scanning backward rather than
                # accepting the first/last thing found.
                continue

            if self._is_environment_roundtrip_reload(update_block, index, induction_reg):
                # A no-op reload of the value the previous instruction
                # just stored - not the update itself. Keep scanning
                # backward onto whatever wrote that value in the first
                # place (see docstring above).
                continue

            if self._is_unsafe_to_reorder(update_block, index, instruction.value):
                # Extracting this instruction into the header's update
                # slot moves it to run AFTER everything else still left
                # in `update_block` (the Printer renders `for`'s update
                # clause as executing once per iteration, following the
                # body - see class docstring's `for` shape). That's only
                # sound if nothing still left behind in this block
                # overwrites a register this instruction's own
                # right-hand side reads; otherwise the update ends up
                # reading a value some LATER statement already clobbered,
                # instead of the one actually live at this point in the
                # real bytecode. See `_is_unsafe_to_reorder`'s own
                # docstring - this produced a real, confirmed bug in
                # `loopBreakCrossesTryBoundaryTest`: the real increment
                # (`r2 = r0 + 1`) reads the OLD index out of r0, but a
                # later instruction in the very same block reloads r0
                # with `param1.length` for the next condition check -
                # extracting the increment into the header let that
                # reload run first every iteration, so the loop compared
                # the freshly-incremented counter against `length + 1`-
                # ish garbage instead of the real length, and exited (or
                # never entered) immediately. Bail out exactly the way
                # every other unrecoverable shape in this method does -
                # leave `loop.update` empty and the instruction in place
                # as an ordinary body statement, where its original
                # position keeps it correctly ordered relative to
                # whatever it shares the block with.
                return

            loop.update = AssignmentExpression(
                left=Identifier(name=f"r{instruction.dest_reg}"),
                operator=AssignmentOperator.ASSIGN,
                right=instruction.value,
            )

            update_block.instructions.remove(instruction)
            return

    @staticmethod
    def _is_unsafe_to_reorder(update_block: BasicBlock, index: int, value) -> bool:
        """True when some instruction AFTER `update_block.instructions[index]`
        (up to, but not including, the block's terminator) writes a
        register that `value` - the candidate update instruction's own
        right-hand side - reads.

        Only registers `value` actually reads are checked - a later
        write to some unrelated register is fine, since nothing about
        moving the update instruction changes when THAT write runs
        relative to anything that reads it. `dest_reg is None` (no
        assignment, can't clobber anything) and a terminator-carrier
        instruction (about to become the loop's own condition, not
        ordinary body content) are both skipped, matching how the rest
        of this method treats them.
        """
        read_registers = LoopConditionRegionPass._registers_read(value)

        if not read_registers:
            return False

        for later in update_block.instructions[index + 1:]:
            if later.terminator is not None:
                continue

            if later.dest_reg is not None and later.dest_reg in read_registers:
                return True

        return False

    @staticmethod
    def _registers_read(node) -> set[int]:
        """Collect every register number read by `node` (an `Expression`
        subtree). Generic `dataclasses.fields` walk, same technique
        `LoopInductionAliasPass._repoint_node` uses to traverse an
        arbitrary IR node without hardcoding each `Expression` subclass's
        own shape.
        """
        registers: set[int] = set()

        def visit(n) -> None:
            if isinstance(n, Identifier):
                if n.name.startswith("r") and n.name[1:].isdigit():
                    registers.add(int(n.name[1:]))
                return

            if not dataclasses.is_dataclass(n) or not isinstance(n, Node):
                return

            for field in dataclasses.fields(n):
                value = getattr(n, field.name)

                if isinstance(value, Node):
                    visit(value)
                elif isinstance(value, tuple):
                    for item in value:
                        if isinstance(item, Node):
                            visit(item)

        visit(node)
        return registers

    @staticmethod
    def _is_environment_roundtrip_reload(update_block: BasicBlock, index: int, reg: int) -> bool:
        """True when `update_block.instructions[index]` is `r{reg} = <loc>`
        and the instruction immediately before it is `<loc> = r{reg}` for
        that exact same location - i.e. a value gets stored out and then
        read straight back into the same register with nothing in
        between, a pure round trip with no observable effect. Only the
        immediately adjacent case is recognized; anything less direct
        (an intervening instruction, a different register, a different
        location) is left to the caller's existing fallback rather than
        guessed at.
        """
        if index == 0:
            return False

        reload = update_block.instructions[index]
        store = update_block.instructions[index - 1]

        if store.terminator is not None:
            return False

        if not isinstance(store.value, AssignmentExpression):
            return False

        stored_from = store.value.right

        if not isinstance(stored_from, Identifier) or stored_from.name != f"r{reg}":
            return False

        # Same location on both sides (what got stored is exactly what
        # gets read back) - compared structurally, since these `Expression`
        # nodes don't define `__eq__`.
        return repr(store.value.left) == repr(reload.value)

    def _extract_initializer(self, loop: LoopRegion) -> None:
        """Pull the induction register's initial value into loop.initializer.

        Requires:

        - Exactly one predecessor of the header lies outside the loop
          body (the natural fall-in edge). Multiple out-of-loop
          predecessors mean there's no single unambiguous place the
          initializer could live, so this bails out.
        - The induction register can be inferred from loop.condition
          (see `_infer_induction_register`).
        - That predecessor's most recent write to the induction
          register (scanning backward from the end of the block, i.e.,
          the actual value the register holds at loop entry) has a
          safely capturable type.

        The most-recent-write requirement matters: scanning further
        back past a disqualified write, looking for an earlier one
        that does qualify, is wrong regardless of how "safe" that
        earlier value looks in isolation - if the register was written
        again afterward (by anything: a call's return value, an
        unrelated reassignment) before the loop was entered, that
        earlier value is stale and was never the register's value at
        loop entry. This produced a real bug in
        `tryCatchInsideLoopTest`: the predecessor wrote the induction
        register with an unrelated string literal and then overwrote
        it with a console.log(...) call's return value right before
        falling into the loop; scanning past the unsafe most-recent
        write surfaced the stale string as the initializer, rendering
        `for (r3 = "...start"; ...)` for what is actually a numeric
        loop.

        The fix: decide at the most recent write - use it if its type
        is safe, otherwise leave loop.initializer as None (empty
        header slot, still correct) - and never look further back.
        """
        header = loop.header_block

        covered = loop.body.covered_blocks

        outside_predecessors = [
            predecessor
            for predecessor in header.predecessors
            if predecessor not in covered
        ]

        if len(outside_predecessors) != 1:
            return

        predecessor = outside_predecessors[0]

        induction_reg = self._infer_induction_register(loop.condition, loop.update_block, loop.condition_block)

        if induction_reg is None:
            return

        for instruction in reversed(predecessor.instructions):
            if instruction.terminator is not None:
                continue

            if instruction.dest_reg != induction_reg:
                continue

            # This is the register's MOST RECENT write in this
            # predecessor, i.e., its actual value at loop entry.
            # Decide here and now - do not keep scanning further back
            # past it (see docstring above).
            if (
                    instruction.value is not None
                    and isinstance(instruction.value, _SAFE_INIT_VALUE_TYPES)
            ):
                loop.initializer = AssignmentExpression(
                    left=Identifier(name=f"r{induction_reg}"),
                    operator=AssignmentOperator.ASSIGN,
                    right=instruction.value,
                )

                predecessor.instructions.remove(instruction)

            return

    def _infer_induction_register(
            self,
            condition: Expression | None,
            update_block: BasicBlock,
            condition_block: BasicBlock | None = None,
    ) -> int | None:
        """Identify the induction register via reaching definitions.

        When both the condition's left and right operands are
        registers, whichever one is redefined inside update_block
        (per address-ordered reg_definitions) is the induction
        register. Unlike the previous behavior, this does not depend
        on operand order (left vs. right).

        `condition_block`, when given, tightens this from "does
        SOME definition of this register number exist anywhere in
        update_block" (a register-NUMBER-level check) to "does the
        SPECIFIC value read at condition_block's own use site actually
        REACH here from a definition inside update_block" (a proper,
        block-position-aware reaching-definition check).

        The distinction matters whenever a candidate register number
        gets reused for multiple, unrelated logical values across the
        loop - `cfg.reg_definitions[reg]` lists every block that ever
        writes `reg` ANYWHERE in the function, with no notion of which
        one a given read actually observes. A register can then
        appear to be "defined in update_block" by pure coincidence -
        some entirely unrelated temporary reusing the same register
        number there - while the value the condition ACTUALLY reads
        comes from somewhere else entirely (often the real induction
        register's own per-iteration alias - see
        `LoopInductionAliasPass`'s own docstring on why that alias
        exists in the first place). This produced a real, confirmed
        bug in tryCatchInsideLoopTest/section_15085: `r3 < r2`'s `r3`
        happened to ALSO be redefined (for an unrelated purpose) in
        update_block, so the old register-number-only check picked it
        as "the" induction register - when the condition's `r3` is
        actually just that iteration's alias of the REAL induction
        register (`r8`), which never appears in the condition
        expression at all. `r3`'s own reaching value at loop entry
        then resolved to unrelated, unsafe content (a `console.log(...)`
        call's return value), so `_extract_initializer` correctly
        refused to guess - but only because it got the wrong register
        in the first place; `items[i]` also then had no way to ever
        read anything but the loop's very first iteration's value.
        """

        node = condition
        if isinstance(node, UnaryExpression) and node.operator == UnaryOperator.LOGICAL_NOT:
            node = node.operand

        if not isinstance(node, BinaryExpression):
            return None

        candidates = []
        for operand in (node.left, node.right):
            if (
                    isinstance(operand, Identifier)
                    and operand.name.startswith("r")
                    and operand.name[1:].isdigit()
            ):
                candidates.append(int(operand.name[1:]))

        if condition_block is not None:
            for reg in candidates:
                reaching_block = self._reaching_definition_block(reg, condition_block)
                if reaching_block is update_block:
                    return reg

            # Every candidate's OWN reaching definition was positively
            # resolved but NONE of them point to update_block - the
            # register-number-only check below would very likely
            # produce a wrong answer here too (the same coincidental-
            # reuse risk it's always exposed to), so this is exactly
            # the case worth refusing rather than falling through to
            # it. Still allow the fallback below for the case this
            # tighter check couldn't resolve at all (ambiguous/
            # multi-predecessor reaching definition - ordinary
            # separated-update forms most commonly hit this, and the
            # old heuristic remains the best available signal there).
            if any(
                    self._reaching_definition_block(reg, condition_block) is not None
                    for reg in candidates
            ):
                return candidates[0] if candidates else None

        for reg in candidates:
            definitions = self.cfg.reg_definitions.get(reg, [])
            if any(block is update_block for _, block, _ in definitions):
                return reg

        # If neither candidate is defined in update_block, fall back to
        # the old left-operand assumption - the update may live in a
        # separate block (separated-update form), which this simple
        # reaching-def check can't resolve.
        return candidates[0] if candidates else None

    def _reaching_definition_block(self, reg: int, before_block: BasicBlock) -> BasicBlock | None:
        """Find which BasicBlock holds the reaching definition of `reg`
        for a read occurring in `before_block` - mirrors
        `ForEachRegionPass._resolve_identifier`'s own backward-BFS
        technique (see that method for the fuller rationale of each
        step), but returns the DEFINING BLOCK's identity rather than
        the defined VALUE, since that's all `_infer_induction_register`
        needs to compare against `update_block`.

        Requires every explored path that finds a definition to agree
        on the SAME block - a genuine disagreement (the register is
        defined differently depending on how control reached
        `before_block`) means there's no single answer to give, so
        this returns None rather than picking one arbitrarily.
        """
        for instr in reversed(before_block.instructions):
            if instr.dest_reg == reg and instr.value is not None:
                return before_block

        visited = {before_block}
        queue = deque(before_block.predecessors)
        found_blocks = set()

        while queue:
            block = queue.popleft()

            if block in visited:
                continue
            visited.add(block)

            defines_here = any(
                instr.dest_reg == reg and instr.value is not None
                for instr in block.instructions
            )

            if defines_here:
                found_blocks.add(block)
                continue

            queue.extend(block.predecessors)

        if len(found_blocks) == 1:
            return next(iter(found_blocks))

        return None
