class IfStructurer:

    def __init__(self, root, cfg):

        self.root = root
        self.cfg = cfg

    def run(self):

        return

class LoopStructurer:

    def __init__(self, root, cfg):

        self.root = root
        self.cfg = cfg

    def run(self):

        #
        # next PR
        #

        return
from hermes_decompiler.regions_new.models.SequenceRegion import SequenceRegion
from hermes_decompiler.regions_new.models.InstructionRegion import InstructionRegion


class SequenceStructurer:

    def __init__(self, cfg):

        self.cfg = cfg

    def run(self):

        root = SequenceRegion()

        for block in self.cfg.blocks:

            root.append(
                InstructionRegion(block)
            )

        return root

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

