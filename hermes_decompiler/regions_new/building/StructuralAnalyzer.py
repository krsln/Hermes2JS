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

        LoopStructurer(self.cfg).run()

        IfStructurer(self.cfg).run()

        SwitchStructurer(self.cfg).run()

        TryStructurer(self.cfg).run()

        return SequenceStructurer(self.cfg).run()