from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

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

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        try:
            offset = _parse_jump(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            f"goto label_{target};",
        )
        analysis.add_result(entry, variable, goto=target)

        return OpcodeResult(entry, variable, goto=target)


class Jmp(Jump):
    pass


class JmpLong(Jump):
    pass


# --------------------------------------------------------------------------
# Base Conditional Jump
# --------------------------------------------------------------------------

class ConditionalJump(OpcodeHandler, ABC):

    @abstractmethod
    def BuildCondition(self, value: str) -> str:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        try:
            offset, reg = _parse_conditional(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)
        value = self.get_register_value(analysis, reg)

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            f"if ({self.BuildCondition(value)}) {{ /* jump to label_{target} */ }}"
        )
        analysis.add_result(entry, variable, goto=target)

        return OpcodeResult(entry, variable, goto=target)


class JmpTrue(ConditionalJump):
    def BuildCondition(self, value: str) -> str:
        return value


class JmpFalse(ConditionalJump):
    def BuildCondition(self, value: str) -> str:
        return f"!{value}"


class JmpUndefined(ConditionalJump):
    def BuildCondition(self, value: str) -> str:
        return f"{value} === undefined"


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
    def build_condition(self, value: str, builtin: int) -> str:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        try:
            offset, builtin, reg = _parse_builtin(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)
        value = self.get_register_value(analysis, reg)

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            f"if ({self.build_condition(value, builtin)}) {{ /* jump to label_{target} */ }}"
        )
        analysis.add_result(entry, variable, goto=target)

        return OpcodeResult(entry, variable, goto=target)


class JmpBuiltinIs(BuiltinConditionalJump):
    def build_condition(self, value: str, builtin: int) -> str:
        return f"{value} === builtin_{builtin}"


class JmpBuiltinIsNot(BuiltinConditionalJump):
    def build_condition(self, value: str, builtin: int) -> str:
        return f"{value} !== builtin_{builtin}"


class JmpBuiltinIsLong(JmpBuiltinIs):
    pass


class JmpBuiltinIsNotLong(JmpBuiltinIsNot):
    pass


# --------------------------------------------------------------------------
# TypeOf Conditional Jump
# --------------------------------------------------------------------------

class TypeOfConditionalJump(OpcodeHandler, ABC):

    @abstractmethod
    def BuildCondition(self, value: str, type_name: str) -> str:
        ...

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        try:
            offset, reg, type_id = _parse_typeof(entry)
        except ValueError as e:
            return self.build_invalid_args_result(analysis, entry, str(e))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)
        value = self.get_register_value(analysis, reg)
        type_name = TYPEOF_MAP.get(type_id, f"<{type_id}>")

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            f"if ({self.BuildCondition(value, type_name)}) {{ /* jump to label_{target} */ }}"
        )
        analysis.add_result(entry, variable, goto=target)

        return OpcodeResult(entry, variable, goto=target)


class JmpTypeOfIs(TypeOfConditionalJump):

    def BuildCondition(self, value: str, type_name: str) -> str:
        return f'typeof {value} == "{type_name}"'
