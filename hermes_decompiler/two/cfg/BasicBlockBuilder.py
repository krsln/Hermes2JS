from hermes_decompiler.two.cfg.BasicBlock import BasicBlock
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

            • jump targets (single `goto`, or any of `extra_gotos` -
              the latter covers SwitchImm's multiple case targets)

            • instruction immediately after an instruction with a
              `goto` and/or `extra_gotos`

            • catch handlers (future)
        """

        leaders: set[int] = {
            results[0].opcode.address,
        }

        for index, result in enumerate(results):

            has_targets = result.goto is not None or bool(result.extra_gotos)

            if result.goto is not None:
                leaders.add(result.goto)

            for extra_target in result.extra_gotos:
                leaders.add(extra_target)

            #
            # instruction after a jump (single- or multi-target)
            #
            if has_targets and index + 1 < len(results):
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
