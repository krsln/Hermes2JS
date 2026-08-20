from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor
from hermes_decompiler.analysis.models.regions import LoopKind, LoopRegion
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
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
    """
    Extracts the loop condition and classifies the physical loop shape.

    Supported shapes:

        while:

            header
              |
              +-- condition false --> exit
              |
              v
             body
              |
              +--------------------> header


        do-while:

            header
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

        if header is None:
            return

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
            if self._consume_guard(
                    header,
                    loop,
                    LoopKind.DO_WHILE,
                    update_block=None,
            ):
                loop.continue_target = header
                return

            logger.warning(
                "Loop header block %d (0x%x): self-loop with no valid "
                "guard; leaving loop unclassified.",
                header.id,
                header.address,
            )
            return

        # ------------------------------------------------------------------
        # 2. Top-tested loop: while (...)
        # ------------------------------------------------------------------

        if self._consume_guard(
                header,
                loop,
                LoopKind.WHILE,
                update_block=None,
        ):
            loop.continue_target = header
            return

        # ------------------------------------------------------------------
        # 3. Bottom-tested loop
        # ------------------------------------------------------------------

        if len(loop.latches) != 1:
            logger.warning(
                "Loop header block %d (0x%x): expected exactly one latch "
                "for bottom-tested loop classification, got %d.",
                header.id,
                header.address,
                len(loop.latches),
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
                header.id,
                header.address,
                latch.id,
                latch.address,
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
            if self._consume_guard(
                    latch,
                    loop,
                    LoopKind.FOR,
                    update_block=update_block,
            ):
                loop.update_block = update_block
                loop.continue_target = update_block

                # Best-effort recovery of `initializer` / `update` so the
                # Printer can render a real `for (init; cond; update)`
                # header instead of leaving those slots blank. This is
                # purely cosmetic metadata extraction - it never changes
                # the loop's classification or its condition.
                self._extract_for_components(loop)  # NOTE: latest change
                return

        # Otherwise it is a normal bottom-tested loop.
        if self._consume_guard(
                latch,
                loop,
                LoopKind.DO_WHILE,
                update_block=None,
        ):
            loop.continue_target = latch
            return

        logger.warning(
            "Loop header block %d (0x%x): no valid loop guard found.",
            header.id,
            header.address,
        )

    # ------------------------------------------------------------------
    # Guard extraction
    # ------------------------------------------------------------------

    def _consume_guard(
            self,
            block: BasicBlock,
            loop: LoopRegion,
            kind: LoopKind,
            update_block: BasicBlock | None,
    ) -> bool:
        """
        Consume a conditional branch that has exactly one edge leaving
        the current loop.

        The branch is removed from the BasicBlock because its condition
        becomes `loop.condition`.

        `update_block` is metadata only; it is not used to determine
        the condition itself.
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
        """
        For Hermes' canonical numeric-for lowering, the update operation
        and the loop guard can live in the same BasicBlock:

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
        """
        Best-effort recovery of the classic `for (initializer; condition;
        update)` slots for a loop already classified as `LoopKind.FOR`.

        This is purely cosmetic: it only affects what the Printer shows
        in the `for (...)` header. It never touches `loop.condition` or
        `loop.loop_kind`, which are already final by the time this runs.

        Two independent lookups happen here:

        1. `update`: the trailing register-defining instruction still
           sitting in `loop.update_block` (e.g. `Inc r5, r6` /
           `Mov r5, r6`). That instruction is removed from the block so
           it isn't ALSO rendered as an ordinary statement inside the
           loop body - it now lives exclusively in the `for` header.

        2. `initializer`: the last assignment to the loop's induction
           register found in the loop header's single out-of-loop
           predecessor (e.g. `LoadConstZero r5` -> `let r5 = 0`).
           Likewise removed from that block once captured.

        Both lookups are deliberately conservative and bail out (leaving
        `loop.initializer` / `loop.update` as `None`) whenever the shape
        isn't the simple, unambiguous case described above. A missing
        initializer or update is not an error - the Printer already
        renders an empty slot for either (`for (; cond; update)` etc.),
        which is a strictly worse but still correct fallback.
        """

        self._extract_update(loop)
        self._extract_initializer(loop)

    def _extract_update(self, loop: LoopRegion) -> None:
        """
        Pull the induction register's OWN update instruction out of
        `loop.update_block` and turn it into `loop.update`.

        Register-aware by design, mirroring `_extract_initializer`
        below (`_infer_induction_register` first, then search for
        THAT register's definition) rather than blindly taking
        whichever dest_reg-bearing instruction happens to sit last in
        the block.

        An earlier revision took the plain last-instruction-in-block
        without checking which register it wrote to. That's
        indistinguishable from the correct behavior as long as
        `update_block` contains exactly one candidate instruction -
        true for a single loop, or even two levels of nesting - but
        breaks for a THIRD level: `_find_for_update_block`'s generic
        "unique in-loop predecessor of the guard" fallback can, at
        that depth, resolve to a block that also holds some deeper
        nested loop's own unrelated top-of-body instruction (e.g. an
        alias `Mov`, or an unrelated counter `Inc` sitting at that
        address purely by CFG shape - see `tripleNestedLabeledTest`'s
        `Inc r4, r13` hit-counter, which shares a block with the
        innermost loop's real machinery). The old code would silently
        grab that unrelated instruction as if it were the induction
        register's own update whenever it happened to sit textually
        last, producing a `for` header with a self-referential-looking
        update (`r13 = r13 + 1`) that doesn't match the induction
        register at all.

        Filtering by `instruction.dest_reg == induction_reg` makes
        this fail SAFE instead: if the real update instruction isn't
        in this block, nothing here matches, and `loop.update` simply
        stays `None` (Printer already renders an empty update slot -
        see `_extract_for_components`'s own docstring) rather than a
        wrong one.
        """
        update_block = loop.update_block

        if update_block is None:
            return

        induction_reg = self._infer_induction_register(loop.condition, update_block)

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
                operator="=",
                right=instruction.value,
            )

            update_block.instructions.remove(instruction)
            return

    def _extract_initializer(self, loop: LoopRegion) -> None:
        """
        Pull the induction register's initial assignment out of the loop
        header's single out-of-loop predecessor and turn it into
        `loop.initializer`.

        Requires:

        - Exactly one predecessor of the header lies outside the loop
          body (the natural fall-in edge). Multiple out-of-loop
          predecessors mean there's no single unambiguous place the
          initializer could live, so this bails out.
        - The induction register can be inferred from `loop.condition`
          (see `_infer_induction_register`).
        - That predecessor's MOST RECENT write to the induction
          register (scanning backward from the end of the block, i.e.
          the actual value the register holds at loop entry) has a
          safely capturable type.

        That last point matters: an earlier revision kept scanning
        PAST a most-recent write that didn't qualify
        (`not isinstance(..., _SAFE_INIT_VALUE_TYPES)`), looking
        further back for an EARLIER write to the same register that
        did. That's wrong regardless of how "safe" the earlier value
        looks in isolation: if the register was written again after
        it (by anything - a call's return value, an unrelated
        reassignment, ...) before the loop was ever entered, that
        earlier value is stale and was never actually the register's
        value at loop entry. This produced a real bug in
        `tryCatchInsideLoopTest`: the predecessor block wrote the
        induction register with a string literal (unrelated log
        message) and THEN overwrote it with a `console.log(...)`
        call's return value (a `CallExpression`, not in
        `_SAFE_INIT_VALUE_TYPES`) right before falling into the loop.
        The old code skipped past that unsafe, most-recent write and
        happily reported the STALE string literal as the loop's
        initializer, rendering `for (r3 = "...start"; ...)` for what
        is actually a numeric loop.

        The fix: find the most recent write to the induction register
        and decide right there - use it if its type is safe, otherwise
        leave `loop.initializer` as `None` (empty header slot, still
        correct - see `_extract_for_components`'s docstring) - but
        never keep looking further back past it.
        """
        header = loop.header_block

        if header is None:
            return

        covered = loop.body.covered_blocks

        outside_predecessors = [
            predecessor
            for predecessor in header.predecessors
            if predecessor not in covered
        ]

        if len(outside_predecessors) != 1:
            return

        predecessor = outside_predecessors[0]

        induction_reg = self._infer_induction_register(loop.condition, loop.update_block)

        if induction_reg is None:
            return

        for instruction in reversed(predecessor.instructions):
            if instruction.terminator is not None:
                continue

            if instruction.dest_reg != induction_reg:
                continue

            # This is the register's MOST RECENT write in this
            # predecessor, i.e. its actual value at loop entry.
            # Decide here and now - do not keep scanning further back
            # past it (see docstring above).
            if instruction.value is not None and isinstance(instruction.value, _SAFE_INIT_VALUE_TYPES):
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
    ) -> int | None:
        """
        Reaching-definition tabanlı tespit: koşulun sol VE sağ operandı
        register ise, hangisi update_block içinde yeniden tanımlanıyorsa
        (adres-sıralı reg_definitions üzerinden) o, induction register'dır.
        Operand sırasına (sol/sağ) bağımlı değildir - eski davranışın
        aksine.
        """

        node = condition
        if isinstance(node, UnaryExpression) and node.operator == UnaryOperator.LOGICAL_NOT:
            node = node.operand

        if not isinstance(node, BinaryExpression):
            return None

        candidates = []
        for operand in (node.left, node.right):
            if isinstance(operand, Identifier) and operand.name.startswith("r") and operand.name[1:].isdigit():
                candidates.append(int(operand.name[1:]))

        for reg in candidates:
            defs = self.cfg.reg_definitions.get(reg, [])
            if any(block is update_block for _, block, _ in defs):
                return reg

        # Hiçbiri update_block'ta tanımlanmıyorsa eski davranışa (sol
        # operand varsayımı) düş - update ayrı bir blokta olabilir
        # (separated-update formu), bu durumda reaching-def bu basit
        # kontrolle bulunamaz.
        return candidates[0] if candidates else None
