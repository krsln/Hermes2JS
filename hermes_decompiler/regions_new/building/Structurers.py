from __future__ import annotations

from hermes_decompiler.regions_new.building.RegionGraph import RegionGraph
from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    LoopRegion,
    Region,
)


class SequenceStructurer:

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self):
        root = SequenceRegion()
        root.children.extend(self.cfg.blocks)

        return root


class LoopStructurer:

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):

        if self.cfg.loop_analysis is None:
            return

        loops = sorted(
            self.cfg.loop_analysis.loops.values(),
            key=lambda l: len(l.members),
            reverse=True,
        )

        for loop in loops:
            self._wrap_loop(loop)

    def _wrap_loop(self, loop):

        region = LoopRegion(loop)

        #
        # Header bilgisi
        #
        region.header_block = loop.header

        #
        # Önce header'ın sahibi bulunur.
        #
        owner = self.graph.owner(loop.header)

        if owner is None:
            return

        #
        # Header'ın yerine LoopRegion koy.
        #
        self.graph.replace_block(
            loop.header,
            region,
        )

        #
        # Header artık loop body'sinin ilk elemanı.
        #
        region.body.children.append(loop.header)

        self.graph.block_owner[loop.header] = region.body

        #
        # Diğer loop blocklarını body'ye taşı.
        #
        for block in sorted(loop.members, key=lambda b: b.id):

            if block is loop.header:
                continue

            self.graph.move(
                block,
                region.body,
            )


class IfStructurer:

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):
        #
        # Şimdilik placeholder.
        #
        # StatementBuilder geldikten sonra
        # gerçek IfRegion oluşturacağız.
        #
        return


class SwitchStructurer:

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):
        return


class TryStructurer:

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):
        return
