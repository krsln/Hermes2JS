from __future__ import annotations

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
)


class SequenceStructurer:

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self) -> SequenceRegion:

        root = SequenceRegion()

        #
        # Şimdilik Sequence.children içine BasicBlock koyuyoruz.
        # StatementBuilder daha sonra bunları Statement'a dönüştürecek.
        #
        root.children.extend(self.cfg.blocks)

        return root


class LoopStructurer:

    def __init__(self, root: SequenceRegion, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):

        if self.cfg.loop_analysis is None:
            return

        loops = sorted(
            self.cfg.loop_analysis.loops.values(),
            key=lambda loop: len(loop.members),
            reverse=True,
        )

        for loop in loops:
            self._wrap_loop(loop)

    # ---------------------------------------------------------

    def _wrap_loop(self, loop):

        region = LoopRegion(loop)

        #
        # Header ayrı tutuluyor.
        #
        region.header_block = loop.header

        new_children = []

        for child in self.root.children:

            #
            # Nested region'lara şimdilik dokunmuyoruz.
            #
            if not isinstance(child, BasicBlock):
                new_children.append(child)
                continue

            if child == loop.header:
                continue

            if child in loop.members:
                region.body.children.append(child)
            else:
                new_children.append(child)

        #
        # Header'ın bulunduğu yere insert ediyoruz.
        #
        insert_index = 0

        for i, child in enumerate(self.root.children):
            if child == loop.header:
                insert_index = i
                break

        new_children.insert(insert_index, region)

        self.root.children = new_children

        #
        # Header artık body'nin ilk bloğu.
        #
        region.body.children.insert(0, loop.header)


class IfStructurer:

    def __init__(self, root: SequenceRegion, cfg):
        self.root = root
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

    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):
        return


class TryStructurer:

    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg

    def run(self):
        return