from __future__ import annotations

from typing import ClassVar, Optional, Tuple

from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.handlers import OpcodeHandler, REG, ADDR, sequence
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression, UnaryExpression
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis

# Compiled once at import time instead of on every `handle()` call.
_COMPARE_PATTERN = sequence(ADDR, REG, REG)


def _parse_compare(entry: OpcodeEntry) -> Tuple[int, int, int]:
    """
    Parse comparison jump arguments.

        Addr, Reg, Reg
    """
    match = _COMPARE_PATTERN.match(entry.args.strip())

    if not match:
        raise ValueError(
            f"Invalid arguments for {entry.opcode}: {entry.args}"
        )

    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )


class JCompareX(OpcodeHandler):
    """
    Base class for every comparison jump opcode.

    Two ways to express a comparison, mutually exclusive:

    - `operator`: a direct `BinaryOperator` used as-is, e.g.
      `BinaryExpression(lhs, operator, rhs)`. Use this for opcodes whose
      condition genuinely IS that binary operator (JLess -> `<`,
      JEqual -> `==`, ...).

    - `negate_of`: a `BinaryOperator` that gets wrapped in a logical NOT,
      e.g. `!(lhs negate_of rhs)`. Use this for the historical
      "inverted-jump" family (`JNotLess`, `JNotLessEqual`, `JNotGreater`,
      `JNotGreaterEqual`).

    Why the distinction matters: Hermes' `JNotLess` jumps when
    `lhs < rhs` is NOT true. In plain arithmetic that's equivalent to
    `lhs >= rhs`, but in JavaScript it is NOT equivalent whenever a
    comparison involves `NaN`:

        !(NaN < 5)   === true
        (NaN >= 5)   === false

    Collapsing `JNotLess` straight to `GREATER_EQUAL` would silently
    change program behavior for NaN operands. Modeling it as
    `!(lhs < rhs)` instead reproduces the VM's actual semantics exactly,
    regardless of operand types.
    """

    operator: ClassVar[Optional[BinaryOperator]] = None
    negated_operator: ClassVar[Optional[BinaryOperator]] = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Only validate concrete leaf-ish classes that actually set one of
        # the two class vars in their own __dict__; classes that merely
        # inherit (e.g. the *Long / *N aliases) are left alone.
        own_operator = cls.__dict__.get("operator")
        own_negate_of = cls.__dict__.get("negate_of")
        if own_operator is not None and own_negate_of is not None:
            raise TypeError(
                f"{cls.__name__}: set exactly one of `operator` or "
                f"`negate_of`, not both"
            )

    def build_condition(self, lhs: Expression, rhs: Expression) -> Expression:
        if self.operator is not None:
            return BinaryExpression(left=lhs, operator=self.operator, right=rhs)
        if self.negated_operator is not None:
            inner = BinaryExpression(left=lhs, operator=self.negated_operator, right=rhs)
            return UnaryExpression(UnaryOperator.LOGICAL_NOT, inner)
        raise NotImplementedError(
            f"{type(self).__name__}: neither `operator` nor `negate_of` is set"
        )

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            offset, lhs_reg, rhs_reg = _parse_compare(entry)
        except ValueError as exc:
            return self.build_invalid_args_result(analysis, entry, str(exc))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        lhs = self.get_register_expression(analysis, lhs_reg)
        rhs = self.get_register_expression(analysis, rhs_reg)

        condition = self.build_condition(lhs, rhs)
        terminator = TerminatorConditionalBranch(condition=condition, target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None)
        analysis.add_result(result)

        return result


# @formatter:off
# Equality
# --------
# `==` / `!=` / `===` / `!==` have no NaN-related direction issue - the
# operator itself already fully captures the semantics - so these use
# `operator` directly.
class JEqual(JCompareX): operator = BinaryOperator.EQUAL
class JEqualLong(JEqual): pass

class JNotEqual(JCompareX): operator = BinaryOperator.NOT_EQUAL
class JNotEqualLong(JNotEqual): pass

class JStrictEqual(JCompareX): operator = BinaryOperator.STRICT_EQUAL
class JStrictEqualLong(JStrictEqual): pass

class JStrictNotEqual(JCompareX): operator = BinaryOperator.STRICT_NOT_EQUAL
class JStrictNotEqualLong(JStrictNotEqual): pass

# Less
# ----
# Direct (non-inverted) family: condition IS the comparison.
class JLess(JCompareX): operator = BinaryOperator.LESS_THAN
class JLessLong(JLess): pass
class JLessN(JLess): pass
class JLessNLong(JLessN): pass

class JLessEqual(JCompareX): operator = BinaryOperator.LESS_EQUAL
class JLessEqualLong(JLessEqual): pass
class JLessEqualN(JLessEqual): pass
class JLessEqualNLong(JLessEqualN): pass

# Inverted family: jump when NOT(lhs < rhs) / NOT(lhs <= rhs).
# Modeled as `!(...)` rather than flipped to `>=`/`>` to stay correct for
# NaN operands (see JCompareX docstring).
class JNotLess(JCompareX): negated_operator = BinaryOperator.LESS_THAN
class JNotLessLong(JNotLess): pass
class JNotLessN(JNotLess): pass
class JNotLessNLong(JNotLessN): pass

class JNotLessEqual(JCompareX): negated_operator = BinaryOperator.LESS_EQUAL
class JNotLessEqualLong(JNotLessEqual): pass
class JNotLessEqualN(JNotLessEqual): pass
class JNotLessEqualNLong(JNotLessEqualN): pass

# Greater
# -------
class JGreater(JCompareX): operator = BinaryOperator.GREATER_THAN
class JGreaterLong(JGreater): pass
class JGreaterN(JGreater): pass
class JGreaterNLong(JGreaterN): pass

class JGreaterEqual(JCompareX): operator = BinaryOperator.GREATER_EQUAL
class JGreaterEqualLong(JGreaterEqual): pass
class JGreaterEqualN(JGreaterEqual): pass
class JGreaterEqualNLong(JGreaterEqualN): pass

# Inverted family: jump when NOT(lhs > rhs) / NOT(lhs >= rhs).
class JNotGreater(JCompareX): negated_operator = BinaryOperator.GREATER_THAN
class JNotGreaterLong(JNotGreater): pass
class JNotGreaterN(JNotGreater): pass
class JNotGreaterNLong(JNotGreaterN): pass

class JNotGreaterEqual(JCompareX): negated_operator = BinaryOperator.GREATER_EQUAL
class JNotGreaterEqualLong(JNotGreaterEqual): pass
class JNotGreaterEqualN(JNotGreaterEqual): pass
class JNotGreaterEqualNLong(JNotGreaterEqualN): pass
# @formatter:on
