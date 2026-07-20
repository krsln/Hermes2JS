from dataclasses import dataclass

from hermes_decompiler.cfg.regions.Region import Region


@dataclass(slots=True)
class SequenceRegion(Region):
    """
    Ordered sequence of child regions.
    """

    pass