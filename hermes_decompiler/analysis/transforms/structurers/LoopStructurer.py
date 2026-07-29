from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer


class LoopStructurer(RegionStructurer):

    def run(self):

        if self.cfg.loop_analysis is None:
            return

        roots = [
            loop
            for loop in self.cfg.loop_analysis.loops.values()
            if loop.parent is None
        ]

        for loop in roots:
            # Build each top-level loop under whatever SequenceRegion
            # currently owns its header block - NOT unconditionally
            # graph.root. A prior pass (TryStructurer) may already have
            # relocated the header (and its would-be members) into a
            # try/catch body's own SequenceRegion; hardcoding root here
            # would silently rip those blocks back out of the try body
            # and re-home the loop at the top level, leaving an empty
            # `try {}` behind. See RegionGraph.owner().
            parent_sequence = self.graph.owner(loop.header)

            if parent_sequence is None:
                # Header isn't tracked anywhere yet (shouldn't normally
                # happen post-SequenceStructurer) - fall back to root
                # rather than crashing.
                parent_sequence = self.graph.root

            self._build_loop(loop, parent_sequence)

        # TODO: activate with a condition
        # print("\n===== REGION TREE =====")
        # self._dump(self.graph.root)

    def _build_loop(
            self,
            loop,
            parent_sequence: SequenceRegion,
    ):

        region = LoopRegion(loop)

        if loop.header not in parent_sequence.children:

            old_owner = self.graph.owner(loop.header)

            if old_owner and loop.header in old_owner.children:
                old_owner.children.remove(loop.header)

            parent_sequence.children.append(
                loop.header
            )

            loop.header.parent = parent_sequence

            self.graph.block_owner[loop.header] = parent_sequence

        index = parent_sequence.children.index(
            loop.header
        )

        parent_sequence.children[index] = region

        region.parent = parent_sequence

        region.body.children.append(
            loop.header
        )

        self.graph.block_owner[loop.header] = region.body

        child_members = set()

        for child in loop.children:
            child_members.update(child.members)

        for block in sorted(loop.members, key=lambda b: b.id):

            if block == loop.header:
                continue

            if block in child_members:
                continue

            self.graph.move(
                block,
                region.body
            )

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
