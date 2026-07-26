from __future__ import annotations

from hermes_decompiler.analysis.regions.Regions import SequenceRegion


class SequenceStructurer:

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self):
        root = SequenceRegion()
        root.children.extend(self.cfg.blocks)

        return root
