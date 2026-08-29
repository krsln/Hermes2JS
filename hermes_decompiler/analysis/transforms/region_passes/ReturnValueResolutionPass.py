from __future__ import annotations

import dataclasses
from collections import deque

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.transforms.shared import structural_key
from hermes_decompiler.ir.expressions import (
    ArrayExpression, CallExpression, Identifier, ObjectExpression,
)
from hermes_decompiler.ir.statements import ReturnStatement, ThrowStatement

from ._base import RegionPass


class ReturnValueResolutionPass(RegionPass):
    """Safely folds a bare `return rN;` / `throw rN;` back into its
    defining expression, once real CFG information is available.

    `Ret`/`Throw`'s own opcode handlers deliberately keep their value
    symbolic (`Identifier(f"r{N}")`, never inlined) rather than calling
    `get_register_expression` - that method inlines whatever value was
    MOST RECENTLY seen for a register during a single linear,
    ADDRESS-ORDER scan of the bytecode, with no notion of control flow
    at all. A register written only CONDITIONALLY (e.g. inside a
    `catch` block, or on only some loop iterations) and never
    rewritten afterward in ADDRESS order would get that conditional
    write inlined as if it always executes - silently producing a
    WRONG return/thrown value whenever the actual runtime path never
    took that write. This is exactly the bug this pass fixes for real:
    see tryCatchInsideLoopTest/section_15085, where `Ret r0` was
    rendering as `return r2 + 1;` - a copy of the `failures` counter's
    `catch`-only increment - regardless of whether any exception was
    ever actually caught during that particular call.

    This pass runs AFTER structuring, so (unlike the opcode handler)
    it has real CFG predecessor edges to work with. For each bare
    `rN` argument, it walks backward from the Return/Throw's own
    instruction across every predecessor path (the same
    reaching-definition technique as
    `ForEachRegionPass._resolve_identifier` - see that pass for the
    fuller rationale), and only folds in a value when EVERY path that
    finds a definition agrees on the exact same one. Any disagreement,
    or no definition found at all, leaves the bare reference in place
    - a missed inlining is a readability regression, a wrong one is a
    correctness regression, and this pass - like the rest of this
    codebase's region passes - always prefers the former.
    """

    def run(self) -> None:
        for block in list(self.graph.blocks()):
            for instr in list(block.instructions):
                statement = instr.statement

                if not isinstance(statement, (ReturnStatement, ThrowStatement)):
                    continue

                argument = statement.argument

                register = self._bare_register(argument)

                if register is None:
                    continue

                resolved, definition_instr = self._resolve_register(register, instr, block)

                if resolved is None:
                    continue

                new_statement = statement.__class__(argument=resolved)
                instr.statement = new_statement
                instr.value = resolved

                terminator = instr.terminator

                if terminator is not None and hasattr(terminator, "value"):
                    instr.terminator = dataclasses.replace(terminator, value=resolved)

                # Only NOW - having actually committed to substituting
                # `resolved` into the Return/Throw statement - mark the
                # instruction that produced it as consumed
                # (`RegionPrinter` skips printing an instruction's own
                # `rN = ...;` fallback statement when
                # `definition_used` is set, the same flag
                # `get_register_expression`'s own `mark_used()` sets on
                # a normal, successful inline).
                #
                # Marking this EARLIER - e.g. unconditionally in
                # `Ret.py`/`Throw.py` itself, before this pass even
                # runs and regardless of whether a safe definition is
                # ever actually found - was tried and reverted: it told
                # the printer "this value was consumed elsewhere" for
                # EVERY return, even the many cases (identity-sensitive
                # values, ambiguous/conditional definitions) this pass
                # deliberately leaves unresolved. The defining
                # instruction's own statement (e.g. `let r0 = {};`,
                # `r0 = HermesInternal.concat.call(...)`) would then
                # silently vanish from the printed function while the
                # return still only said `return r0;` - the
                # computation itself disappearing from the output
                # entirely. Marking only HERE, exactly when (and only
                # when) a fold genuinely happens, keeps the two in
                # lockstep.
                if definition_instr is not None:
                    definition_instr.definition_used = True

    # -----------------------------------------------------------------
    # Bare-register detection
    # -----------------------------------------------------------------

    @staticmethod
    def _bare_register(expr) -> int | None:
        if (
                isinstance(expr, Identifier)
                and expr.name.startswith("r")
                and expr.name[1:].isdigit()
        ):
            return int(expr.name[1:])
        return None

    # -----------------------------------------------------------------
    # Reaching-definition resolution (mirrors
    # ForEachRegionPass._resolve_identifier - see that pass for the
    # full rationale of each step; duplicated rather than imported per
    # this codebase's own established precedent of not sharing
    # extraction targets across unrelated passes, e.g.
    # LoopInductionAliasPass's `_repoint_node`).
    # -----------------------------------------------------------------

    def _resolve_register(self, reg: int, before_instr, before_block: BasicBlock):
        """Resolve `reg`'s value at the point of `before_instr` (inside
        `before_block`) via backward BFS across every predecessor path,
        requiring every path that finds a definition to agree.

        Also refuses to fold in an identity-sensitive expression
        (`ObjectExpression`/`ArrayExpression`/`CallExpression`) - the
        same rule `get_register_expression` itself applies - since
        substituting those changes the code's aliasing semantics
        rather than simply naming a value, and isn't a mechanical
        "same value" fold the way a literal or arithmetic expression
        is.

        Returns `(value, defining_instr)` on success, so the caller
        can mark the instruction that produced it as consumed (see
        `run`'s own comment on why that has to happen only upon an
        actual, committed fold). Returns `(None, None)` (leave the
        bare reference as-is) unless a single, safe, unambiguous
        definition is found.
        """
        found, found_instr = self._find_definition_in_instructions(
            before_block.instructions, reg, stop_before=before_instr
        )

        if found is None:
            visited = {before_block}
            queue = deque(before_block.predecessors)
            found_values = []

            while queue:
                block = queue.popleft()

                if block in visited:
                    continue
                visited.add(block)

                value, value_instr = self._find_definition_in_instructions(block.instructions, reg)

                if value is not None:
                    found_values.append((value, value_instr))
                    continue

                queue.extend(block.predecessors)

            if not found_values:
                return None, None

            first, first_instr = found_values[0]

            for other, _ in found_values[1:]:
                if structural_key(other) != structural_key(first):
                    return None, None

            found, found_instr = first, first_instr

        if isinstance(found, (ObjectExpression, ArrayExpression, CallExpression)):
            return None, None

        return found, found_instr

    @staticmethod
    def _find_definition_in_instructions(instructions, reg: int, stop_before=None):
        if stop_before is not None:
            try:
                cutoff = instructions.index(stop_before)
            except ValueError:
                cutoff = len(instructions)
            instructions = instructions[:cutoff]

        for instr in reversed(instructions):
            if instr.dest_reg == reg and instr.value is not None:
                return instr.value, instr

        return None, None
