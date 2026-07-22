from __future__ import annotations

from abc import ABC

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock


class Region(ABC):

    def __init__(self):
        self.parent: "Region | None" = None


class LoopRegion(Region):

    def __init__(self, natural_loop):
        super().__init__()

        self.loop = natural_loop

        self.children: list[Region] = []

    def append(self, region):
        region.parent = self
        self.children.append(region)


class SequenceRegion(Region):

    def __init__(self):
        super().__init__()

        self.children: list[Region] = []

    def append(self, region: Region):
        region.parent = self
        self.children.append(region)


class InstructionRegion(Region):

    def __init__(self, block: BasicBlock):
        super().__init__()

        self.block = block
