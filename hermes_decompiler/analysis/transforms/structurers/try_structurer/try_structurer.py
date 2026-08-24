from __future__ import annotations

from hermes_decompiler.analysis.models.regions import TryRegion
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

from ._finally_attacher import _FinallyAttacher
from ._finally_matcher import find_finally_wrapper_target
from ._handler_builder import _HandlerBuilder


class TryStructurer(RegionStructurer):
    """
    Builds TryRegions (with catch/finally) from the exception table.

    Hermes has no bytecode-level finally construct: a
    try/catch/finally is lowered as two overlapping exception handlers
    sharing the same start - a narrow one covering just the try (real
    catch), and a wider one covering try+catch together, whose target
    is a block that re-runs the cleanup code and rethrows. This class
    recognizes the wider handler as a finally-wrapper for the region
    the narrower handler already built, rather than structuring it as
    a second, nested try/catch (see `_finally_matcher`).

    A plain `try { } finally { }` (no catch at all) compiles to a
    single handler, since there's no separate narrower handler to pair
    it with. That case is only distinguishable from an ordinary catch
    by its content (cleanup code followed by an unconditional rethrow
    of the exception it just caught) and is reinterpreted after every
    handler has been resolved (see `_finally_attacher`).

    This class only owns handler dedup/ordering and the dispatch
    between "attach as finally" vs. "build a fresh try/catch"; all the
    actual recognition/construction/attachment logic lives in
    `_finally_matcher`, `_HandlerBuilder`, and `_FinallyAttacher`
    respectively.
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)
        self._handler_builder = _HandlerBuilder(graph, cfg)
        self._attacher = _FinallyAttacher(graph)

    def run(self):

        # Some functions list two handlers with the identical
        # [start, end] range but different targets (seen e.g., in
        # tryCatchFinallyImplicitThrowTest's [start=0x19,end=0x3f,
        # target=0x55] / [start=0x19, end=0x3f, target=0x87] pair).
        # Exception tables are matched in listed order, so for any
        # exception raised inside that identical range, the first entry
        # always wins - the second is permanently shadowed and never
        # actually fires at runtime. Structuring it anyway produces a
        # phantom empty wrapper once its target block gets legitimately
        # claimed elsewhere (see the finally-wrapper for the real,
        # first handler). Drop shadowed duplicates before doing
        # anything else.
        seen_ranges = set()
        handlers = []

        for handler in self.cfg.exception_handlers:
            key = (handler["start"], handler["end"])

            if key in seen_ranges:
                continue

            seen_ranges.add(key)
            handlers.append(handler)

        # Process narrower-scoped handlers before the wider ones that
        # wrap them, so `_HandlerBuilder.build`'s splicing always finds
        # its inner region already built. Sorting by raw range size
        # (end - start) breaks down when a wrapper's start sits later
        # than the handler it wraps (its end alone can then make it
        # look "smaller"). Sorting by end ascending is safe regardless:
        # a finally-wrapper protects through the end of the catch it
        # wraps, so its end is always >= the wrapped handler's end -
        # that ordering constraint holds no matter where either
        # handler's start falls.
        handlers = sorted(
            handlers,
            key=lambda h: h["end"],
        )

        processed: list[tuple[dict, TryRegion]] = []

        for handler in handlers:

            wrapped = find_finally_wrapper_target(handler, processed, self.cfg)

            if wrapped is not None:
                inner_handler, try_region = wrapped
                self._attacher.attach(handler, try_region, inner_handler, self.cfg)
                continue

            try_region = self._handler_builder.build(handler)

            if try_region is not None:
                processed.append((handler, try_region))

        # A plain `try { } finally { }` (no catch at all) never goes
        # through `_attacher.attach` above (see class docstring).
        # Reinterpret those as finally after the fact, once every
        # handler has been resolved.
        for _, try_region in processed:
            if try_region.finally_ is None:
                self._attacher.maybe_reinterpret_as_finally(try_region)

        self.dump_region_tree_if_debug(type(self).__name__)
