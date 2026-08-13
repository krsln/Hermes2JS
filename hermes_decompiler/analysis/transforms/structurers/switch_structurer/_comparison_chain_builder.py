from __future__ import annotations

from hermes_decompiler.analysis.models.regions import IfRegion, SequenceRegion, SwitchCase, SwitchRegion
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression
from hermes_decompiler.ir.expressions.Literals import Literal

from ._predicates import is_empty_or_transparent_body, is_transparent, same_body

_EQUALITY_OPERATORS = (BinaryOperator.EQUAL, BinaryOperator.STRICT_EQUAL)
_INEQUALITY_OPERATORS = (BinaryOperator.NOT_EQUAL, BinaryOperator.STRICT_NOT_EQUAL)


class _ComparisonChainSwitchBuilder:
    """
    Recovers a `SwitchRegion` from the small/sparse-switch shape
    Hermes compiles to: a chain of `IfRegion`s, already produced by
    `IfStructurer`, each testing the same discriminant against a
    different constant literal.

    Sibling to `_JumpTableSwitchBuilder` - see that class's docstring
    for the disjointness argument.

    Shared-body and inverted-residual recovery
    -------------------------------------------
    When two or more case labels share a single body
    (`case 3: case 4: sharedBody`), `IfStructurer`'s dominance-based
    conversion typically attaches the body to the first label only.
    Later labels remain as residual conditionals that later folding
    often turns into inverted tests inside what looks like the
    `default` arm, e.g.:

        case 3:
            sharedBody
        default:
            if (4 !== disc) { realDefault }

    `_try_recover_shared_or_inverted` / `_try_recover_inverted_default`
    recover those residual tests:

    * Consecutive equality tests that resolve to the same body are
      merged into a single multi-value `SwitchCase`.
    * An inverted residual of the form `if (C !== disc) { realDefault }`
      (or the symmetric operand order) contributes `C` to the preceding
      case's test list and promotes the residual's then-body to the
      true `default`.

    Anything that cannot be recovered cleanly is left as the default
    body; the printer's raw-terminator fallback still renders a
    correct (if less tidy) result.
    """

    def __init__(self, graph):
        self.graph = graph

    def try_build(self, region: SequenceRegion, root: IfRegion, min_cases: int) -> bool:
        chain = self._match_chain(root)

        if chain is None:
            return False

        discriminant, cases, default_body = chain

        if len(cases) < min_cases:
            return False

        switch_region = SwitchRegion(discriminant)
        for tests, body in cases:
            switch_region.add_case(SwitchCase(tests, body))
        if default_body is not None:
            switch_region.default_body = default_body

        self.graph.replace(root, switch_region)
        return True

    # -------------------------------------------------------------
    # Comparison-chain matching
    # -------------------------------------------------------------

    def _match_chain(self, root: IfRegion):
        """
        Walk `root`'s `else if` chain as far as it validly extends.

        Returns `(discriminant, cases, default_body)` where `cases` is
        `[(tests, body), …]` in source order, or `None` when `root`
        itself is not even a single `discriminant == constant` test.

        Shared-body and inverted-residual recovery are performed
        inline so that labels such as `case 3: case 4:` are restored
        instead of leaving a residual conditional inside `default`.
        """

        discriminant = None
        cases: list[tuple[list[Expression], SequenceRegion]] = []
        current = root

        # SequenceRegion that directly contains `current` once we have
        # moved past `root`. Used as a safe fallback default body when
        # a later link fails to parse as a case test.
        container: SequenceRegion | None = None

        while True:
            parsed = self._parse_test(current.condition, discriminant, _EQUALITY_OPERATORS)

            if parsed is None:
                # Attempt inverted / shared recovery before giving up.
                recovered = self._try_recover_shared_or_inverted(
                    current, discriminant, cases, container
                )

                if recovered is not None:
                    return recovered

                if container is not None:
                    return discriminant, cases, container

                return None

            disc_expr, test_value = parsed
            discriminant = disc_expr

            body = current.then_body

            if cases and same_body(cases[-1][1], body):
                # Same physical body as the previous case - multi-value
                # label (case N: case M: sharedBody).
                cases[-1][0].append(test_value)
            else:
                cases.append(([test_value], body))

            else_body = current.else_body
            if else_body is None:
                return discriminant, cases, None

            # Continue the chain when the else arm is exactly one more
            # equality-test IfRegion (optionally preceded by a
            # transparent spent const-setup block left by IfStructurer).
            if (
                    len(else_body.children) == 1
                    and isinstance(else_body.children[0], IfRegion)
            ):
                current = else_body.children[0]
                container = else_body
                continue

            if (
                    len(else_body.children) == 2
                    and is_transparent(else_body.children[0])
                    and isinstance(else_body.children[1], IfRegion)
            ):
                current = else_body.children[1]
                container = else_body
                continue

            # else_body does not extend the chain. Try to recover an
            # inverted residual that still belongs to the last case.
            recovered_default = self._try_recover_inverted_default(
                else_body, discriminant, cases
            )

            if recovered_default is not None:
                return discriminant, cases, recovered_default

            return discriminant, cases, else_body

    # -------------------------------------------------------------
    # Shared-body / inverted residual recovery
    # -------------------------------------------------------------

    def _try_recover_shared_or_inverted(
            self,
            current: IfRegion,
            discriminant,
            cases: list,
            container: SequenceRegion | None,
    ):
        """
        Called when `current.condition` is not a plain equality test.
        Handles the common residual shape produced after IfStructurer
        and compound-condition folding:

            if (C !== disc) { realDefault }          # else empty
            if (disc != C)  { realDefault }

        The constant `C` is appended to the most recent case's test
        list and the residual's then-body becomes the true default.
        """
        if discriminant is None or not cases:
            return None

        inv = self._parse_test(current.condition, discriminant, _INEQUALITY_OPERATORS)
        if inv is None:
            return None

        _, extra_value = inv

        # Prefer the shape where the then-arm is the real default and
        # the else-arm is empty / transparent.
        if is_empty_or_transparent_body(current.else_body):
            cases[-1][0].append(extra_value)
            return discriminant, cases, current.then_body

        # Symmetric shape: then empty, else is the real default.
        if is_empty_or_transparent_body(current.then_body):
            cases[-1][0].append(extra_value)
            return discriminant, cases, current.else_body

        return None

    def _try_recover_inverted_default(
            self,
            else_body: SequenceRegion,
            discriminant,
            cases: list,
    ):
        """
        Inspect a non-chain else arm for a single inverted residual:

            SequenceRegion
              └── IfRegion  condition = (C !== disc)   else = None
                    └── then = realDefault

        On success appends `C` to the last case and returns the residual
        then-body as the switch's default.
        """
        if discriminant is None or not cases:
            return None
        if not isinstance(else_body, SequenceRegion):
            return None

        # Tolerate a leading transparent block (spent const load).
        meaningful = [c for c in else_body.children if not is_transparent(c)]
        if len(meaningful) != 1 or not isinstance(meaningful[0], IfRegion):
            return None

        residual = meaningful[0]
        if residual.else_body is not None and not is_empty_or_transparent_body(
                residual.else_body
        ):
            return None

        inv = self._parse_test(residual.condition, discriminant, _INEQUALITY_OPERATORS)
        if inv is None:
            return None

        _, extra_value = inv
        cases[-1][0].append(extra_value)
        return residual.then_body

    # -------------------------------------------------------------
    # Condition parsing
    # -------------------------------------------------------------

    @staticmethod
    def _parse_test(condition, expected_discriminant, operators: tuple):
        """
        Recognise `<discriminant> <op> <constant>` for `op` in
        `operators` (either operand order). When `expected_discriminant`
        is already set it must structurally match. Returns
        `(discriminant_expr, constant)` or `None`.

        Single home for what used to be two near-identical parsers
        (`_parse_case_test` for `==`/`===`, `_parse_inverted_case_test`
        for `!=`/`!==`) - the only thing that ever differed between
        them was the operator set, so callers now just pass
        `_EQUALITY_OPERATORS` or `_INEQUALITY_OPERATORS`.
        """
        if not isinstance(condition, BinaryExpression):
            return None

        if condition.operator not in operators:
            return None

        left, right = condition.left, condition.right
        left_is_const = isinstance(left, Literal)
        right_is_const = isinstance(right, Literal)

        if right_is_const and not left_is_const:
            disc_expr, test_value = left, right
        elif left_is_const and not right_is_const:
            disc_expr, test_value = right, left
        else:
            return None

        if (
                expected_discriminant is not None
                and not disc_expr.structurally_equal(expected_discriminant)
        ):
            return None

        return disc_expr, test_value
