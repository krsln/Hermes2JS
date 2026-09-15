from __future__ import annotations

from hermes_decompiler.backend.transforms.structurers import RegionStructurer

from ._compound_folder import _CompoundConditionFolder
from ._dominance_builder import _DominanceIfBuilder


class IfStructurer(RegionStructurer):
    """Builds structured IfRegions and folds short-circuit conditions.

    Thin orchestrator over two independently testable passes:

    - `_DominanceIfBuilder` - builds new IfRegions from raw CFG blocks,
      purely by dominance.
    - `_CompoundConditionFolder` - rewrites those IfRegions, collapsing
      `&&`/`||` cascades and absorbing residual jumps. Never introduces
      a region from scratch.

    Order matters: the folder pattern matches against IfRegions the
    builder produces, so the builder must run first.

    Not yet handled by either pass: labeled break/continue and other
    cross-branch/tail-merged jumps. Those still surface as raw
    goto/switch statements downstream.
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)
        self._builder = _DominanceIfBuilder(graph, cfg)
        self._folder = _CompoundConditionFolder(graph, cfg)

    def run(self) -> None:
        self._builder.run()
        self._folder.run(self.graph.root)
        self.dump_region_tree_if_debug(type(self).__name__)
