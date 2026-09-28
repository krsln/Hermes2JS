from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import SequenceRegion
from hermes_decompiler.ir.expressions import UndefinedLiteral
from hermes_decompiler.ir.statements import ReturnStatement
from ._base import RegionPass


class TrailingReturnRegionPass(RegionPass):
    """Drops the function's own final `return undefined;`.

    Hermes ends every function that falls off its end with an explicit
    `LoadConstUndefined rN; Ret rN` - the bytecode has no implicit
    return - so a source function with no `return` at all decompiles to
    `... return undefined;`. In JavaScript, running off the end of a
    function IS `return undefined`, so that last statement adds nothing
    and only makes every void function look as if it returned a value.

    Only the very last statement of the function's own top-level
    sequence qualifies: falling off the end of the function body is
    exactly what it stands for. Anywhere else - inside an `if`, a
    loop, a `try`, or with more code after it - `return undefined;`
    is a real early exit and stays untouched (a `try`/`finally`
    ending in a return, for instance, can still route through the
    `finally` block on the way out, so the tail of a nested region is
    never treated as the function's end here).

    Only a literal `undefined` argument (or none) is dropped. A bare
    `return r0;` whose register `ReturnValueResolutionPass` could not
    prove to hold `undefined` is left alone - a missed cleanup is a
    readability cost, a wrong one would swallow a real return value.

    The instruction stays in its block, just with no statement left to
    print, so verbose output still shows the `<Ret>` line in its usual
    `// CODE →` trace.

    Must run after `ReturnValueResolutionPass` (which is what turns
    `return r0;` into `return undefined;` in the first place).
    """

    def run(self) -> None:
        root = self.graph.root

        if not isinstance(root, SequenceRegion) or not root.children:
            return

        last = root.children[-1]

        if not isinstance(last, BasicBlock) or not last.instructions:
            return

        instruction = last.instructions[-1]
        statement = instruction.statement

        if not isinstance(statement, ReturnStatement):
            return

        if statement.argument is not None and not isinstance(statement.argument, UndefinedLiteral):
            return

        # `value` too: with `statement` gone the printer falls back to
        # rendering `value` as a bare expression statement (`undefined`).
        instruction.statement = None
        instruction.terminator = None
        instruction.value = None
