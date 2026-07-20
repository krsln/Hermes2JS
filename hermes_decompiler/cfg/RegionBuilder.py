from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.ConditionExtractor import ConditionExtractor
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph

from hermes_decompiler.cfg.regions.BlockRegion import BlockRegion
from hermes_decompiler.cfg.regions.IfRegion import IfRegion
from hermes_decompiler.cfg.regions.SequenceRegion import SequenceRegion


class RegionBuilder:
    """
    Converts a Control Flow Graph into a hierarchy of Regions.
    """

    @classmethod
    def build(cls, cfg: ControlFlowGraph) -> SequenceRegion:

        root = SequenceRegion()

        visited = set()

        current = cfg.entry

        while current:

            if current.id in visited:
                break

            visited.add(current.id)

            region = cls._try_build_if(cfg, current)

            if region is None:
                region = BlockRegion(current)

            root.children.append(region)

            if len(current.successors) != 1:
                break

            current = cfg.get_block(next(iter(current.successors)))

        return root

    @classmethod
    def _try_build_if(
            cls,
            cfg: ControlFlowGraph,
            block: BasicBlock,
    ) -> IfRegion | None:

        if not cls._is_if_candidate(block):
            return None

        successors = cfg.successors(block)

        if len(successors) != 2:
            return None

        return IfRegion(
            condition=ConditionExtractor.extract(block.last),
            then_region=BlockRegion(successors[0]),
            else_region=BlockRegion(successors[1]),
        )

    @classmethod
    def _is_if_candidate(cls, block: BasicBlock) -> bool:
        """
        Return True if the block looks like an if-statement header.
        """

        if not block.is_conditional:
            return False

        if block.last.goto is None:
            return False

        return True
