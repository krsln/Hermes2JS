from __future__ import annotations

from abc import ABC, abstractmethod

from hermes_decompiler.analysis.terminators import TerminatorJump, TerminatorConditionalBranch
from hermes_decompiler.handlers import OpcodeHandler, REG, ADDR, UINT8, UINT16, sequence
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import (
    Expression,
    UnaryExpression,
    BinaryExpression,
    UndefinedLiteral,
    StringLiteral,
    Identifier,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis

TYPEOF_MAP = {
    0: "undefined",
    1: "object",
    2: "function",
    3: "string",
    4: "number",
    5: "boolean",
    6: "symbol",
    7: "bigint",
}


# --------------------------------------------------------------------------
# Jmp (Unconditional)
# --------------------------------------------------------------------------

# Addr8 (total size 1)
# Example: <Jmp>: <Addr8: 40>  # Address: 00000068
class Jmp(OpcodeHandler):
    """Unconditional jump."""

    _PATTERN = sequence(ADDR)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, f"Invalid arguments: {entry.args}")

        offset = int(match.group(1))

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        terminator = TerminatorJump(target=target)

        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# Addr32 (total size 4)
# Example: <JmpLong>: <Addr32: 129>  # Address: 000000d9
class JmpLong(Jmp):
    """Long unconditional jump."""
    pass


# --------------------------------------------------------------------------
# Conditional jumps
# --------------------------------------------------------------------------
class ConditionalJump(OpcodeHandler, ABC):
    _PATTERN = sequence(ADDR, REG)

    @abstractmethod
    def build_condition(self, value: Expression) -> Expression:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, f"Invalid arguments: {entry.args}")

        offset, reg = map(int, match.groups())

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        condition = self.build_condition(self.get_register_expression(analysis, reg))

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# Addr8, Reg8 (total size 2)
# Example: <JmpTrue>: <Addr8: 54, Reg8: 5>  # Address: 000003e6
class JmpTrue(ConditionalJump):
    def build_condition(self, value: Expression) -> Expression:
        return value


# Addr32, Reg8 (total size 5)
# Example: <JmpTrueLong>: <Addr32: 997, Reg8: 1>  # Address: 000003e9
class JmpTrueLong(JmpTrue):
    pass


# Addr8, Reg8 (total size 2)
# Example: <JmpFalse>: <Addr8: 18, Reg8: 1>  # Address: 00000025
class JmpFalse(ConditionalJump):
    def build_condition(self, value: Expression) -> Expression:
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, value)


# Addr32, Reg8 (total size 5)
# Example: <JmpFalseLong>: <Addr32: 143, Reg8: 5>  # Address: 000000d9
class JmpFalseLong(JmpFalse):
    pass


# Addr8, Reg8 (total size 2)
# Example: <JmpUndefined>: <Addr8: 38, Reg8: 5>  # Address: 0000004e
class JmpUndefined(ConditionalJump):
    def build_condition(self, value: Expression) -> Expression:
        return BinaryExpression(value, BinaryOperator.STRICT_EQUAL, UndefinedLiteral())


# Addr32, Reg8 (total size 5)
class JmpUndefinedLong(JmpUndefined):
    pass


# --------------------------------------------------------------------------
# Builtin conditional jumps
# --------------------------------------------------------------------------
class BuiltinConditionalJump(OpcodeHandler, ABC):
    _PATTERN = sequence(ADDR, UINT8, REG)

    @abstractmethod
    def build_condition(self, value: Expression, builtin: int) -> Expression:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, f"Invalid arguments: {entry.args}")

        offset, builtin, reg = map(int, match.groups())

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        condition = self.build_condition(self.get_register_expression(analysis, reg), builtin)

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# Addr8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(JmpBuiltinIs, Addr8, UInt8, Reg8)
# Example:
class JmpBuiltinIs(BuiltinConditionalJump):
    def build_condition(self, value: Expression, builtin: int) -> Expression:
        return BinaryExpression(
            value,
            BinaryOperator.STRICT_EQUAL,
            Identifier(name=f"builtin_{builtin}"),
        )


# Addr32, UInt8, Reg8 (total size 6)
# DEFINE_OPCODE_3(JmpBuiltinIsLong, Addr32, UInt8, Reg8)
# Example:
class JmpBuiltinIsLong(JmpBuiltinIs):
    pass


# Addr8, UInt8, Reg8 (total size 3)
# DEFINE_OPCODE_3(JmpBuiltinIsNot, Addr8, UInt8, Reg8)
# Example:
class JmpBuiltinIsNot(BuiltinConditionalJump):
    def build_condition(self, value: Expression, builtin: int) -> Expression:
        return BinaryExpression(
            value,
            BinaryOperator.STRICT_NOT_EQUAL,
            Identifier(name=f"builtin_{builtin}"),
        )


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
    _PATTERN = sequence(ADDR, REG, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, f"Invalid arguments: {entry.args}")

        offset, reg, type_id = map(int, match.groups())

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        condition = BinaryExpression(
            UnaryExpression(UnaryOperator.TYPEOF, self.get_register_expression(analysis, reg)),
            BinaryOperator.STRICT_EQUAL,
            StringLiteral(TYPEOF_MAP.get(type_id, f"<{type_id}>")),
        )

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result
