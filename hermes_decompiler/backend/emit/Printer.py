from __future__ import annotations

import dataclasses
import json
from contextlib import contextmanager

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import (
    SequenceRegion,
    LoopKind,
    LoopRegion,
    IfRegion,
    TryRegion,
    SwitchRegion,
    Region,
)
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import NodeVisitor
from hermes_decompiler.ir import (
    precedence,
)
from hermes_decompiler.ir.expressions import (
    Identifier,
    ParenthesizedExpression,
    NumericLiteral,
    BigIntLiteral,
    StringLiteral,
    BooleanLiteral,
    NullLiteral,
    UndefinedLiteral,
    RegExpLiteral,
    TemplateLiteral,
    UnaryExpression,
    UpdateExpression,
    BinaryExpression,
    AssignmentExpression,
    ConditionalExpression,
    SequenceExpression,
    MemberExpression,
    CallExpression,
    NewExpression,
    SpreadElement,
    ArrayExpression,
    ObjectExpression,
    ObjectProperty,
    PropertyKind,
    FunctionExpression,
    ArrowFunctionExpression,
    AwaitExpression,
    YieldExpression,
    RawExpression,
)
from hermes_decompiler.ir.statements import (

    BlockStatement,
    EmptyStatement,
    ExpressionStatement,
    VariableDeclaration,
    IfStatement,
    ReturnStatement,
    DebuggerStatement,
    LabeledStatement,
    BreakStatement,
    ContinueStatement,
    ThrowStatement,
)

__all__ = [
    "Printer",
]

logger = get_logger(__name__)


class Printer(NodeVisitor):
    """
    Converts the structured RegionGraph into JavaScript source.

    Assumptions
    -----------

    * CFG construction is complete.
    * Structural analysis is complete.
    * Every control-flow construct is represented by a Region.
    * BasicBlocks contain only ordinary IR statements.
    * Block terminators have already been consumed by the structurers.

    Pretty-printing improvements
    ----------------------------
    * `else if` chains are emitted as a flat cascade instead of nested
      `else { if … }`.
    * Verbose block / bytecode comments appear only when `verbose=True`.
    * Dead register assignments (`rN = call(…)`) are omitted when the
      definition is unused.
    * A `LoopRegion` with `.label` set (see `LoopLabeledExitStructurer`
      - assigned only when some `break`/`continue` inside it, or
      inside a loop nested inside it, needs to target it by name)
      gets an explicit `label:` line immediately before it.
    """

    INDENT = "    "

    def __init__(self, *, verbose: bool = False):
        self.verbose = verbose
        self._indent = 0

    @contextmanager
    def _indented(self):
        self._indent += 1
        try:
            yield
        finally:
            self._indent -= 1

    # ---------------------------------------------------------
    # public
    # ---------------------------------------------------------

    def print_region(self, region) -> list[str]:

        self._indent = 1

        lines: list[str] = []

        self._emit_region(region, lines)

        return lines

    # ---------------------------------------------------------
    # dispatcher
    # ---------------------------------------------------------

    def _emit_region(
            self,
            region: Region | SequenceRegion | LoopRegion | IfRegion | TryRegion | SwitchRegion | BasicBlock,
            lines: list[str]
    ) -> None:
        match region:

            case SequenceRegion():
                self._emit_sequence(region, lines)

            case LoopRegion():
                self._emit_loop(region, lines)

            case IfRegion():
                self._emit_if(region, lines)

            case TryRegion():
                self._emit_try(region, lines)

            case SwitchRegion():
                self._emit_switch(region, lines)

            case BasicBlock():
                self._emit_block(region, lines)

            case _:
                raise TypeError(type(region))

    # ---------------------------------------------------------
    # shared condition-readability annotation
    # ---------------------------------------------------------

    def _emit_condition_comment(
            self,
            condition,
            lines: list[str],
            *,
            source_block: BasicBlock | None,
            before_index: int | None = None,
    ) -> None:
        """
        Single shared readability aid for every place a structured or
        unstructured CONDITION can still carry bare `rN` operands that
        were deliberately left symbolic (loop-carried values resolved via
        `get_register_symbolic` - see OpcodeHandler resolver notes:
        inlining these risks a stale-value correctness bug). Restates
        each `rN`'s last known definition IN A COMMENT, purely for
        readability - never changes the rendered expression itself.

        Two distinct call shapes feed into this one method:

        - A still-unconsumed `instruction.terminator` (`_emit_block`):
          the guard instruction is still physically present in
          `source_block`, so `before_index` is that instruction's own
          index - only strictly earlier instructions in the same block
          are eligible definitions.

        - An already-consumed `region.condition` (`_emit_loop`, and
          potentially `_emit_if`/`_emit_switch`): the original guard
          instruction was popped from `source_block` once its condition
          was extracted (see `LoopConditionRegionPass._consume_guard`),
          so there's no specific index to stop at - `before_index`
          defaults to `len(source_block.instructions)`, i.e. "every
          instruction still in this block is eligible."

        `source_block=None` (or an empty/unknown block) is a silent
        no-op - some conditions (e.g. a loop with no `latches`/`header`
        resolvable, or a condition that's already a clean expression with
        no `rN` operands at all) simply have nothing local to show, which
        isn't an error.

        Deliberately local-only: no cross-block/cross-pass data-flow
        lookup, no register-state resolution. If a `rN` was defined
        outside `source_block` entirely, it's just omitted - this is a
        display convenience, not an analysis.
        """
        # if not self.verbose:
        #     return
        if condition is None or source_block is None:
            return

        names = sorted(self.__collect_register_names(condition))
        if not names:
            return

        index = len(source_block.instructions) if before_index is None else before_index

        parts = []
        for name in names:
            definition_text = self.__find_local_definition_text(source_block, index, name)
            if definition_text is not None:
                parts.append(f"{name} = {definition_text}")

        if parts:
            self._write(lines, "// → " + "; ".join(parts))

    @staticmethod
    def __collect_register_names(node) -> set[str]:
        """
        Every bare `rN` Identifier reachable inside `node`'s expression
        tree, found generically via the same field-walk shape used by
        `_repoint_node` in the region passes - no per-expression-type
        special-casing needed.
        """
        found: set[str] = set()

        def walk(n):
            if isinstance(n, Identifier):
                if n.name.startswith("r") and n.name[1:].isdigit():
                    found.add(n.name)
                return

            if not dataclasses.is_dataclass(n):
                return

            for field in dataclasses.fields(n):
                value = getattr(n, field.name)
                if dataclasses.is_dataclass(value):
                    walk(value)
                elif isinstance(value, tuple):
                    for item in value:
                        if dataclasses.is_dataclass(item):
                            walk(item)

        walk(node)
        return found

    def __find_local_definition_text(self, block: BasicBlock, before_index: int, name: str) -> str | None:
        """
        Last instruction in `block` (strictly before `before_index`) whose
        `dest_reg` matches `name`, rendered as plain text.
        """
        reg = int(name[1:])

        for earlier in reversed(block.instructions[:before_index]):
            if earlier.dest_reg == reg and earlier.value is not None:
                try:
                    return self.print_expression(earlier.value)
                except Exception:
                    return None

        return None

    # ---------------------------------------------------------
    # basic block
    # ---------------------------------------------------------

    def _emit_block(
            self,
            block: BasicBlock,
            lines: list[str],
    ):

        if self.verbose:
            self._write(lines, f"// ──────────────── Block {block.id} ──────────────── ")

        for index, instruction in enumerate(block.instructions):

            if self.verbose:
                bytecode = instruction.entry.bytecode
                bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

                self._write(lines, f"// CODE → {bytecode}")

            if instruction.statement is not None:
                rendered = self.print_statement(instruction.statement)

                self._write(lines, rendered)

                continue

            if instruction.terminator is not None:
                self._emit_condition_comment(
                    getattr(instruction.terminator, "condition", None),
                    lines,
                    source_block=block,
                    before_index=index,
                )
                rendered = self.print_terminator(instruction.terminator)

                self._write(lines, rendered)

                continue

            if instruction.value is None:
                continue

            rendered = self.print_expression(instruction.value)

            if instruction.dest_reg is not None:
                if not instruction.definition_used and rendered.startswith("globalThis.console.log"):
                    rendered = rendered.replace("globalThis.", "")
                else:
                    rendered = f"r{instruction.dest_reg} = {rendered}"

            if instruction.definition_used:
                if self.verbose:
                    self._write(lines, f"// USED → {rendered};")
            else:
                self._write(lines, rendered)

    # ---------------------------------------------------------
    # sequence
    # ---------------------------------------------------------

    def _emit_sequence(self, region: SequenceRegion, lines):

        for child in region.children:
            self._emit_region(child, lines)

    # ---------------------------------------------------------
    # if  (with else-if flattening)
    # ---------------------------------------------------------

    def _emit_if(self, region: IfRegion, lines, *, _chain: bool = False):
        """
        Emit an IfRegion.  When the else-body consists of a single
        nested IfRegion we emit a flat `else if` cascade instead of
        nested braces – matching the original source style.
        """
        cond = self.print_expression(region.condition)

        self._emit_condition_comment(
            region.condition, lines,
            source_block=self.__nearest_preceding_block(region),
        )

        if _chain:
            self._write(lines, f"}} else if ({cond}) {{")
        else:
            self._write(lines, f"if ({cond}) {{")

        with self._indented():
            self._emit_region(region.then_body, lines)

        if region.else_body is None:
            self._write(lines, "}")
            return

        # Detect classic else-if: else body is a SequenceRegion that
        # contains exactly one IfRegion (and nothing else).
        nested = self._extract_single_if(region.else_body)
        if nested is not None:
            self._emit_if(nested, lines, _chain=True)
            return

        # Ordinary else
        self._write(lines, "} else {")

        with self._indented():
            self._emit_region(region.else_body, lines)

        self._write(lines, "}")

    @staticmethod
    def __nearest_preceding_block(region: IfRegion) -> BasicBlock | None:
        """
        The nearest `BasicBlock` sibling immediately preceding `region`
        in its own parent `SequenceRegion`, if any - this is where the
        guard's operands (the `Greater`/`Less`/`JStrictEqual`/... setup
        instructions IfStructurer consumed into `region.condition`) still
        physically live, same as how `LoopConditionRegionPass._consume_guard`
        leaves everything except the branch instruction itself sitting in
        the header/latch block.

        Only ever walks LOCAL siblings within the immediate parent - never
        crosses into a grandparent `SequenceRegion` (e.g. stepping out of
        a nested `if`/`try` into whatever encloses it). A condition whose
        operands were defined further out than that has nothing reliable
        to show here anyway; returning `None` in that case is correct,
        not a bug to work around - see `_emit_condition_comment`'s own
        docstring for why this stays a local convenience rather than a
        real data-flow lookup.

        Returns `None` if:
          - `region.parent` isn't a `SequenceRegion` (shouldn't normally
            happen post-structuring, but IfRegion.parent is only ever
            actually guaranteed to exist once some structurer has run),
          - `region` isn't found in its own parent's `children` (stale
            reference after a mutation that didn't update `.parent`), or
          - no `BasicBlock` sibling precedes it (e.g. `region` is the very
            first child of its `SequenceRegion`).
        """
        parent = region.parent

        if not isinstance(parent, SequenceRegion):
            return None

        try:
            index = parent.children.index(region)
        except ValueError:
            return None

        for sibling in reversed(parent.children[:index]):
            if isinstance(sibling, BasicBlock):
                return sibling
            # A non-BasicBlock sibling (another Region) sitting directly
            # before this IfRegion means there's no flat block adjacency
            # to walk back into - stop rather than reaching past it.
            return None

        return None

    @staticmethod
    def _is_skippable_prefix(item) -> bool:
        """True for BasicBlocks that only prepare values (loads / consts)
        and have no terminator and no side-effecting statements.

        Hermes frequently leaves the constant load for the next
        comparison (`r1 = 5`) as a sibling BasicBlock in front of the
        nested IfRegion.  Those blocks must not block else-if
        flattening even when `definition_used` is still True (the
        constant is already embedded in the IfRegion condition).
        """
        if not isinstance(item, BasicBlock):
            return False
        if item.terminator is not None:
            return False
        for instr in item.instructions:
            if instr.statement is not None:
                return False
            if instr.terminator is not None:
                return False
            if instr.value is not None and isinstance(
                    instr.value,
                    (CallExpression, NewExpression, AssignmentExpression,
                     UpdateExpression, AwaitExpression, YieldExpression),
            ):
                return False
        return True

    @classmethod
    def _extract_single_if(cls, body) -> IfRegion | None:
        if isinstance(body, IfRegion):
            return body
        if not isinstance(body, SequenceRegion):
            return None
        # Allow a pure prefix (const/param loads) before the single
        # IfRegion so else-if cascades flatten correctly.
        meaningful = [c for c in body.children if not cls._is_skippable_prefix(c)]
        if len(meaningful) == 1 and isinstance(meaningful[0], IfRegion):
            return meaningful[0]
        if len(body.children) == 1 and isinstance(body.children[0], IfRegion):
            return body.children[0]
        return None

    # ---------------------------------------------------------
    # loop
    # ---------------------------------------------------------

    def _emit_loop(self, region: LoopRegion, lines):
        """
        Render an already-structured LoopRegion.

        This method deliberately does not infer loop shape from CFG.
        All loop classification and metadata recovery belongs to the
        analysis / region-pass layer.
        """

        if region.label is not None:
            self._write(lines, f"{region.label}:")

        kind = region.loop_kind

        if self.verbose:
            self._write(
                lines,
                f"// LOOP → START ({kind.value if kind else 'unknown'})"
            )

        if kind in (LoopKind.FOR_OF, LoopKind.FOR_IN):
            self._emit_for_each(region, lines)

        elif kind is LoopKind.FOR:
            self._emit_for(region, lines)

        elif kind is LoopKind.DO_WHILE:
            self._emit_do_while(region, lines)

        elif kind is LoopKind.WHILE:
            self._emit_while(region, lines)

        elif kind is LoopKind.ENDLESS:
            self._emit_endless_loop(region, lines)

        else:
            self._emit_while(region, lines)

        if self.verbose:
            self._write(lines, "// LOOP → END")

    @staticmethod
    def __condition_source_block(region: LoopRegion, *, is_do_while: bool) -> BasicBlock | None:
        """
        The block `LoopConditionRegionPass._consume_guard` actually pulled
        the condition off of: the header for a top-tested (WHILE) loop,
        the single latch for a bottom-tested (DO_WHILE) one - mirrors that
        pass's own `_extract` logic exactly (including the self-loop case,
        where header IS the latch).
        """
        if not is_do_while:
            return region.header_block

        latches = getattr(region, "latches", None)
        if latches and len(latches) == 1:
            return next(iter(latches))

        # Self-loop: header is its own sole latch.
        return region.header_block

    def _render_for_component(self, value) -> str:
        if value is None:
            return ""

        if isinstance(value, str):
            return value

        return self.print_expression(value)

    def _emit_for(self, region: LoopRegion, lines: list[str]) -> None:
        initializer = self._render_for_component(region.initializer)
        condition = (
            self.print_expression(region.condition)
            if region.condition is not None
            else ""
        )
        update = self._render_for_component(region.update)

        self._emit_condition_comment(
            region.condition,
            lines,
            source_block=self.__condition_source_block(
                region,
                is_do_while=False,
            ),
        )

        self._write(
            lines,
            f"for ({initializer}; {condition}; {update}) {{",
        )

        with self._indented():
            self._emit_region(region.body, lines)

        self._write(lines, "}")

    def _emit_for_each(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:

        keyword = (
            "of"
            if region.loop_kind is LoopKind.FOR_OF
            else "in"
        )

        source = (
            self.print_expression(region.iterable)
            if region.iterable is not None
            else "/* missing iterable */"
        )

        if region.loop_binding is None:
            binding = "item"
        elif isinstance(region.loop_binding, str):
            binding = region.loop_binding
        else:
            binding = f"r{region.loop_binding}"

        self._write(
            lines,
            f"for (const {binding} {keyword} {source}) {{",
        )

        with self._indented():
            self._emit_region(region.body, lines)

        self._write(lines, "}")

    def _emit_while(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:

        condition = (
            self.print_expression(region.condition)
            if region.condition is not None
            else "true"
        )

        self._emit_condition_comment(
            region.condition,
            lines,
            source_block=self.__condition_source_block(
                region,
                is_do_while=False,
            ),
        )

        self._write(lines, f"while ({condition}) {{")

        with self._indented():
            self._emit_region(region.body, lines)

        self._write(lines, "}")

    def _emit_do_while(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:

        condition = (
            self.print_expression(region.condition)
            if region.condition is not None
            else "true"
        )

        self._write(lines, "do {")

        with self._indented():
            self._emit_region(region.body, lines)

        self._emit_condition_comment(
            region.condition,
            lines,
            source_block=self.__condition_source_block(
                region,
                is_do_while=True,
            ),
        )

        self._write(lines, f"}} while ({condition});")

    def _emit_endless_loop(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:

        self._write(lines, "while (true) {")

        with self._indented():
            self._emit_region(region.body, lines)

        self._write(lines, "}")

    # ---------------------------------------------------------
    # try
    # ---------------------------------------------------------

    def _emit_try(self, region: TryRegion, lines):

        self._write(lines, "try {")

        with self._indented():
            self._emit_region(region.try_body, lines)

        if region.catch:
            name = region.catch.exception

            self._write(lines, f"}} catch ({name}) {{")

            with self._indented():
                self._emit_region(region.catch.body, lines)

        if region.finally_:
            self._write(lines, "} finally {")

            with self._indented():
                self._emit_region(region.finally_.body, lines)

        self._write(lines, "}")

    # ---------------------------------------------------------
    # switch
    # ---------------------------------------------------------

    def _emit_switch(self, region: SwitchRegion, lines):

        disc = self.print_expression(region.discriminant)

        if self.verbose:
            self._write(lines, f"// Switch → START")

        self._write(lines, f"switch ({disc}) {{")
        self._indent += 1

        for case in region.cases:

            for test in case.tests:
                self._write(lines, f"case {self.print_expression(test)}:")

            with self._indented():
                self._emit_region(case.body, lines)
                self._ensure_case_terminated(lines)

        if region.default_body is not None:
            self._write(lines, "default:")

            with self._indented():
                self._emit_region(region.default_body, lines)
                self._ensure_case_terminated(lines)

        self._indent -= 1
        self._write(lines, "}")

        if self.verbose:
            self._write(lines, f"// Switch → END")

    def _ensure_case_terminated(self, lines: list[str]) -> None:
        """
        JS `case` bodies fall through to the next case unless they end
        in a terminating statement. Hermes-compiled switch bodies
        always end in one (return/throw/break/continue - the VM has no
        implicit fallthrough), but insert an explicit `break;` here
        anyway as a safety net for any case body this pass produces
        without one, since silently falling through would change the
        emitted program's behavior from the original.
        """

        for line in reversed(lines):
            stripped = line.strip()
            if not stripped or stripped.startswith("//"):
                continue
            if stripped.startswith(("return", "throw", "break", "continue")):
                return
            break

        self._write(lines, "break;")

    # ---------------------------------------------------------
    # helpers
    # ---------------------------------------------------------

    def _write(self, lines: list[str], text: str):
        lines.append(f"{self.INDENT * self._indent}{text}")

    # ------------------------------------------------------------------
    # Public entry points
    # ------------------------------------------------------------------

    def print_expression(self, node) -> str:
        return self.visit(node)

    def print_statement(self, node) -> str:
        return self.visit(node)

    def print_terminator(self, node) -> str:
        return self.visit(node)

    # ------------------------------------------------------------------
    # Fallback
    # ------------------------------------------------------------------

    def generic_visit(self, node) -> str:
        logger.warning("Printer: unsupported node type %s", type(node).__name__)
        return f"/* unsupported: {type(node).__name__} */"

    # ------------------------------------------------------------------
    # Expressions - primitives
    # ------------------------------------------------------------------

    def visit_Identifier(self, node: Identifier) -> str:
        return node.name

    def visit_ParenthesizedExpression(self, node: ParenthesizedExpression) -> str:
        return f"({self.visit(node.expression)})"

    def visit_RawExpression(self, node: RawExpression) -> str:
        return node.source

    # ------------------------------------------------------------------
    # Expressions - literals
    # ------------------------------------------------------------------

    def visit_NumericLiteral(self, node: NumericLiteral) -> str:
        value = node.value

        if value != value:  # NaN
            return "NaN"
        if value == float("inf"):
            return "Infinity"
        if value == float("-inf"):
            return "-Infinity"
        if isinstance(value, float) and value.is_integer():
            return str(int(value))

        return repr(value)

    def visit_BigIntLiteral(self, node: BigIntLiteral) -> str:
        return f"{node.value}n"

    def visit_StringLiteral(self, node: StringLiteral) -> str:
        return json.dumps(node.value)

    def visit_BooleanLiteral(self, node: BooleanLiteral) -> str:
        return "true" if node.value else "false"

    def visit_NullLiteral(self, node: NullLiteral) -> str:
        return "null"

    def visit_UndefinedLiteral(self, node: UndefinedLiteral) -> str:
        return "undefined"

    def visit_RegExpLiteral(self, node: RegExpLiteral) -> str:
        return f"/{node.pattern}/{node.flags}"

    def visit_TemplateLiteral(self, node: TemplateLiteral) -> str:
        parts = []

        for i, quasi in enumerate(node.quasis):
            parts.append(quasi.raw)

            if i < len(node.expressions):
                parts.append("${" + self.visit(node.expressions[i]) + "}")

        return "`" + "".join(parts) + "`"

    # ------------------------------------------------------------------
    # Expressions - operations
    # ------------------------------------------------------------------

    def visit_UnaryExpression(self, node: UnaryExpression) -> str:
        # Word operators (typeof/void/delete) already carry a trailing
        # space in UnaryOperator's values; symbolic ones (+/-/!/~) don't
        # need one. Simple concatenation covers both.
        operand = self._wrap_operand(node.operand, node)
        return f"{node.operator}{operand}"

    def visit_UpdateExpression(self, node: UpdateExpression) -> str:
        argument = self.visit(node.argument)

        if node.prefix:
            return f"{node.operator}{argument}"

        return f"{argument}{node.operator}"

    def visit_BinaryExpression(self, node: BinaryExpression) -> str:
        left = self._wrap_side(node.left, node, is_right=False)
        right = self._wrap_side(node.right, node, is_right=True)
        return f"{left} {node.operator} {right}"

    def visit_AssignmentExpression(self, node: AssignmentExpression) -> str:
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"{left} {node.operator} {right}"

    def visit_ConditionalExpression(self, node: ConditionalExpression) -> str:
        test = self._wrap_operand(node.test, node)
        consequent = self.visit(node.consequent)
        alternate = self.visit(node.alternate)
        return f"{test} ? {consequent} : {alternate}"

    def visit_SequenceExpression(self, node: SequenceExpression) -> str:
        return ", ".join(self.visit(e) for e in node.expressions)

    # ------------------------------------------------------------------
    # Expressions - access / calls
    # ------------------------------------------------------------------

    def visit_MemberExpression(self, node: MemberExpression) -> str:
        receiver = self._wrap_operand(node.receiver, node)
        access = "?." if node.optional else ""

        if node.computed:
            return f"{receiver}{access}[{self.visit(node.member)}]"

        if node.optional:
            return f"{receiver}?.{self.visit(node.member)}"

        return f"{receiver}.{self.visit(node.member)}"

    def visit_CallExpression(self, node: CallExpression) -> str:
        callee = self._wrap_operand(node.callee, node)
        args = ", ".join(self.visit(a) for a in node.arguments)
        call = "?.(" if node.optional else "("
        return f"{callee}{call}{args})"

    def visit_NewExpression(self, node: NewExpression) -> str:
        callee = self._wrap_operand(node.callee, node)
        args = ", ".join(self.visit(a) for a in node.arguments)
        return f"new {callee}({args})"

    def visit_SpreadElement(self, node: SpreadElement) -> str:
        return f"...{self.visit(node.argument)}"

    # ------------------------------------------------------------------
    # Expressions - collections
    # ------------------------------------------------------------------

    def visit_ArrayExpression(self, node: ArrayExpression) -> str:
        return "[" + ", ".join(self.visit(e) for e in node.elements) + "]"

    def visit_ObjectExpression(self, node: ObjectExpression) -> str:
        return "{ " + ", ".join(self.visit(p) for p in node.properties) + " }"

    def visit_ObjectProperty(self, node: ObjectProperty) -> str:
        if node.shorthand:
            return self.visit(node.value)

        key = f"[{self.visit(node.key)}]" if node.computed else self.visit(node.key)
        value = self.visit(node.value)

        if node.kind == PropertyKind.GET:
            return f"get {key}() {{ return {value}; }}"

        if node.kind == PropertyKind.SET:
            return f"set {key}(v) {{ {value} = v; }}"

        return f"{key}: {value}"

    # ------------------------------------------------------------------
    # Expressions - functions
    # ------------------------------------------------------------------

    def visit_FunctionExpression(self, node: FunctionExpression) -> str:
        name = self.visit(node.name) if node.name else ""
        params = ", ".join(self.visit(p) for p in node.parameters)
        prefix = "async function" if node.async_ else "function"
        star = "*" if node.generator else ""
        return f"{prefix}{star} {name}({params}) {{ ... }}"

    def visit_ArrowFunctionExpression(self, node: ArrowFunctionExpression) -> str:
        params = ", ".join(self.visit(p) for p in node.parameters)
        prefix = "async " if node.async_ else ""
        return f"{prefix}({params}) => {{ ... }}"

    def visit_AwaitExpression(self, node: AwaitExpression) -> str:
        return f"await {self._wrap_operand(node.argument, node)}"

    def visit_YieldExpression(self, node: YieldExpression) -> str:
        star = "*" if node.delegate else ""

        if node.argument is None:
            return f"yield{star}"

        return f"yield{star} {self.visit(node.argument)}"

    # ------------------------------------------------------------------
    # Statements
    # ------------------------------------------------------------------

    def visit_BlockStatement(self, node: BlockStatement) -> str:
        # Multi-statement expansion is JSRenderer's responsibility (it
        # walks the region tree, not this flat block). Used only when a
        # BlockStatement shows up inline (e.g. as a function body stub).
        return "{ ... }"

    def visit_EmptyStatement(self, node: EmptyStatement) -> str:
        return ";"

    def visit_ExpressionStatement(self, node: ExpressionStatement) -> str:
        return f"{self.visit(node.expression)};"

    def visit_VariableDeclaration(self, node: VariableDeclaration) -> str:
        parts = []

        for decl in node.declarations:
            id_text = self.visit(decl.id)

            if decl.init is not None:
                parts.append(f"{id_text} = {self.visit(decl.init)}")
            else:
                parts.append(id_text)

        return f"{node.kind} " + ", ".join(parts) + ";"

    def visit_IfStatement(self, node: IfStatement) -> str:
        # JSRenderer renders if/else structurally via IfRegion; this
        # covers the case of printing just the condition/header text.
        return f"if ({self.visit(node.test)})"

    def visit_ReturnStatement(self, node: ReturnStatement) -> str:
        if node.argument is None:
            return "return;"

        return f"return {self.visit(node.argument)};"

    def visit_DebuggerStatement(self, node: DebuggerStatement) -> str:
        return "debugger;"

    def visit_ThrowStatement(self, node: ThrowStatement) -> str:
        return f"throw {self.visit(node.argument)};"

    def visit_BreakStatement(self, node: BreakStatement) -> str:
        if node.label is None:
            return "break;"

        return f"break {self.visit(node.label)};"

    def visit_ContinueStatement(self, node: ContinueStatement) -> str:
        if node.label is None:
            return "continue;"

        return f"continue {self.visit(node.label)};"

    def visit_LabeledStatement(self, node: LabeledStatement) -> str:
        return f"{self.visit(node.label)}:"

    # ------------------------------------------------------------------
    # Pre-structural control flow (see regions/models/Statements.py)
    # ------------------------------------------------------------------

    def visit_TerminatorJump(self, node) -> str:
        return f"goto label_{node.target};"

    def visit_TerminatorConditionalBranch(self, node) -> str:
        return f"if ({self.visit(node.condition)}) goto label_{node.target};"

    def visit_TerminatorSwitch(self, node) -> str:
        return "// Raw TerminatorSwitch reached Printer. SwitchStructurer should have converted it into a SwitchRegion."

    # ------------------------------------------------------------------
    # Operator precedence helpers
    # ------------------------------------------------------------------

    def _wrap_operand(self, operand, parent) -> str:
        """Parenthesize `operand` if it's a lower-precedence expression."""

        text = self.visit(operand)

        if isinstance(operand, (BinaryExpression, ConditionalExpression, AssignmentExpression, SequenceExpression)):
            return f"({text})"

        return text

    def _wrap_side(self, side, parent: BinaryExpression, is_right: bool) -> str:
        text = self.visit(side)

        if isinstance(side, BinaryExpression):
            parent_prec = precedence(parent.operator)
            side_prec = precedence(side.operator)

            if side_prec < parent_prec or (is_right and side_prec == parent_prec):
                return f"({text})"

        elif isinstance(side, (ConditionalExpression, AssignmentExpression, SequenceExpression)):
            return f"({text})"

        return text
