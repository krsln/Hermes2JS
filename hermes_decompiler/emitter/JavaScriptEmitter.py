from hermes_decompiler.regions.SequenceRegion import SequenceRegion


class JavaScriptEmitter:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._lines: list[str] = []

    def emit(self, region) -> list[str]:
        region.accept(self)
        return self._lines

    def visit_sequence(self, region):
        for block in region.blocks:
            self._emit_block(block)

    def visit_if(self, region):
        self.write(
            f"if ({region.condition}) {{"
        )

        region.then_region.accept(self)

        self.write("}")

    def _emit_block(self, block):

        for result in block.instructions:
            self._emit_result(result)

    def _emit_result(self, result):

        self.write(result.result)

    def write(self, line: str):

        self._lines.append(line)
