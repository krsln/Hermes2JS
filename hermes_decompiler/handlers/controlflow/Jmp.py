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


class JmpTrue(ConditionalJump):
    def build_condition(self, value: Expression) -> Expression:
        return value


class JmpFalse(ConditionalJump):
    def build_condition(self, value: Expression) -> Expression:
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, value)


class JmpUndefined(ConditionalJump):
    def build_condition(self, value: Expression) -> Expression:
        return BinaryExpression(value, BinaryOperator.STRICT_EQUAL, UndefinedLiteral())


class JmpTrueLong(JmpTrue):
    pass


class JmpFalseLong(JmpFalse):
    pass


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


class JmpBuiltinIs(BuiltinConditionalJump):
    def build_condition(self, value: Expression, builtin: int) -> Expression:
        return BinaryExpression(
            value,
            BinaryOperator.STRICT_EQUAL,
            Identifier(name=f"builtin_{builtin}"),
        )


class JmpBuiltinIsNot(BuiltinConditionalJump):
    def build_condition(self, value: Expression, builtin: int) -> Expression:
        return BinaryExpression(
            value,
            BinaryOperator.STRICT_NOT_EQUAL,
            Identifier(name=f"builtin_{builtin}"),
        )


class JmpBuiltinIsLong(JmpBuiltinIs):
    pass


class JmpBuiltinIsNotLong(JmpBuiltinIsNot):
    pass


# --------------------------------------------------------------------------
# TypeOf conditional jumps
# --------------------------------------------------------------------------

class TypeOfConditionalJump(OpcodeHandler, ABC):
    _PATTERN = sequence(ADDR, REG, UINT16)

    @abstractmethod
    def build_condition(self, value: Expression, type_name: str) -> Expression:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, f"Invalid arguments: {entry.args}")

        offset, reg, type_id = map(int, match.groups())

        target = entry.target_address or (entry.address + offset)
        analysis.gotoList.append(target)

        condition = self.build_condition(
            self.get_register_expression(analysis, reg),
            TYPEOF_MAP.get(type_id, f"<{type_id}>"),
        )

        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


class JmpTypeOfIs(TypeOfConditionalJump):
    def build_condition(self, value: Expression, type_name: str) -> Expression:
        return BinaryExpression(
            UnaryExpression(UnaryOperator.TYPEOF, value),
            BinaryOperator.STRICT_EQUAL,
            StringLiteral(type_name),
        )
