from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.models.OpcodeResult import OpcodeResult


class BasicBlockBuilder:
    """
    Builds linear BasicBlocks from a list of OpcodeResults.

    Blocks are split according to the classical compiler leader algorithm.
    """

    @classmethod
    def build(cls, results: list[OpcodeResult]) -> list[BasicBlock]:

        if not results:
            return []

        leaders = cls._find_leaders(results)

        return cls._build_blocks(results, leaders)

    @classmethod
    def _find_leaders(
        cls,
        results: list[OpcodeResult],
    ) -> set[int]:
        """
        Determine every instruction that begins a BasicBlock.

        Leaders are:

            • first instruction

            • jump targets

            • instruction immediately after a jump

            • catch handlers (future)
        """

        leaders: set[int] = {
            results[0].opcode.address,
        }

        for index, result in enumerate(results):

            #
            # explicit jump target
            #
            if result.goto is not None:
                leaders.add(result.goto)

            #
            # instruction after jump
            #
            if result.goto is not None:

                if index + 1 < len(results):
                    leaders.add(
                        results[index + 1].opcode.address
                    )

        return leaders

    @classmethod
    def _build_blocks(
        cls,
        results: list[OpcodeResult],
        leaders: set[int],
    ) -> list[BasicBlock]:

        blocks: list[BasicBlock] = []

        current: BasicBlock | None = None

        for result in results:

            address = result.opcode.address

            #
            # new block begins
            #
            if address in leaders:

                if current is not None:

                    current.end_addr = (
                        current.instructions[-1].opcode.address
                    )

                    blocks.append(current)

                current = BasicBlock(
                    start_addr=address,
                )

            if current is None:
                continue

            current.instructions.append(result)

        if current is not None:

            current.end_addr = (
                current.instructions[-1].opcode.address
            )

            blocks.append(current)

        return blocks