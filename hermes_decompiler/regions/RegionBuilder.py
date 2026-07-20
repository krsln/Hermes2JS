from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.regions.SequenceRegion import SequenceRegion


class RegionBuilder:
    """
    Converts a CFG into a hierarchical Region tree.
    """

    @classmethod
    def build(
        cls,
        analysis: CFGAnalysis,
    ):

        return cls._build_sequence(analysis)

    @classmethod
    def _build_sequence(
        cls,
        analysis: CFGAnalysis,
    ) -> SequenceRegion:

        return SequenceRegion(
            blocks=analysis.reverse_post_order
        )