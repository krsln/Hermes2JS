from abc import ABC, abstractmethod
from typing import Dict, Optional, List

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry


# Base class auto-registering all subclasses
class OpcodeHandler(ABC):
    """Abstract base class for handling Hermes bytecode opcodes."""
    registry: Dict[str, 'OpcodeHandler'] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__name__ != "OpcodeHandler":
            # Register a singleton instance of the handler
            OpcodeHandler.registry[cls.__name__] = cls()

    @abstractmethod
    def Handle(self, analysis: HermesAnalysis, line: OpcodeEntry) -> OpcodeResult:
        """
        Process a Hermes bytecode opcode and produce a corresponding JavaScript variable or result.

        Args:
            analysis (HermesAnalysis): The analysis context containing variables and state.
            line (OpcodeEntry): The opcode entry to process, including opcode name and arguments.

        Returns:
            OpcodeResult: The result of processing the opcode, including the processed line and
                         a JSVariable (or error information if processing fails).
        """
        pass

    @classmethod
    def GetHandler(cls, opcode: str) -> Optional['OpcodeHandler']:
        return cls.registry.get(opcode)

    @classmethod
    def InvalidArgs(cls, analysis: HermesAnalysis, entry: OpcodeEntry,
                    error_detail: str = "Invalid arguments") -> OpcodeResult:
        error_msg = f"// Error: {cls.__name__} at address {entry.address}: {error_detail}: {entry.args}"

        variable = JSVariable(cls.__name__, entry.address, "", error_msg)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @classmethod
    def Exception(cls, analysis: HermesAnalysis, entry: OpcodeEntry, error: str) -> OpcodeResult:
        variable = JSVariable(cls.__name__, entry.address, "", error)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @classmethod
    def GetFuncArgs(cls, analysis: HermesAnalysis, regs: list[int]) -> list[str]:
        args = []

        for reg in regs:
            variable = analysis.registers.get(f"r{reg}")

            if (
                    variable
                    and variable.handler != "ResumeGenerator"
                    and not variable.handler.endswith("Environment")
            ):
                variable.used = True
                args.append(variable.value)
            else:
                args.append(f"r{reg}")

        return args

    @classmethod
    def GetVariableByReg(cls, analysis: HermesAnalysis, reg: int) -> JSVariable | None:
        variable = analysis.registers.get(f"r{reg}")

        if (
                variable
                and variable.handler != "ResumeGenerator"
                and not variable.handler.endswith("Environment")
        ):
            variable.used = True
            return variable

        return None

    @classmethod
    def GetValueByReg(cls, analysis: HermesAnalysis, reg: int) -> str:

        variable = analysis.registers.get(f"r{reg}")

        if (
                variable
                and variable.handler != "ResumeGenerator"
                and not variable.handler.endswith("Environment")
        ):
            variable.used = True
            return variable.value

        return f"r{reg}"
