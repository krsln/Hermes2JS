from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Optional

from hermes_decompiler.core.logging import get_logger
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
    def build_invalid_args_result(cls, analysis: HermesAnalysis, entry: OpcodeEntry,
                                  error_detail: str = "Invalid arguments") -> OpcodeResult:
        logger.warning(
            "Invalid arguments for opcode '%s' at address %d: %s (args=%r)",
            entry.opcode,
            entry.address,
            error_detail,
            entry.args,
        )

        error_msg = f"// Error: {cls.__name__} at address {entry.address}: "    f"{error_detail}: {entry.args}"
        result = OpcodeResult(entry, value=RawExpression(source=error_msg))
        analysis.add_result(result)

        return result

    @classmethod
    def build_exception_result(cls, analysis: HermesAnalysis, entry: OpcodeEntry, error: str) -> OpcodeResult:
        logger.error("%s failed while processing opcode '%s' at address %d: %s",
                     cls.__name__, entry.opcode, entry.address, error)

        result = OpcodeResult(entry, value=RawExpression(source=error))
        analysis.add_result(result)

        return result

    @classmethod
    def get_register_expression(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Return the current expression assigned to a register.

        This exposes the actual IR node currently stored in the register
        (ObjectExpression, Literal, BinaryExpression, CallExpression, etc.)
        and should only be used by optimization or analysis passes that need
        the defining expression.

        If the register has never been defined, fall back to its symbolic
        identifier.
        """

        result = analysis.registers.get(f"r{reg}")

        if result is None:
            return Identifier(name=f"r{reg}")

        if isinstance(result.value, Expression):
            result.definition_used = True
            return result.value

        return Identifier(name=f"r{reg}")

    @classmethod
    def get_register_reference(cls, analysis: HermesAnalysis, reg: int) -> Identifier:
        """
        Return a symbolic reference to a register.

        Unlike get_register_expression(), this never inlines the expression
        currently stored in the register. It always returns the register
        identifier itself (e.g. Identifier('r3')).

        This should be used by almost every opcode handler because Hermes
        bytecode operands refer to registers, not to the expressions that
        originally defined them.
        """

        result = analysis.registers.get(f"r{reg}")

        if result is not None:
            result.register_read = True

        return Identifier(name=f"r{reg}")
