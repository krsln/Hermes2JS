from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionGraph
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorSwitch
from hermes_decompiler.analysis.transforms.cfg_passes import (
    ShortCircuitConditionCfgPass,
)
from hermes_decompiler.analysis.transforms.region_passes import (
    BooleanChainRegionPass,
    ConditionalExpressionRegionPass,
    ForEachRegionPass,
    LoopConditionRegionPass,
    LoopContinueRegionPass,
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
    operates on the representation produced by the previous stage.
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        # ---- 1. cfg_passes --------------------------------------------
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
        ConditionalExpressionRegionPass(graph, self.cfg).run()  # ternary
        NullishAssignmentRegionPass(graph, self.cfg).run()
        LoopConditionRegionPass(graph, self.cfg).run()

        # Converts residual unconditional jumps to the loop latch into
        # a `continue` statement. This requires the final If/Loop nesting.
        LoopContinueRegionPass(graph, self.cfg).run()

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
