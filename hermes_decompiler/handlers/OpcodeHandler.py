from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Optional

from hermes_decompiler.core import get_logger
from hermes_decompiler.ir.expressions import Expression, Identifier, RawExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis

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
        Process a Hermes bytecode opcode and produce the corresponding
        `OpcodeResult`.
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

        result = OpcodeResult(entry, value=RawExpression(source=error_msg))
        analysis.add_result(result)

        return result

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

        result = OpcodeResult(entry, value=RawExpression(source=error))
        analysis.add_result(result)

        return result

    @classmethod
    def get_register_variable(cls, analysis: HermesAnalysis, reg: int) -> OpcodeResult | None:
        result = cls._get_register_result(analysis, reg)

        if not result:
            return None

        result.used = True
        return result

    @classmethod
    def get_register_value(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Resolve the current value of a register as an IR expression.

        Falls back to a plain `Identifier(f"r{reg}")` when the register
        hasn't been assigned yet in this analysis pass (e.g. it's a
        parameter, or the assigning instruction wasn't tracked).
        """

        result = cls._get_register_result(analysis, reg)

        if not result:
            return Identifier(name=f"r{reg}")

        if isinstance(result.value, Expression):
            value = result.value
        else:
            value = Identifier(name=f"r{reg}")

        result.used = True
        return value

    @classmethod
    def _get_register_result(cls, analysis: HermesAnalysis, reg: int) -> OpcodeResult | None:
        return analysis.registers.get(f"r{reg}")
