"""Public entry points for the region-pass pipeline stage."""

from ._base import RegionPass
from .BooleanChainRegionPass import BooleanChainRegionPass
from .ConditionalExpressionRegionPass import ConditionalExpressionRegionPass
from .DeadMovEliminationPass import DeadMovEliminationPass
from .ForEachRegionPass import ForEachRegionPass
from .GeneratorStateMachineRegionPass import GeneratorStateMachineRegionPass
from .IfTailMergeRegionPass import IfTailMergeRegionPass
from .LoopConditionRegionPass import LoopConditionRegionPass
from .LoopInductionAliasPass import LoopInductionAliasPass
from .LoopContinueRegionPass import LoopContinueRegionPass
from .NullishAssignmentRegionPass import NullishAssignmentRegionPass
from .RedundantJumpRegionPass import RedundantJumpRegionPass
from .ReturnValueResolutionPass import ReturnValueResolutionPass
from .TrailingReturnRegionPass import TrailingReturnRegionPass

__all__ = [
    "RegionPass",
    "BooleanChainRegionPass",
    "ConditionalExpressionRegionPass",
    "DeadMovEliminationPass",
    "ForEachRegionPass",
    "GeneratorStateMachineRegionPass",
    "IfTailMergeRegionPass",
    "LoopConditionRegionPass",
    "LoopInductionAliasPass",
    "LoopContinueRegionPass",
    "NullishAssignmentRegionPass",
    "RedundantJumpRegionPass",
    "ReturnValueResolutionPass",
    "TrailingReturnRegionPass",
]
