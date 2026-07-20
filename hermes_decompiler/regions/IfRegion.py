from dataclasses import dataclass

from hermes_decompiler.cfg import BasicBlock
from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.regions.Region import Region


@dataclass(slots=True)
class IfRegion(Region):
    """
    Represents a single-branch conditional region.

    if (condition) {
        ...
    }
    """

    condition: str

    then_region: Region

    def accept(self, visitor):
        return visitor.visit_if(self)

    @classmethod
    def build(
            cls,
            analysis: CFGAnalysis,
    ) -> Region:
        region = cls._build_if(analysis)

        if region is not None:
            return region

        return cls._build_sequence(analysis)

    @classmethod
    def _build_if(
            cls,
            analysis: CFGAnalysis,
    ):

        for block in analysis.reverse_post_order:

            if not cls._is_if_header(block):
                continue

            #
            # sonraki adımda gerçek dönüşüm yapılacak
            #

        return None

    @staticmethod
    def _is_if_header(block: BasicBlock) -> bool:

        if len(block.outgoing) != 2:
            return False

        last = block.instructions[-1]

        return last.handler.startswith("Jmp")