from hermes_decompiler.analysis.transforms.LoopConditionExtractor import LoopConditionExtractor
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.transforms.StatementBuilder import StatementBuilder
from hermes_decompiler.analysis.transforms.structurers import (
    SequenceStructurer,
    LoopStructurer,
    IfStructurer,
    BooleanChainFolder,
    SwitchStructurer,
    TryStructurer,
)


class StructuralAnalyzer:

    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):

        root = SequenceStructurer(self.cfg).run()

        graph = RegionGraph(root)

        LoopStructurer(graph, self.cfg).run()
        IfStructurer(graph, self.cfg).run()

        # Fold `r = E1; if (!E1) { r = E2; }` idioms back into
        # `r = E1 || E2;` (and the `&&` counterpart) before the
        # condition is flattened to text. Must run after IfStructurer
        # (needs real IfRegions) and before StatementBuilder (needs
        # BasicBlocks still intact, not yet flattened to
        # InstructionStates).
        BooleanChainFolder().run(graph.root)

        LoopConditionExtractor(graph.root).run()

        SwitchStructurer(graph, self.cfg).run()
        TryStructurer(graph, self.cfg).run()

        StatementBuilder().build(root)

        return root