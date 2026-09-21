import dataclasses

from hermes_decompiler.ir import Expression, Node
from hermes_decompiler.ir.expressions import (
    ArrowFunctionExpression,
    CallExpression,
    ClassExpression,
    FunctionExpression,
    NewExpression,
    AssignmentExpression,
    UpdateExpression,
    AwaitExpression,
    YieldExpression,

    Identifier,
    StringLiteral,
    NumericLiteral,
    BooleanLiteral
)

# Same set BooleanChainFolder guards against in `_is_pure` - an
# instruction whose value is one of these is independently observable
# (a call's side effect, an assignment's mutation, ...) even when it
# hasn't yet been promoted to its own `.statement` node. Absorbing one
# of these into a ConditionalExpression's operand silently drops or
# reorders that side effect.
IMPURE_EXPRESSION_TYPES = (
    CallExpression,
    NewExpression,
    AssignmentExpression,
    UpdateExpression,
    AwaitExpression,
    YieldExpression,
)

# Calls that never have an effect of their own, so folding one away or moving
# it across another instruction changes nothing observable:
#
# - `getEnvironment` / `getParentEnvironment` / `createEnvironment`: the
#   closure-environment plumbing (`GetEnvironment`, `GetParentEnvironment`,
#   `CreateEnvironment` opcodes), which is not a JS call at all.
# - `exponentiationOperator`: `a ** b`. Hermes itself treats it as
#   side-effect free - it hoists it ABOVE the conditional that uses it
#   (see the `x > 0.008856 ? x ** 3 : ...` idiom).
#
# Deliberately NOT included: `copyDataProperties`, `arraySpread`, `apply`,
# `iteratorNext`, ... They mutate their arguments or run user code.
PURE_CALLEES = frozenset({
    "getEnvironment",
    "getParentEnvironment",
    "createEnvironment",
    "exponentiationOperator",
})

# adjust to actual literal type names
TRIVIAL_NODE_TYPES = (
    Identifier,
    StringLiteral,
    NumericLiteral,
    BooleanLiteral
)


def is_pure(instruction) -> bool:
    """
    True if `instruction`'s value can be safely absorbed into the
    fold without needing its own printed statement.

    "Pure" here means "not independently observable as a separate
    statement" (instruction.statement is None) - NOT "side effect
    free". A CallExpression with no .statement of its own is still
    fully consumed by the chain tail's expression tree (e.g.
    `a && sideEffect(...)`), so folding it away from block.instructions
    doesn't drop the call. - It relocates it into `then_result.value`,
    which is exactly what happens for any other value in this fold.
    A block whose call genuinely needs an independent evaluation order
    would already have `.statement` set by whatever pass decides
    that (unrelated to this pass), and is correctly rejected above.
    """
    if instruction.statement is not None:
        return False
    if not isinstance(instruction.value, Expression):
        return False
    return True


def has_side_effects(node) -> bool:
    """True if evaluating `node` can run a call, construction, assignment,
    update, await or yield.

    Deep: a call nested inside a binary/member/conditional expression counts.
    A function/class expression only creates a value - what is in its body
    does not run. Calls to `PURE_CALLEES` do not count themselves, but their
    arguments are still inspected.
    """
    if isinstance(node, (FunctionExpression, ArrowFunctionExpression, ClassExpression)):
        return False

    if (
            isinstance(node, CallExpression)
            and isinstance(node.callee, Identifier)
            and node.callee.name in PURE_CALLEES
    ):
        return any(has_side_effects(argument) for argument in node.arguments)

    if isinstance(node, IMPURE_EXPRESSION_TYPES):
        return True

    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return False

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        for child in (value if isinstance(value, tuple) else (value,)):
            if isinstance(child, Node) and has_side_effects(child):
                return True

    return False
