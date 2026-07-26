from __future__ import annotations

from hermes_decompiler.ir.expressions import BinaryExpression, Expression, UnaryExpression
from hermes_decompiler.ir.Operators import BinaryOperator, LogicalOperator, UnaryOperator
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
)
from hermes_decompiler.analysis.regions.Statements import IfGotoStatement


class SwitchStructurer:

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):
        return
