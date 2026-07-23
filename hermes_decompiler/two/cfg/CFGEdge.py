from dataclasses import dataclass

from hermes_decompiler.two.cfg.EdgeKind import EdgeKind


@dataclass(slots=True, frozen=True)
class CFGEdge:
    """
    Directed edge in the Control Flow Graph.
    """

    source: int

    target: int

    kind: EdgeKind