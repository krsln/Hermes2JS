from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.models.OpcodeResult import OpcodeResult


class BasicBlockBuilder:

    @classmethod
    def build(cls, results: list[OpcodeResult]) -> list[BasicBlock]:
        """
        Build linear BasicBlocks from opcode results.
        """
        if not results:
            return []

        leaders = cls._find_leaders(results)

        return cls._build_blocks(results, leaders)

    @staticmethod
    def _find_leaders(results: list[OpcodeResult]) -> set[int]:
        leaders = {
            results[0].opcode.address,
        }

        #
        # TODO
        #   jump targets
        #   catch handlers
        #   instruction after jump
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

            addr = result.opcode.address

            if addr in leaders:

                if current is not None:
                    current.end_addr = current.instructions[-1].opcode.address
                    blocks.append(current)

                current = BasicBlock(start_addr=addr)

            current.instructions.append(result)

        if current is not None:
            current.end_addr = current.instructions[-1].opcode.address
            blocks.append(current)

        return blocks
