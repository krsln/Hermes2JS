from __future__ import annotations

from hermes_decompiler.regions_new.models.InstructionRegion import InstructionRegion
from hermes_decompiler.regions_new.models.LoopRegion import LoopRegion
from hermes_decompiler.regions_new.models.SequenceRegion import SequenceRegion


class JSRenderer:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def render(self, root):
        output = []

        self._render(root, output, 0)

        return output

    def _render(self, region, output, indent):

        if isinstance(region, SequenceRegion):
            self._render_sequence(region, output, indent)

        elif isinstance(region, InstructionRegion):
            self._render_instruction(region, output, indent)

        elif isinstance(region, LoopRegion):
            self._render_loop(region, output, indent)

        else:
            raise TypeError(
                f"Unsupported region: {type(region).__name__}"
            )

    def _render_sequence(self, region, output, indent):

        for child in region.children:
            self._render(child, output, indent)

    def _render_instruction(self, region, output, indent):

        block = region.block

        if self.verbose:
            output.append(f"{'    ' * indent}// Block {block.id}")

        for result in block.instructions:

            if result.result:
                output.append(
                    ("    " * indent) + result.result
                )

    def _render_loop(self, region, output, indent):

        if self.verbose:
            output.append(f"{'    ' * indent}// Loop")

        for child in region.children:
            self._render(child, output, indent + 1)

        if self.verbose:
            output.append(f"{'    ' * indent}// EndLoop")