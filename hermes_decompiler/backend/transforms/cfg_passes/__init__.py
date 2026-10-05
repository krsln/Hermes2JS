"""Public entry point for the CFG-level passes."""

from . import _generator_dispatch as generator_dispatch
from .ArrayDestructuringCfgPass import ArrayDestructuringCfgPass
from .GeneratorStateDispatchCfgPass import GeneratorStateDispatchCfgPass
from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass

__all__ = [
    "ArrayDestructuringCfgPass",
    "GeneratorStateDispatchCfgPass",
    "ShortCircuitConditionCfgPass",
    "generator_dispatch",
]
