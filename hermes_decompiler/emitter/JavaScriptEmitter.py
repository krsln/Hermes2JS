from hermes_decompiler.regions.SequenceRegion import SequenceRegion


class JavaScriptEmitter:

    def __init__(self):
        self._lines: list[str] = []

    def emit(self, region) -> list[str]:
        region.accept(self)
        return self._lines

    def visit_sequence(
        self,
        region: SequenceRegion,
    ) -> None:

        for block in region.blocks:

            self._lines.append(
                f"// BasicBlock {block.start_addr}"
            )

            for instruction in block.instructions:
                self._lines.append(
                    instruction.result
                )