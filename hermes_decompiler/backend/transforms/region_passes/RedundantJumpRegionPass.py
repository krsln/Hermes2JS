from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, LoopRegion, SequenceRegion, TryRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.terminators import TerminatorJump
from ._base import RegionPass

logger = get_logger(__name__)


class RedundantJumpRegionPass(RegionPass, RegionVisitor):
    """Drops a bare unconditional-Jmp block whose target is simply the
    next sibling block that already executes right after it, AND a
    loop's own trailing back-edge jump to its header.

    Upstream structurers (LoopBreakStructurer,
    LoopLabeledExitStructurer, ...) sometimes leave one of these
    behind as a byproduct of matching a loop's natural-completion
    address through it. - See
    `LoopLabeledExitStructurer._chase_trampoline_address`, which walks
    straight through a block exactly like this one to find the real
    merge address an escaping edge needs to compare against, but never
    revisits the trampoline block itself once that comparison
    succeeds. The escape edge it was chased through gets consumed and
    converted; the trampoline, still sitting harmlessly in sequence
    with nothing left pointing at it except plain fallthrough, is
    not. Left-alone it prints as a pointless `goto label_N`
    immediately followed by the very code label_N points to.

    Deliberately narrow: only handles the case where the jump's target
    address is the address of the VERY NEXT sibling BasicBlock in the
    same SequenceRegion - i.e., removing the jump changes nothing
    about control flow, since falling off the end of the previous
    statement already reaches the same place. Any other shape (target
    is a LoopRegion's/IfRegion's/SwitchRegion's first block rather
    than a bare sibling BasicBlock, target is further away, etc.) is
    left as an explicit goto rather than guessed at - resolving \"the
    first address a compound sibling region would execute\" would
    require walking region-kind-specific internals (LoopRegion.body,
    IfRegion.then_body, SwitchRegion.cases, ...) this pass has no need
    to become coupled to for the one narrow shape actually observed in
    practice.

    That "removing the jump changes nothing" reasoning holds
    regardless of what else is in `block` - a block that runs real
    statements and only then falls into a redundant jump to its own
    next sibling (e.g. a labeled `continue`'s target loop iteration
    falling through past dead code into the loop's own back edge; see
    LabeledTests/labeledContinueTest) is exactly as redundant as the
    pure single-instruction trampoline case above, just with real
    code ahead of the jump instead of nothing. Only the jump
    *instruction itself* is dropped in that case (same
    terminator-only-vs-whole-instruction treatment as
    `_strip_back_edge_jumps` below); the block is only removed
    entirely when nothing besides that jump instruction is left in it
    - the original pure-trampoline shape.

    A second, related shape this pass also drops: a LOOP's own trailing
    back-edge jump (from one of `loop.latches`) straight to
    `loop.header_block`. Unlike the sibling-trampoline case above, this
    one has NOTHING analogous for `while (...)`/`for (...)` to fall
    through into - the `for`/`while` construct itself already implies
    "go back to the top", so printing the underlying `goto label_N;`
    is pure noise for a shape every structured loop already expresses
    without it (see forOfTest/section_15092, whose loop body used to
    end with a redundant `goto label_35;` pointing right back at its
    own header). Only removed when the latch's OWN terminator is still
    a bare `Jmp` (top-tested `while`/`for-of`/`for-in` loops, where the
    condition lives at the header and the latch carries nothing but
    the back-edge) - a bottom-tested loop's latch instead carries the
    loop's real guard, already consumed into `loop.condition` by
    `LoopConditionRegionPass` (leaving `latch.terminator` as `None` by
    the time this pass runs), so this never fires for that shape.

    A third shape, the TryRegion analogue of the sibling-trampoline
    case: `try_body`'s (or `catch.body`'s) own trailing jump past
    whatever else the TryRegion prints (the catch handler, the finally
    block) straight to the address that already follows the whole
    `try {} catch {} finally {}` statement in its parent SequenceRegion
    - Hermes bytecode needs this Jmp to physically skip over the catch
    handler's own bytecode range on the normal-completion path, but the
    printed JS's own try/catch/finally semantics already imply exactly
    that "fall through to what comes after" once try (or catch)
    completes normally, so it's exactly as redundant as the sibling
    case above; see ExceptionTests/tryCatchInsideLoopTest, whose try
    block used to end with a redundant `goto label_158;` right past its
    own catch handler.

    Matched the same way as the loop back-edge case - by comparing the
    jump's target against a BasicBlock's `.address`, not the address of
    whatever instruction happens to still be first in it. The two can
    differ: `_FinallyAttacher` (see try_structurer/) already recognizes
    a finally block Hermes duplicated inline for the normal-completion
    path as equivalent to the one canonical `finally_.body` printed
    once, and drops the now-redundant duplicate's instructions from
    the block that follows the TryRegion - but that block's `.address`
    stays what it was before the duplicate was stripped from it (the
    original bytecode offset the duplicate itself started at, which is
    exactly what the try_body's own Jmp still targets). Comparing
    against `.address` rather than the surviving first instruction's
    own address is what makes the match succeed regardless.

    Pipeline placement
    -------------------
    Safe to run any time after all structurers have finished producing
    the final SequenceRegion shape - it only ever removes a block or a
    terminator, never rewrites a ``condition`` or ``register``, so it
    has no data dependency on LoopConditionRegionPass /
    LoopInductionAliasPass / ForEachRegionPass, though it DOES rely on
    LoopConditionRegionPass having already run (see the previous
    paragraph on why a bottom-tested loop's latch is naturally exempt
    only once its own terminator has already been consumed) and, for
    the third shape above, on TryStructurer's `_FinallyAttacher` having
    already stripped any duplicated-inline-finally instructions from
    the block a try_body/catch_body Jmp targets (see that shape's own
    paragraph on why `.address` rather than the first surviving
    instruction's address is what this pass compares against - that
    only holds once the duplicate has actually been stripped).
    TryStructurer already runs well before this pass in
    StructuralAnalyzer.build(), so this is naturally satisfied. Grouped
    alongside LoopContinueRegionPass in StructuralAnalyzer.build()
    since both clean up residual TerminatorJump-only blocks, though
    neither depends on the other's output - ordering between the two
    doesn't matter.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)
        self._strip_redundant_jumps(node)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self.visit(node.body)
        self._strip_back_edge_jumps(node)

    def visit_TryRegion(self, node: TryRegion) -> None:
        self.visit(node.try_body)

        if node.catch is not None:
            self.visit(node.catch.body)

        if node.finally_ is not None:
            self.visit(node.finally_.body)

        self._strip_try_exit_jumps(node)

    def _strip_redundant_jumps(self, region: SequenceRegion) -> None:
        children = region.children

        index = 0
        while index < len(children) - 1:
            block = children[index]
            next_sibling = children[index + 1]

            if (
                    isinstance(block, BasicBlock) and isinstance(next_sibling, BasicBlock)
                    and self._is_redundant_jump(block, next_sibling)
            ):
                self._clear_trailing_jump(block, block.terminator)

                if block.instructions:
                    # Real statements remain ahead of the jump - keep
                    # the block, just without its now-redundant
                    # terminator; falling off its end already reaches
                    # next_sibling.
                    logger.debug(
                        "RedundantJumpRegionPass: dropped trailing "
                        "jump in block %d (0x%x) - target was already "
                        "the next statement.",
                        block.id, block.address,
                    )
                    index += 1
                    continue

                # Nothing left at all (the original pure
                # single-instruction trampoline shape) - drop the now
                # empty block from the region entirely.
                del children[index]
                logger.debug(
                    "RedundantJumpRegionPass: dropped bare jump block %d "
                    "(0x%x) - target was already the next statement.",
                    block.id, block.address,
                )
                continue

            index += 1

    @staticmethod
    def _is_redundant_jump(block: BasicBlock, next_sibling: BasicBlock) -> bool:
        if not isinstance(block.terminator, TerminatorJump):
            return False

        if not block.instructions or block.instructions[-1].terminator is not block.terminator:
            # The terminator isn't owned by this block's own last
            # instruction (unusual - bail rather than guess which
            # instruction actually carries it).
            return False

        return block.terminator.target == next_sibling.address

    def _strip_back_edge_jumps(self, loop: LoopRegion) -> None:
        header = loop.header_block

        if header is None:
            return

        for latch in loop.latches:
            terminator = latch.terminator

            if not isinstance(terminator, TerminatorJump):
                # Either not a plain back-edge jump, or (bottom-tested
                # loop) already consumed by LoopConditionRegionPass
                # into loop.condition - nothing to strip either way.
                continue

            if terminator.target != header.address:
                # An escape/break edge or something else this pass
                # doesn't recognize - leave it as an explicit goto.
                continue

            if self._clear_trailing_jump(latch, terminator):
                logger.debug(
                    "RedundantJumpRegionPass: dropped loop %d's own "
                    "back-edge jump in latch block %d (0x%x) - implied "
                    "by the loop construct itself.",
                    header.id, latch.id, latch.address,
                )

    def _strip_try_exit_jumps(self, node: TryRegion) -> None:
        exit_address = self._try_exit_address(node)

        if exit_address is None:
            # No next sibling to fall through into (the TryRegion is
            # the last thing in its parent) - nothing this pass can
            # confirm a bare Jmp here is redundant against.
            return

        candidates = [node.try_body]

        if node.catch is not None:
            candidates.append(node.catch.body)

        for body in candidates:
            if not body.children or not isinstance(body.children[-1], BasicBlock):
                continue

            block = body.children[-1]
            terminator = block.terminator

            if not isinstance(terminator, TerminatorJump):
                continue

            if terminator.target != exit_address:
                # Some other jump this pass doesn't recognize (an
                # early return/break out of an enclosing construct,
                # for instance) - leave it as an explicit goto.
                continue

            if self._clear_trailing_jump(block, terminator):
                logger.debug(
                    "RedundantJumpRegionPass: dropped a try/catch's own "
                    "trailing jump in block %d (0x%x) past its handler - "
                    "implied by falling through to what already follows "
                    "the whole try/catch/finally statement.",
                    block.id, block.address,
                )

    @staticmethod
    def _try_exit_address(node: TryRegion) -> int | None:
        parent = node.parent

        if not isinstance(parent, SequenceRegion):
            # Every TryRegion observed in practice sits inside a
            # SequenceRegion (every compound region's body/then_body/
            # etc. slot is one, even for a single child) - bail rather
            # than guess at some other parent kind's notion of "next".
            return None

        try:
            index = parent.children.index(node)
        except ValueError:
            return None

        if index + 1 >= len(parent.children):
            return None

        next_sibling = parent.children[index + 1]

        if not isinstance(next_sibling, BasicBlock):
            # Same narrow-scope reasoning as _is_redundant_jump above:
            # resolving "the first address a compound sibling region
            # would execute" needs region-kind-specific internals this
            # pass has no need to become coupled to for the one shape
            # actually observed.
            return None

        return next_sibling.address

    @staticmethod
    def _clear_trailing_jump(block: BasicBlock, terminator: TerminatorJump) -> bool:
        """Drops `terminator` from `block`, keeping any real statements
        ahead of it intact. Returns False (and changes nothing) if the
        invariant every caller relies on - `terminator` is owned by
        `block`'s own last instruction - doesn't hold, since that
        means this isn't the plain trailing-Jmp shape either caller
        expects and guessing which instruction to touch would be
        unsafe.
        """
        if not block.instructions or block.instructions[-1].terminator is not terminator:
            return False

        last = block.instructions[-1]

        if last.value is not None or last.statement is not None:
            # This instruction does more than just carry the jump
            # (unusual for a bare Jmp, but don't guess) - only clear
            # the terminator, keep the instruction itself.
            last.terminator = None
        else:
            block.instructions.pop()

        block.terminator = None
        return True
