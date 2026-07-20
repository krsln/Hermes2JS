from __future__ import annotations

from hermes_decompiler.regions.model.TryRegion import TryRegion


class TryStructurer:
    """
    Builds a TryRegion from an ExceptionAnalysis entry.

    STATUS: best-effort. This has NOT been validated against a real
    .hbc sample containing exception handlers - it's built purely from
    reading ExceptionAnalysis/ExceptionRegion and the Catch handler.
    Before trusting this in production, feed it a function compiled
    from a real `try { } catch (e) { }` and confirm:

      - `ExceptionRegion.start` actually lines up with a BasicBlock
        start address (if Hermes' metadata range starts mid-block,
        this needs to search for the containing block instead of
        doing an exact `blocks[start_id]` lookup).
      - `ExceptionRegion.handler` is exactly the address of the block
        whose first instruction is the `Catch` opcode.
      - There's no `finally` support at all yet - Hermes bytecode
        doesn't (as far as investigated so far) expose a clean
        "finally range" the way it does try/catch ranges, so
        `finally_region` is always None here. If finally blocks show
        up as ordinary duplicated code inlined at every exit path
        instead, that needs a different detection strategy entirely
        (probably not a TryRegion concern at all).
    """

    def __init__(self, analyzer):
        self._a = analyzer

    def build(self, start_id: int) -> tuple[TryRegion, int | None]:

        exception_region = self._a.exceptions_by_start[start_id]

        try_body, _ = self._a.structure_range(
            start_id,
            stop_id=exception_region.end,
            bound=None,
        )

        handler_id = exception_region.handler
        merge = self._a.merge_of(start_id)

        catch_body, _ = self._a.structure_range(
            handler_id,
            stop_id=merge,
            bound=None,
        )

        exception_name = self._exception_var_name(handler_id)

        region = TryRegion(
            try_region=try_body,
            catch_region=catch_body,
            finally_region=None,
            exception_name=exception_name,
        )

        return region, merge

    def _exception_var_name(self, handler_id: int) -> str:

        block = self._a.cfg.get_block(handler_id)

        if block and block.instructions:
            first = block.instructions[0]
            if first.handler == "Catch" and first.variable.name:
                return first.variable.name

        return "e"
