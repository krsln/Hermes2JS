from dataclasses import dataclass, field

from hermes_decompiler.two.regions.model.Region import Region


@dataclass(slots=True)
class SequenceRegion(Region):
    """
    Ordered list of child regions that execute one after another.

    BREAKING CHANGE from the old SequenceRegion: it used to hold
    `list[BasicBlock]` directly. That made it a leaf-only container -
    it could describe "these blocks run in order" but had no way to
    embed an IfRegion/LoopRegion/TryRegion *between* two blocks, which
    is exactly what real structured code needs. Holding `list[Region]`
    instead lets a SequenceRegion freely mix BlockRegions with any
    other region type, which is what makes actual nesting possible.
    """

    regions: list[Region] = field(default_factory=list)

    def accept(self, visitor):
        return visitor.visit_sequence(self)
