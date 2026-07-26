from abc import ABC
from typing import ClassVar

from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.expressions import Expression, Identifier, NewExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


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

        match = self.Pattern().match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, ArgCount")

        dest_reg, func_reg, arg_count = map(int, match.groups())

        constructor = self.get_register_value(analysis, func_reg)
        arguments = self.resolve_arguments(analysis, func_reg, arg_count)

        # `ir.NewExpression` names this field `callee` (not `constructor`),
        # matching CallExpression's naming for consistency.
        expression = NewExpression(callee=constructor, arguments=arguments)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result

    def resolve_arguments(self, analysis: HermesAnalysis, func_reg: int, arg_count: int) -> tuple[Expression, ...]:
        values = [
            self.get_register_value(analysis, reg)
            for reg in range(func_reg - arg_count, func_reg)
        ]

        # Hermes CreateThis inserts an implicit "this" as the first
        # constructor argument slot; `ThisValue` no longer exists as a
        # distinct type (see decision on RegisterValue/ThisValue ->
        # Identifier), so the check becomes a name comparison.
        if values and isinstance(values[0], Identifier) and values[0].name == "this":
            values = values[1:]

        return tuple(values)


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
