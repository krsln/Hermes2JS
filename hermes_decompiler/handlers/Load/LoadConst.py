from __future__ import annotations

import re
from abc import ABC
from typing import ClassVar

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, sequence
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

_REG_PATTERN = sequence(REG)
_UINT8_PATTERN = sequence(REG, UINT8)
_STRING_PATTERN = sequence(REG, r"string_id:\s*(\d+)")
_INT_PATTERN = re.compile(
    r"^Reg8:\s*(\d+),\s*Imm32:\s*(-?\d+)$"
)
_DOUBLE_PATTERN = re.compile(
    r"^Reg8:\s*(\d+),\s*Double:\s*(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)$"
)

# ---------------------------------------------------------------------------
# Base classes
# ---------------------------------------------------------------------------

class LoadConstBase(OpcodeHandler, ABC):
    """
    Base class for all LoadConst opcodes.
    """

    _PATTERN = _REG_PATTERN

    def _CreateVariable(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
            register: int,
            value: str,
    ) -> OpcodeResult:
        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            f"r{register}",
            value,
        )

        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadSimpleConst(LoadConstBase):
    """
    Base class for simple constant loaders.

        Reg8
    """

    CONSTANT: ClassVar[str]

    def Handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected Reg8 argument",
            )

        register = int(match.group(1))

        return self._CreateVariable(
            analysis,
            entry,
            register,
            self.CONSTANT,
        )


# ---------------------------------------------------------------------------
# Simple constants
# ---------------------------------------------------------------------------

class LoadConstZero(LoadSimpleConst):
    CONSTANT = "0"


class LoadConstUndefined(LoadSimpleConst):
    CONSTANT = "undefined"


class LoadConstNull(LoadSimpleConst):
    CONSTANT = "null"


class LoadConstTrue(LoadSimpleConst):
    CONSTANT = "true"


class LoadConstFalse(LoadSimpleConst):
    CONSTANT = "false"


class LoadConstEmpty(LoadSimpleConst):
    CONSTANT = "empty"


# ---------------------------------------------------------------------------
# Numeric constants
# ---------------------------------------------------------------------------

class LoadConstUInt8(LoadConstBase):
    _PATTERN = _UINT8_PATTERN

    def Handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected Reg8, UInt8",
            )

        register = int(match.group(1))
        value = match.group(2)

        return self._CreateVariable(
            analysis,
            entry,
            register,
            value,
        )


class LoadConstInt(LoadConstBase):
    _PATTERN = _INT_PATTERN

    def Handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected Reg8, Imm32",
            )

        register = int(match.group(1))
        value = match.group(2)

        return self._CreateVariable(
            analysis,
            entry,
            register,
            value,
        )


class LoadConstDouble(LoadConstBase):
    _PATTERN = _DOUBLE_PATTERN

    def Handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected Reg8, Double",
            )

        register = int(match.group(1))
        value = match.group(2)

        return self._CreateVariable(
            analysis,
            entry,
            register,
            value,
        )


# ---------------------------------------------------------------------------
# String constants
# ---------------------------------------------------------------------------

class LoadConstString(LoadConstBase):
    _PATTERN = _STRING_PATTERN

    def ResolveString(
            self,
            analysis: HermesAnalysis,
            string_id: str,
    ) -> str:
        return analysis.stringTable.get(
            string_id,
            f"str_{string_id}",
        )

    def Handle(
            self,
            analysis: HermesAnalysis,
            entry: OpcodeEntry,
    ) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(
                analysis,
                entry,
                "Expected Reg8, string_id",
            )

        register = int(match.group(1))
        string_id = match.group(2)

        value = f'"{self.ResolveString(analysis, string_id)}"'

        return self._CreateVariable(
            analysis,
            entry,
            register,
            value,
        )


class LoadConstStringLongIndex(LoadConstString):
    """
    UInt32 string index variant.
    """
    pass
