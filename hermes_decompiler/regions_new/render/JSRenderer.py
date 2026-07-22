from __future__ import annotations

from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
)

from hermes_decompiler.regions_new.models.Statements import (
    InstructionStatement,
    ReturnStatement,
    ThrowStatement,
    BreakStatement,
    ContinueStatement,
    GotoStatement,
    IfGotoStatement,
)


class JSRenderer:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    # ---------------------------------------------------------

    def render(self, root):

        output = []

        self._render_region(root, output, 1)

        return output

    # ---------------------------------------------------------

    def _render_region(
            self,
            region,
            output,
            indent,
    ):
        if isinstance(region, SequenceRegion):
            self._render_sequence(region, output, indent)

        elif isinstance(region, LoopRegion):
            self._render_loop(region, output, indent)

        elif isinstance(region, IfRegion):
            self._render_if(region, output, indent)

        else:
            print(f"Unsupported region: {type(region).__name__}")
            # raise TypeError(
            #     f"Unsupported region: {type(region).__name__}"
            # )

    # ---------------------------------------------------------

    def _render_sequence(self, region, output, indent):

        current_block = None

        for stmt in region.statements:

            if (
                    self.verbose
                    and hasattr(stmt, "block")
                    and stmt.block is not current_block
            ):
                current_block = stmt.block
                output.append(
                    f"{'    ' * indent}// Block {current_block.id}"
                )

            self._render_statement(stmt, output, indent)

        for child in region.children:
            self._render_region(child, output, indent)

    # ---------------------------------------------------------

    def _render_loop(
            self,
            region: LoopRegion,
            output,
            indent,
    ):

        if self.verbose:

            if region.loop_kind:
                kind = region.loop_kind

                if hasattr(kind, "value"):
                    kind = kind.value

                if kind is None:
                    kind = "loop"

                output.append(f"{'    ' * indent}// Loop ({kind})")

            else:

                output.append(
                    f"{'    ' * indent}// Loop"
                )

        self._render_region(
            region.body,
            output,
            indent + 1,
        )

        if self.verbose:
            output.append(
                f"{'    ' * indent}// EndLoop"
            )

    # ---------------------------------------------------------

    def _render_if(
            self,
            region: IfRegion,
            output,
            indent,
    ):

        output.append(
            ("    " * indent)
            + f"if ({region.condition}) {{"
        )

        self._render_region(
            region.then_body,
            output,
            indent + 1,
        )

        if region.else_body:
            output.append(
                ("    " * indent)
                + "} else {"
            )

            self._render_region(
                region.else_body,
                output,
                indent + 1,
            )

        output.append(
            ("    " * indent)
            + "}"
        )

    # ---------------------------------------------------------

    def _render_statement(
            self,
            stmt,
            output,
            indent,
    ):

        prefix = "    " * indent

        if isinstance(stmt, InstructionStatement):

            output.append(
                prefix + stmt.result.result
            )

        elif isinstance(stmt, ReturnStatement):

            if stmt.value is None:

                output.append(prefix + "return;")

            else:

                output.append(
                    prefix + f"return {stmt.value};"
                )

        elif isinstance(stmt, ThrowStatement):

            output.append(
                prefix + f"throw {stmt.value};"
            )

        elif isinstance(stmt, BreakStatement):

            output.append(prefix + "break;")

        elif isinstance(stmt, ContinueStatement):

            output.append(prefix + "continue;")

        elif isinstance(stmt, GotoStatement):

            #
            # Goto'lar geçici.
            # Break/Continue analizinden sonra
            # büyük çoğunluğu kaybolacak.
            #

            output.append(
                prefix
                + f"goto label_{stmt.target};"
            )

        elif isinstance(stmt, IfGotoStatement):

            output.append(
                prefix
                + f"if ({stmt.condition}) goto label_{stmt.target};"
            )

        else:
            print(f"Unsupported statement: {type(stmt).__name__}")
            # raise TypeError(
            #     f"Unsupported statement: {type(stmt).__name__}"
            # )
