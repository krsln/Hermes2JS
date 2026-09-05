from __future__ import annotations

from typing import ClassVar, Optional

from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, ADDR
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression, UnaryExpression
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch


class BaseJCompare(OpcodeHandler):
    """
    `BaseJCompare` comparison jump, and shared base implementation for every
    other comparison jump opcode. A real opcode is used as the shared
    base - see `Add` in `handlers/arithmetic/Binary.py` for the rationale.

    Two ways to express a comparison, mutually exclusive:

    - `operator`: a direct `BinaryOperator` used as-is, e.g.
      `BinaryExpression(lhs, operator, rhs)`. Use this for opcodes whose
      condition genuinely IS that binary operator (JLess -> `<`,
      JEqual -> `==`, ...).

    - `negated_operator`: a `BinaryOperator` that gets wrapped in a
      logical NOT, e.g. `!(lhs negated_operator rhs)`. Use this for the
      historical "inverted-jump" family (`JNotLess`, `JNotLessEqual`,
      `JNotGreater`, `JNotGreaterEqual`).

    Why the distinction matters: Hermes' `JNotLess` jumps when
    `lhs < rhs` is NOT true. In plain arithmetic that's equivalent to
    `lhs >= rhs`, but in JavaScript it is NOT equivalent whenever a
    comparison involves `NaN`:

        !(NaN < 5) === true
        (NaN >= 5) === false

    Collapsing `JNotLess` straight to `GREATER_EQUAL` would silently
    change program behavior for NaN operands. Modeling it as
    `!(lhs < rhs)` instead reproduces the VM's actual semantics exactly,
    regardless of operand types.
    """

    _abstract = True
    operator: ClassVar[Optional[BinaryOperator]] = None
    negated_operator: ClassVar[Optional[BinaryOperator]] = None

    ARGUMENTS = ArgsPattern(sequence(ADDR, REG, REG), "Addr8, Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        offset, lhs_reg, rhs_reg = map(int, match.groups())

        target = ctx.entry.target_address
        if target is None:
            target = ctx.entry.address + offset

        ctx.analysis.gotoList.append(target)

        # Jump conditions must stay symbolic — do not inline definitions.
        lhs = self.resolve_condition_argument(ctx.analysis, lhs_reg)
        rhs = self.resolve_condition_argument(ctx.analysis, rhs_reg)

        condition = self.build_condition(lhs, rhs)
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

    def build_condition(self, lhs: Expression, rhs: Expression) -> Expression:
        if self.operator is not None:
            return BinaryExpression(left=lhs, operator=self.operator, right=rhs)
        if self.negated_operator is not None:
            inner = BinaryExpression(left=lhs, operator=self.negated_operator, right=rhs)
            return UnaryExpression(UnaryOperator.LOGICAL_NOT, inner)
        raise NotImplementedError(
            f"{type(self).__name__}: neither `operator` nor `negated_operator` is set"
        )


# @formatter:off
# Equality
# --------
# `==` / `!=` / `===` / `!==` have no NaN-related direction issue - the
# operator itself already fully captures the semantics - so these use
# `operator` directly.
class JEqual(BaseJCompare): operator = BinaryOperator.EQUAL
class JEqualLong(JEqual): pass

class JNotEqual(BaseJCompare): operator = BinaryOperator.NOT_EQUAL
class JNotEqualLong(JNotEqual): pass

class JStrictEqual(BaseJCompare): operator = BinaryOperator.STRICT_EQUAL
class JStrictEqualLong(JStrictEqual): pass

class JStrictNotEqual(BaseJCompare): operator = BinaryOperator.STRICT_NOT_EQUAL
class JStrictNotEqualLong(JStrictNotEqual): pass

# Less
# ----
# Direct (non-inverted) family: condition IS the comparison.
class JLess(BaseJCompare): operator = BinaryOperator.LESS_THAN
class JLessLong(JLess): pass
class JLessN(JLess): pass
class JLessNLong(JLessN): pass

class JLessEqual(BaseJCompare): operator = BinaryOperator.LESS_EQUAL
class JLessEqualLong(JLessEqual): pass
class JLessEqualN(JLessEqual): pass
class JLessEqualNLong(JLessEqualN): pass

# Inverted family: jump when NOT(lhs < rhs) / NOT(lhs <= rhs).
# Modeled as `!(...)` rather than flipped to `>=`/`>` to stay correct for
# NaN operands (see JCompareX docstring).
class JNotLess(BaseJCompare): negated_operator = BinaryOperator.LESS_THAN
class JNotLessLong(JNotLess): pass
class JNotLessN(JNotLess): pass
class JNotLessNLong(JNotLessN): pass

class JNotLessEqual(BaseJCompare): negated_operator = BinaryOperator.LESS_EQUAL
class JNotLessEqualLong(JNotLessEqual): pass
class JNotLessEqualN(JNotLessEqual): pass
class JNotLessEqualNLong(JNotLessEqualN): pass

# Greater
# -------
class JGreater(BaseJCompare): operator = BinaryOperator.GREATER_THAN
class JGreaterLong(JGreater): pass
class JGreaterN(JGreater): pass
class JGreaterNLong(JGreaterN): pass

class JGreaterEqual(BaseJCompare): operator = BinaryOperator.GREATER_EQUAL
class JGreaterEqualLong(JGreaterEqual): pass
class JGreaterEqualN(JGreaterEqual): pass
class JGreaterEqualNLong(JGreaterEqualN): pass

# Inverted family: jump when NOT(lhs > rhs) / NOT(lhs >= rhs).
class JNotGreater(BaseJCompare): negated_operator = BinaryOperator.GREATER_THAN
class JNotGreaterLong(JNotGreater): pass
class JNotGreaterN(JNotGreater): pass
class JNotGreaterNLong(JNotGreaterN): pass

class JNotGreaterEqual(BaseJCompare): negated_operator = BinaryOperator.GREATER_EQUAL
class JNotGreaterEqualLong(JNotGreaterEqual): pass
class JNotGreaterEqualN(JNotGreaterEqual): pass
class JNotGreaterEqualNLong(JNotGreaterEqualN): pass
# @formatter:on
