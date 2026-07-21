from __future__ import annotations

from hermes_decompiler.cfg.EdgeKind import EdgeKind


def control_flow_edges(block):
    """
    `block.outgoing` filtered to exclude EdgeKind.EXCEPTION.

    Exception edges (added by ControlFlowGraphBuilder._connect_exceptions
    so catch handlers are reachable) are a real CFG edge, but not a
    "normal" control-flow successor - a block inside a try range isn't
    a 3-way branch just because an exception *could* occur. Every place
    that reasons about "how many ways can control leave this block
    normally" (if-header detection, single-successor following, loop
    entry/exit classification) must go through this instead of reading
    `block.outgoing` directly, or a block sitting at the start of a try
    range would spuriously look like a switch/multi-way block.

    Kept in its own module (rather than living in _StructuralAnalyzer.py
    where it's used most) so both _StructuralAnalyzer and _LoopStructurer
    can import it without creating a circular import between the two.
    """
    return [edge for edge in block.outgoing if edge.kind != EdgeKind.EXCEPTION]
