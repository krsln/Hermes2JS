from __future__ import annotations

from .Region import Region


class InstructionRegion(Region):

    def __init__(self, block):
        super().__init__()

        self.block = block