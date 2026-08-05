from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Optional

from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import Expression, Identifier, RawExpression
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
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

    Dispatch resolves handlers by exact class name (`OpcodeEntry.opcode`),
    so every registered class name must be a real Hermes opcode. Shared
    logic between related opcodes should live directly on one of the real
    opcode classes (the others subclass it and override just what differs -
    see e.g. `Add`/`Sub`/`Mul` in `handlers/arithmetic/Binary.py`), rather
    than on a separate non-opcode base class. If a genuinely non-opcode
    helper class is unavoidable, set `_abstract = True` on it so it is
    skipped here instead of being instantiated and registered under its
    own (non-opcode) name.

    `_abstract` is deliberately a plain class attribute rather than relying
    on `abc.abstractmethod` + instantiation failure: `__init_subclass__`
    runs *during* class creation, before `ABCMeta` finishes computing
    `__abstractmethods__` on the new class, so instantiating an
    ABC-abstract subclass here can silently succeed instead of raising -
    the instantiation-time abstractness check simply isn't active yet at
    that point. Don't rely on `ABC`/`@abstractmethod` alone to keep a base
    class out of the registry; use `_abstract = True` explicitly.
    """

    registry: Dict[str, "OpcodeHandler"] = {}

    #: Set to True on a class (not inherited implicitly - see
    #: `__init_subclass__` below) to opt it out of registration. Only
    #: meant for genuine non-opcode helper/mixin classes.
    _abstract: bool = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.__name__ == "OpcodeHandler":
            return

        # Only a class's OWN `_abstract = True` opts it out - it must not
        # be inherited, or a real opcode subclassing an abstract base
        # would silently stay unregistered too.
        if cls.__dict__.get("_abstract", False):
            return

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

        state = analysis.registers.get(f"r{reg}")

        if state is None or state.definition is None:
            return Identifier(name=f"r{reg}_undefined")

        state_value = state.value
        if isinstance(state_value, Expression):
            state.reads += 1
            state.definition.definition_used = True
            return state_value

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

        state = analysis.registers.get(f"r{reg}")

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        if state is not None:
            state.reads += 1

        return Identifier(name=f"r{reg}")
