from __future__ import annotations

from hermes_decompiler.models.OpcodeResult import OpcodeResult

from .Region import Region


class InstructionRegion(Region):
    """
    Leaf node representing one instruction.
    """

    def __init__(self, result: OpcodeResult):
        self.result = result