from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionVisitor import RegionVisitor
from hermes_decompiler.analysis.regions.Regions import (
    LoopKind,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.analysis.transforms._shared import _structural_key
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression

from ._base import RegionPass


class ForEachRegionPass(RegionPass, RegionVisitor):
    """
    Reclassifies a plain `LoopRegion` (`loop_kind == LoopKind.WHILE`,
    the default `LoopStructurer` / `LoopConditionRegionPass` leave
    every loop in) as `FOR_OF` or `FOR_IN` when its header matches the
    fixed instruction sequence Hermes emits for those constructs:

        for-of:  IteratorBegin (before the loop) -> IteratorNext
                 (loop header's first instruction) -> optional
                 IteratorClose, folded by TryStructurer into an
                 enclosing TryRegion.finally_
        for-in:  GetPNameList (before the loop) -> GetNextPName
                 (loop header's first instruction), no try/finally

    Must run AFTER LoopStructurer, TryStructurer and
    LoopConditionRegionPass:
      - LoopStructurer:         loop.header_block must exist
      - TryStructurer:          for-of's IteratorClose must already be
                                 folded into a real FinallyRegion, or
                                 there is nothing here to match against
      - LoopConditionRegionPass: header.terminator has already been
                                 consumed into loop.condition, so the
                                 header's *first* instruction is
                                 reliably the IteratorNext/GetNextPName
                                 call and nothing else

    Conservative by design: any pattern that doesn't match exactly
    (wrong callee, mismatched iterator identity, unexpected finally
    content) is left as a plain `while` loop rather than guessed at -
    a missed for-of is a readability regression, a wrongly-claimed one
    is a correctness regression (silently drops real cleanup code).
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    # -----------------------------------------------------------------
    # Tree walk - only TryRegion and LoopRegion need pass-specific
    # ordering (recognize-then-descend / descend-then-recognize);
    # every other region kind uses RegionVisitor's default recursion
    # unchanged, which already reaches SwitchRegion case/default
    # bodies without any special-casing here.
    # -----------------------------------------------------------------

    def visit_TryRegion(self, node: TryRegion) -> None:
        self.visit(node.try_body)
        # Check for-of *after* descending, so a nested loop inside
        # try_body is already itself recognized/unwrapped if it's
        # for-of; `_try_recognize_for_of` only acts on a LoopRegion
        # that is a *direct* child of try_body.
        self._try_recognize_for_of(node)
        if node.catch:
            self.visit(node.catch.body)
        if node.finally_:
            self.visit(node.finally_.body)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._try_recognize_for_in(node)
        self.visit(node.body)

    # -----------------------------------------------------------------
    # for-of
    # -----------------------------------------------------------------

    def _try_recognize_for_of(self, try_region: TryRegion) -> None:

        loop = self._direct_loop_child(try_region.try_body)

        if loop is None or loop.loop_kind is not LoopKind.WHILE:
            return

        next_call, next_instr, header_block = self._match_header_call(loop, "next")

        if next_call is None:
            return

        iterator_expr = self._resolve_identifier(next_call.callee.receiver)

        iterable = self._match_call(iterator_expr, "GetIterator")

        if iterable is None:
            return

        if try_region.finally_ is not None:
            if not self._finally_matches_iterator_close(try_region, iterator_expr):
                # Something else lives in this finally (or the
                # iterator identity doesn't line up) - don't touch it,
                # the cleanup code is real and must stay visible.
                return

        loop.loop_kind = LoopKind.FOR_OF
        loop.iterable = iterable
        loop.loop_binding = next_instr.dest_reg

        self._strip_instruction(header_block, next_instr)

        if try_region.finally_ is not None:
            self._unwrap_try(try_region, loop)

    # -----------------------------------------------------------------
    # for-in
    # -----------------------------------------------------------------

    def _try_recognize_for_in(self, loop: LoopRegion) -> None:

        if loop.loop_kind is not LoopKind.WHILE:
            return

        next_call, next_instr, header_block = self._match_header_call(loop, "next")

        if next_call is None:
            return

        list_expr = self._resolve_identifier(next_call.callee.receiver)

        obj = self._match_call(list_expr, "HermesPropertyIterator")

        if obj is None:
            return

        loop.loop_kind = LoopKind.FOR_IN
        loop.iterable = obj
        loop.loop_binding = next_instr.dest_reg

        self._strip_instruction(header_block, next_instr)

    def _resolve_identifier(self, expr):
        """
        Some handlers inline a register's defining expression directly
        (`get_register_expression` - e.g. IteratorNext's `iterator`,
        IteratorClose's `.return()` receiver), others deliberately keep
        a bare register reference (`get_register_reference` - e.g.
        GetNextPName's `list_val`, precisely to avoid re-embedding a
        large/side-effecting expression at every `.next()` call site).

        This pass needs the *actual* defining expression either way to
        recognize `GetIterator(...)` / `HermesPropertyIterator(...)`,
        so when `expr` is still a bare `r{N}` reference, resolve it by
        finding that register's defining instruction among every block
        currently in the region tree. This pass has no access to
        `HermesAnalysis.registers` (region passes only receive
        `graph`/`cfg`), so this walks `RegionGraph.blocks()` instead -
        a reasonable substitute given Hermes registers are effectively
        single-assignment for the pre-loop setup values this matches
        against (GetPNameList/IteratorBegin each run exactly once,
        right before the loop). Returns `expr` unchanged if nothing
        resolves (already inlined, or no defining instruction found).
        """
        if not (isinstance(expr, Identifier) and expr.name.startswith("r") and expr.name[1:].isdigit()):
            return expr

        reg = int(expr.name[1:])

        for block in self.graph.blocks():
            for instr in block.instructions:
                if instr.dest_reg == reg and instr.value is not None:
                    return instr.value

        return expr

    # -----------------------------------------------------------------
    # Shared matching helpers
    # -----------------------------------------------------------------

    @staticmethod
    def _direct_loop_child(sequence: SequenceRegion) -> LoopRegion | None:
        for child in sequence.children:
            if isinstance(child, LoopRegion):
                return child
        return None

    @staticmethod
    def _match_header_call(loop: LoopRegion, method_name: str):
        """
        The header block's first instruction must be exactly
        `<something>.method_name()` - what IteratorNext/GetNextPName
        always lower to (see Iterator.py / GetNextPName.py handlers).
        Returns (CallExpression, OpcodeResult, BasicBlock), or
        (None, None, None) if it doesn't match.
        """
        header = loop.header_block
        if header is None:
            return None, None, None

        first = header.first_instruction
        if first is None:
            return None, None, None

        value = first.value
        if not isinstance(value, CallExpression):
            return None, None, None

        callee = value.callee

        if not isinstance(callee, MemberExpression):
            return None, None, None

        prop = callee.member

        if not isinstance(prop, Identifier) or prop.name != method_name:
            return None, None, None

        return value, first, header

    @staticmethod
    def _match_call(expr, callee_name: str):
        """
        Returns the single argument of `callee_name(arg)` if `expr` is
        exactly that pseudo-call (as produced by IteratorBegin /
        GetPNameList), else None.
        """
        if (
                isinstance(expr, CallExpression)
                and isinstance(expr.callee, Identifier)
                and expr.callee.name == callee_name
                and len(expr.arguments) == 1
        ):
            return expr.arguments[0]
        return None

    @staticmethod
    def _finally_matches_iterator_close(try_region: TryRegion, iterator_expr) -> bool:
        """
        True iff the entire finally body is a single `.return()` call
        on the same iterator expression IteratorNext was called on.
        Expression trees don't reliably define `__eq__` (see
        `_structural_key`'s own docstring for the same problem) so
        identity is compared structurally, not with `==`.
        """
        finally_body = try_region.finally_.body

        values = [
            instr.value
            for block in finally_body.covered_blocks
            for instr in block.instructions
            if instr.value is not None
        ]

        if len(values) != 1:
            return False

        value = values[0]

        if not isinstance(value, CallExpression) or value.arguments:
            return False

        if not isinstance(value.callee, MemberExpression):
            return False

        prop = value.callee.member

        if not isinstance(prop, Identifier) or prop.name != "return":
            return False

        return _structural_key(value.callee.receiver) == _structural_key(iterator_expr)

    # -----------------------------------------------------------------
    # Mutation
    # -----------------------------------------------------------------

    @staticmethod
    def _strip_instruction(block: BasicBlock, instr) -> None:
        if instr in block.instructions:
            block.instructions.remove(instr)

    @staticmethod
    def _unwrap_try(try_region: TryRegion, loop: LoopRegion) -> None:
        """
        `for (const x of arr) {}` implies the iterator close - once
        loop.loop_kind is FOR_OF the wrapping try/finally is pure
        scaffolding left over from how Hermes lowers the construct,
        not something the source ever wrote. Replace the TryRegion in
        its parent SequenceRegion with the LoopRegion directly.

        Deliberately NOT routed through RegionGraph's block-level
        primitives (move/append/etc) - those operate on BasicBlocks,
        and this splices one Region (LoopRegion) in for another
        (TryRegion) as siblings inside the same parent SequenceRegion.
        covered_blocks caching is kept correct by calling
        invalidate_coverage() explicitly, same contract those
        primitives follow internally.
        """
        parent = try_region.parent

        if not isinstance(parent, SequenceRegion):
            # Shouldn't happen post-TryStructurer/IfStructurer, but
            # don't silently corrupt the tree if it ever does.
            return

        idx = parent.children.index(try_region)

        try_region.try_body.children.remove(loop)
        try_region.try_body.invalidate_coverage()

        parent.children[idx] = loop
        loop.parent = parent
        parent.invalidate_coverage()
