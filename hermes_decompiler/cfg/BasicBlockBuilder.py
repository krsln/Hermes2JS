from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.models.OpcodeResult import OpcodeResult


class BasicBlockBuilder:

    @classmethod
    def build(cls, results: list[OpcodeResult]) -> list[BasicBlock]:
        if not results:
            return []

        leaders = cls._find_leaders(results)

        return cls._build_blocks(results, leaders)

    @staticmethod
    def _find_leaders(results: list[OpcodeResult]) -> set[int]:

        leaders = {
            results[0].opcode.address,
        }

        for index, result in enumerate(results):

            #
            # jump target
            #

            if result.goto is not None:
                leaders.add(result.goto)

            #
            # instruction after branch
            #

            if (
                    result.goto is not None
                    or result.handler in {
                "Ret",
                "Throw",
            }
            ):

                if index + 1 < len(results):
                    leaders.add(
                        results[index + 1].opcode.address
                    )

            #
            # Catch starts a block
            #

            if result.handler == "Catch":
                leaders.add(result.opcode.address)

        return leaders

    @staticmethod
    def _build_blocks(
        results: list[OpcodeResult],
        leaders: set[int],
    ) -> list[BasicBlock]:

        blocks: list[BasicBlock] = []

        current: BasicBlock | None = None

        for result in results:

            address = result.opcode.address

            if address in leaders:

                if current is not None:
                    current.end_addr = current.instructions[-1].opcode.address
                    blocks.append(current)

                current = BasicBlock(start_addr=address)

            if current is None:
                continue

            current.instructions.append(result)

        if current is not None:
            current.end_addr = current.instructions[-1].opcode.address
            blocks.append(current)

        return blocks