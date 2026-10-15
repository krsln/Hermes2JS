"""Public entry points for the region-pass pipeline stage."""

from ._base import RegionPass
from .BooleanChainRegionPass import BooleanChainRegionPass
from .ConditionalExpressionRegionPass import ConditionalExpressionRegionPass
from .DeadMovEliminationPass import DeadMovEliminationPass
from .DeadThisPlaceholderPass import DeadThisPlaceholderPass
from .DeadUndefinedStorePass import DeadUndefinedStorePass, FlowSnapshot
from .ForEachRegionPass import ForEachRegionPass
from .GeneratorStateMachineRegionPass import GeneratorStateMachineRegionPass
from .IfTailMergeRegionPass import IfTailMergeRegionPass
from .InductionVariableNamingPass import InductionVariableNamingPass
from .LoopConditionRegionPass import LoopConditionRegionPass
from .LoopGuardInitializerPass import LoopGuardInitializerPass
from .LoopInductionAliasPass import LoopInductionAliasPass
from .LoopContinueRegionPass import LoopContinueRegionPass
from .NullishAssignmentRegionPass import NullishAssignmentRegionPass
from .RedundantJumpRegionPass import RedundantJumpRegionPass
from .ReturnValueResolutionPass import ReturnValueResolutionPass
from .TrailingReturnRegionPass import TrailingReturnRegionPass
from .ConditionalContinueRegionPass import ConditionalContinueRegionPass
from .UnfoldedMergeRepairPass import UnfoldedMergeRepairPass
from .LoopCarriedDefinitionPass import LoopCarriedDefinitionPass

__all__ = [
    "RegionPass",
    "BooleanChainRegionPass",
    "ConditionalExpressionRegionPass",
    "DeadMovEliminationPass",
    "DeadThisPlaceholderPass",
    "DeadUndefinedStorePass", "FlowSnapshot",
    "ForEachRegionPass",
    "GeneratorStateMachineRegionPass",
    "IfTailMergeRegionPass",
    "InductionVariableNamingPass",
    "LoopConditionRegionPass",
    "LoopGuardInitializerPass",
    "LoopInductionAliasPass",
    "LoopContinueRegionPass",
    "NullishAssignmentRegionPass",
    "RedundantJumpRegionPass",
    "ReturnValueResolutionPass",
    "TrailingReturnRegionPass",
    "ConditionalContinueRegionPass",
    "UnfoldedMergeRepairPass",
    "LoopCarriedDefinitionPass",
]
