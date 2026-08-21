from __future__ import annotations

from typing import Any

from hermes_decompiler.analysis.models.regions import SequenceRegion, SwitchRegion, TryRegion, IfRegion, LoopRegion

"""
Read-only, dispatch-by-type traversal of the region tree
(`SequenceRegion`, `LoopRegion`, `IfRegion`, `TryRegion`,
`SwitchRegion`, `BasicBlock`, ...).

Mirrors `hermes_decompiler.ir.Visitor.NodeVisitor`'s design (define
`visit_<ClassName>`, fall back to `generic_visit`) but is intentionally
a SEPARATE class rather than a reuse of it: `ir.Node` exposes a
uniform `.children` tuple every node type shares, so one generic
recursion works for all of them. The region tree has no such
uniformity - a `SequenceRegion`'s children live in `.children`, an
`IfRegion`'s in `.then_body`/`.else_body`, a `TryRegion`'s across
`.try_body`/`.catch.body`/`.finally_.body`, a `SwitchRegion`'s across
each `SwitchCase.body`/`.default_body` - so each known region kind
gets its own `visit_<ClassName>` here, already implementing the
"visit each real child" default. `generic_visit` is only the fallback
for a genuinely unknown node type (most commonly `BasicBlock`, a true
leaf).

Why this exists: `structurers/_base.py`'s debug-dump used to
re-implement this exact same traversal locally as one big `isinstance`
chain - and silently forgot `SwitchRegion` when that region kind was
added, since nothing forced every such chain in the codebase to be
updated together. Centralizing the traversal here means a future new
region kind needs its `visit_<ClassName>` added in exactly one place;
existing callers that only care about a subset of node types keep
working via `generic_visit` (they'll just stop recursing past a node
kind they haven't been taught about, same as before).

Not yet retrofitted onto every ad-hoc `_visit`/`_fold_all` traversal
already living in `transforms/structurers/` and
`transforms/region_passes/` (`IfStructurer`'s builder, `SwitchStructurer`,
`BooleanChainRegionPass`, `ConditionalExpressionRegionPass`, ... each
still hand-rolls the same isinstance chain, usually with its own
pre/post-order hooks around it). That consolidation is a real, larger
follow-up - out of scope here, which is scoped to fixing the debug
dump specifically.
"""


class RegionVisitor:

    def visit(self, node: Any) -> None:
        method = getattr(
            self,
            f"visit_{type(node).__name__}",
            self.generic_visit,
        )
        method: Any
        method(node)

    def generic_visit(self, node: Any) -> None:
        """
        Leaf default for any node type this visitor hasn't been taught
        a `visit_<ClassName>` for (chiefly `BasicBlock`). Override
        instead of this for a specific type.
        """
        return

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self.visit(node.body)

    def visit_IfRegion(self, node: IfRegion) -> None:
        self.visit(node.then_body)
        if node.else_body is not None:
            self.visit(node.else_body)

    def visit_TryRegion(self, node: TryRegion) -> None:
        self.visit(node.try_body)

        node_catch = node.catch
        if node_catch is not None:
            self.visit(node_catch.body)

        node_finally = node.finally_
        if node_finally is not None:
            self.visit(node_finally.body)

    def visit_SwitchRegion(self, node: SwitchRegion) -> None:
        for case in node.cases:
            self.visit(case.body)
        if node.default_body is not None:
            self.visit(node.default_body)
