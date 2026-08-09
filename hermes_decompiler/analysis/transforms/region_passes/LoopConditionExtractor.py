from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion, LoopRegion, LoopKind, IfRegion, TryRegion, SwitchRegion,
)
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.expressions import Expression, UnaryExpression

logger = get_logger(__name__)


class LoopConditionExtractor:
    """
    Determines a loop's real continuation test (if any) and, from where
    that test physically sits in the CFG, whether the loop is top-tested
    (`while`) or bottom-tested (`do-while`):

    - If the HEADER block (the first block executed every iteration,
      including the first) ends in a valid loop-guard branch, the test
      runs before the body can execute at all -> `while (cond) { body }`.
    - Otherwise, if the loop's single LATCH block (the block that jumps
      back to the header - i.e. the last block executed each iteration)
      ends in one, the body always runs at least once before the test
      -> `do { body } while (cond)`.
    - If neither has a valid guard-shaped branch, no condition is
      extracted and the loop stays `while (true)` (with whatever
      unresolved conditional branch remains inside the body still
      visible - see `StructuralAnalyzer._audit_unstructured_blocks`).

    This distinction is not cosmetic: Hermes (like most compilers)
    performs loop rotation, so a source-level `while (cond) { body }`
    whose guard is provably true on entry commonly loses its separate
    top-of-loop check entirely and compiles down to exactly the
    bottom-tested shape above - indistinguishable, from bytecode alone,
    from a `do-while` written in the source. Rendering it as `do-while`
    is the structurally honest choice: it matches the actual
    "body runs, then test" control flow, whereas silently defaulting to
    `while (cond) {...}` here would misrepresent loops that must execute
    at least once as ones that might execute zero times.
    """

    def __init__(self, root):
        self.root = root

    def run(self):
        self._visit(self.root)

    def _visit(self, region):

        if isinstance(region, SequenceRegion):
            for child in region.children:
                self._visit(child)
            return

        if isinstance(region, LoopRegion):
            self._extract(region)
            self._visit(region.body)
            return

        if isinstance(region, IfRegion):
            # A loop very commonly ends up nested inside an IfRegion -
            # e.g. Hermes' standard "pre-header guard" idiom for a
            # rotated for/while loop (`if (i < len) { while (true) {
            # ... } }`, where the outer `if` exists purely so the loop
            # is never entered at all when the guard is false on
            # entry). Without descending here, any loop living behind
            # such a guard - or inside an ordinary nested `if` - is
            # never reached by `_extract` at all: its guard branch
            # survives untouched and later shows up as a raw,
            # unstructured `if (...) goto label_N;` in the output (see
            # `StructuralAnalyzer._audit_unstructured_blocks`), not
            # because the guard itself couldn't be recognized, but
            # because this walker never got there to look.
            self._visit(region.then_body)
            if region.else_body:
                self._visit(region.else_body)
            return

        if isinstance(region, TryRegion):
            self._visit(region.try_body)
            if region.catch:
                self._visit(region.catch.body)
            if region.finally_:
                self._visit(region.finally_.body)
            return

        if isinstance(region, SwitchRegion):
            for case in region.cases:
                self._visit(case.body)
            if region.default_body:
                self._visit(region.default_body)
            return

        if hasattr(region, "body"):
            self._visit(region.body)

    def _extract(self, loop: LoopRegion):

        header = loop.header_block
        if header is None:
            return

        # A self-loop (single block, its own back edge) makes the
        # header its own sole latch. Structurally that block always
        # runs body-then-test on every entry, including the first -
        # there is no separate top-of-loop check physically preceding
        # it, since header and latch are literally the same
        # instruction stream. That's definitionally bottom-tested
        # (do-while), even though `_consume_guard`'s generic edge-shape
        # check on the header can't tell the difference and would
        # happily also accept it as WHILE. Must check for this case
        # BEFORE attempting the top-tested path below, or a self-loop
        # gets silently misclassified as `while (cond) { body }`,
        # which is a real semantic change (predicts zero executions
        # whenever `cond` starts false, when the actual bytecode
        # always executes the body at least once).
        if header in loop.latches:
            if self._consume_guard(header, loop, LoopKind.DO_WHILE):
                return

            logger.warning(
                "Loop header block %d (0x%x): self-loop with no valid "
                "guard on its own branch - leaving as `while (true)`.",
                header.id, header.address,
            )
            return

        # 1) Top-tested: does the header itself carry a valid guard?
        if self._consume_guard(header, loop, LoopKind.WHILE):
            return

        # 2) Bottom-tested: does the loop's one latch carry a valid
        # guard? (Multiple latches - e.g. two different `continue`-like
        # back edges with different conditions - don't collapse to a
        # single trailing `while (cond)` unambiguously, so those are
        # deliberately left alone rather than guessed at.)
        if len(loop.latches) == 1:
            latch = next(iter(loop.latches))
            if latch is not header and self._consume_guard(latch, loop, LoopKind.DO_WHILE):
                return

        logger.warning(
            "Loop header block %d (0x%x): no valid guard found on the "
            "header or its single latch - leaving as `while (true)`.",
            header.id, header.address,
        )

    def _consume_guard(self, block: BasicBlock, loop: LoopRegion, kind: LoopKind) -> bool:
        """
        If `block`'s terminator is a conditional branch with exactly one
        edge leaving the loop (a real loop guard's defining shape),
        extract it as `loop.condition`, set `loop.loop_kind`, and remove
        the now-redundant terminator/instruction from `block`. Returns
        whether extraction succeeded; does nothing and returns False
        otherwise, so the caller can try the next candidate block.
        """

        branch = block.terminator
        if not isinstance(branch, TerminatorConditionalBranch):
            return False

        exits = set(loop.exits)

        target_block = next((s for s in block.successors if s.address == branch.target), None)
        fallthrough_candidates = [s for s in block.successors if s is not target_block]
        fallthrough_block = fallthrough_candidates[0] if len(fallthrough_candidates) == 1 else None

        target_is_exit = target_block is not None and target_block in exits
        fallthrough_is_exit = fallthrough_block is not None and fallthrough_block in exits

        condition: Expression
        if target_is_exit and not fallthrough_is_exit:
            # `if (condition) goto <outside the loop>` - taking the
            # branch means leaving; the loop keeps iterating exactly
            # when the condition does NOT hold.
            condition = UnaryExpression(UnaryOperator.LOGICAL_NOT, branch.condition)
        elif fallthrough_is_exit and not target_is_exit:
            # `if (condition) goto <still inside the loop>`, and falling
            # through (condition false) leaves the loop - the loop keeps
            # iterating exactly when the condition holds, as-is.
            condition = branch.condition
        else:
            # Neither edge cleanly identifies a single loop-exit - this
            # branch doesn't have the shape a loop guard must have (e.g.
            # it belongs to an unrelated `if` that happens to sit in
            # this block). Don't guess.
            return False

        block.terminator = None
        loop.condition = condition
        loop.loop_kind = kind

        # `block.terminator` is only consulted for CFG edges - Printer
        # renders per-*instruction* terminators (`instruction.terminator`
        # in `_emit_block`), a separate field on whichever OpcodeResult
        # originally produced this branch. Nulling `block.terminator`
        # alone leaves that instruction sitting in `block.instructions`,
        # so it would still print as a standalone `if (...) goto label;`
        # even though its condition was "consumed" into `loop.condition`.
        # Must also drop the instruction itself.
        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()

        return True
