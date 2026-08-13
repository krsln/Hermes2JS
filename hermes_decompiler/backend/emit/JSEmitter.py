from __future__ import annotations

from hermes_decompiler.analysis.models.RegionGraph import SequenceRegion
from .Printer import Printer


class JSEmitter:
    """
    Emits JavaScript from a structured SequenceRegion.

    The graph is assumed to be fully structured
    (loops, ifs, try/catch, switch, ...).

    No control-flow analysis is performed here.
    """

    def __init__(self, verbose: bool = False):
        self.printer = Printer(verbose=verbose)

    def emit(self, root: SequenceRegion) -> list[str]:
        return self.printer.print_region(root)
