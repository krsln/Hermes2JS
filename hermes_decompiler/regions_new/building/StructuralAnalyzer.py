from hermes_decompiler.regions_new.models.InstructionRegion import InstructionRegion
from hermes_decompiler.regions_new.models.SequenceRegion import SequenceRegion


class StructuralAnalyzer:

    def __init__(self, cfg):

        self.cfg = cfg

    def build(self):

        root = SequenceRegion()

        for block in self.cfg.blocks:

            for instruction in block.instructions:
                root.children.append(
                    InstructionRegion(instruction)
                )

        return root
