from abc import ABC

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


class EnvironmentAccess(OpcodeHandler, ABC):
    """Common helpers for Hermes lexical-environment opcodes."""

    def ResolveEnvironment(self, analysis: HermesAnalysis, env_reg: int) -> str:
        """
        Resolve an environment register.

        Falls back to the raw register when no value has been
        produced yet.
        """
        return self.GetValueByReg(analysis, env_reg) or f"r{env_reg}"

    def ResolveValue(self, analysis: HermesAnalysis, value_reg: int) -> str:
        """
        Resolve a value register.
        """
        return self.GetValueByReg(analysis, value_reg) or f"r{value_reg}"

    @staticmethod
    def FormatSlot(environment: str, slot: int) -> str:
        """
        Format a lexical environment slot.

        Example:
            r92[3]
        """
        return f"{environment}[{slot}]"
