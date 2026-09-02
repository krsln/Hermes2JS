"""Public entry points for the region-pass pipeline stage."""

from hermes_decompiler.transforms.region_passes.BaseRegionPass import RegionPass
from .BooleanChainRegionPass import BooleanChainRegionPass
from .ConditionalExpressionRegionPass import ConditionalExpressionRegionPass
from hermes_decompiler.transforms.region_passes.DeadMovEliminationPass import DeadMovEliminationPass
from .ForEachRegionPass import ForEachRegionPass
from .GeneratorStateMachineRegionPass import GeneratorStateMachineRegionPass
from .LoopConditionRegionPass import LoopConditionRegionPass
from .LoopInductionAliasPass import LoopInductionAliasPass
from .LoopContinueRegionPass import LoopContinueRegionPass
from hermes_decompiler.transforms.region_passes.NullishAssignmentRegionPass import NullishAssignmentRegionPass
from .RedundantJumpRegionPass import RedundantJumpRegionPass
from .ReturnValueResolutionPass import ReturnValueResolutionPass

__all__ = [
    "RegionPass",
    "BooleanChainRegionPass",
    "ConditionalExpressionRegionPass",
    "DeadMovEliminationPass",
    "ForEachRegionPass",
    "GeneratorStateMachineRegionPass",
    "LoopConditionRegionPass",
    "LoopInductionAliasPass",
    "LoopContinueRegionPass",
    "NullishAssignmentRegionPass",
    "RedundantJumpRegionPass",
    "ReturnValueResolutionPass",
]
