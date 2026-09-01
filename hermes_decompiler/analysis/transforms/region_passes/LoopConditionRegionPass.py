from __future__ import annotations

from collections import deque

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor, TerminatorConditionalBranch
from hermes_decompiler.analysis.models.regions import LoopKind, LoopRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import AssignmentOperator
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

            if update_block is not None:
                if self._consume_guard(latch, loop, LoopKind.FOR, update_block=update_block):
                    loop.update_block = update_block
                    loop.continue_target = update_block
                    self._extract_for_components(loop)
                    return

            if self._consume_guard(latch, loop, LoopKind.DO_WHILE, update_block=None):
                loop.continue_target = latch
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

        if update_block is not None:
            if self._consume_guard(latch, loop, LoopKind.FOR, update_block=update_block):
                loop.update_block = update_block
                loop.continue_target = update_block

                # Best-effort recovery of `initializer` / `update` so the
                # Printer can render a real `for (init; cond; update)`
                # header instead of leaving those slots blank. This is
                # purely cosmetic metadata extraction - it never changes
                # the loop's classification or its condition.
                self._extract_for_components(loop)
                return

        if self._consume_guard(latch, loop, LoopKind.DO_WHILE, update_block=None):
            loop.continue_target = latch
            return

        logger.warning(
            "Loop header block %d (0x%x): no valid loop guard found.",
            header.id, header.address,
        )

    # ------------------------------------------------------------------
    # Guard extraction
    # ------------------------------------------------------------------

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
        """
        update_block = loop.update_block

        if update_block is None:
            return

        induction_reg = self._infer_induction_register(loop.condition, update_block, loop.condition_block)

        if induction_reg is None:
            return

        for instruction in reversed(update_block.instructions):
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

            loop.update = AssignmentExpression(
                left=Identifier(name=f"r{instruction.dest_reg}"),
                operator=AssignmentOperator.ASSIGN,
                right=instruction.value,
            )

            update_block.instructions.remove(instruction)
            return

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
