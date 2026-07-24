from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple

from hermes_decompiler.ir.Expressions import UnaryExpression, BinaryExpression, Expression, TypeOfExpression
from hermes_decompiler.ir.Statements import IfStatement, GotoStatement
from hermes_decompiler.ir.Values import Value, UndefinedValue, ConstantValue, BuiltinValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult, ControlFlowType

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT16, ADDR, sequence

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

    return (
        int(match.group(1)),
        int(match.group(2)),
    )


def _parse_builtin(entry: OpcodeEntry) -> Tuple[int, int, int]:
    match = _JMP_BUILTIN_PATTERN.match(entry.args.strip())
    if not match:
        raise ValueError(f"Invalid arguments: {entry.args}")

    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )


def _parse_typeof(entry: OpcodeEntry) -> Tuple[int, int, int]:
    match = _JMP_TYPEOF_PATTERN.match(entry.args.strip())
    if not match:
        raise ValueError(f"Invalid arguments: {entry.args}")

    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )


# --------------------------------------------------------------------------
# Base Jump
# --------------------------------------------------------------------------

class Jump(OpcodeHandler):
    """Base class for unconditional jumps."""

    def handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:

        handler = self.__class__.__name__

        try:
            offset = _parse_jump(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        variable = JSVariable(
            handler,
            entry.address,
            "",
            GotoStatement(target),
        )

        analysis.add_result(
            entry,
            variable,
            goto=target,
        )

        return OpcodeResult(
            entry,
            variable,
            goto=target,
            control_flow=ControlFlowType.UNCONDITIONAL,
        )


class Jmp(Jump):
    pass


class JmpLong(Jump):
    pass


# --------------------------------------------------------------------------
# Base Conditional Jump
# --------------------------------------------------------------------------

class ConditionalJump(OpcodeHandler, ABC):

    @abstractmethod
    def build_condition(self, value: Value) -> Value:
        ...

    def handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:

        handler = self.__class__.__name__

        try:
            offset, reg = _parse_conditional(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        value = self.get_register_value_new(analysis, reg)
        condition = self.build_condition(value)

        variable = JSVariable(
            handler,
            entry.address,
            "",
            IfStatement(
                condition=condition,
                target=target,
            ),
        )

        analysis.add_result(
            entry,
            variable,
            goto=target,
        )

        return OpcodeResult(
            entry,
            variable,
            goto=target,
            control_flow=ControlFlowType.CONDITIONAL,
        )


class JmpTrue(ConditionalJump):

    def build_condition(self, value: Value) -> Value:
        return value


class JmpFalse(ConditionalJump):

    def build_condition(self, value: Value) -> Value:
        return UnaryExpression(
            operator="!",
            operand=value,
        )


class JmpUndefined(ConditionalJump):

    def build_condition(self, value: Value) -> Value:
        return BinaryExpression(
            left=value,
            operator="===",
            right=UndefinedValue(),
        )


class JmpTrueLong(JmpTrue):
    pass


class JmpFalseLong(JmpFalse):
    pass


class JmpUndefinedLong(JmpUndefined):
    pass


# --------------------------------------------------------------------------
# Builtin Conditional Jump
# --------------------------------------------------------------------------

class BuiltinConditionalJump(OpcodeHandler, ABC):

    @abstractmethod
    def build_condition(self, value: Value, builtin: int) -> Value:
        ...

    def handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:

        handler = self.__class__.__name__

        try:
            offset, builtin, reg = _parse_builtin(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        value = self.get_register_value_new(analysis, reg)

        condition = self.build_condition(value, builtin)

        variable = JSVariable(
            handler,
            entry.address,
            "",
            IfStatement(
                condition=condition,
                target=target,
            ),
        )

        analysis.add_result(
            entry,
            variable,
            goto=target,
        )

        return OpcodeResult(
            entry,
            variable,
            goto=target,
            control_flow=ControlFlowType.CONDITIONAL,
        )


class JmpBuiltinIs(BuiltinConditionalJump):

    def build_condition(
            self,
            value: Value,
            builtin: int,
    ) -> Value:
        return BinaryExpression(
            left=value,
            operator="===",
            right=BuiltinValue(builtin),
        )


class JmpBuiltinIsNot(BuiltinConditionalJump):

    def build_condition(
            self,
            value: Value,
            builtin: int,
    ) -> Value:
        return BinaryExpression(
            left=value,
            operator="!==",
            right=BuiltinValue(builtin),
        )


class JmpBuiltinIsLong(JmpBuiltinIs):
    pass


class JmpBuiltinIsNotLong(JmpBuiltinIsNot):
    pass


# --------------------------------------------------------------------------
# TypeOf Conditional Jump
# --------------------------------------------------------------------------

class TypeOfConditionalJump(OpcodeHandler, ABC):

    @abstractmethod
    def build_condition(
            self,
            value: Value,
            type_name: str,
    ) -> Value:
        ...

    def handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:

        handler = self.__class__.__name__

        try:
            offset, reg, type_id = _parse_typeof(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        value = self.get_register_value_new(analysis, reg)

        condition = self.build_condition(
            value,
            TYPEOF_MAP.get(type_id, f"<{type_id}>"),
        )

        variable = JSVariable(
            handler,
            entry.address,
            "",
            IfStatement(
                condition=condition,
                target=target,
            ),
        )

        analysis.add_result(
            entry,
            variable,
            goto=target,
        )

        return OpcodeResult(
            entry,
            variable,
            goto=target,
            control_flow=ControlFlowType.CONDITIONAL,
        )


class JmpTypeOfIs(TypeOfConditionalJump):

    def build_condition(self, value: Value, type_name: str) -> Value:
        return BinaryExpression(
            left=TypeOfExpression(value),
            operator="===",
            right=ConstantValue(type_name),
        )
