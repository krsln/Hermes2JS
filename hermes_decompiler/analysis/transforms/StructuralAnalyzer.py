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

        # Runs after Loop/If: try/catch bodies routinely wrap only a
        # *sub-slice* of a loop iteration (e.g. everything except the
        # loop header/back-edge - see TryStructurer docstring), so the
        # try range's blocks need to already be resolved into their
        # final loop/if nesting (and adjacent IfRegions already folded
        # in) before we can find them as flat siblings within whatever
        # SequenceRegion they now live in.
        TryStructurer(graph, self.cfg).run()

        BooleanChainFolder(self.cfg).run(graph.root)
        LoopConditionExtractor(graph.root).run()
        SwitchStructurer(graph, self.cfg).run()

        StatementBuilder().build(root)
        return root
