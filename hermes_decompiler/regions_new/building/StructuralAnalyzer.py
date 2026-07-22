from __future__ import annotations

from hermes_decompiler.regions_new.building.IfStructurer import IfStructurer
from hermes_decompiler.regions_new.building.LoopStructurer import LoopStructurer
from hermes_decompiler.regions_new.building.SequenceStructurer import SequenceStructurer
from hermes_decompiler.regions_new.building.SwitchStructurer import SwitchStructurer
from hermes_decompiler.regions_new.building.TryStructurer import TryStructurer


class StructuralAnalyzer:

    def __init__(self, cfg):

        self.cfg = cfg

    def build(self):

        root = SequenceStructurer(self.cfg).run()

        LoopStructurer(root, self.cfg).run()

        IfStructurer(root, self.cfg).run()

        SwitchStructurer(root, self.cfg).run()

        TryStructurer(root, self.cfg).run()

        return root