from __future__ import annotations

from collections import deque

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    RegionVisitor,
    LoopKind,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.backend.transforms.shared import structural_key
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Expression
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression
from .BaseRegionPass import RegionPass

logger = get_logger(__name__)


class ForEachRegionPass(RegionPass, RegionVisitor):
    """Reclassifies a plain LoopRegion as FOR_OF or FOR_IN where it matches.

    Targets loops LoopStructurer / LoopConditionRegionPass leave as
    the default `loop_kind == LoopKind.WHILE`, when the header matches
    the fixed instruction sequence Hermes emits for those constructs:

        for-of:  IteratorBegin (before the loop) -> IteratorNext
                 (loop header's first instruction) -> optional
                 IteratorClose, folded by TryStructurer into an
                 enclosing TryRegion.finally_
        for-in:  GetPNameList (before the loop) -> GetNextPName
                 (loop header's first instruction), no try/finally

    Must run after LoopStructurer, TryStructurer, and
    LoopConditionRegionPass:
      - LoopStructurer:          loop.header_block must exist
      - TryStructurer:           for-of's IteratorClose must already be
                                  folded into a real FinallyRegion, or
                                  there is nothing here to match against
      - LoopConditionRegionPass: header.terminator has already been
                                  consumed into loop.condition, so the
                                  header's first instruction is
                                  reliably the IteratorNext/GetNextPName
                                  call and nothing else

    Conservative by design: any pattern that doesn't match exactly
    (wrong callee, mismatched iterator identity, unexpected `finally`
    content) is left as a plain while loop rather than guessed at - a
    missed for-of is a readability regression, a wrongly claimed one
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

        node_catch = node.catch
        if node_catch:
            self.visit(node_catch.body)

        node_finally = node.finally_
        if node_finally:
            self.visit(node_finally.body)

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

        raw_iterator_ref = next_call.callee.obj

        iterator_expr = self._resolve_identifier(raw_iterator_ref, next_instr, header_block)

        iterable = self._match_call(iterator_expr, "GetIterator")

        if iterable is None:
            return

        if try_region.finally_ is not None:
            if not self._finally_matches_iterator_close(try_region, raw_iterator_ref, iterator_expr):
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

        list_expr = self._resolve_identifier(next_call.callee.obj, next_instr, header_block)

        obj = self._match_call(list_expr, "HermesPropertyIterator")

        if obj is None:
            return

        loop.loop_kind = LoopKind.FOR_IN
        loop.iterable = obj
        loop.loop_binding = next_instr.dest_reg

        self._strip_instruction(header_block, next_instr)

    def _resolve_identifier(self, expr: Expression, before_instr, before_block: BasicBlock):
        """Resolve a possibly-still-bare register reference to its defining expression.

        Some handlers inline a register's defining expression directly
        (get_register_expression - e.g., IteratorNext's iterator,
        IteratorClose's .return() receiver), others deliberately keep
        a bare register reference (get_register_reference - e.g.,
        GetNextPName's list_val, to avoid re-embedding a large or
        side-effecting expression at every .next() call site).

        This pass needs the actual defining expression either way to
        recognize GetIterator(...) / HermesPropertyIterator(...), so
        when expr is still a bare r{N} reference, resolve it to the
        register's REACHING definition at the point of use
        (before_block/before_instr) - not just any definition found
        anywhere in the function.

        A prior version of this method picked either the first
        definition found by a flat scan of every block (wrong when the
        register was reused earlier for an unrelated value - e.g. a
        `console` lookup temporary later repurposed as the iterator
        register), or the definition with the highest
        cfg.reg_definitions address below before_instr.address (wrong
        because nothing else in this codebase relies on that address
        field being globally comparable across blocks -
        LoopConditionRegionPass._infer_induction_register only ever
        uses it for block identity, `block is update_block`, never for
        cross-instruction ordering - so trusting it as a sortable
        offset was an unverified assumption that silently broke the
        single-definition for-in case).

        This version instead walks the actual CFG, which is the one
        source of ordering this pass can trust:

          1. Scan before_block's own instructions strictly before
             before_instr, in reverse, for a write to `reg`.
          2. If not found, do a backward BFS over EVERY predecessor
             path from before_block (not just a unique-predecessor
             chain - before_block is very often a loop header or a
             `finally` block, both of which always have more than one
             predecessor: an outside entry edge plus one or more
             in-loop back/exceptional edges - requiring a single
             predecessor would bail out immediately on exactly the
             shapes this pass targets). Each path stops exploring
             further back as soon as it finds ANY write to `reg`,
             collecting that value.

        The register is only resolved if every path that found a
        definition agrees, via structural_key, on the same value. The
        single-assignment assumption above means genuine matches
        always agree here regardless of how many paths were walked
        (a loop's back edge never redefines the pre-loop setup
        register, so exploring through it just contributes nothing,
        not a conflicting value); a real structural disagreement means
        this isn't the simple shape this pass targets after all, so it
        bails rather than guessing which path is "the" reaching
        definition. Returns expr unchanged in that case, or if no path
        finds a definition at all.
        """
        if not (
                isinstance(expr, Identifier)
                and expr.name.startswith("r")
                and expr.name[1:].isdigit()
        ):
            return expr

        reg = int(expr.name[1:])

        # 1. Same block, strictly before before_instr.
        found = self._find_definition_in_instructions(
            before_block.instructions, reg, stop_before=before_instr
        )
        if found is not None:
            return found

        # 2. Backward BFS over every predecessor path.
        visited = {before_block}
        queue = deque(before_block.predecessors)
        found_values = []

        while queue:
            block = queue.popleft()

            if block in visited:
                continue
            visited.add(block)

            value = self._find_definition_in_instructions(block.instructions, reg)

            if value is not None:
                found_values.append(value)
                # Don't look further back past a definition on this path.
                continue

            queue.extend(block.predecessors)

        if not found_values:
            return expr

        first = found_values[0]

        for other in found_values[1:]:
            if structural_key(other) != structural_key(first):
                # Different paths reach different definitions - not
                # the clean single-assignment shape this pass targets.
                return expr

        return first

    @staticmethod
    def _find_definition_in_instructions(instructions, reg: int, stop_before=None):
        """Scan `instructions` in reverse for the most recent write to `reg`.

        If `stop_before` is given, only instructions strictly before it
        (in list order) are considered - used to search "everything
        before the use site" within before_block itself.
        """
        if stop_before is not None:
            try:
                cutoff = instructions.index(stop_before)
            except ValueError:
                cutoff = len(instructions)
            instructions = instructions[:cutoff]

        for instr in reversed(instructions):
            if instr.dest_reg == reg and instr.value is not None:
                return instr.value

        return None

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
        """Match the header's first instruction against `<x>.method_name()`.

        That shape is what IteratorNext/GetNextPName always lower to
        (see Iterator.py / GetNextPName.py handlers). Returns
        (CallExpression, OpcodeResult, BasicBlock), or
        (None, None, None) if it doesn't match.
        """
        header = loop.header_block

        first = header.first_instruction
        if first is None:
            return None, None, None

        value = first.value
        if not isinstance(value, CallExpression):
            return None, None, None

        callee = value.callee

        if not isinstance(callee, MemberExpression):
            return None, None, None

        prop = callee.prop

        if not isinstance(prop, Identifier) or prop.name != method_name:
            return None, None, None

        return value, first, header

    @staticmethod
    def _match_call(expr: Expression, callee_name: str):
        """Return the single argument of `callee_name(arg)`, or None.

        Matches the exact pseudo-call shape produced by IteratorBegin
        / GetPNameList.
        """
        if (
                isinstance(expr, CallExpression)
                and isinstance(expr.callee, Identifier)
                and expr.callee.name == callee_name
                and len(expr.arguments) == 1
        ):
            return expr.arguments[0]
        return None

    def _finally_matches_iterator_close(
            self, try_region: TryRegion, raw_iterator_ref, iterator_expr
    ) -> bool:
        """Return True if the `finally` body is a single matching .return() call.

        The `finally`/Catch block here is reached ONLY through Hermes'
        implicit exception dispatch (see CFGBuilder._connect_edges,
        whose own docstring lists "Exception edges" under "Not yet
        supported") - it is never linked to the try body via ordinary
        `BasicBlock.predecessors`/`.successors` edges the way a normal
        fallthrough or jump target would be. Any attempt to resolve a
        bare register reference FROM this block by walking predecessors
        (`_resolve_identifier`'s CFG walk) therefore starts from an
        empty predecessor list and can never reach the iterator's real
        definition, no matter how correct the walk itself is elsewhere.

        Working around that by walking OUT from the header instead
        isn't needed: Hermes registers are stable for the whole
        function body (never renamed per block), so IteratorNext's
        iterator operand and IteratorClose's `.return()` receiver are
        simply the SAME register number when they refer to the same
        iterator - comparing the two bare references by name is both
        correct and entirely independent of the missing exception
        edges. `_resolve_identifier`'s CFG-walk-based structural
        comparison is kept as a fallback only, for the case (unproven
        so far, but allowed for by this pass's own docstring) where
        one side is already an inlined expression rather than a bare
        register.

        Expression trees don't reliably define __eq__ (see
        `_structural_key`'s own docstring for the same problem), so
        identity is compared structurally, not with `==`, whenever the
        fallback path is used.
        """
        node_finally = try_region.finally_

        if node_finally is None:
            return False

        finally_body = node_finally.body

        candidates = [
            (block, instr)
            for block in finally_body.covered_blocks
            for instr in block.instructions
            if instr.value is not None
        ]

        if len(candidates) != 1:
            return False

        finally_block, instr = candidates[0]
        value = instr.value

        if not isinstance(value, CallExpression) or value.arguments:
            return False

        if not isinstance(value.callee, MemberExpression):
            return False

        prop = value.callee.prop

        if not isinstance(prop, Identifier) or prop.name != "return":
            return False

        close_ref = value.callee.obj

        # Fast, CFG-independent path: same bare register name.
        if (
                isinstance(close_ref, Identifier)
                and isinstance(raw_iterator_ref, Identifier)
                and close_ref.name == raw_iterator_ref.name
        ):
            return True

        # Fallback: CFG-walk resolution (only reachable if the finally
        # block happens to have real predecessor edges after all, or if
        # close_ref was already inlined to a non-Identifier expression).
        resolved = self._resolve_identifier(close_ref, instr, finally_block)
        return structural_key(resolved) == structural_key(iterator_expr)

    # -----------------------------------------------------------------
    # Mutation
    # -----------------------------------------------------------------

    @staticmethod
    def _strip_instruction(block: BasicBlock, instr) -> None:
        if instr in block.instructions:
            block.instructions.remove(instr)

    @staticmethod
    def _unwrap_try(try_region: TryRegion, loop: LoopRegion) -> None:
        """Replace try_region with loop directly in the parent SequenceRegion.

        `for (const x of arr) {}` implies the iterator close - once
        `loop.loop_kind` is FOR_OF, the wrapping try/finally is pure
        scaffolding left over from how Hermes lowers the construct,
        not something the source ever wrote.

        Deliberately not routed through RegionGraph's block-level
        primitives (move/append/etc) - those operate on BasicBlocks,
        and this splices one Region (LoopRegion) in for another
        (TryRegion) as siblings inside the same parent SequenceRegion.
        `covered_blocks` caching is kept correct by calling
        invalidate_coverage() explicitly, the same contract those
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
