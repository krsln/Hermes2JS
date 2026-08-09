from __future__ import annotations

from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

from ._compound_folder import _CompoundConditionFolder
from ._dominance_builder import _DominanceIfBuilder


class IfStructurer(RegionStructurer):
    """
    Converts BasicBlocks terminated by a ConditionalBranch into
    structured IfRegions, then folds the common Hermes short-circuit
    (`&&`/`||`) idioms back into compound conditions.

    This class is a thin orchestrator over two independently testable
    passes (see each for the full mechanics):

      - `_DominanceIfBuilder`   - builds new `IfRegion`s from raw CFG
                                   blocks, purely by dominance.
      - `_CompoundConditionFolder` - rewrites the `IfRegion`s that
                                   `_DominanceIfBuilder` just built,
                                   collapsing `&&`/`||` cascades and
                                   absorbing residual jumps. Never
                                   introduces a region from scratch.

    They must run in this order: the folder pattern-matches against
    already-built `IfRegion`s, so it is meaningless before the builder
    has run at least once.

    Not yet handled by either pass: labeled break/continue and other
    cross-branch/tail-merged jumps (blocks whose target lives in a
    different region entirely). Those still surface as raw
    goto/switch statements downstream - see the transforms roadmap's
    labeled-break-support phase.
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)
        self._builder = _DominanceIfBuilder(graph, cfg)
        self._folder = _CompoundConditionFolder(graph)

    def run(self) -> None:
        self._builder.run()
        self._folder.run(self.graph.root)
        self.dump_region_tree_if_debug(type(self).__name__)
