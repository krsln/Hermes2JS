from abc import ABC
from typing import ClassVar

from hermes_decompiler.ir.Expressions import NewExpression
from hermes_decompiler.ir.Values import ThisValue, Value
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    UINT32,
    sequence,
)


class ConstructBase(OpcodeHandler, ABC):
    """
    Base implementation for Construct opcodes.

    Hermes semantics:

        dest = new closure(arg1, arg2, ...)

    Arguments are stored immediately before the closure register.

    Example:

        Construct r2, r8, 3

    Means

        r2 = new r8(r5, r6, r7)
    """

    ARG_PATTERN: ClassVar[str] = UINT8

    @classmethod
    def Pattern(cls):
        return sequence(REG, REG, cls.ARG_PATTERN)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        handler = self.__class__.__name__

        match = self.Pattern().match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, ArgCount")

        dest_reg, func_reg, arg_count = map(int, match.groups())

        constructor = self.get_register_value(analysis, func_reg)
        arguments = self.resolve_arguments(analysis, func_reg, arg_count)

        value = NewExpression(
            constructor=constructor,
            arguments=arguments,
        )

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    def resolve_arguments(self, analysis: HermesAnalysis, func_reg: int, arg_count: int) -> list[Value]:
        values = [
            self.get_register_value(analysis, reg)
            for reg in range(func_reg - arg_count, func_reg)
        ]

        # Hermes CreateThis inserts an implicit "this"
        if values and isinstance(values[0], ThisValue):
            values = values[1:]

        return values


class Construct(ConstructBase):
    """
    Construct using UInt8 argument count.
    """
    ARG_PATTERN = UINT8


class ConstructLong(ConstructBase):
    """
    Construct using UInt32 argument count.
    """
    ARG_PATTERN = UINT32
