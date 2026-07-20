from dataclasses import dataclass

from hermes_decompiler.regions.Region import Region


@dataclass(slots=True)
class IfRegion(Region):

    condition: str

    then_region: Region

    else_region: Region | None = None

    def accept(self, visitor):
        return visitor.visit_if(self)