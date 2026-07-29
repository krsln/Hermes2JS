from __future__ import annotations

from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.transforms.cfg_passes import ShortCircuitConditionMerger
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
)
from hermes_decompiler.analysis.transforms.lowering import StatementBuilder


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

        # ---- 3. region_passes -------------------------------------------
        BooleanChainFolder(self.cfg).run(graph.root)
        LoopConditionExtractor(graph.root).run()

        # SwitchStructurer is kept in this historical position (after
        # region_passes, not batched with the other structurers in
        # stage 2) even though it's currently a no-op stub - preserved
        # exactly as-is rather than reordered on a guess, since a
        # future real implementation may depend on running after
        # BooleanChainFolder/LoopConditionExtractor for reasons not
        # yet documented here.
        SwitchStructurer(graph, self.cfg).run()

        # ---- 4. lowering ------------------------------------------------
        StatementBuilder().build(root)

        return root
