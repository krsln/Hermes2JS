from dataclasses import dataclass

from hermes_decompiler.cfg.regions.Region import Region


@dataclass(slots=True)
class IfRegion(Region):
    """
    Represents a reconstructed if/else statement.
    """

    condition: str

    then_region: Region

    else_region: Region | None = None