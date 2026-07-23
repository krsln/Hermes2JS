from dataclasses import dataclass

from hermes_decompiler.two.regions.model.Region import Region


@dataclass(slots=True)
class TryRegion(Region):

    try_region: Region

    catch_region: Region | None = None

    finally_region: Region | None = None

    exception_name: str | None = None

    def accept(self, visitor):
        return visitor.visit_try(self)
