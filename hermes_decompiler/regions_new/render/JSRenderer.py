from __future__ import annotations

from hermes_decompiler.regions_new.models.Regions import InstructionRegion, LoopRegion, SequenceRegion, IfRegion


class JSRenderer:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def render(self, root):
        output = []

        self._render(root, output, 1)

        return output

    def _render(self, region, output, indent):

        if isinstance(region, SequenceRegion):
            self._render_sequence(region, output, indent)

        elif isinstance(region, IfRegion):
            self._render_if(region, output, indent)

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

    def _render_if(self, region, output, indent):

        output.append(
            "    " * indent +
            f"if ({region.condition}) {{"
        )

        self._render(
            region.true_region,
            output,
            indent + 1
        )

        output.append(
            "    " * indent +
            "}"
        )

    def _render_instruction(self, region, output, indent):
        block = region.block

        if self.verbose:
            output.append(f"{'    ' * indent}// Block {block.id}")

        for result in block.instructions:
            line = result.result.strip()

            if result.result:
                output.append(("    " * indent) + line)

    def _render_loop(self, region, output, indent):
        if self.verbose:
            output.append(f"{'    ' * indent}// Loop (header={region.loop.header.id})")

        # Body'yi render et
        for child in region.children:
            self._render(child, output, indent + 1)

        if self.verbose:
            output.append(f"{'    ' * indent}// EndLoop")
