from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Optional

from hermes_decompiler.ir import Expression, Identifier, RawExpression
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

    registry: Dict[str, "OpcodeHandler"] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__name__ != "OpcodeHandler":
            OpcodeHandler.registry[cls.__name__] = cls()

    @abstractmethod
    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        """
        Process a Hermes bytecode opcode and produce a corresponding
        JavaScript variable or result.
        """
        ...

    @classmethod
    def get_handler(cls, opcode: str) -> Optional["OpcodeHandler"]:
        return cls.registry.get(opcode)

    @classmethod
    def build_invalid_args_result(
        cls,
        analysis: HermesAnalysis,
        entry: OpcodeEntry,
        error_detail: str = "Invalid arguments",
    ) -> OpcodeResult:
        error_msg = (
            f"// Error: {cls.__name__} at address {entry.address}: "
            f"{error_detail}: {entry.args}"
        )
        logger.warning(
            "%s at address %s: %s (args=%r)",
            cls.__name__, entry.address, error_detail, entry.args,
        )

        variable = JSVariable(
            cls.__name__, entry.address, "", RawExpression(error_msg),
        )
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @classmethod
    def build_exception_result(
        cls,
        analysis: HermesAnalysis,
        entry: OpcodeEntry,
        error: str,
    ) -> OpcodeResult:
        logger.error(
            "%s raised at address %s: %s", cls.__name__, entry.address, error,
        )

        variable = JSVariable(
            cls.__name__, entry.address, "", RawExpression(error),
        )
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @classmethod
    def get_register_variable(cls, analysis: HermesAnalysis, reg: int) -> JSVariable | None:
        variable = cls._get_register_variable(analysis, reg)

        if not variable:
            return None

        variable.used = True
        return variable

    @classmethod
    def get_register_value(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Resolve the current value of a register as an IR expression.

        Falls back to a plain `Identifier(f"r{reg}")` when the register
        hasn't been assigned yet in this analysis pass (e.g. it's a
        parameter, or the assigning instruction wasn't tracked) - this is
        the direct replacement for the old `RegisterValue` node, which no
        longer exists as a separate IR type.
        """

        variable = cls._get_register_variable(analysis, reg)

        if not variable:
            return Identifier(name=f"r{reg}")

        if isinstance(variable.value, Expression):
            value = variable.value
        else:
            value = Identifier(name=f"r{reg}")

        variable.used = True
        return value

    @classmethod
    def _get_register_variable(cls, analysis: HermesAnalysis, reg: int) -> JSVariable | None:
        variable = analysis.registers.get(f"r{reg}")

        if variable:
            return variable

        return None