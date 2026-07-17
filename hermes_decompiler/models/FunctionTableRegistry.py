"""
Replaces the old `JSConverter._functionTable` class attribute.

The old code kept cross-section function-name knowledge in a *class-level*
dict, which meant:
  - it silently persisted across unrelated `convert()` calls
  - it was not thread-safe (concurrent conversions would corrupt each other)
  - tests polluted each other unless someone remembered to reset it
  - there was no way to run two independent conversions in the same process

If cross-section function-name resolution is genuinely needed (e.g. calling
function #11947 by name instead of by id, even when #11947 itself hasn't
been converted yet), that requirement should be modeled explicitly by the
*caller* (e.g. FileOps, which already iterates all sections) via this
registry - not hidden inside the converter.

Usage:
    registry = FunctionTableRegistry()
    for filename, section_index in files:
        JSConverter.convert(content, section_index, function_registry=registry)
"""
import threading
from typing import Dict, Optional


class FunctionTableRegistry:
    """Thread-safe, explicitly-scoped store of function_id -> function_name."""

    def __init__(self, initial: Optional[Dict[str, str]] = None):
        self._lock = threading.Lock()
        self._table: Dict[str, str] = dict(initial) if initial else {}

    def merge(self, entries: Dict[str, str]) -> None:
        with self._lock:
            self._table.update(entries)

    def snapshot(self) -> Dict[str, str]:
        """Return a shallow copy, safe to hand to a single conversion pass."""
        with self._lock:
            return dict(self._table)

    def get(self, function_id: str, default: Optional[str] = None) -> Optional[str]:
        with self._lock:
            return self._table.get(function_id, default)

    def __len__(self) -> int:
        with self._lock:
            return len(self._table)
