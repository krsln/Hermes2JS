from dataclasses import dataclass

from hermes_decompiler.two.regions.model.Region import Region


@dataclass(slots=True)
class IfRegion(Region):
    """
    Single-branch conditional region:

        if (condition) {
            then_region
        }
        // falls through to whatever follows in the parent sequence

    NOTE: the old IfRegion carried its own `build()` / `_build_if()` /
    `_is_if_header()` classmethods, but `build()` was never actually
    called from anywhere (RegionBuilder always went straight to
    `_build_sequence`), and `_build_if` was an empty stub that always
    returned None. That construction logic has moved to
    `regions.building._StructuralAnalyzer`, which has the RPO/dominator/
    post-dominator context it needs to do the job properly - a model
    class like this one shouldn't own graph-traversal logic itself.
    """

    condition: str
    then_region: Region

    def accept(self, visitor):
        return visitor.visit_if(self)
