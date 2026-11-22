from __future__ import annotations

from hermes_decompiler.backend.regions import SequenceRegion
from .printer import Printer


class JSEmitter:
    """
    Emits JavaScript from a structured SequenceRegion.

    The graph is assumed to be fully structured
    (loops, ifs, try/catch, switch, ...).

    No control-flow analysis is performed here.
    """

    def __init__(self, verbose: bool = False):
        self.printer = Printer(verbose=verbose)

    def emit(self, root: SequenceRegion, *, labeled_exits: bool = False) -> list[str]:
        return self.printer.print_region(root, labeled_exits=labeled_exits)
