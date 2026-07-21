from __future__ import annotations

from hermes_decompiler.regions.model.LoopRegion import LoopKind
from hermes_decompiler.regions.model.GotoRegion import ControlTransferKind
from hermes_decompiler.regions.visitor.RegionVisitor import RegionVisitor

# Handlers that were consumed structurally - they became the condition
# of an IfRegion/IfElseRegion/LoopRegion, or were absorbed into an
# ordinary fallthrough edge - during CFG/region construction. Their raw
# `goto label_X;` / `if (...) { /* jump ... */ }` text must NOT be
# re-emitted here, or the control flow they represent would appear
# twice: once as the structured if/while, and once as leftover text.
#
# Kept as a set literal (mirroring ControlFlowGraphBuilder's handler
# lists) rather than importing from handlers/Jump/Jmp.py, to avoid a
# dependency from emitter -> handlers. If this drifts out of sync with
# Jmp.py's handler classes, structured jumps will "leak" through as
# extra lines - grep for `/* jump to` in generated output as a signal.
_STRUCTURAL_JUMP_HANDLERS = {
    "Jmp", "JmpLong",
    "JmpTrue", "JmpTrueLong",
    "JmpFalse", "JmpFalseLong",
    "JmpUndefined", "JmpUndefinedLong",
    "JmpBuiltinIs", "JmpBuiltinIsLong",
    "JmpBuiltinIsNot", "JmpBuiltinIsNotLong",
    "JmpTypeOfIs",
}


class JavaScriptEmitter(RegionVisitor):
    """
    Renders a Region tree into indented JavaScript source lines.

    Indentation is a depth counter pushed/popped around each nested
    region visit rather than a flat counter mutated by manual
    open/close bookkeeping (as the old generate_js_OLD did) - every
    visit_* method is responsible only for its own region's lines, so
    nesting is correct "for free" instead of needing hand-matched
    indent_lvl +=/-= 1 pairs scattered through a single loop.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._lines: list[str] = []
        self._depth = 1
        self._return_points: set[int] = set()

    def emit(self, region) -> list[str]:
        region.accept(self)
        return self._lines

    # ------------------------------------------------------------
    # RegionVisitor implementation
    # ------------------------------------------------------------

    def visit_block(self, region):
        for result in region.block.instructions:
            self._emit_instruction(result)

    def visit_sequence(self, region):
        for child in region.regions:
            child.accept(self)

    def visit_if(self, region):
        self._write(f"if ({region.condition}) {{")
        self._nested(region.then_region)
        self._write("}")

    def visit_if_else(self, region):
        self._write(f"if ({region.condition}) {{")
        self._nested(region.then_region)
        self._write("} else {")
        self._nested(region.else_region)
        self._write("}")

    def visit_loop(self, region):

        if region.kind is LoopKind.WHILE:
            self._write(f"while ({region.condition}) {{")
            self._nested(region.body)
            self._write("}")

        elif region.kind is LoopKind.DO_WHILE:
            self._write("do {")
            self._nested(region.body)
            self._write(f"}} while ({region.condition});")

        else:  # LoopKind.INFINITE
            self._write("while (true) {")
            self._nested(region.body)
            self._write("}")

    def visit_try(self, region):

        self._write("try {")
        self._nested(region.try_region)

        if region.catch_region is not None:
            name = region.exception_name or "e"
            self._write(f"}} catch ({name}) {{")
            self._nested(region.catch_region)

        if region.finally_region is not None:
            self._write("} finally {")
            self._nested(region.finally_region)

        self._write("}")

    def visit_goto(self, region):
        if region.kind is ControlTransferKind.BREAK:
            self._write("break;")
        elif region.kind is ControlTransferKind.CONTINUE:
            self._write("continue;")
        else:
            self._write(f"goto {region.label};  // unstructured control flow, needs review")

    # ------------------------------------------------------------
    # Instruction-level emission (ported from generate_js_OLD, adapted
    # to write into the current region's indent depth instead of a
    # hand-tracked indent_lvl)
    # ------------------------------------------------------------

    def _emit_instruction(self, result):

        variable = result.variable
        handler = variable.handler

        if handler == "CompleteGenerator":
            return

        if handler in _STRUCTURAL_JUMP_HANDLERS:
            # Already represented by the enclosing IfRegion/IfElseRegion
            # /LoopRegion/fallthrough - emitting it again would
            # duplicate the control flow as text.
            if self.verbose:
                self._write(f"// CODE → {self._original_bytecode(result)}")
            return

        if self.verbose:
            self._write(f"// CODE → {self._original_bytecode(result)}")

        if handler == "SaveGenerator":
            self._write(f"// await yield; // Resume at label_{result.goto}")
            return

        if handler == "ResumeGenerator":
            self._write(f"{result.result}; // Resume generator")
            return

        if handler == "Ret":
            if variable.address in self._return_points:
                return
            self._return_points.add(variable.address)
            self._write(variable.value)
            return

        if variable.used:
            if self.verbose:
                self._write(f"// USED → {result.result}")
            return

        self._write(result.result)

    @staticmethod
    def _original_bytecode(result) -> str:
        bytecode = result.opcode.bytecode
        return bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

    # ------------------------------------------------------------

    def _nested(self, region):
        self._depth += 1
        region.accept(self)
        self._depth -= 1

    def _write(self, line: str):
        self._lines.append(("    " * self._depth) + line)
