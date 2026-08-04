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
    IfStructurer,
    TryStructurer,
    SwitchStructurer,
)
from hermes_decompiler.analysis.transforms.region_passes import (
    BooleanChainFolder,
    LoopConditionExtractor,
    ForEachRecognizer,
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
        IfStructurer(graph, self.cfg).run()

        # Runs after Loop/If: try/catch bodies routinely wrap only a
        # *sub-slice* of a loop iteration (e.g. everything except the
        # loop header/back-edge - see TryStructurer's docstring), so
        # the try range's blocks need to already be resolved into
        # their final loop/if nesting before we can find them as flat
        # siblings within whatever SequenceRegion they now live in.
        TryStructurer(graph, self.cfg).run()

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
        SwitchStructurer(graph, self.cfg).run()

        # ---- 3. region_passes -------------------------------------------
        BooleanChainFolder(self.cfg).run(graph.root)
        LoopConditionExtractor(graph.root).run()
        ForEachRecognizer(graph).run()

        # ---- 4. lowering ------------------------------------------------
        StatementBuilder().build(root)

        self._audit_unstructured_blocks(root)

        return root

    @staticmethod
    def _audit_unstructured_blocks(root) -> None:
        """
        Log (once, as a single warning listing every offender) any block
        still holding a conditional-branch or switch terminator after
        every structurer has run. This is diagnostic only - it never
        changes output - but makes an otherwise-silent structuring gap
        visible in normal logs instead of only showing up as an odd
        `if (...) goto label_N;` line buried in `--verbose` JS output.
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

        details = ", ".join(f"block {b.id} (0x{b.address:x})" for b in unresolved)
        logger.warning(
            "%d block(s) were not fully structured by any structurer and "
            "will render as raw goto/switch statements: %s",
            len(unresolved), details,
        )
