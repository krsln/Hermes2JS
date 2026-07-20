from dataclasses import dataclass

from hermes_decompiler.regions.model.Region import Region


@dataclass(slots=True)
class IfElseRegion(Region):
    """
    Two-branch conditional region:

        if (condition) {
            then_region
        } else {
            else_region
        }
    """

    condition: str
    then_region: Region
    else_region: Region

    def accept(self, visitor):
        return visitor.visit_if_else(self)
