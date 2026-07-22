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

        self.header = natural_loop.header
        self.members = natural_loop.members
        self.exits = natural_loop.exits

        self.children = []


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


class IfRegion(Region):

    def __init__(
            self,
            condition,
            true_region,
            false_region=None
    ):
        super().__init__()

        self.condition = condition
        self.true_region = true_region
        self.false_region = false_region

        true_region.parent = self

        if false_region:
            false_region.parent = self


class ConditionalRegion(Region):

    def __init__(
            self,
            condition,
            true_region,
            false_region=None
    ):
        super().__init__()

        self.condition = condition
        self.true_region = true_region
        self.false_region = false_region
