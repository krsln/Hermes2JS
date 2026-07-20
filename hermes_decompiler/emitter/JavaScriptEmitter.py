from __future__ import annotations

from hermes_decompiler.regions.RegionVisitor import RegionVisitor


class JavaScriptEmitter(RegionVisitor):

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.lines: list[str] = []
        self.indent = 0

    def emit(self, region):
        region.accept(self)
        return self.lines

    def visit_sequence(self, region):

        for block in region.blocks:

            if self.verbose:
                self.lines.append(
                    f"// BasicBlock {block.start_addr}"
                )

            for instruction in block.instructions:
                self.lines.append(
                    "    " * self.indent +
                    instruction.result
                )

    def visit_if(self, region):
        raise NotImplementedError

    def visit_loop(self, region):
        raise NotImplementedError

    def visit_try(self, region):
        raise NotImplementedError
