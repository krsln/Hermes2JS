from dataclasses import dataclass

from hermes_decompiler.regions.Region import Region


@dataclass(slots=True)
class LoopRegion(Region):

    condition: str | None

    body: Region

    def accept(self, visitor):
        return visitor.visit_loop(self)