"""Public entry point for the CFG-level passes."""

from . import _generator_dispatch as generator_dispatch
from .ArrayDestructuringCfgPass import ArrayDestructuringCfgPass
from .EnvArrayDestructuringCfgPass import EnvArrayDestructuringCfgPass
from .GeneratorStateDispatchCfgPass import GeneratorStateDispatchCfgPass
from .SharedReturnDuplicationCfgPass import SharedReturnDuplicationCfgPass
from .SharedTailDuplicationCfgPass import SharedTailDuplicationCfgPass
from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass

__all__ = [
    "ArrayDestructuringCfgPass",
    "EnvArrayDestructuringCfgPass",
    "GeneratorStateDispatchCfgPass",
    "SharedReturnDuplicationCfgPass",
    "SharedTailDuplicationCfgPass",
    "ShortCircuitConditionCfgPass",
    "generator_dispatch",
]
