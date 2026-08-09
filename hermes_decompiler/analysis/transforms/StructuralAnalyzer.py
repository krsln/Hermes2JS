from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorSwitch
from hermes_decompiler.analysis.transforms.cfg_passes import (
    ShortCircuitConditionMerger,
)
from hermes_decompiler.analysis.transforms.structurers import (
    SequenceStructurer,
    LoopStructurer,
    LoopBreakRecognizer,
    IfStructurer,
    TryStructurer,
    SwitchStructurer,
)
from hermes_decompiler.analysis.transforms.region_passes import (
    BooleanChainFolder,
    LoopConditionExtractor,
    ForEachRecognizer,
    ConditionalExpressionFolder, NullishAssignmentFolder,
)
from hermes_decompiler.analysis.transforms.lowering import StatementBuilder
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)

# Terminators that a structurer is always expected to consume. A
# `BasicBlock` left holding one of these after `build()` means some CFG
# shape wasn't recognized by any structurer - not a crash, but a real
# gap: `Printer._emit_block` will render it as a raw
# `if (...) goto label_N;` (or a switch dump) instead of proper
# `if`/`while`/`switch` JS syntax. `TerminatorJump`/`Return`/`Throw` are
# intentionally excluded: those render correctly as plain leaf
# statements even inside a fully-structured tree, so their presence
# isn't a sign of anything unresolved.
_UNSTRUCTURED_TERMINATOR_KINDS = (TerminatorConditionalBranch, TerminatorSwitch)


class StructuralAnalyzer:
    """
    Owns the full CFG -> region-tree -> statement-list pipeline, and is
    the ONLY place any transform pass is ever invoked. Callers (e.g.
    `HermesAnalysis.generate_js_v1`) run CFG-level analyses that
    passes here depend on (`cfg.verify()` /
    `cfg.compute_dominators()` / `cfg.compute_post_dominators()` /
    `cfg.compute_loops()`) beforehand, then call
    `StructuralAnalyzer(cfg).build()` and take the resulting root -
    no pass is ever wired up or called from anywhere else.

    Passes run in four stages, each living in its own subpackage under
    `transforms/`:

        1. `cfg_passes/`     - rewrite the raw CFG (blocks, edges,
                                terminators) before any region exists.
                                e.g. `ShortCircuitConditionMerger`.

        2. `structurers/`    - build the region tree (Sequence, Loop,
                                If, Try, Switch regions) out of the
                                CFG. Every structurer but the
                                bootstrapping `SequenceStructurer`
                                extends the common `RegionStructurer`
                                base (`__init__(graph, cfg)` /
                                `run() -> None`).

        3. `region_passes/`  - post-process the already-built region
                                tree (fold/extract) without
                                introducing a new region *kind*.
                                e.g. `BooleanChainFolder`,
                                `LoopConditionExtractor`.

        4. `lowering/`       - turn the final region tree into the
                                flat per-block statement list
                                (`region.items`) that `JSEmitter`/
                                `Printer` render from.
                                e.g. `StatementBuilder`.

    A pass never reaches into a later stage's concerns and never runs
    outside this method - if a new pass is added, it's wired in here,
    in the stage that matches what it actually does, not bolted onto
    whichever caller happens to need it that day.
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        # ---- 1. cfg_passes --------------------------------------------
        ShortCircuitConditionMerger(self.cfg).run()

        # ---- 2. structurers -------------------------------------------
        root = SequenceStructurer(self.cfg).run()
        graph = RegionGraph(root)

        LoopStructurer(graph, self.cfg).run()

        # Must run after LoopStructurer (needs LoopRegion.body.covered_blocks
        # to tell loop-internal blocks from break targets) and before
        # IfStructurer (which would otherwise permanently strand the
        # break-test block's terminator - see StructuralAnalyzer's
        # unstructured-block audit for exactly this shape).
        LoopBreakRecognizer(graph, self.cfg).run()  # ✅

        IfStructurer(graph, self.cfg).run()

        # Runs after Loop/If: try/catch bodies routinely wrap only a
        # *sub-slice* of a loop iteration (e.g. everything except the
        # loop header/back-edge - see TryStructurer's docstring), so
        # the try range's blocks need to already be resolved into
        # their final loop/if nesting before we can find them as flat
        # siblings within whatever SequenceRegion they now live in.
        TryStructurer(graph, self.cfg).run()  # ✅

        # SwitchStructurer runs after the other structurers because it
        # recognizes two different switch representations:
        #
        #   * raw TerminatorSwitch jump tables left untouched by
        #     IfStructurer
        #
        #   * comparison chains that IfStructurer has already converted into
        #     nested IfRegions
        #
        # Running here allows it to fold both forms into a single
        # SwitchRegion representation before lowering.
        SwitchStructurer(graph, self.cfg).run()  # ✅

        # ---- 3. region_passes -------------------------------------------
        BooleanChainFolder(self.cfg).run(graph.root)  # `&&`/`||` (e.g. a bare`if (a || b) { ... }
        ConditionalExpressionFolder(self.cfg).run(graph.root)  # ternary
        NullishAssignmentFolder(self.cfg).run(graph.root)
        LoopConditionExtractor(graph.root).run()
        ForEachRecognizer(graph).run()

        # ---- 4. lowering ------------------------------------------------
        # StatementBuilder().build(root) # ❌ no effect at all

        self._audit_unstructured_blocks(root, graph, self.cfg)

        return root

    @staticmethod
    def _audit_unstructured_blocks(root, graph: RegionGraph, cfg) -> None:
        """
        Log (once, as a single warning listing every offender) any block
        still holding a conditional-branch or switch terminator after
        every structurer has run. This is diagnostic only - it never
        changes output - but makes an otherwise-silent structuring gap
        visible in normal logs instead of only showing up as an odd
        `if (...) goto label_N;` line buried in `--verbose` JS output.

        For a conditional branch, also resolves and reports where its
        target actually lives (which `SequenceRegion`, and whether that
        region is the same one the source block itself belongs to).
        Concretely distinguishes the two known failure shapes instead of
        leaving both looking identical in the log:

        - target's owner differs from the source block's own owner:
          the target is reachable another way this pass doesn't handle
          - most commonly compiler-side tail-merging/code-sharing across
            branches (see `IfStructurer` module docstring) - and finding
            the shared block by address by hand is exactly the kind of
            lookup this log line exists to save.
        - target has no owner / isn't a known block address at all:
          something upstream produced an inconsistent CFG - worth
          escalating rather than assuming it's the tail-merge case.
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
                # TerminatorSwitch (or any future addition to
                # _UNSTRUCTURED_TERMINATOR_KINDS): no single "target" to
                # resolve, just report the block itself.
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
