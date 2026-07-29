from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Tuple

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

# --------------------------------------------------------------------------
# Patterns
# --------------------------------------------------------------------------
_JMP_PATTERN = sequence(ADDR)
_JMP_CONDITIONAL_PATTERN = sequence(ADDR, REG)
_JMP_BUILTIN_PATTERN = sequence(ADDR, UINT8, REG)
_JMP_TYPEOF_PATTERN = sequence(ADDR, REG, UINT16)

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
# Parsers
# --------------------------------------------------------------------------
def _parse_jump(entry: OpcodeEntry) -> int:
    match = _JMP_PATTERN.match(entry.args.strip())
    if not match:
        raise ValueError(f"Invalid arguments: {entry.args}")
    return int(match.group(1))


def _parse_conditional(entry: OpcodeEntry) -> Tuple[int, int]:
    match = _JMP_CONDITIONAL_PATTERN.match(entry.args.strip())
    if not match:
        raise ValueError(f"Invalid arguments: {entry.args}")
    return int(match.group(1)), int(match.group(2))


def _parse_builtin(entry: OpcodeEntry) -> Tuple[int, int, int]:
    match = _JMP_BUILTIN_PATTERN.match(entry.args.strip())
    if not match:
        raise ValueError(f"Invalid arguments: {entry.args}")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def _parse_typeof(entry: OpcodeEntry) -> Tuple[int, int, int]:
    match = _JMP_TYPEOF_PATTERN.match(entry.args.strip())
    if not match:
        raise ValueError(f"Invalid arguments: {entry.args}")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


# --------------------------------------------------------------------------
# Base Jump (Unconditional)
# --------------------------------------------------------------------------
class Jump(OpcodeHandler):
    """Base class for unconditional jumps."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            offset = _parse_jump(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        terminator = TerminatorJump(target=target)

        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


class Jmp(Jump):
    pass


class JmpLong(Jump):
    pass


# --------------------------------------------------------------------------
# Base Conditional Jump
# --------------------------------------------------------------------------
class ConditionalJumpBase(OpcodeHandler, ABC):
    @abstractmethod
    def parse(self, entry: OpcodeEntry) -> tuple[int, int, tuple]:
        """Returns: (offset, register, extra_args)"""
        ...

    @abstractmethod
    def build_condition(self, value: Expression, *extra: Any) -> Expression:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            offset, reg, extra = self.parse(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        value = self.get_register_value(analysis, reg)
        condition = self.build_condition(value, *extra)

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# --------------------------------------------------------------------------
# Normal Conditional Jumps
# --------------------------------------------------------------------------
class ConditionalJump(ConditionalJumpBase, ABC):
    def parse(self, entry: OpcodeEntry) -> tuple[int, int, tuple]:
        offset, reg = _parse_conditional(entry)
        return offset, reg, ()


class JmpTrue(ConditionalJump):
    def build_condition(self, value: Expression, *extra: Any):
        return value


class JmpFalse(ConditionalJump):
    def build_condition(self, value: Expression, *extra: Any) -> Expression:
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, value)


class JmpUndefined(ConditionalJump):
    def build_condition(self, value: Expression, *extra: Any) -> Expression:
        return BinaryExpression(value, BinaryOperator.STRICT_EQUAL, UndefinedLiteral())


class JmpTrueLong(JmpTrue): pass


class JmpFalseLong(JmpFalse): pass


class JmpUndefinedLong(JmpUndefined): pass


# --------------------------------------------------------------------------
# Builtin Conditional Jumps
# --------------------------------------------------------------------------
class BuiltinConditionalJump(ConditionalJumpBase, ABC):
    def parse(self, entry: OpcodeEntry) -> tuple[int, int, tuple]:
        offset, builtin, reg = _parse_builtin(entry)
        return offset, reg, (builtin,)


# DEFINE_OPCODE_3(JmpBuiltinIs, Addr8, UInt8, Reg8)
class JmpBuiltinIs(BuiltinConditionalJump):
    def build_condition(self, value: Expression, *extra: Any) -> Expression:
        builtin = extra[0]
        return BinaryExpression(value, BinaryOperator.STRICT_EQUAL, Identifier(name=f"builtin_{builtin}"))


# DEFINE_OPCODE_3(JmpBuiltinIsNot, Addr8, UInt8, Reg8)
class JmpBuiltinIsNot(BuiltinConditionalJump):
    def build_condition(self, value: Expression, *extra: Any) -> Expression:
        builtin = extra[0]
        return BinaryExpression(value, BinaryOperator.STRICT_NOT_EQUAL, Identifier(name=f"builtin_{builtin}"))


# DEFINE_OPCODE_3(JmpBuiltinIsLong, Addr32, UInt8, Reg8)
class JmpBuiltinIsLong(JmpBuiltinIs): pass


# DEFINE_OPCODE_3(JmpBuiltinIsNotLong, Addr32, UInt8, Reg8)
class JmpBuiltinIsNotLong(JmpBuiltinIsNot): pass


# --------------------------------------------------------------------------
# TypeOf Conditional Jump
# --------------------------------------------------------------------------
class TypeOfConditionalJump(ConditionalJumpBase, ABC):
    def parse(self, entry: OpcodeEntry) -> tuple[int, int, tuple]:
        offset, reg, type_id = _parse_typeof(entry)
        type_name = TYPEOF_MAP.get(type_id, f"<{type_id}>")
        return offset, reg, (type_name,)


# DEFINE_OPCODE_3(JmpTypeOfIs, Addr32, Reg8, UInt16)
class JmpTypeOfIs(TypeOfConditionalJump):
    def build_condition(self, value: Expression, *extra: Any) -> Expression:
        type_name = extra[0]
        return BinaryExpression(
            UnaryExpression(UnaryOperator.TYPEOF, value),
            BinaryOperator.STRICT_EQUAL,
            StringLiteral(type_name),
        )
