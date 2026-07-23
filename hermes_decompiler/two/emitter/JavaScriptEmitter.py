from __future__ import annotations

from hermes_decompiler.two.regions.model.BlockRegion import BlockRegion
from hermes_decompiler.two.regions.model.SequenceRegion import SequenceRegion
from hermes_decompiler.two.regions.model.IfRegion import IfRegion
from hermes_decompiler.two.regions.model.IfElseRegion import IfElseRegion
from hermes_decompiler.two.regions.model.LoopRegion import LoopKind, LoopRegion
from hermes_decompiler.two.regions.model.TryRegion import TryRegion
from hermes_decompiler.two.regions.model.GotoRegion import ControlTransferKind, GotoRegion
from hermes_decompiler.two.regions.visitor.RegionVisitor import RegionVisitor

# Handlers that were consumed structurally - they became the condition
# of an IfRegion/IfElseRegion/LoopRegion, or were absorbed into an
# ordinary fallthrough edge - during CFG/region construction. Their raw
# `goto label_X;` / `if (...) { /* jump ... */ }` text must NOT be
# re-emitted here, or the control flow they represent would appear
# twice: once as the structured if/while, and once as leftover text.
# BUG FIX (was): missing the handlers/Jump/JCompare.py family
# (JEqual/JNotEqual/JStrictEqual/JStrictNotEqual/JLess*/JGreater*/...).
# Kept in sync with ControlFlowGraphBuilder._CONDITIONAL_HANDLERS -
# see that set's comment for the full story. Without this, a
# JCompare-family conditional that ControlFlowGraphBuilder now
# correctly recognizes as an if-header still leaked its raw
# "if (lhs OP rhs) { /* jump to label_X */ }" instruction text into
# the output a second time, on top of the properly structured
# IfRegion/IfElseRegion/LoopRegion condition built from it.
_STRUCTURAL_JUMP_HANDLERS = {
    "Jmp", "JmpLong",
    "JmpTrue", "JmpTrueLong",
    "JmpFalse", "JmpFalseLong",
    "JmpUndefined", "JmpUndefinedLong",
    "JmpBuiltinIs", "JmpBuiltinIsLong",
    "JmpBuiltinIsNot", "JmpBuiltinIsNotLong",
    "JmpTypeOfIs",
    "JEqual", "JEqualLong", "JNotEqual", "JNotEqualLong",
    "JStrictEqual", "JStrictEqualLong", "JStrictNotEqual", "JStrictNotEqualLong",
    "JLess", "JLessLong", "JLessN", "JLessNLong",
    "JLessEqual", "JLessEqualLong", "JLessEqualN",
    "JNotLess", "JNotLessLong", "JNotLessN", "JNotLessNLong",
    "JNotLessEqual", "JNotLessEqualLong", "JNotLessEqualN", "JNotLessEqualNLong",
    "JGreater", "JGreaterLong", "JGreaterN", "JGreaterNLong",
    "JGreaterEqual", "JGreaterEqualLong", "JGreaterEqualN", "JGreaterEqualNLong",
    "JNotGreater", "JNotGreaterLong", "JNotGreaterN", "JNotGreaterNLong",
    "JNotGreaterEqual", "JNotGreaterEqualLong", "JNotGreaterEqualN", "JNotGreaterEqualNLong",
}


class JavaScriptEmitter(RegionVisitor):
    """
    Renders a Region tree into indented JavaScript source lines.

    RECURSION NOTE: `emit()` walks the Region tree using an explicit
    work-stack (`_dispatch`), not Python call recursion. The Region
    tree's nesting depth is proportional to how many sequential
    if/else guards a function has - exactly the pattern generator/
    async state-machine bytecode produces in long chains for large
    functions - so a naive `region.accept(self)` -> `visit_if_else` ->
    `self._nested(region.else_region)` -> `region.accept(self)` -> ...
    recursive chain hits Python's recursion limit on real production
    .hbc input (confirmed: this was the third of three independent
    recursion sites found via the same root cause, alongside
    `cfg.analysis.ReversePostOrder` and
    `regions.building._StructuralAnalyzer`).

    The `visit_*` methods below (required by the `RegionVisitor` ABC)
    are kept for interface compatibility and are safe to call directly
    for a SINGLE level of manual dispatch - but they still recurse via
    `_nested`/`.accept()` if called on a deeply nested tree directly.
    Only `emit()` is guaranteed recursion-safe for arbitrary depth;
    always prefer it over calling `.accept()` on a Region yourself.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._lines: list[str] = []
        self._depth = 1
        self._return_points: set[int] = set()

    def emit(self, region) -> list[str]:
        """
        Recursion-safe entry point. Walks `region` depth-first using
        an explicit `work` stack of (op, payload) instructions instead
        of Python call recursion:

          ("visit", region)  - dispatch on `region`'s type, which for
                                composite regions (if/else/loop/try/
                                sequence) pushes the operations that a
                                recursive visit would have performed,
                                in reverse order (so the first one ends
                                up on top of the stack and is executed
                                - i.e. popped - first).
          ("line", text)     - append one indented output line.
          ("depth", delta)   - adjust the current indent depth by
                                delta (+1 entering a block, -1 leaving
                                it) - replaces the old `_nested()`
                                push/pop-around-a-Python-call pattern.

        Because a composite region's own `_dispatch` call pushes its
        children's work *after* (i.e. on top of) the closing-brace/
        depth-pop instructions already queued for itself, children are
        always fully processed before their parent's remaining
        instructions run - reproducing exactly the ordering a
        recursive descent would give, without ever growing the Python
        call stack past a small constant number of frames regardless
        of how deeply the Region tree is nested.
        """

        work: list[tuple[str, object]] = [("visit", region)]

        while work:
            op, payload = work.pop()

            if op == "line":
                self._write(payload)  # type: ignore[arg-type]
            elif op == "depth":
                self._depth += payload  # type: ignore[operator]
            elif op == "visit":
                self._dispatch(payload, work)
            else:
                raise ValueError(f"JavaScriptEmitter: unknown work op {op!r}")

        return self._lines

    def _dispatch(self, region, work: list) -> None:
        """
        Push (or directly perform, for leaves) the operations needed
        to render `region`, using the "build a forward-order op list,
        then push it reversed" pattern so each region type reads in
        the same top-to-bottom order it will actually execute in.
        """

        if isinstance(region, BlockRegion):
            for result in region.block.instructions:
                self._emit_instruction(result)
            return

        if isinstance(region, SequenceRegion):
            work.extend(("visit", child) for child in reversed(region.regions))
            return

        if isinstance(region, IfRegion):
            ops = [
                ("line", f"if ({region.condition}) {{"),
                ("depth", 1),
                ("visit", region.then_region),
                ("depth", -1),
                ("line", "}"),
            ]
            work.extend(reversed(ops))
            return

        if isinstance(region, IfElseRegion):
            ops = [
                ("line", f"if ({region.condition}) {{"),
                ("depth", 1),
                ("visit", region.then_region),
                ("depth", -1),
                ("line", "} else {"),
                ("depth", 1),
                ("visit", region.else_region),
                ("depth", -1),
                ("line", "}"),
            ]
            work.extend(reversed(ops))
            return

        if isinstance(region, LoopRegion):
            if region.kind is LoopKind.WHILE:
                ops = [
                    ("line", f"while ({region.condition}) {{"),
                    ("depth", 1),
                    ("visit", region.body),
                    ("depth", -1),
                    ("line", "}"),
                ]
            elif region.kind is LoopKind.DO_WHILE:
                ops = [
                    ("line", "do {"),
                    ("depth", 1),
                    ("visit", region.body),
                    ("depth", -1),
                    ("line", f"}} while ({region.condition});"),
                ]
            else:  # LoopKind.INFINITE
                ops = [
                    ("line", "while (true) {"),
                    ("depth", 1),
                    ("visit", region.body),
                    ("depth", -1),
                    ("line", "}"),
                ]
            work.extend(reversed(ops))
            return

        if isinstance(region, TryRegion):
            ops: list[tuple[str, object]] = [
                ("line", "try {"),
                ("depth", 1),
                ("visit", region.try_region),
                ("depth", -1),
            ]

            if region.catch_region is not None:
                name = region.exception_name or "e"
                ops += [
                    ("line", f"}} catch ({name}) {{"),
                    ("depth", 1),
                    ("visit", region.catch_region),
                    ("depth", -1),
                ]

            if region.finally_region is not None:
                ops += [
                    ("line", "} finally {"),
                    ("depth", 1),
                    ("visit", region.finally_region),
                    ("depth", -1),
                ]

            ops.append(("line", "}"))
            work.extend(reversed(ops))
            return

        if isinstance(region, GotoRegion):
            self._emit_goto(region)
            return

        raise TypeError(f"JavaScriptEmitter: unknown region type {type(region).__name__}")

    # ------------------------------------------------------------
    # RegionVisitor implementation
    #
    # Kept for interface compatibility / single-level manual dispatch.
    # NOT recursion-safe for deep trees when called via `.accept()` -
    # use `emit()` instead. Implemented in terms of `_nested()`, which
    # still uses a real Python call for `region.accept(self)`.
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
        self._emit_goto(region)

    def _emit_goto(self, region):
        if region.kind is ControlTransferKind.BREAK:
            self._write("break;")
        elif region.kind is ControlTransferKind.CONTINUE:
            self._write("continue;")
        else:
            self._write(f"goto {region.label};  // unstructured control flow, needs review")

    # ------------------------------------------------------------
    # Instruction-level emission (ported from generate_js_OLD, adapted
    # to write into the current region's indent depth)
    # ------------------------------------------------------------

    def _emit_instruction(self, result):

        variable = result.variable
        handler = variable.handler

        if handler == "CompleteGenerator":
            self._verbose_code(result)
            return

        if handler in _STRUCTURAL_JUMP_HANDLERS:
            # Already represented by the enclosing IfRegion/IfElseRegion
            # /LoopRegion/fallthrough - emitting it again would
            # duplicate the control flow as text.
            self._verbose_code(result)
            return

        self._verbose_code(result)

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
                self._write(f"// USED -> {result.result}")
            return

        self._write(result.result)

    @staticmethod
    def _original_bytecode(result) -> str:
        bytecode = result.opcode.bytecode
        return bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

    # ------------------------------------------------------------

    def _verbose_code(self, result):
        if self.verbose:
            self._write(f"// CODE -> {self._original_bytecode(result)}")

    def _nested(self, region):
        """
        Only used by the `visit_*` compatibility methods above (which
        are themselves recursive) - NOT used by `emit()`'s iterative
        `_dispatch` path, which manages depth via ("depth", delta)
        work items instead.
        """
        self._depth += 1
        region.accept(self)
        self._depth -= 1

    def _write(self, line: str):
        self._lines.append(("    " * self._depth) + line)