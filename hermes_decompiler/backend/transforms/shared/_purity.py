import dataclasses

from hermes_decompiler.ir import Expression, Node
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    Literal,
    ObjectExpression,
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
    BooleanLiteral,
    NullLiteral,
    UndefinedLiteral,
    BigIntLiteral,
    RegExpLiteral,
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

# Nodes that are structurally equal to every OTHER unrelated occurrence of
# the same name/value, so they may only ever be matched by identity (see
# `_repoint.repoint_node`). Every literal kind belongs here - `null` and
# `undefined` were once missing, which let a fold rewrite each unrelated
# `null` in the function.
TRIVIAL_NODE_TYPES = (
    Identifier,
    StringLiteral,
    NumericLiteral,
    BooleanLiteral,
    NullLiteral,
    UndefinedLiteral,
    BigIntLiteral,
    RegExpLiteral,
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
    if is_unfolded_literal_definition(instruction):
        return False
    return True


def is_unfolded_literal_definition(instruction) -> bool:
    """True for a PRINTED definition of a built array/object literal
    (`r7 = [a, b]`, `r7 = { "k": v }`) that nothing folded into a consumer.

    Such a definition can never be absorbed into a fold's expression tree:
    `get_register_expression` never inlines array/object (or call) values,
    so every reader keeps the bare `r7`. Dropping the statement - because
    the arm "only has pure instructions" - therefore leaves those readers
    dangling (`r5[1] = cond && r7` with no `r7 = {...}` anywhere).
    Calls and `new` are already refused as impure; this is the same
    reason for the two literal kinds.
    """
    return (
            instruction.dest_reg is not None
            and not instruction.definition_used
            and isinstance(instruction.value, (ArrayExpression, ObjectExpression))
    )


def prints_non_constant_statement(instruction) -> bool:
    """True if `instruction` prints a statement that is not a mere constant
    load: a definition (`r4 = r5[114]`, `r8 = param1`, `r9 = {...}`) or an
    expression statement that nothing folded into a consumer.

    This is what makes a block more than "clutter in front of the nested
    `if`" for else-if flattening: later code reads such a register by name,
    so skipping the block deletes its only definition (`else if (r0 >= 0)`
    with the `r0 = +param1` that the condition reads silently gone).

    Constant loads (`r1 = 5`) are the clutter that predicate exists to look
    past - the constant is already embedded in the nested condition - and
    stay skippable. Measured over the full hermes-96/98 bundles, treating
    every non-constant printed instruction as non-skippable removes 105 of
    261 (96) and 66 of 362 (98) dangling registers and introduces none;
    also refusing constants removes only 3 more.
    """
    return (
            instruction.value is not None
            and not instruction.definition_used
            and not isinstance(instruction.value, Literal)
    )


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
