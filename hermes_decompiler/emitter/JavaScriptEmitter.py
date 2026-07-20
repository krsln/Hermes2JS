from __future__ import annotations

from hermes_decompiler.analysis.visitors.RegionVisitor import RegionVisitor
from hermes_decompiler.analysis.regions.SequenceRegion import SequenceRegion
from hermes_decompiler.analysis.regions.IfRegion import IfRegion
from hermes_decompiler.analysis.regions.LoopRegion import LoopRegion
from hermes_decompiler.analysis.regions.TryRegion import TryRegion


class JavaScriptEmitter(RegionVisitor):
    """
    Emits clean, properly indented JavaScript from the structured Region tree.
    Supports if, loop, try, sequence regions with automatic indentation.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._lines: list[str] = []
        self._indent_level: int = 0

    def emit(self, region) -> list[str]:
        """Main entry point for code generation."""
        self._lines.clear()
        self._indent_level = 1  # function body starts at indent 1
        region.accept(self)
        return self._lines

    def _write(self, line: str) -> None:
        """Write line with current indentation."""
        indent = "    " * self._indent_level
        self._lines.append(f"{indent}{line}")

    # ==================== Visitor Implementations ====================

    def visit_sequence(self, region: SequenceRegion) -> None:
        """Emit sequence of blocks or nested regions."""
        for item in region.blocks:
            if hasattr(item, 'accept') and callable(item.accept):  # sub-region
                item.accept(self)
            else:
                # BasicBlock
                self._emit_block(item)

    def visit_if(self, region: IfRegion) -> None:
        """Clean if emission."""
        self._write(f"if ({region.condition}) {{")
        self._indent_level += 1
        region.then_region.accept(self)
        self._indent_level -= 1
        if region.else_region:
            self._write("} else {")
            self._indent_level += 1
            region.else_region.accept(self)
            self._indent_level -= 1
        self._write("}")

    def visit_loop(self, region: LoopRegion) -> None:
        """Emit while / for loop (can be refined)."""
        cond = region.condition or "true /* loop condition */"
        self._write(f"while ({cond}) {{")
        self._indent_level += 1
        region.body.accept(self)
        self._indent_level -= 1
        self._write("}")

    def visit_try(self, region: TryRegion) -> None:
        """Emit try/catch/finally."""
        self._write("try {")
        self._indent_level += 1
        region.try_region.accept(self)
        self._indent_level -= 1

        if region.catch_region:
            self._write("} catch (e) {")
            self._indent_level += 1
            region.catch_region.accept(self)
            self._indent_level -= 1

        if region.finally_region:
            self._write("} finally {")
            self._indent_level += 1
            region.finally_region.accept(self)
            self._indent_level -= 1

        self._write("}")

    def _emit_block(self, block) -> None:
        for result in block.instructions:
            if result.handler in ("JmpTrue", "JmpFalse", "JmpTrueLong"):
                continue  # condition already handled in IfRegion

            if self.verbose:
                bytecode = result.opcode.bytecode
                original_bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

                self._write(f"// CODE → {original_bytecode}")

            self._write(result.result)