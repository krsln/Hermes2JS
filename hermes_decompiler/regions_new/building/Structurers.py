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
            if loop.parent is None:
                self._build_loop(loop, self.graph.root)

    def _build_loop(
            self,
            loop,
            parent_sequence: SequenceRegion,
    ):

        region = LoopRegion(loop)

        #
        # Header owner
        #
        owner = self.graph.owner(loop.header)

        if owner is None:
            return

        #
        # Header'ın yerine region koy
        #
        self.graph.replace_block(loop.header, region)

        #
        # Header body'nin ilk elemanı
        #
        region.body.children.append(loop.header)
        self.graph.block_owner[loop.header] = region.body

        #
        # Child loop'lara ait block'ları şimdilik atla
        #
        child_members = set()

        for child in loop.children:
            child_members |= child.members

        #
        # Kalan block'lar
        #
        for block in sorted(loop.members, key=lambda b: b.id):

            if block is loop.header:
                continue

            if block in child_members:
                continue

            self.graph.move(block, region.body)

        #
        # Nested loop'ları oluştur
        #
        for child in sorted(loop.children, key=lambda l: l.header.id):
            self._build_loop(child, region.body)

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
