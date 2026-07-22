from __future__ import annotations

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock

from .Region import Region


class InstructionRegion(Region):

    def __init__(self, block: BasicBlock):
        super().__init__()

        self.block = block
