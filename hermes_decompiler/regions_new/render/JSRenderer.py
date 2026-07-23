from __future__ import annotations

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion, Region, LoopKind,
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
        # self.dump(root)

        output = []
        self._render_region(root, output, 1)
        return output

    def _render_region(self, region, output, indent):

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

    def _render_sequence(self, region, output, indent):
        current_block = None

        for item in region.items:
            if isinstance(item, Region):
                self._render_region(item, output, indent)
            else:
                if self.verbose and hasattr(item, "block") and item.block is not current_block:
                    current_block = item.block
                    output.append(f"{'    ' * indent}// ──────────────── Block {current_block.id} ──────────────── ")

                self._render_statement(item, output, indent)

    def _render_loop(self, region: LoopRegion, output, indent):
        prefix = "    " * indent

        kind = region.loop_kind
        if self.verbose:
            output.append(f"{prefix}// LOOP → START ({kind.value if kind else "unknown"})")

        if kind == LoopKind.WHILE:
            cond = region.condition or "true"
            output.append(f"{prefix}while ({cond}) {{")

        elif kind == LoopKind.DO_WHILE:
            output.append(f"{prefix}do {{")

        self._render_region(region.body, output, indent + 1)

        output.append(f"{prefix}}}")
        output.append(f"{prefix}// LOOP → END")

    def _render_if(self, region: IfRegion, output, indent):
        prefix = "    " * indent

        output.append(prefix + f"if ({region.condition}) {{")
        self._render_region(region.then_body, output, indent + 1)

        if region.else_body:
            output.append(prefix + "} else {")
            self._render_region(region.else_body, output, indent + 1)

        output.append(prefix + "}")

    def _render_statement(self, stmt, output, indent):
        prefix = "    " * indent

        if isinstance(stmt, InstructionStatement):
            if self.verbose:
                bytecode = stmt.result.opcode.bytecode
                bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()
                output.append(prefix + f"// CODE → {bytecode}")
            if stmt.result.variable.used:
                if self.verbose:
                    output.append(prefix + f"// USED → {stmt.result.result}")
            else:
                output.append(prefix + stmt.result.result)

        elif isinstance(stmt, ReturnStatement):
            if stmt.value is None:
                output.append(prefix + "return;")
            else:
                output.append(prefix + f"return {stmt.value};")

        elif isinstance(stmt, ThrowStatement):
            output.append(prefix + f"throw {stmt.value};")

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
            output.append(prefix + f"goto label_{stmt.target};")

        elif isinstance(stmt, IfGotoStatement):
            output.append(prefix + f"if ({stmt.condition}) goto label_{stmt.target};")

        else:
            print(f"Unsupported statement: {type(stmt).__name__}")
            # raise TypeError(
            #     f"Unsupported statement: {type(stmt).__name__}"
            # )

    def dump(self, region, indent=0):
        print(
            " " * indent,
            type(region).__name__,
            "children=",
            len(getattr(region, "children", [])),
            "statements=",
            len(getattr(region, "statements", []))
        )

        for child in getattr(region, "children", []):
            self.dump(child, indent + 4)
