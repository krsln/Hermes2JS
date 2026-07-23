from __future__ import annotations

from hermes_decompiler.two.cfg.CFGAnalysis import CFGAnalysis


class MergePointResolver:
    """
    Finds where a conditional branch reconverges.

    Thin wrapper around `CFGAnalysis.immediate_post_dominators` today,
    kept as its own class (rather than inlined into the structural
    analyzer) so that if merge-point resolution ever needs extra
    sanity checks - e.g. rejecting a merge point that isn't actually
    reachable from both branches, which can happen in pathological
    exception-heavy code - there's an obvious single place to add them
    without touching the traversal logic itself.
    """

    def __init__(self, analysis: CFGAnalysis):
        self._analysis = analysis

    def merge_of(self, header_id: int) -> int | None:
        return self._analysis.immediate_post_dominators.get(header_id)
