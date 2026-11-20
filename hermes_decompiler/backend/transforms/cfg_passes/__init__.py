"""Public entry point for the CFG-level passes."""

from . import _generator_dispatch as generator_dispatch
from .ArrayDestructuringCfgPass import ArrayDestructuringCfgPass
from .ConstantEdgeThreadingCfgPass import ConstantEdgeThreadingCfgPass
from .TerminalTailRegionCopyCfgPass import TerminalTailRegionCopyCfgPass
from .DecidedTestThreadingCfgPass import DecidedTestThreadingCfgPass
from .EnvArrayDestructuringCfgPass import EnvArrayDestructuringCfgPass
from .GeneratorStateDispatchCfgPass import GeneratorStateDispatchCfgPass
from .SharedReturnDuplicationCfgPass import SharedReturnDuplicationCfgPass
from .SharedTailDuplicationCfgPass import SharedTailDuplicationCfgPass
from .FallThroughLayoutCfgPass import FallThroughLayoutCfgPass
from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass
from .TestConstantSinkCfgPass import TestConstantSinkCfgPass
from .ValueConditionFoldCfgPass import ValueConditionFoldCfgPass

__all__ = [
    "ConstantEdgeThreadingCfgPass",
    "TerminalTailRegionCopyCfgPass",
    "DecidedTestThreadingCfgPass",
    "ArrayDestructuringCfgPass",
    "EnvArrayDestructuringCfgPass",
    "GeneratorStateDispatchCfgPass",
    "SharedReturnDuplicationCfgPass",
    "SharedTailDuplicationCfgPass",
    "FallThroughLayoutCfgPass",
    "ShortCircuitConditionCfgPass",
    "TestConstantSinkCfgPass",
    "ValueConditionFoldCfgPass",
    "generator_dispatch",
]
