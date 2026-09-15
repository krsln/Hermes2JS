from hermes_decompiler.ir import Expression
from hermes_decompiler.ir.expressions import (
    CallExpression,
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
