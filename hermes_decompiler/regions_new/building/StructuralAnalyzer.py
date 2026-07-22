from __future__ import annotations

from hermes_decompiler.regions_new.cfg.CFG import CFG
from hermes_decompiler.regions_new.models.InstructionRegion import InstructionRegion
from hermes_decompiler.regions_new.models.SequenceRegion import SequenceRegion


class StructuralAnalyzer:
    """
    Converts CFG into a Region tree.

    Phase-1:
        CFG -> SequenceRegion
    """

    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def build(self) -> SequenceRegion:
        root = SequenceRegion()

        for block in self.cfg.blocks:
            for instruction in block.instructions:
                root.children.append(
                    InstructionRegion(instruction)
                )

        return root