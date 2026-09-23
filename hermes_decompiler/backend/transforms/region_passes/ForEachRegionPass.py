from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    RegionVisitor,
    LoopKind,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.backend.transforms.shared import structural_key
from hermes_decompiler.backend.transforms.shared import resolve_identifier as _shared_resolve_identifier
from hermes_decompiler.backend.transforms.shared import is_bare_register
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Expression
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression
from hermes_decompiler.ir.terminators import TerminatorThrow
from ._base import RegionPass

logger = get_logger(__name__)


def _is_plain_register_copy(instr) -> bool:
    """True for a `Mov`-shaped instruction: `dst = rN` with no other effect.

    Used only to recognize Hermes' own for-of/for-in register
    bookkeeping around the `.next()` call (see `_match_header_call`,
    `_strip_next_call_scaffold`) - never to justify removing a Mov
    anywhere else, where it could easily carry real meaning (e.g.
    aliasing a parameter for later use).
    """
    return instr.value is not None and is_bare_register(instr.value)


class ForEachRegionPass(RegionPass, RegionVisitor):
    """Reclassifies a plain LoopRegion as FOR_OF or FOR_IN where it matches.

    Targets loops LoopStructurer / LoopConditionRegionPass leave as
    the default `loop_kind == LoopKind.WHILE`, when the header matches
    the fixed instruction sequence Hermes emits for those constructs:

        for-of:  IteratorBegin (before the loop) -> IteratorNext
                 (loop header's first instruction) -> optional
                 IteratorClose, folded by TryStructurer into an
                 enclosing TryRegion - as `.finally_` when the try
                 body has an inlined copy of it on some exit (a
                 `break`/`return` inside the loop), otherwise left as
                 the faithful `catch (e) { it.return(); throw e }` it
                 is on the wire (see `_close_scaffold`)
        for-in:  GetPNameList (before the loop) -> GetNextPName
                 (loop header's first instruction), no try/finally

    Must run after LoopStructurer, TryStructurer, and
    LoopConditionRegionPass:
      - LoopStructurer:          loop.header_block must exist
      - TryStructurer:           for-of's IteratorClose must already be
                                  folded into a real FinallyRegion or a
                                  close-and-rethrow CatchRegion, or
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

        scaffold = self._close_scaffold(try_region)

        if scaffold is not None:
            if not self._close_body_matches(scaffold, raw_iterator_ref, iterator_expr):
                if try_region.finally_ is not None:
                    # Something else lives in this finally (or the
                    # iterator identity doesn't line up) - don't touch
                    # it, the cleanup code is real and must stay visible.
                    return

                # A catch that merely LOOKS like close-and-rethrow but
                # closes something else is the user's own catch: the
                # loop is still a for-of, the try stays.
                scaffold = None

        loop.loop_kind = LoopKind.FOR_OF
        loop.iterable = iterable
        loop.loop_binding = next_instr.dest_reg

        self._strip_next_call_scaffold(header_block, next_instr)

        if scaffold is not None:
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

        self._strip_next_call_scaffold(header_block, next_instr)

    def _resolve_identifier(self, expr: Expression, before_instr, before_block: BasicBlock):
        """Resolve a possibly-still-bare register reference to its defining expression.

        Thin wrapper around `transforms.shared.resolve_identifier` - the
        actual CFG-walk logic now lives there (extracted so
        `_finally_matcher`/`_predicates` can reuse it for
        register-aware finally-copy matching). See that function's own
        docstring for the full rationale and algorithm.
        """
        return _shared_resolve_identifier(expr, before_instr, before_block)

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
        """Match the header against `<x>.method_name()`, tolerating one
        priming `Mov` immediately before it.

        `<x>.method_name()` (IteratorNext/GetNextPName's lowering - see
        Iterator.py / GetNextPName.py's own handlers) is the header's
        literal first instruction as far back as hbc96. From hbc98
        onward, Hermes instead re-primes a scratch register from the
        iterable/iterator with a plain `Mov` immediately before every
        `IteratorNext`/`GetNextPName` call (feeding that call's own
        third operand - internal bookkeeping for the VM's fast-path
        check, with no JS-visible meaning: the loop's actual iterator
        identity is still `<x>` itself, read directly off the call's
        own callee, entirely unaffected by this extra Mov). Skipping
        past it here - rather than requiring the call at position 0 -
        is what recognizes hbc98's for-of/for-in at all; see
        `_strip_next_call_scaffold` for removing it once recognized.

        Deliberately tolerates AT MOST one such leading instruction,
        and only when it's a plain register-to-register copy: scanning
        further, or accepting anything else there, risks matching a
        `.next()` call that isn't this scaffold at all - e.g. one that
        genuinely runs after real loop-body content on a prior
        iteration due to how the blocks happened to merge, which is
        not a shape this pass should claim.

        Returns (CallExpression, OpcodeResult, BasicBlock), or
        (None, None, None) if neither position matches.
        """
        header = loop.header_block
        instructions = header.instructions

        if not instructions:
            return None, None, None

        call = ForEachRegionPass._match_next_call_instr(instructions[0], method_name)
        if call is not None:
            return call, instructions[0], header

        if (
                len(instructions) > 1
                and _is_plain_register_copy(instructions[0])
        ):
            call = ForEachRegionPass._match_next_call_instr(instructions[1], method_name)
            if call is not None:
                return call, instructions[1], header

        return None, None, None

    @staticmethod
    def _match_next_call_instr(instr, method_name: str):
        value = instr.value
        if not isinstance(value, CallExpression):
            return None

        callee = value.callee

        if not isinstance(callee, MemberExpression):
            return None

        prop = callee.prop

        if not isinstance(prop, Identifier) or prop.name != method_name:
            return None

        return value

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

    @staticmethod
    def _close_scaffold(try_region: TryRegion):
        """The body that carries this try's iterator-close, or None.

        Hermes lowers a for-of's IteratorClose as an exception handler
        whose body is the `.return()` call followed by a rethrow of the
        caught exception. TryStructurer presents that handler as:

        - `try_region.finally_` when it found the handler's body inlined
          in the try body (Hermes does that at a `break`/`return`), or
        - `try_region.catch`, exactly as compiled, when it found no such
          copy: `catch (e) { it.return(); throw e }`. TryStructurer does
          not turn that into a `finally` - the shape alone cannot tell it
          from a user `catch` that rethrows, and doing so on the success
          path would run the close code that was only ever meant for a
          throw.

        Only a catch of that exact shape - a single block ending in a
        rethrow of its own bound exception - is offered as a scaffold; the
        body itself is then checked by `_close_body_matches`.
        """
        if try_region.finally_ is not None:
            return try_region.finally_.body

        catch = try_region.catch

        if catch is None or len(catch.body.children) != 1:
            return None

        block = catch.body.children[0]

        if not isinstance(block, BasicBlock) or not isinstance(block.terminator, TerminatorThrow):
            return None

        thrown = block.terminator.value

        if not isinstance(thrown, Identifier):
            return None

        expected = f"r{catch.exception_reg}" if catch.exception_reg is not None else catch.exception

        return catch.body if thrown.name == expected else None

    def _close_body_matches(
            self, scaffold_body: SequenceRegion, raw_iterator_ref, iterator_expr
    ) -> bool:
        """Return True if the body is a single matching .return() call.

        (`scaffold_body` is a `finally` body, or a close-and-rethrow
        `catch` body - see `_close_scaffold`. A catch's trailing rethrow
        carries no value of interest and is not counted.)

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
        candidates = [
            (block, instr)
            for block in scaffold_body.covered_blocks
            for instr in block.instructions
            if instr.value is not None and not isinstance(instr.terminator, TerminatorThrow)
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
    def _strip_next_call_scaffold(header_block: BasicBlock, next_instr) -> None:
        """Remove `next_instr` plus its Mov-priming neighbor(s), if any.

        See `_match_header_call`'s own docstring for why a plain
        register-copy immediately BEFORE the matched call is safe to
        remove. The same reasoning applies to one immediately AFTER
        it: Hermes copies the call's own iterator-identity operand
        into another scratch register right after the call, purely to
        feed the loop's own done-check - and that check itself is
        never rendered once `loop_kind` is FOR_OF/FOR_IN (compare
        `forOfTest`'s hbc96 vs hbc98 golden fixtures: neither prints a
        condition), so the register that would-be copy fed is already
        dead the moment recognition succeeds, independent of whether
        the copy instruction itself stays or goes.

        Matches only immediately-adjacent instructions, by position at
        call time - never a wider scan - for the same reason
        `_match_header_call` only looks one instruction ahead: this
        must stay tied to the specific position Hermes' own lowering
        puts it in, not "some Mov somewhere nearby".
        """
        instructions = header_block.instructions

        if next_instr not in instructions:
            return

        idx = instructions.index(next_instr)

        doomed = [next_instr]

        if idx > 0 and _is_plain_register_copy(instructions[idx - 1]):
            doomed.append(instructions[idx - 1])

        if idx + 1 < len(instructions) and _is_plain_register_copy(instructions[idx + 1]):
            doomed.append(instructions[idx + 1])

        for instr in doomed:
            header_block.instructions.remove(instr)

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
