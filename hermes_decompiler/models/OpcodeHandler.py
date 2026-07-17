from abc import ABC, abstractmethod
from typing import Dict, Optional, List

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)


class OpcodeHandler(ABC):
    """
    Abstract base class for handling Hermes bytecode opcodes.

    Note on the `registry` dict: unlike `JSConverter._functionTable`, this
    class-level dict is *not* per-conversion mutable state - it's a
    write-once-at-import-time registry of stateless handler singletons
    (one instance per opcode, populated via __init_subclass__). That's a
    legitimate use of class-level storage and is left as-is.
    """
    registry: Dict[str, 'OpcodeHandler'] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__name__ != "OpcodeHandler":
            OpcodeHandler.registry[cls.__name__] = cls()

    @abstractmethod
    def Handle(self, analysis: HermesAnalysis, line: OpcodeEntry) -> OpcodeResult:
        """
        Process a Hermes bytecode opcode and produce a corresponding JavaScript
        variable or result.
        """
        pass

    @classmethod
    def GetHandler(cls, opcode: str) -> Optional['OpcodeHandler']:
        return cls.registry.get(opcode)

    @classmethod
    def InvalidArgs(cls, analysis: HermesAnalysis, entry: OpcodeEntry,
                     error_detail: str = "Invalid arguments") -> OpcodeResult:
        error_msg = f"// Error: {cls.__name__} at address {entry.address}: {error_detail}: {entry.args}"
        logger.warning("%s at address %s: %s (args=%r)", cls.__name__, entry.address, error_detail, entry.args)

        variable = JSVariable(cls.__name__, entry.address, "", error_msg)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @classmethod
    def Exception(cls, analysis: HermesAnalysis, entry: OpcodeEntry, error: str) -> OpcodeResult:
        logger.error("%s raised at address %s: %s", cls.__name__, entry.address, error)

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
