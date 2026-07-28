from __future__ import annotations

import warnings

from hermes_decompiler.ir import Expression, Statement
from hermes_decompiler.analysis.regions import (
    SequenceRegion, LoopRegion, IfRegion, Region, LoopKind, InstructionState, TryRegion
)
from .Printer import Printer
from ..analysis.terminators import Terminator


class JSEmitter:
    """
    Emits JavaScript from a structured SequenceRegion.

    The graph is assumed to be fully structured
    (loops, ifs, try/catch, switch, ...).

    No control-flow analysis is performed here.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.printer = Printer(verbose=verbose)

    def emit(self, root: SequenceRegion) -> list[str]:
        return self.print_region(root)
        # return self.printer.print_region(root)


    # ---------------------------------------------------------

    def print_region(self, root):
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

        elif isinstance(region, TryRegion):
            self._render_try(region, output, indent)

        else:
            print(f"Unsupported region: {type(region).__name__}")

    def _render_try(self, region, output, indent):
        prefix = "    " * indent

        output.append(prefix + "try {")
        self._render_region(region.try_body, output, indent + 1)
        output.append(prefix + "}")

        if region.catch:
            param = region.catch.exception or "e"
            output.append(prefix + f"catch ({param}) {{")
            self._render_region(region.catch.body, output, indent + 1)
            output.append(prefix + "}")

        if region.finally_:
            output.append(prefix + "finally {")
            self._render_region(region.finally_.body, output, indent + 1)
            output.append(prefix + "}")

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

        condition = self.printer.print_expression(region.condition) if region.condition is not None else ""

        output.append(prefix + f"if ({condition}) {{")
        self._render_region(region.then_body, output, indent + 1)

        if region.else_body:
            output.append(prefix + "} else {")
            self._render_region(region.else_body, output, indent + 1)

        output.append(prefix + "}")

    def _render_statement(self, stmt, output, indent):
        prefix = "    " * indent

        if isinstance(stmt, InstructionState):
            self._render_instruction(stmt, output, indent)
            return

        print(f"Unsupported statement: {type(stmt).__name__}")
        # raise TypeError(
        #     f"Unsupported statement: {type(stmt).__name__}"
        # )

    def _render_instruction(self, stmt: InstructionState, output, indent):
        prefix = "    " * indent
        result = stmt.result

        if self.verbose:
            bytecode = result.opcode.bytecode
            bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()
            output.append(prefix + f"// CODE → {bytecode}")

        if result.used:
            if self.verbose:
                output.append(prefix + f"// USED → {self._render_value(result)}")
            return

        output.append(prefix + self._render_value(result))

    def _render_value(self, result) -> str:
        """
        Renders one instruction's result line via the IR printer.

        Priority:
            1. `result.statement` - the opcode IS a statement/terminator
               (e.g. Throw, Ret). Printed as-is.
            2. `result.value` as a proper IR `Expression` - printed as
               an assignment (`dest = expr;`), or as a bare expression
               statement when there's no destination register.
            3. Legacy string fallback for handlers not yet migrated to
               the `ir` package, so unmigrated opcodes keep rendering
               instead of crashing during the transition.
        """

        if isinstance(result.statement, Statement):
            return self.printer.print_statement(result.statement)
        if isinstance(result.terminator, Terminator):
            return self.printer.print_terminator(result.terminator)

        if isinstance(result.value, Expression):
            rendered = self.printer.print_expression(result.value)

            if result.name:
                return f"{result.name} = {rendered};"

            return f"{rendered};"

        warnings.warn(
            f"Handler produced a non-IR result: {type(result.result).__name__}. "
            "Every opcode handler should now produce IR nodes.",
            stacklevel=2,
        )

        return ""

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
