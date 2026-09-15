from typing import ClassVar

from hermes_decompiler.frontend.handlers import (
    OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, STRING_ID, UINT8, IMM32, DOUBLE, BIGINT_ID
)
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import (
    Expression,
    UndefinedLiteral,
    StringLiteral,
    RawExpression,
    python_literal,
)


# ---------------------------------------------------------------------------
# Simple constants
# ---------------------------------------------------------------------------

# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadConstZero, Reg8)
# Example: <LoadConstZero>: <Reg8: 14>
class LoadConstZero(OpcodeHandler):
    """
    Load the constant `0`, and shared base implementation for the rest
    of the simple (`Reg8`-only) constant loaders. A real opcode is used
    as the shared base (rather than a separate non-opcode
    `LoadSimpleConst` class) - see `Add` in
    `handlers/arithmetic/Binary.py` for the rationale.
    """

    VALUE: ClassVar[Expression | object] = 0

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8 (total size 1)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        value = self.VALUE

        if not isinstance(value, Expression):
            value = python_literal(value)

        result = OpcodeResult(ctx.entry, value=value, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadConstTrue, Reg8)
# Example: <LoadConstTrue>: <Reg8: 4>
class LoadConstTrue(LoadConstZero):
    VALUE = True


# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadConstFalse, Reg8)
# Example: <LoadConstFalse>: <Reg8: 0>
class LoadConstFalse(LoadConstZero):
    VALUE = False


# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadConstNull, Reg8)
# Example: <LoadConstNull>: <Reg8: 1>
class LoadConstNull(LoadConstZero):
    VALUE = None


# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadConstUndefined, Reg8)
# Example: <LoadConstUndefined>: <Reg8: 0>
class LoadConstUndefined(LoadConstZero):
    VALUE = UndefinedLiteral()


# Reg8 (total size 1)
# DEFINE_OPCODE_1(LoadConstEmpty, Reg8)
# Example: <LoadConstEmpty>: <Reg8: 4>
class LoadConstEmpty(LoadConstZero):
    # Hermes' internal "empty" sentinel (e.g. an array hole) has no real
    # JS literal - it isn't `undefined` at the engine level, even though
    # source-visible reads of it usually coerce to `undefined`. Kept as
    # an explicit marker rather than silently lying with UndefinedLiteral.
    VALUE = RawExpression(source="/* empty */")


# ---------------------------------------------------------------------------
# Numeric constants
# ---------------------------------------------------------------------------

# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(LoadConstUInt8, Reg8, UInt8)
# Example: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
class LoadConstUInt8(OpcodeHandler):
    """"Load a constant integer value."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))
        value = python_literal(int(match.group(2)))

        result = OpcodeResult(ctx.entry, value=value, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Imm32 (total size 5)
# DEFINE_OPCODE_2(LoadConstInt, Reg8, Imm32)
# Example: <LoadConstInt>: <Reg8: 11, Imm32: 256>
class LoadConstInt(OpcodeHandler):
    """"Load a constant integer value."""

    ARGUMENTS = ArgsPattern(sequence(REG, IMM32), "Reg8, Imm32")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))
        value = python_literal(int(match.group(2)))

        result = OpcodeResult(ctx.entry, value=value, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt16 (bigint_id) (total size 3)
# DEFINE_OPCODE_2(LoadConstBigInt, Reg8, UInt16)
# Example:
class LoadConstBigInt(OpcodeHandler):
    """a constant BigInt value by bigint table index."""

    ARGUMENTS = ArgsPattern(sequence(REG, BIGINT_ID), "Reg8, UInt16 (bigint_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))
        bigint_id = int(match.group(2))

        resolved = ctx.entry.string_literal

        if resolved is None:
            resolved = ctx.entry.identifier_name

        if resolved is None:
            resolved = f"bigint_{bigint_id}"

        result = OpcodeResult(ctx.entry, value=StringLiteral(resolved), dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt32 (bigint_id) (total size 5)
# DEFINE_OPCODE_2(LoadConstBigIntLongIndex, Reg8, UInt32)
# Example:
class LoadConstBigIntLongIndex(LoadConstBigInt):
    """a constant BigInt value by bigint table index."""
    pass


# Reg8, Double (total size 9)
# DEFINE_OPCODE_2(LoadConstDouble, Reg8, Double)
# Example: <LoadConstDouble>: <Reg8: 0, Double: 7687411609819.0>
class LoadConstDouble(OpcodeHandler):
    """"Load a constant double value."""

    ARGUMENTS = ArgsPattern(sequence(REG, DOUBLE), "Reg8, Double")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))
        value = python_literal(float(match.group(2)))

        result = OpcodeResult(ctx.entry, value=value, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# ---------------------------------------------------------------------------
# String constants
# ---------------------------------------------------------------------------

# Reg8, UInt16 (string_id) (total size 3)
# DEFINE_OPCODE_2(LoadConstString, Reg8, UInt16)
# Example: <LoadConstString>: <Reg8: 2, string_id: 12273>  # String: 'getStaticFeatureFlag' (Identifier)
class LoadConstString(OpcodeHandler):
    """Load a constant string value by string table index."""

    ARGUMENTS = ArgsPattern(sequence(REG, STRING_ID), "Reg8, UInt16 (string_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))
        string_id = match.group(2)

        resolved = ctx.entry.string_literal

        if resolved is None:
            resolved = ctx.entry.identifier_name

        if resolved is None:
            resolved = f"str_{string_id}"

        result = OpcodeResult(ctx.entry, value=StringLiteral(resolved), dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, UInt32 (string_id) (total size 5)
# DEFINE_OPCODE_2(LoadConstStringLongIndex, Reg8, UInt32)
# Example:
class LoadConstStringLongIndex(LoadConstString):
    """Load a constant string value by string table index."""

    pass
