from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.models.OpcodeResult import OpcodeResult


class BasicBlockBuilder:

    @classmethod
    def build(cls, results: list[OpcodeResult]) -> ControlFlowGraph:
        """
        Construct a Control Flow Graph (CFG) from a linear opcode sequence.
        """
        if not results:
            return ControlFlowGraph()

        leaders = cls._find_leaders(results)

        blocks = cls._build_blocks(results, leaders)

        cfg = ControlFlowGraph(blocks)

        cls._connect_blocks(cfg)

        return cfg

    @staticmethod
    def _find_leaders(results: list[OpcodeResult]) -> set[int]:
        """
        Return instruction addresses that begin a basic block.
        """
        leaders = {
            results[0].Opcode.address,
        }

        #
        # Next step:
        # - Jump targets
        # - Catch handlers
        # - Instructions following jumps/returns
        #

        return leaders

    @staticmethod
    def _build_blocks(
            results: list[OpcodeResult],
            leaders: set[int],
    ) -> list[BasicBlock]:

        blocks: list[BasicBlock] = []

        current: BasicBlock | None = None

        for result in results:

            addr = result.Opcode.address

            if addr in leaders:

                if current is not None:
                    current.end_addr = current.instructions[-1].Opcode.address
                    blocks.append(current)

                current = BasicBlock(start_addr=addr)

            if current is None:
                continue

            current.instructions.append(result)

        if current is not None:
            current.end_addr = current.instructions[-1].Opcode.address
            blocks.append(current)

        return blocks

    @classmethod
    def _connect_blocks(cls, cfg: ControlFlowGraph) -> None:
        """
        Connect basic blocks with control-flow edges.

        (Implemented in the next step.)
        """
        pass
