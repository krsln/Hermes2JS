from __future__ import annotations

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
from hermes_decompiler.ir.expressions import (
    CallExpression,
    NewExpression,
    AssignmentExpression,
    UpdateExpression,
    AwaitExpression,
    YieldExpression,
)
from .ExpressionPrinter import ExpressionPrinter
from .StatementPrinter import StatementPrinter
from ._ConditionComment import ConditionCommentPrinter
from ._PrinterContext import PrinterContext

__all__ = [
    "RegionPrinter",
]


class RegionPrinter:
    """
    Converts structured regions and basic blocks into JavaScript lines.

    This class performs rendering only. It does not infer CFG structure,
    classify loops, perform dominance analysis, or mutate regions.
    """

    def __init__(
            self,
            context: PrinterContext,
            expressions: ExpressionPrinter,
            statements: StatementPrinter,
            condition_comments: ConditionCommentPrinter,
    ) -> None:
        self.ctx = context
        self.expressions = expressions
        self.statements = statements
        self.condition_comments = condition_comments

    def print(self, region) -> list[str]:
        """Render one structured region tree."""
        self.ctx.reset()

        lines: list[str] = []

        self._emit_region(region, lines)

        return lines

    # ------------------------------------------------------------------
    # region dispatcher
    # ------------------------------------------------------------------

    def _emit_region(
            self,
            region: (
                    Region
                    | SequenceRegion
                    | LoopRegion
                    | IfRegion
                    | TryRegion
                    | SwitchRegion
                    | BasicBlock
            ),
            lines: list[str],
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

    # ------------------------------------------------------------------
    # basic block
    # ------------------------------------------------------------------

    def _emit_block(self, block: BasicBlock, lines: list[str]) -> None:
        if self.ctx.verbose:
            self.ctx.write(lines, f"// ──────────────── Block {block.id} ──────────────── ", )

        for index, instruction in enumerate(block.instructions):
            if self.ctx.verbose:
                bytecode = instruction.entry.bytecode
                bytecode = (
                    bytecode.split(":", 1)[1].strip()
                    if ":" in bytecode
                    else bytecode.strip()
                )

                self.ctx.write(lines, f"// CODE → {bytecode}")

            if instruction.statement is not None:
                self.ctx.write(lines, self.statements.print(instruction.statement))
                continue

            if instruction.terminator is not None:
                self.condition_comments.emit(
                    getattr(instruction.terminator, "condition", None),
                    lines,
                    source_block=block,
                    before_index=index,
                )

                self.ctx.write(lines, self.statements.print(instruction.terminator))
                continue

            if instruction.value is None:
                continue

            rendered = self.expressions.print(instruction.value)

            if instruction.dest_reg is not None:
                # # A CallExpression whose result is never read is a discarded
                # # call. Keep it as a standalone statement so side effects are
                # # preserved without emitting a dead register assignment.
                # is_discarded_call = (
                #         not instruction.definition_used
                #         and isinstance(instruction.value, CallExpression)
                # )
                #
                # if not is_discarded_call:
                #     rendered = f"r{instruction.dest_reg} = {rendered}"
                passable = (
                    rendered.startswith("console.log")
                )

                if not instruction.definition_used and passable:
                   pass
                else:
                    rendered = f"r{instruction.dest_reg} = {rendered}"

            if instruction.definition_used:
                if self.ctx.verbose:
                    self.ctx.write(lines, f"// USED → {rendered};")
            else:
                self.ctx.write(lines, rendered)

    # ------------------------------------------------------------------
    # sequence
    # ------------------------------------------------------------------

    def _emit_sequence(self, region: SequenceRegion, lines: list[str]) -> None:
        for child in region.children:
            self._emit_region(child, lines)

    # ------------------------------------------------------------------
    # if
    # ------------------------------------------------------------------

    def _emit_if(self, region: IfRegion, lines: list[str], *, _chain: bool = False) -> None:
        """
        Emit an IfRegion.  When the else-body consists of a single
        nested IfRegion, we emit a flat `else if` cascade instead of
        nested braces – matching the original source style.
        """
        condition = self.expressions.print(region.condition)

        self.condition_comments.emit(
            region.condition, lines,
            source_block=self._nearest_preceding_block(region),
        )

        if _chain:
            self.ctx.write(lines, f"}} else if ({condition}) {{")
        else:
            self.ctx.write(lines, f"if ({condition}) {{")

        with self.ctx.indented():
            self._emit_region(region.then_body, lines)

        else_body = region.else_body
        if else_body is None:
            self.ctx.write(lines, "}")
            return

        # Detect classic else-if: else body is a SequenceRegion that
        # contains exactly one IfRegion (and nothing else).
        nested = self._extract_single_if(else_body)

        if nested is not None:
            self._emit_if(nested, lines, _chain=True)
            return

        # Ordinary else
        self.ctx.write(lines, "} else {")

        with self.ctx.indented():
            self._emit_region(else_body, lines)

        self.ctx.write(lines, "}")

    @staticmethod
    def _nearest_preceding_block(region: IfRegion) -> BasicBlock | None:
        """
        The nearest `BasicBlock` sibling immediately preceding `region`
        in its own parent `SequenceRegion`, if any - this is where the
        guard's operands (the `Greater`/`Less`/`JStrictEqual`/... setup
        instructions IfStructurer consumed into `region.condition`) still
        physically live, same as how `LoopConditionRegionPass._consume_guard`
        leaves everything except the branch instruction itself sitting in
        the header/latch block.

        Only ever walks LOCAL siblings within the immediate parent - never
        crosses into a grandparent `SequenceRegion` (e.g., stepping out of
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
    def _is_skippable_prefix(item: BasicBlock | Region) -> bool:
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

        for instruction in item.instructions:
            if instruction.statement is not None:
                return False

            if instruction.terminator is not None:
                return False

            tuple_expressions = (
                CallExpression,
                NewExpression,
                AssignmentExpression,
                UpdateExpression,
                AwaitExpression,
                YieldExpression,
            )
            if (
                    instruction.value is not None
                    and isinstance(instruction.value, tuple_expressions)
            ):
                return False

        return True

    @classmethod
    def _extract_single_if(cls, body: Region) -> IfRegion | None:
        if isinstance(body, IfRegion):
            return body

        if not isinstance(body, SequenceRegion):
            return None

        # Allow a pure prefix (const/param loads) before the single
        # IfRegion so else-if cascades flatten correctly.
        meaningful = [
            child
            for child in body.children
            if not cls._is_skippable_prefix(child)
        ]

        if len(meaningful) == 1:
            value = meaningful[0]

            if isinstance(value, IfRegion):
                return value

        children = body.children

        if len(children) == 1:
            child = children[0]

            if isinstance(child, IfRegion):
                return child

        return None

    # ------------------------------------------------------------------
    # loops
    # ------------------------------------------------------------------

    def _emit_loop(self, region: LoopRegion, lines: list[str]) -> None:
        """
        Render an already-structured LoopRegion.

        Loop classification belongs to analysis / region passes.
        """
        if region.label is not None:
            self.ctx.write(lines, f"{region.label}:")

        kind = region.loop_kind

        if self.ctx.verbose:
            self.ctx.write(
                lines,
                (
                    f"// LOOP → START ({kind.value if kind else 'unknown'})"
                ),
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

        if self.ctx.verbose:
            self.ctx.write(lines, "// LOOP → END")

    @staticmethod
    def _condition_source_block(region: LoopRegion, *, is_do_while: bool) -> BasicBlock | None:
        """
        The block `LoopConditionRegionPass._consume_guard` actually pulled
        the condition off of: the header for a top-tested (WHILE) loop,
        the single latch for a bottom-tested (DO_WHILE) one - it mirrors that
        pass's own `_extract` logic exactly (including the self-loop case,
        where header IS the latch).
        """
        if not is_do_while:
            return region.header_block

        latches = region.latches

        if latches and len(latches) == 1:
            return next(iter(latches))

        # Self-loop: header is its own sole latch.
        return region.header_block

    def _render_for_component(self, value) -> str:
        if value is None:
            return ""

        if isinstance(value, str):
            return value

        return self.expressions.print(value)

    def _emit_for(self, region: LoopRegion, lines: list[str]) -> None:
        initializer = self._render_for_component(region.initializer)

        condition = (
            self.expressions.print(region.condition)
            if region.condition is not None
            else ""
        )

        update = self._render_for_component(region.update)

        self.condition_comments.emit(
            region.condition, lines,
            source_block=self._condition_source_block(region, is_do_while=False),
        )

        self.ctx.write(lines, f"for ({initializer}; {condition}; {update}) {{")

        with self.ctx.indented():
            self._emit_region(region.body, lines)

        self.ctx.write(lines, "}")

    def _emit_for_each(self, region: LoopRegion, lines: list[str], ) -> None:
        keyword = (
            "of"
            if region.loop_kind is LoopKind.FOR_OF
            else "in"
        )

        source = (
            self.expressions.print(region.iterable)
            if region.iterable is not None
            else "/* missing iterable */"
        )

        if region.loop_binding is None:
            binding = "item"
        elif isinstance(region.loop_binding, str):
            binding = region.loop_binding
        else:
            binding = f"r{region.loop_binding}"

        self.ctx.write(lines, f"for (const {binding} {keyword} {source}) {{")

        with self.ctx.indented():
            self._emit_region(region.body, lines)

        self.ctx.write(lines, "}")

    def _emit_while(self, region: LoopRegion, lines: list[str]) -> None:
        condition = (
            self.expressions.print(region.condition)
            if region.condition is not None
            else "true"
        )

        self.condition_comments.emit(
            region.condition, lines,
            source_block=self._condition_source_block(region, is_do_while=False),
        )

        self.ctx.write(lines, f"while ({condition}) {{")

        with self.ctx.indented():
            self._emit_region(region.body, lines)

        self.ctx.write(lines, "}")

    def _emit_do_while(self, region: LoopRegion, lines: list[str]) -> None:
        condition = (
            self.expressions.print(region.condition)
            if region.condition is not None
            else "true"
        )

        self.ctx.write(lines, "do {")

        with self.ctx.indented():
            self._emit_region(
                region.body,
                lines,
            )

        self.condition_comments.emit(
            region.condition, lines,
            source_block=self._condition_source_block(region, is_do_while=True),
        )

        self.ctx.write(lines, f"}} while ({condition});", )

    def _emit_endless_loop(self, region: LoopRegion, lines: list[str]) -> None:
        self.ctx.write(lines, "while (true) {")

        with self.ctx.indented():
            self._emit_region(region.body, lines)

        self.ctx.write(lines, "}")

    # ------------------------------------------------------------------
    # try
    # ------------------------------------------------------------------

    def _emit_try(self, region: TryRegion, lines: list[str]) -> None:
        self.ctx.write(lines, "try {")

        with self.ctx.indented():
            self._emit_region(region.try_body, lines)

        catch_field = region.catch
        if catch_field:
            self.ctx.write(lines, f"}} catch ({catch_field.exception}) {{")

            with self.ctx.indented():
                self._emit_region(catch_field.body, lines)

        finally_field = region.finally_
        if finally_field:
            self.ctx.write(lines, "} finally {")

            with self.ctx.indented():
                self._emit_region(finally_field.body, lines)

        self.ctx.write(lines, "}")

    # ------------------------------------------------------------------
    # switch
    # ------------------------------------------------------------------

    def _emit_switch(self, region: SwitchRegion, lines: list[str]) -> None:
        discriminant = self.expressions.print(region.discriminant)

        if self.ctx.verbose:
            self.ctx.write(lines, "// Switch → START")

        self.ctx.write(lines, f"switch ({discriminant}) {{")

        with self.ctx.indented():
            for case in region.cases:
                for test in case.tests:
                    self.ctx.write(lines, f"case {self.expressions.print(test)}:")

                with self.ctx.indented():
                    self._emit_region(case.body, lines)
                    self._ensure_case_terminated(lines)

            default_body = region.default_body
            if default_body is not None:
                self.ctx.write(lines, "default:")

                with self.ctx.indented():
                    self._emit_region(default_body, lines)
                    self._ensure_case_terminated(lines)

        self.ctx.write(lines, "}")

        if self.ctx.verbose:
            self.ctx.write(lines, f"// Switch → END")

    def _ensure_case_terminated(self, lines: list[str]) -> None:
        """
        Ensure a switch case cannot accidentally fall through.

        This is a backend safety net. Structured Hermes switch bodies are
        expected to already contain explicit terminating control flow.
        """
        for line in reversed(lines):
            stripped = line.strip()

            if not stripped or stripped.startswith("//"):
                continue

            if stripped.startswith(("return", "throw", "break", "continue")):
                return

            break

        self.ctx.write(lines, "break;")
