from dataclasses import dataclass

from hermes_decompiler.cfg.regions.Region import Region


@dataclass(slots=True)
class TryRegion(Region):
    try_region: Region

    catch_region: Region | None = None

    finally_region: Region | None = None
