from abc import ABC, abstractmethod
from typing import Dict, Optional, List

from conversion.hermes2js.models.HermesAnalysis import HermesAnalysis
from conversion.hermes2js.models.JSVariable import JSVariable
from conversion.hermes2js.models.OpcodeResult import OpcodeResult
from conversion.hermes2js.models.OpcodeEntry import OpcodeEntry


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
    def GetFuncArgs(cls, results: List[OpcodeResult], args: list[int]) -> list[str]:
        sorted_variables = sorted(results, key=lambda x: x.Variable.address, reverse=True)

        argList = []
        for r in args:
            if not isinstance(r, int):
                raise ValueError(f"Expected integer register, got {r}")

            matching_var = next((var.Variable for var in sorted_variables if var.Variable.name == f"r{r}"), None)
            if (matching_var
                    # and not matching_var.handler.startswith('Call')
                    and not matching_var.handler.endswith('Environment')
            ):
                argList.append(matching_var.value)
                matching_var.used = True
            else:
                argList.append(f"r{r}")

        return argList

    @classmethod
    def GetVariableByReg(cls, results: List[OpcodeResult], obj_reg: int) -> JSVariable | None:
        sorted_variables = sorted(results, key=lambda x: x.Variable.address, reverse=True)

        func_name = f"r{obj_reg}"
        variable = next((var.Variable for var in sorted_variables if var.Variable.name == func_name), None)

        if (variable
                and variable.handler != 'ResumeGenerator'
                # and not variable.handler.startswith('Call')
                and not variable.handler.endswith('Environment')
        ):
            variable.used = True
            return variable

        return None

    @classmethod
    def GetValueByReg(cls, results: List[OpcodeResult], obj_reg: int) -> str:
        # sorted_variables = sorted(results, key=lambda x: getattr(x.Variable, 'address', 0), reverse=True)
        sorted_variables = sorted(results, key=lambda x: x.Variable.address, reverse=True)

        func_name = f"r{obj_reg}"
        variable = next((var.Variable for var in sorted_variables if var.Variable.name == func_name), None)

        if (variable
                and variable.handler != 'ResumeGenerator'
                # and not variable.handler.startswith('Call')
                and not variable.handler.endswith('Environment')
        ):
            func_name = variable.value
            variable.used = True

        return func_name
