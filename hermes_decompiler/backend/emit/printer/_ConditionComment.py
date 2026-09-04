from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import Identifier

from ._PrinterContext import PrinterContext
from .ExpressionPrinter import ExpressionPrinter

__all__ = [
    "ConditionCommentPrinter",
]

logger = get_logger(__name__)


class ConditionCommentPrinter:
    """
    Emits optional local register-definition annotations for conditions.

    This is deliberately a display-only facility.

    It does not perform register-state resolution, data-flow analysis,
    cross-block lookup, or expression rewriting.
    """

    def __init__(self, context: PrinterContext, expressions: ExpressionPrinter) -> None:
        self.ctx = context
        self.expressions = expressions

    def emit(
            self,
            condition,
            lines: list[str],
            *,
            source_block: BasicBlock | None,
            before_index: int | None = None,
    ) -> None:
        """
        Emit a local definition comment for bare rN operands.

        Only definitions physically present in `source_block` are considered.
        """
        if condition is None or source_block is None:
            return

        names = sorted(self._collect_register_names(condition))

        if not names:
            return

        index = (
            len(source_block.instructions)
            if before_index is None
            else before_index
        )

        parts: list[str] = []

        for name in names:
            definition = self._find_local_definition_text(source_block, index, name)

            if definition is not None:
                parts.append(f"{name} = {definition}")

        if parts:
            self.ctx.write(lines, "// → " + "; ".join(parts))

    @staticmethod
    def _collect_register_names(node) -> set[str]:
        """
        Find bare rN identifiers recursively in an expression tree.

        This intentionally mirrors the dataclass/tuple walking semantics
        used by the analysis layer without depending on analysis code.
        """
        found: set[str] = set()

        def walk(value) -> None:
            if isinstance(value, Identifier):
                if (
                        value.name.startswith("r")
                        and value.name[1:].isdigit()
                ):
                    found.add(value.name)
                return

            if not dataclasses.is_dataclass(value):
                return

            for field in dataclasses.fields(value):
                child = getattr(value, field.name)

                if dataclasses.is_dataclass(child):
                    walk(child)

                elif isinstance(child, tuple):
                    for item in child:
                        if dataclasses.is_dataclass(item):
                            walk(item)

        walk(node)

        return found

    def _find_local_definition_text(self, block: BasicBlock, before_index: int, name: str) -> str | None:
        """
        Find the last local definition of `name` before `before_index`.
        """
        register = int(name[1:])

        for instruction in reversed(block.instructions[:before_index]):
            if (
                    instruction.dest_reg == register
                    and instruction.value is not None
            ):
                try:
                    return self.expressions.print(instruction.value)
                except Exception as exc:
                    # Condition comments are diagnostic-only. A failure while rendering
                    # one must never affect the actual JavaScript emission.
                    logger.debug("Failed to render condition comment expression: %s", exc)
                    return None

        return None
