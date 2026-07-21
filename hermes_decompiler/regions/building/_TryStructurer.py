from __future__ import annotations

from hermes_decompiler.regions.model.TryRegion import TryRegion


class TryStructurer:

    def __init__(self, analyzer):
        self._a = analyzer

    def build(self, start_id: int) -> tuple[TryRegion, int | None]:

        # Same in-progress protection as LoopStructurer - see the
        # comment in _StructuralAnalyzer.__init__.
        self._a._exception_starts_in_progress.add(start_id)
        try:
            exception_region = self._a.exceptions_by_start[start_id]

            stop_id = self._resolve_stop_block(exception_region.end)

            try_body, _ = self._a.structure_range(
                start_id,
                stop_id=stop_id,
                bound=None,
                suppress_exception_start=start_id,
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
        finally:
            self._a._exception_starts_in_progress.discard(start_id)

    def _resolve_stop_block(self, end_addr: int) -> int | None:

        candidates = sorted(
            block.start_addr for block in self._a.cfg
            if block.start_addr >= end_addr
        )

        return candidates[0] if candidates else None

    def _exception_var_name(self, handler_id: int) -> str:

        block = self._a.cfg.get_block(handler_id)

        if block and block.instructions:
            first = block.instructions[0]
            if first.handler == "Catch" and first.variable.name:
                return first.variable.name

        return "e"