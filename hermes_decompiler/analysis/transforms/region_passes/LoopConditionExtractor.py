import re

from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch

_IF_PATTERN = re.compile(r"if\s*\((.*)\)")


class LoopConditionExtractor:

    def __init__(self, root):
        self.root = root

    def run(self):
        self._visit(self.root)

    def _visit(self, region):

        if isinstance(region, SequenceRegion):
            for child in region.children:
                self._visit(child)
            return

        if isinstance(region, LoopRegion):
            self._extract(region)
            self._visit(region.body)

    def _extract(self, loop: LoopRegion):

        header = loop.header_block
        if header is None:
            return

        # last = header.last_instruction

        # if last is not None:
        #     text = self._render_result(last)
        #     match = _IF_PATTERN.search(text)
        #
        #     if not match:
        #         return

        branch = header.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return

        header.terminator = None
        loop.condition = branch.condition

        # `header.terminator` is only consulted for CFG edges - Printer
        # renders per-*instruction* terminators (`instruction.terminator`
        # in `_emit_block`), which is a completely separate field on
        # whichever OpcodeResult originally produced this branch (e.g.
        # JmpUndefined/JStrictEqual). Nulling `header.terminator` alone
        # leaves that instruction sitting in `header.instructions`, so
        # it still prints as a standalone `if (...) goto label;` inside
        # the loop body even though its condition was "consumed" into
        # `loop.condition`. Must also drop the instruction itself.
        if header.instructions and header.instructions[-1].terminator is branch:
            header.instructions.pop()

        # loop.condition = match.group(1).strip()
        # loop.loop_kind = LoopKind.WHILE

    # @classmethod
    # def _render_result(cls, result: OpcodeResult) -> str:
    #     """
    #     Human-readable one-line summary of this instruction's effect,
    #     used by verbose logging/dumps and any legacy code path that
    #     hasn't moved to `JSRenderer`/`Printer` yet.
    #
    #     Callable again after mutating `value`/`statement` (e.g.
    #     `Dispatcher._handle_generator_await` wraps a previous result's
    #     `value` in an `AwaitExpression` and recomputes `.result`).
    #     """
    #
    #     # Imported lazily to avoid a hard dependency from `models` on
    #     # `regions` at module load time; `models` is the lower layer.
    #     from hermes_decompiler.emit import Printer
    #
    #     printer = Printer()
    #
    #     if isinstance(result.statement, Statement):
    #         return printer.print_statement(result.statement)
    #     if isinstance(result.terminator, Terminator):
    #         return printer.print_terminator(result.terminator)
    #
    #     if isinstance(result.value, Expression):
    #         rendered = printer.print_expression(result.value)
    #
    #         if result.name:
    #             return f"{result.name} = {rendered}"
    #
    #         return rendered
    #
    #     if result.value is None:
    #         # No statement and no value: nothing meaningful to show.
    #         # Shouldn't normally happen for a well-formed handler.
    #         return ""
    #
    #     # Legacy fallback: value is still a plain string (handler not
    #     # yet migrated to the `ir` package).
    #     if result.name:
    #         return f"{result.name} = {result.value}"
    #
    #     return f"{result.value}"
