from __future__ import annotations

from hermes_decompiler.two.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.two.cfg.analysis.ReversePostOrder import ReversePostOrder
from hermes_decompiler.two.cfg.analysis.DominatorAnalysis import DominatorAnalysis
from hermes_decompiler.two.cfg.analysis.ImmediateDominatorAnalysis import (
    ImmediateDominatorAnalysis,
)
from hermes_decompiler.two.cfg.analysis.PostDominatorAnalysis import (
    PostDominatorAnalysis,
)
from hermes_decompiler.two.cfg.analysis.ImmediatePostDominatorAnalysis import (
    ImmediatePostDominatorAnalysis,
)
from hermes_decompiler.two.cfg.analysis.LoopAnalysis import LoopAnalysis
from hermes_decompiler.two.cfg.analysis.ExceptionAnalysis import ExceptionAnalysis


class CFGAnalysis:
    """
    Provides reusable analyses over a Control Flow Graph.
    """

    def __init__(
            self,
            cfg: ControlFlowGraph,
            metadata: dict | None = None,
    ):
        self.cfg = cfg
        self.metadata = metadata or {}

        self._rpo = None
        self._dominators = None
        self._immediate_dominators = None
        self._post_dominators = None
        self._immediate_post_dominators = None
        self._loops = None
        self._exceptions = None

    @property
    def reverse_post_order(self):

        if self._rpo is None:
            self._rpo = ReversePostOrder.build(self.cfg)

        return self._rpo

    @property
    def dominators(self):

        if self._dominators is None:
            self._dominators = DominatorAnalysis.build(
                self.cfg,
                self.reverse_post_order,
            )

        return self._dominators

    @property
    def immediate_dominators(self):

        if self._immediate_dominators is None:
            self._immediate_dominators = (
                ImmediateDominatorAnalysis.build(
                    self.cfg,
                    self.dominators,
                )
            )

        return self._immediate_dominators

    @property
    def post_dominators(self):

        if self._post_dominators is None:
            self._post_dominators = (
                PostDominatorAnalysis.build(
                    self.cfg,
                    self.reverse_post_order,
                )
            )

        return self._post_dominators

    @property
    def immediate_post_dominators(self):
        """
        block.id -> the immediate post-dominator of that block, i.e.
        the merge point where its outgoing branches reconverge.

        This is what RegionBuilder uses to decide where an IfRegion /
        IfElseRegion ends and the enclosing sequence resumes.
        """

        if self._immediate_post_dominators is None:
            self._immediate_post_dominators = (
                ImmediatePostDominatorAnalysis.build(
                    self.cfg,
                    self.post_dominators,
                )
            )

        return self._immediate_post_dominators

    @property
    def loops(self):

        if self._loops is None:
            self._loops = (
                LoopAnalysis.build(
                    self.cfg,
                    self.dominators,
                )
            )

        return self._loops

    @property
    def exceptions(self):

        if self._exceptions is None:
            self._exceptions = (
                ExceptionAnalysis.build(
                    self.metadata,
                )
            )

        return self._exceptions
