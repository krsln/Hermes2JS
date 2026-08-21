from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionGraph, TerminatorConditionalBranch, TerminatorSwitch
from hermes_decompiler.analysis.transforms.cfg_passes import (
    ShortCircuitConditionCfgPass,
)
from hermes_decompiler.analysis.transforms.region_passes import (
    BooleanChainRegionPass,
    ConditionalExpressionRegionPass,
    ForEachRegionPass,
    LoopConditionRegionPass,
    LoopContinueRegionPass,
    LoopInductionAliasPass,
    NullishAssignmentRegionPass,
)
from hermes_decompiler.analysis.transforms.structurers import (
    SequenceStructurer,
    LoopStructurer,
    LoopBreakStructurer,
    LoopLabeledExitStructurer,
    IfStructurer,
    TryStructurer,
    SwitchStructurer,
)
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)

# Terminators that should always be consumed by a structurer.
# If one remains after build(), the CFG shape was not recognized and
# will be emitted as a raw goto/switch instead of structured JS.
#
# Jump, Return, and Throw are intentionally excluded because they are
# valid leaf terminators and do not indicate an incomplete structure.
_UNSTRUCTURED_TERMINATOR_KINDS = (TerminatorConditionalBranch, TerminatorSwitch)


class StructuralAnalyzer:
    """
    Builds the structured representation from a CFG.

    The pipeline has three stages:

        1. CFG passes
           Rewrite the CFG before region construction.

        2. Structurers
           Convert CFG blocks into the region tree.

        3. Region passes
           Fold or extract expressions from the completed region tree.

    This class is the single entry point for all structural passes.
    Passes are invoked here in dependency order so that each stage only
    operates on the representation produced by the previous stage - and,
    within a stage, several passes have real correctness dependencies on
    each other's output, not just a conventional ordering. Each call
    below documents its own "must run after X" reasoning inline; when
    adding a new pass, place it where its actual data dependency lives
    rather than at the end of its stage by default.
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        # ---- 1. cfg_passes --------------------------------------------

        # Collapses a chain of single-purpose test blocks that share a
        # branch target (the CFG-level encoding of a pure control-flow
        # `&&`/`||`, e.g. `if (a||b) { ... }`) into one block with a
        # combined condition. Must run FIRST before any region exists:
        # it operates on raw block/edge shape, and once IfStructurer
        # has built an IfRegion around one of these blocks, the merge
        # this pass performs can no longer be expressed as a simple
        # CFG edit.
        ShortCircuitConditionCfgPass(self.cfg).run()

        # ---- 2. structurers -------------------------------------------
        root = SequenceStructurer(self.cfg).run()
        graph = RegionGraph(root)

        LoopStructurer(graph, self.cfg).run()

        # LoopBreakStructurer must run after LoopStructurer so it can
        # distinguish loop-internal blocks from loop exit targets.
        # It must also run before IfStructurer, which could otherwise
        # consume the break-test block as an ordinary conditional.
        LoopBreakStructurer(graph, self.cfg).run()

        # Handles exits that cross one or more enclosing loops and
        # therefore require a labeled break/continue.
        #
        # This must remain before IfStructurer for the same reason as
        # LoopBreakStructurer: once the block is consumed by an IfRegion,
        # the loop-level exit can no longer be recognized reliably.
        LoopLabeledExitStructurer(graph, self.cfg).run()

        # Builds IfRegions out of whatever conditional branches the
        # loop-exit structurers above didn't already claim. Must run
        # after both of them for the shared reason noted on each:
        # once a block is folded into an IfRegion here, its original
        # branch is gone, so a loop-exit shape that IfStructurer
        # reaches first can never be recovered as a `break`/`continue`
        # afterward - only ever as a plain (and, for a labeled exit,
        # WRONG) nested `if`.
        IfStructurer(graph, self.cfg).run()

        # Try regions may cover only part of a loop iteration, so loop
        # and if nesting must already be established before try/catch
        # ranges are identified.
        TryStructurer(graph, self.cfg).run()

        # SwitchStructurer handles both raw switch terminators and
        # comparison chains already converted into IfRegions.
        SwitchStructurer(graph, self.cfg).run()

        # ---- 3. region_passes -------------------------------------------
        BooleanChainRegionPass(graph, self.cfg).run()  # `&&`/`||` (e.g. a bare-if (a || b) { ... }

        # Must run after BooleanChainRegionPass: a then/else arm's own
        # condition may itself be an unfolded `&&`/`||` chain that
        # needs collapsing first, so this pass can read clean,
        # already-folded conditions instead of having to fold
        # sub-chains itself.
        ConditionalExpressionRegionPass(graph, self.cfg).run()  # ternary

        # No ordering dependency on the other region_passes - matches
        # a narrow, self-contained `if (x == null) { x = v; }` shape
        # and only ever touches the one IfRegion it folds.
        NullishAssignmentRegionPass(graph, self.cfg).run()

        # Must run after IfStructurer/SwitchStructurer, not just after
        # the loop structurers above: for a `for` loop, the body's own
        # inner conditions (e.g. `if (i === 3) continue;`) are only
        # available as clean IfRegion/SwitchRegion conditions once
        # those two have already run - beforehand they're still raw
        # BasicBlock terminators. LoopInductionAliasPass (right below)
        # depends on that same ordering to repoint those conditions,
        # not just this pass's own condition/initializer/update
        # extraction.
        LoopConditionRegionPass(graph, self.cfg).run()

        # Must run right after LoopConditionRegionPass (needs
        # loop.update/loop.initializer already populated to know the
        # induction register's identity. See its own docstring for
        # why it derives that from metadata rather than position) and
        # before ForEachRegionPass (fewer, unaliased registers make
        # that pass's own register-resolution walk less likely to
        # land on the wrong candidate).
        LoopInductionAliasPass(graph, self.cfg).run()

        # Converts residual unconditional jumps to the loop latch into
        # a `continue` statement. This requires the final If/Loop nesting.
        LoopContinueRegionPass(graph, self.cfg).run()

        # Reclassifies a plain `while` LoopRegion as `for-of`/`for-in`
        # by matching a fixed IteratorNext/GetNextPName instruction
        # sequence at the loop header. Must run after LoopStructurer,
        # TryStructurer, AND LoopConditionRegionPass - the last
        # because it relies on the header's terminator already having
        # been consumed into `loop.condition`, so the header's first
        # remaining instruction is reliably the iterator call and
        # nothing else. Ordering relative to LoopInductionAliasPass/
        # LoopContinueRegionPass doesn't matter; neither touches the
        # header's leading instruction the way this pass needs to.
        ForEachRegionPass(graph, self.cfg).run()

        # ---- Diagnostics ------------------------------------------------

        self._audit_unstructured_blocks(root, graph, self.cfg)

        return root

    @staticmethod
    def _audit_unstructured_blocks(root, graph: RegionGraph, cfg) -> None:
        """
        Report blocks that still contain a conditional or switch
        terminator after all structurers have run.

        Such blocks indicate a CFG shape that was not recognized by the
        structuring pipeline and will be emitted as a raw goto/switch.

        Conditional branches additionally report the relationship between
        the source block and its target:

        - Same region:
          Unexpected; the branch should normally have been consumed.

        - Different region:
          Likely a cross-branch or tail-merged block that is not handled
          by the current structurers.

        - No owner or unknown target:
          Indicates an inconsistent or incomplete CFG.
        """

        unresolved: list[BasicBlock] = sorted(
            (
                block for block in root.covered_blocks
                if isinstance(block.terminator, _UNSTRUCTURED_TERMINATOR_KINDS)
            ),
            key=lambda block: block.id,
        )

        if not unresolved:
            return

        address_to_block = {block.address: block for block in cfg.blocks}

        def describe(block: BasicBlock) -> str:
            terminator = block.terminator
            own_owner = graph.owner(block)

            if not isinstance(terminator, TerminatorConditionalBranch):
                # TerminatorSwitch has no single target to resolve.
                return f"block {block.id} (0x{block.address:x})"

            target_block = address_to_block.get(terminator.target)

            if target_block is None or not isinstance(target_block, BasicBlock):
                return (
                    f"block {block.id} (0x{block.address:x}) -> target "
                    f"0x{terminator.target:x} doesn't match any known block"
                )

            target_owner = graph.owner(target_block)

            if target_owner is None:
                relation = "target has no region owner (already consumed/detached?)"
            elif target_owner is own_owner:
                relation = "target IS a sibling in the same region - unexpected, investigate"
            else:
                relation = "target belongs to a DIFFERENT region (likely cross-branch/tail-merged code)"

            return (
                f"block {block.id} (0x{block.address:x}) -> goto "
                f"block {target_block.id} (0x{target_block.address:x}): {relation}"
            )

        details = "; ".join(describe(b) for b in unresolved)
        logger.warning(
            "%d block(s) were not fully structured by any structurer and "
            "will render as raw goto/switch statements: %s",
            len(unresolved), details,
        )
