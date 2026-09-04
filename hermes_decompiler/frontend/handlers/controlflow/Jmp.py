from __future__ import annotations

from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, ADDR, UINT8, UINT16
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import (
    Expression,
    UnaryExpression,
    BinaryExpression,
    UndefinedLiteral,
    StringLiteral,
    Identifier,
)
from hermes_decompiler.ir.terminators import TerminatorJump, TerminatorConditionalBranch


# --------------------------------------------------------------------------
# Jmp (Unconditional)
# --------------------------------------------------------------------------

# Addr8 (total size 1)
# Example: <Jmp>: <Addr8: 40>  # Address: 00000068
class Jmp(OpcodeHandler):
    """Unconditional jump."""

    ARGUMENTS = ArgsPattern(sequence(ADDR), "Addr8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        offset = int(match.group(1))

        target = ctx.entry.target_address or (ctx.entry.address + offset)
        ctx.analysis.gotoList.append(target)

        terminator = TerminatorJump(target=target)
        # print(
        #     f"{ctx.entry.opcode}: "
        #     f"address={ctx.entry.address}, "
        #     f"offset={offset}, "
        #     f"target={target}, "
        #     f"calculated={ctx.entry.address + offset}"
        # )

        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Addr32 (total size 4)
# Example: <JmpLong>: <Addr32: 129>  # Address: 000000d9
class JmpLong(Jmp):
    """Long unconditional jump."""
    pass


# --------------------------------------------------------------------------
# Conditional jumps
# --------------------------------------------------------------------------

# Addr8, Reg8 (total size 2)
# Example: <JmpTrue>: <Addr8: 54, Reg8: 5>  # Address: 000003e6
class JmpTrue(OpcodeHandler):
    """
    Conditional jump on Arg2 truthiness, and shared base implementation
    for the rest of the single-register conditional jumps (`JmpFalse`,
    `JmpUndefined`). See `Add` in `handlers/arithmetic/Binary.py` for why
    a real opcode - rather than a separate non-opcode `ABC` base class -
    is used as the shared base.
    """

    ARGUMENTS = ArgsPattern(sequence(ADDR, REG), "Addr8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        offset, reg = map(int, match.groups())

        target = ctx.entry.target_address or (ctx.entry.address + offset)
        ctx.analysis.gotoList.append(target)

        condition = self.build_condition(self.get_register_expression(ctx.analysis, reg))

        terminator = TerminatorConditionalBranch(condition=condition, target=target)
        # print(
        #     f"{ctx.entry.opcode}: "
        #     f"address={ctx.entry.address}, "
        #     f"offset={offset}, "
        #     f"target={target}, "
        #     f"calculated={ctx.entry.address + offset}"
        # )

        # pure control flow: no operand value of its own
        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=None)
        ctx.analysis.add_result(result)

        return result

    def build_condition(self, value: Expression) -> Expression:
        """Subclasses override this to change only the condition."""
        return value


# Addr32, Reg8 (total size 5)
# Example: <JmpTrueLong>: <Addr32: 997, Reg8: 1>  # Address: 000003e9
class JmpTrueLong(JmpTrue):
    pass


# Addr8, Reg8 (total size 2)
# Example: <JmpFalse>: <Addr8: 18, Reg8: 1>  # Address: 00000025
class JmpFalse(JmpTrue):
    def build_condition(self, value: Expression) -> Expression:
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, value)


# Addr32, Reg8 (total size 5)
# Example: <JmpFalseLong>: <Addr32: 143, Reg8: 5>  # Address: 000000d9
class JmpFalseLong(JmpFalse):
    pass


# Addr8, Reg8 (total size 2)
# Example: <JmpUndefined>: <Addr8: 38, Reg8: 5>  # Address: 0000004e
class JmpUndefined(JmpTrue):
    def build_condition(self, value: Expression) -> Expression:
        return BinaryExpression(value, BinaryOperator.STRICT_EQUAL, UndefinedLiteral())


# Addr32, Reg8 (total size 5)
class JmpUndefinedLong(JmpUndefined):
    pass


# --------------------------------------------------------------------------
# Builtin conditional jumps
# --------------------------------------------------------------------------
# Addr8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(JmpBuiltinIs, Addr8, UInt8, Reg8)
# Example:
class JmpBuiltinIs(OpcodeHandler):
    """
    `JmpBuiltinIs` conditional jump, and shared base implementation for
    `JmpBuiltinIsNot`. See `Add` in `handlers/arithmetic/Binary.py` for
    why a real opcode is used as the shared base instead of a separate
    non-opcode `ABC` class.
    """

    ARGUMENTS = ArgsPattern(sequence(ADDR, UINT8, REG), "Addr8, UInt8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        offset, builtin, reg = map(int, match.groups())

        target = ctx.entry.target_address or (ctx.entry.address + offset)
        ctx.analysis.gotoList.append(target)

        builtin_name = f"builtin_{builtin}"
        if ctx.entry.builtin_function is not None:
            builtin_name = ctx.entry.builtin_function.name

        expression = self.get_register_expression(ctx.analysis, reg)
        builtin_expression = Identifier(name=builtin_name)

        condition = self.build_condition(expression, builtin_expression)

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=None)
        ctx.analysis.add_result(result)

        return result

    def build_condition(self, value: Expression, builtin: Expression) -> Expression:
        return BinaryExpression(value, BinaryOperator.STRICT_EQUAL, builtin)


# Addr32, UInt8, Reg8 (total size 6)
# DEFINE_OPCODE_3(JmpBuiltinIsLong, Addr32, UInt8, Reg8)
# Example:
class JmpBuiltinIsLong(JmpBuiltinIs):
    pass


# Addr8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(JmpBuiltinIsNot, Addr8, UInt8, Reg8)
# Example:
class JmpBuiltinIsNot(JmpBuiltinIs):
    def build_condition(self, value: Expression, builtin: Expression) -> Expression:
        return BinaryExpression(value, BinaryOperator.STRICT_NOT_EQUAL, builtin)


# Addr32, UInt8, Reg8 (total size 6)
# DEFINE_OPCODE_3(JmpBuiltinIsNotLong, Addr32, UInt8, Reg8)
# Example:
class JmpBuiltinIsNotLong(JmpBuiltinIsNot):
    pass


# --------------------------------------------------------------------------
# TypeOf conditional jumps
# --------------------------------------------------------------------------

# /// Jump if the type matches the TypeOfIsTypes in Arg3.
# /// Arg1 is the target.
# /// Arg2 is the value to test.
# /// Arg3 is the TypeOfIsTypes (see Typeof.h).
# DEFINE_OPCODE_3(JmpTypeOfIs, Addr32, Reg8, UInt16)

# Addr32, Reg8, UInt16 (total size 7)
# DEFINE_OPCODE_3(JmpTypeOfIs, Addr32, Reg8, UInt16)
# Example: <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000031
class JmpTypeOfIs(OpcodeHandler):
    """Jump if the type matches the TypeOfIsTypes in Arg3."""

    TYPEOF_FLAGS = {
        1 << 0: "undefined",
        1 << 1: "null",
        1 << 2: "boolean",
        1 << 3: "number",
        1 << 4: "string",
        1 << 5: "symbol",
        1 << 6: "bigint",
        1 << 7: "function",
        1 << 8: "object",
    }

    ARGUMENTS = ArgsPattern(sequence(ADDR, REG, UINT16), "Addr32, Reg8, UInt16")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        offset, reg, type_id = map(int, match.groups())

        target = ctx.entry.target_address if ctx.entry.target_address is not None else (ctx.entry.address + offset)
        ctx.analysis.gotoList.append(target)

        condition = self.build_typeof_condition(
            self.get_register_expression(ctx.analysis, reg), type_id
        )

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=None)
        ctx.analysis.add_result(result)

        return result

    @classmethod
    def build_typeof_condition(cls, value: Expression, mask: int) -> Expression:
        typeof_expr = UnaryExpression(UnaryOperator.TYPEOF, value)
        conditions = [
            BinaryExpression(typeof_expr, BinaryOperator.STRICT_EQUAL, StringLiteral(name))
            for bit, name in cls.TYPEOF_FLAGS.items()
            if mask & bit
        ]

        if not conditions:
            return BinaryExpression(typeof_expr, BinaryOperator.STRICT_EQUAL, StringLiteral(f"<mask:{mask}>"))

        result = conditions[0]
        for cond in conditions[1:]:
            result = BinaryExpression(result, LogicalOperator.OR, cond)

        return result
