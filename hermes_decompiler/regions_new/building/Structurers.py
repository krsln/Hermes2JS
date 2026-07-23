from __future__ import annotations

from hermes_decompiler.regions_new.building.RegionGraph import RegionGraph
from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock
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

        roots = [
            loop
            for loop in self.cfg.loop_analysis.loops.values()
            if loop.parent is None
        ]

        for loop in roots:
            self._build_loop(loop, self.graph.root)

        # print("\n===== REGION TREE =====")
        # self._dump(self.graph.root)

    def _build_loop(
            self,
            loop,
            parent_sequence: SequenceRegion,
    ):

        region = LoopRegion(loop)

        #
        # Eğer root veya parent içinde header yoksa
        # header'ı ekle
        #
        if loop.header not in parent_sequence.children:

            old_owner = self.graph.owner(loop.header)

            if old_owner and loop.header in old_owner.children:
                old_owner.children.remove(loop.header)

            parent_sequence.children.append(
                loop.header
            )

            loop.header.parent = parent_sequence

            self.graph.block_owner[loop.header] = parent_sequence

        #
        # Header yerine LoopRegion koy
        #
        index = parent_sequence.children.index(
            loop.header
        )

        parent_sequence.children[index] = region

        region.parent = parent_sequence

        #
        # Header body içine
        #
        region.body.children.append(
            loop.header
        )

        self.graph.block_owner[loop.header] = region.body

        #
        # Child loop bloklarını ayır
        #
        child_members = set()

        for child in loop.children:
            child_members.update(child.members)

        #
        # Normal blokları taşı
        #
        for block in sorted(loop.members, key=lambda b: b.id):

            if block == loop.header:
                continue

            if block in child_members:
                continue

            self.graph.move(
                block,
                region.body
            )

        #
        # Child loops
        #
        for child in sorted(
                loop.children,
                key=lambda l: l.header.id
        ):
            self._build_loop(child, region.body)

    def _dump(self, region, indent=0):

        prefix = " " * indent

        if isinstance(region, SequenceRegion):
            print(f"{prefix}SequenceRegion")

            for child in region.children:
                self._dump(child, indent + 4)

            return

        if isinstance(region, LoopRegion):
            print(f"{prefix}LoopRegion(header={region.header_block.id})")
            self._dump(region.body, indent + 4)
            return

        if isinstance(region, BasicBlock):
            print(f"{prefix}Block {region.id}")
            return

        print(f"{prefix}{type(region).__name__}")


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
