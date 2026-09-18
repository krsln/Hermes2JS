from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, LoopRegion, SequenceRegion, SwitchRegion, TryRegion
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

    A fourth shape, the SwitchRegion analogue of the third: a case's
    (or `default:`'s) own trailing `break`-equivalent jump straight to
    wherever control resumes once the whole switch statement finishes
    - implied by the switch construct itself exactly the way a loop's
    back edge is implied by `for`/`while`, so it's dropped the same
    way. Unlike the loop and TryRegion cases, though, a SwitchRegion
    built from a comparison chain (see _comparison_chain_builder.py -
    the shape Hermes emits for a small/sparse set of case values,
    where IfStructurer's own `else`-chain folding already got there
    first) has no `header`/`latches` of its own to inspect: whichever
    case IfStructurer's chain happened to fold most directly already
    lost its trailing jump as an ordinary same-SequenceRegion sibling
    match (the first, sibling-trampoline shape above) purely as a side
    effect of chain-folding order - not because it's structurally any
    different from a case IfStructurer's folding left an explicit jump
    in, most often whichever case ends up as `default:`, the chain's
    innermost/last alternative with no further sibling of its own to
    match against (see ExceptionTests/switchInsideTryTest, whose
    `default:` case used to end with a redundant `goto label_115;`).

    Resolving that target takes one more step than the third shape:
    `default:`'s own body sits inside a SwitchRegion that itself has no
    next sibling of its own (it's the last - often only - statement in
    whatever contains it, e.g. a TryRegion's try_body in
    switchInsideTryTest), so there's no sibling BasicBlock to compare
    against at the SwitchRegion's own level at all. `_strip_switch_exit_jumps`
    doesn't special-case that - it calls the same walk-up-through-
    parents-with-no-sibling-of-their-own helper `_strip_try_exit_jumps`
    above already uses (`_next_fallthrough_address`), which keeps
    climbing past a childless SequenceRegion into whatever wraps it
    (the switch's own enclosing TryRegion, here) until it finds an
    actual sibling BasicBlock to compare against - exactly the address
    `_strip_try_exit_jumps` would independently compute for that same
    enclosing TryRegion.

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

    def visit_SwitchRegion(self, node: SwitchRegion) -> None:
        for case in node.cases:
            self.visit(case.body)

        if node.default_body is not None:
            self.visit(node.default_body)

        self._strip_switch_exit_jumps(node)

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
        exit_address = self._next_fallthrough_address(node)

        if exit_address is None:
            # No next sibling to fall through into anywhere up the
            # parent chain - nothing this pass can confirm a bare Jmp
            # here is redundant against.
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

    def _strip_switch_exit_jumps(self, node: SwitchRegion) -> None:
        exit_address = self._next_fallthrough_address(node)

        if exit_address is None:
            return

        candidates = [case.body for case in node.cases]

        if node.default_body is not None:
            candidates.append(node.default_body)

        for body in candidates:
            if not body.children or not isinstance(body.children[-1], BasicBlock):
                continue

            block = body.children[-1]
            terminator = block.terminator

            if not isinstance(terminator, TerminatorJump):
                continue

            if terminator.target != exit_address:
                # An early return/break out of an enclosing construct,
                # or (fallthrough to the NEXT case, no `break` in the
                # source) a jump this pass doesn't try to recognize -
                # leave it as an explicit goto either way.
                continue

            if self._clear_trailing_jump(block, terminator):
                logger.debug(
                    "RedundantJumpRegionPass: dropped a switch case's own "
                    "trailing break-jump in block %d (0x%x) - implied by "
                    "falling through to what already follows the whole "
                    "switch statement.",
                    block.id, block.address,
                )

    @staticmethod
    def _next_fallthrough_address(region) -> int | None:
        """Address where control resumes once `region` (a TryRegion or
        SwitchRegion, currently the only callers) finishes running
        normally.

        Walks up through parents with nothing of their own to fall
        into - a `default:` body that's the last thing in its
        SwitchRegion, itself the last thing in a TryRegion's try_body,
        for instance - until an actual next-sibling BasicBlock turns
        up. Bails (returns None) the moment a step can't be resolved
        cleanly rather than guess: an unrecognized parent kind, or a
        next sibling that isn't a bare BasicBlock (a compound region,
        whose own first address this pass has no need to become
        coupled to resolving - see the class docstring's stated
        reasoning for staying deliberately narrow).
        """
        node = region

        while node is not None:
            parent = node.parent

            if not isinstance(parent, SequenceRegion):
                return None

            try:
                index = parent.children.index(node)
            except ValueError:
                return None

            if index + 1 < len(parent.children):
                next_sibling = parent.children[index + 1]
                return next_sibling.address if isinstance(next_sibling, BasicBlock) else None

            # `node` is the last child of its own SequenceRegion - that
            # SequenceRegion has no address of its own to fall into,
            # so keep climbing from whatever wraps it (the compound
            # region `parent` is itself a try_body/case-body/etc. slot
            # of).
            node = parent.parent

        return None

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
