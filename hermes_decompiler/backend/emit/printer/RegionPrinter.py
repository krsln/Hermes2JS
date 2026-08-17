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

from ._PrinterContext import PrinterContext
from .ExpressionPrinter import ExpressionPrinter
from .StatementPrinter import StatementPrinter
from ._ConditionComment import ConditionCommentPrinter

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
        self.context = context
        self.expressions = expressions
        self.statements = statements
        self.condition_comments = condition_comments

    def print(self, region) -> list[str]:
        """Render one structured region tree."""
        self.context.reset()

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

    def _emit_block(
            self,
            block: BasicBlock,
            lines: list[str],
    ) -> None:
        if self.context.verbose:
            self.context.write(
                lines,
                f"// ──────────────── Block {block.id} ──────────────── ",
            )

        for index, instruction in enumerate(block.instructions):
            if self.context.verbose:
                bytecode = instruction.entry.bytecode
                bytecode = (
                    bytecode.split(":", 1)[1].strip()
                    if ":" in bytecode
                    else bytecode.strip()
                )

                self.context.write(
                    lines,
                    f"// CODE → {bytecode}",
                )

            if instruction.statement is not None:
                self.context.write(
                    lines,
                    self.statements.print(
                        instruction.statement
                    ),
                )
                continue

            if instruction.terminator is not None:
                self.condition_comments.emit(
                    getattr(
                        instruction.terminator,
                        "condition",
                        None,
                    ),
                    lines,
                    source_block=block,
                    before_index=index,
                )

                self.context.write(
                    lines,
                    self.statements.print(
                        instruction.terminator
                    ),
                )
                continue

            if instruction.value is None:
                continue

            rendered = self.expressions.print(
                instruction.value
            )

            if instruction.dest_reg is not None:
                if (
                        not instruction.definition_used
                        and rendered.startswith(
                    "globalThis.console.log"
                )
                ):
                    rendered = rendered.replace(
                        "globalThis.",
                        "",
                    )
                else:
                    rendered = (
                        f"r{instruction.dest_reg} = "
                        f"{rendered}"
                    )

            if instruction.definition_used:
                if self.context.verbose:
                    self.context.write(
                        lines,
                        f"// USED → {rendered};",
                    )
            else:
                self.context.write(
                    lines,
                    rendered,
                )

    # ------------------------------------------------------------------
    # sequence
    # ------------------------------------------------------------------

    def _emit_sequence(
            self,
            region: SequenceRegion,
            lines: list[str],
    ) -> None:
        for child in region.children:
            self._emit_region(child, lines)

    # ------------------------------------------------------------------
    # if
    # ------------------------------------------------------------------

    def _emit_if(
            self,
            region: IfRegion,
            lines: list[str],
            *,
            _chain: bool = False,
    ) -> None:
        condition = self.expressions.print(
            region.condition
        )

        self.condition_comments.emit(
            region.condition,
            lines,
            source_block=self._nearest_preceding_block(region),
        )

        if _chain:
            self.context.write(
                lines,
                f"}} else if ({condition}) {{",
            )
        else:
            self.context.write(
                lines,
                f"if ({condition}) {{",
            )

        with self.context.indented():
            self._emit_region(
                region.then_body,
                lines,
            )

        if region.else_body is None:
            self.context.write(lines, "}")
            return

        nested = self._extract_single_if(
            region.else_body
        )

        if nested is not None:
            self._emit_if(
                nested,
                lines,
                _chain=True,
            )
            return

        self.context.write(
            lines,
            "} else {",
        )

        with self.context.indented():
            self._emit_region(
                region.else_body,
                lines,
            )

        self.context.write(lines, "}")

    @staticmethod
    def _nearest_preceding_block(
            region: IfRegion,
    ) -> BasicBlock | None:
        parent = region.parent

        if not isinstance(parent, SequenceRegion):
            return None

        try:
            index = parent.children.index(region)
        except ValueError:
            return None

        for sibling in reversed(
                parent.children[:index]
        ):
            if isinstance(sibling, BasicBlock):
                return sibling

            return None

        return None

    @staticmethod
    def _is_skippable_prefix(item) -> bool:
        if not isinstance(item, BasicBlock):
            return False

        if item.terminator is not None:
            return False

        for instruction in item.instructions:
            if instruction.statement is not None:
                return False

            if instruction.terminator is not None:
                return False

            if (
                    instruction.value is not None
                    and isinstance(
                instruction.value,
                (
                        CallExpression,
                        NewExpression,
                        AssignmentExpression,
                        UpdateExpression,
                        AwaitExpression,
                        YieldExpression,
                ),
            )
            ):
                return False

        return True

    @classmethod
    def _extract_single_if(
            cls,
            body,
    ) -> IfRegion | None:
        if isinstance(body, IfRegion):
            return body

        if not isinstance(body, SequenceRegion):
            return None

        meaningful = [
            child
            for child in body.children
            if not cls._is_skippable_prefix(child)
        ]

        if (
                len(meaningful) == 1
                and isinstance(meaningful[0], IfRegion)
        ):
            return meaningful[0]

        if (
                len(body.children) == 1
                and isinstance(body.children[0], IfRegion)
        ):
            return body.children[0]

        return None

    # ------------------------------------------------------------------
    # loops
    # ------------------------------------------------------------------

    def _emit_loop(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:
        """
        Render an already-structured LoopRegion.

        Loop classification belongs to analysis / region passes.
        """
        if region.label is not None:
            self.context.write(
                lines,
                f"{region.label}:",
            )

        kind = region.loop_kind

        if self.context.verbose:
            self.context.write(
                lines,
                (
                    "// LOOP → START "
                    f"({kind.value if kind else 'unknown'})"
                ),
            )

        if kind in (
                LoopKind.FOR_OF,
                LoopKind.FOR_IN,
        ):
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

        if self.context.verbose:
            self.context.write(
                lines,
                "// LOOP → END",
            )

    @staticmethod
    def _condition_source_block(
            region: LoopRegion,
            *,
            is_do_while: bool,
    ) -> BasicBlock | None:
        if not is_do_while:
            return region.header_block

        latches = getattr(
            region,
            "latches",
            None,
        )

        if latches and len(latches) == 1:
            return next(iter(latches))

        return region.header_block

    def _render_for_component(
            self,
            value,
    ) -> str:
        if value is None:
            return ""

        if isinstance(value, str):
            return value

        return self.expressions.print(value)

    def _emit_for(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:
        initializer = self._render_for_component(
            region.initializer
        )

        condition = (
            self.expressions.print(region.condition)
            if region.condition is not None
            else ""
        )

        update = self._render_for_component(
            region.update
        )

        self.condition_comments.emit(
            region.condition,
            lines,
            source_block=self._condition_source_block(
                region,
                is_do_while=False,
            ),
        )

        self.context.write(
            lines,
            (
                f"for ({initializer}; "
                f"{condition}; "
                f"{update}) {{"
            ),
        )

        with self.context.indented():
            self._emit_region(
                region.body,
                lines,
            )

        self.context.write(lines, "}")

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

        self.context.write(
            lines,
            (
                f"for (const {binding} "
                f"{keyword} {source}) {{"
            ),
        )

        with self.context.indented():
            self._emit_region(
                region.body,
                lines,
            )

        self.context.write(lines, "}")

    def _emit_while(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:
        condition = (
            self.expressions.print(region.condition)
            if region.condition is not None
            else "true"
        )

        self.condition_comments.emit(
            region.condition,
            lines,
            source_block=self._condition_source_block(
                region,
                is_do_while=False,
            ),
        )

        self.context.write(
            lines,
            f"while ({condition}) {{",
        )

        with self.context.indented():
            self._emit_region(
                region.body,
                lines,
            )

        self.context.write(lines, "}")

    def _emit_do_while(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:
        condition = (
            self.expressions.print(region.condition)
            if region.condition is not None
            else "true"
        )

        self.context.write(lines, "do {")

        with self.context.indented():
            self._emit_region(
                region.body,
                lines,
            )

        self.condition_comments.emit(
            region.condition,
            lines,
            source_block=self._condition_source_block(
                region,
                is_do_while=True,
            ),
        )

        self.context.write(
            lines,
            f"}} while ({condition});",
        )

    def _emit_endless_loop(
            self,
            region: LoopRegion,
            lines: list[str],
    ) -> None:
        self.context.write(
            lines,
            "while (true) {",
        )

        with self.context.indented():
            self._emit_region(
                region.body,
                lines,
            )

        self.context.write(lines, "}")

    # ------------------------------------------------------------------
    # try
    # ------------------------------------------------------------------

    def _emit_try(
            self,
            region: TryRegion,
            lines: list[str],
    ) -> None:
        self.context.write(lines, "try {")

        with self.context.indented():
            self._emit_region(
                region.try_body,
                lines,
            )

        if region.catch:
            self.context.write(
                lines,
                f"}} catch ({region.catch.exception}) {{",
            )

            with self.context.indented():
                self._emit_region(
                    region.catch.body,
                    lines,
                )

        if region.finally_:
            self.context.write(
                lines,
                "} finally {",
            )

            with self.context.indented():
                self._emit_region(
                    region.finally_.body,
                    lines,
                )

        self.context.write(lines, "}")

    # ------------------------------------------------------------------
    # switch
    # ------------------------------------------------------------------

    def _emit_switch(
            self,
            region: SwitchRegion,
            lines: list[str],
    ) -> None:
        discriminant = self.expressions.print(
            region.discriminant
        )

        if self.context.verbose:
            self.context.write(
                lines,
                "// Switch → START",
            )

        self.context.write(
            lines,
            f"switch ({discriminant}) {{",
        )

        with self.context.indented():
            for case in region.cases:
                for test in case.tests:
                    self.context.write(
                        lines,
                        (
                                "case "
                                + self.expressions.print(test)
                                + ":"
                        ),
                    )

                with self.context.indented():
                    self._emit_region(
                        case.body,
                        lines,
                    )
                    self._ensure_case_terminated(lines)

            if region.default_body is not None:
                self.context.write(
                    lines,
                    "default:",
                )

                with self.context.indented():
                    self._emit_region(
                        region.default_body,
                        lines,
                    )
                    self._ensure_case_terminated(lines)

        self.context.write(lines, "}")

        if self.context.verbose:
            self.context.write(
                lines,
                "// Switch → END",
            )

    def _ensure_case_terminated(
            self,
            lines: list[str],
    ) -> None:
        """
        Ensure a switch case cannot accidentally fall through.

        This is a backend safety net. Structured Hermes switch bodies are
        expected to already contain explicit terminating control flow.
        """
        for line in reversed(lines):
            stripped = line.strip()

            if not stripped or stripped.startswith("//"):
                continue

            if stripped.startswith(
                    (
                            "return",
                            "throw",
                            "break",
                            "continue",
                    )
            ):
                return

            break

        self.context.write(lines, "break;")
