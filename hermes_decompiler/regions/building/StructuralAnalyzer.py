from hermes_decompiler.regions.building.LoopConditionExtractor import LoopConditionExtractor
from hermes_decompiler.regions.building.RegionGraph import RegionGraph
from hermes_decompiler.regions.building.StatementBuilder import StatementBuilder
from hermes_decompiler.regions.building.Structurers import (
    SequenceStructurer,
    LoopStructurer,
    IfStructurer,
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

        LoopConditionExtractor(graph.root).run()

        SwitchStructurer(graph, self.cfg).run()
        TryStructurer(graph, self.cfg).run()

        StatementBuilder().build(root)

        return root