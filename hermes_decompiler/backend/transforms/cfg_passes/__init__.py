"""Public entry point for the CFG-level passes."""

from . import _generator_dispatch as generator_dispatch
from .ArrayDestructuringCfgPass import ArrayDestructuringCfgPass
from .EnvArrayDestructuringCfgPass import EnvArrayDestructuringCfgPass
from .GeneratorStateDispatchCfgPass import GeneratorStateDispatchCfgPass
from .SharedReturnDuplicationCfgPass import SharedReturnDuplicationCfgPass
from .SharedTailDuplicationCfgPass import SharedTailDuplicationCfgPass
from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass
from .ValueConditionFoldCfgPass import ValueConditionFoldCfgPass

__all__ = [
    "ArrayDestructuringCfgPass",
    "EnvArrayDestructuringCfgPass",
    "GeneratorStateDispatchCfgPass",
    "SharedReturnDuplicationCfgPass",
    "SharedTailDuplicationCfgPass",
    "ShortCircuitConditionCfgPass",
    "ValueConditionFoldCfgPass",
    "generator_dispatch",
]
