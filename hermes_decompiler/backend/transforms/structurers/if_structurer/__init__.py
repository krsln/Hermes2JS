"""Public entry point for the IfStructurer transform pass."""

from ._compound_folder import restore_dropped_case_jumps
from .if_structurer import IfStructurer

__all__ = ["IfStructurer", "restore_dropped_case_jumps"]
