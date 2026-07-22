from __future__ import annotations

from hermes_decompiler.regions_new.building.Structurers import (
    IfStructurer, LoopStructurer, SequenceStructurer, SwitchStructurer, TryStructurer
)


class StructuralAnalyzer:

    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        root = SequenceStructurer(self.cfg).run()

        LoopStructurer(root, self.cfg).run()
        IfStructurer(root, self.cfg).run()

        # SwitchStructurer(root, self.cfg).run()
        # TryStructurer(root, self.cfg).run()

        return root
