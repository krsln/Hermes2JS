from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, IfRegion, SequenceRegion
from hermes_decompiler.backend.transforms.shared import (
    negate_condition, has_side_effects, repoint_references, reclaim_definition, is_unfolded_literal_definition,
    absorb_arm_definitions, substitute_register,
)
from hermes_decompiler.backend.transforms.shared._repoint import _reads_register_by_name
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import ConditionalExpression, Expression, Identifier
from ._base import RegionPass

logger = get_logger(__name__)


def _mentions_register(node, register: int) -> bool:
    if isinstance(node, Identifier) and node.name == f"r{register}":
        return True

    return any(_mentions_register(child, register) for child in node.children if isinstance(child, Node))


class ConditionalExpressionRegionPass(RegionPass, RegionVisitor):
    """Folds a value-producing ternary (c ? a : b) into a ConditionalExpression.

    Runs once IfStructurer has already built an IfRegion with an
    else_body.

    Sibling to BooleanChainRegionPass, not a replacement: that pass
    explicitly declines whenever `if_region.else_body is not None`
    (see its `_try_fold`) - this pass exists specifically to cover
    that declined case. The two are disjointed on that one condition, so
    both can run in the same stage without overlap.

    Must run after BooleanChainRegionPass in the pass ordering: a
    then/else arm's own condition may itself be an &&/|| chain that
    needs folding first, so this pass reads clean conditions rather
    than needing to fold sub-chains itself.

    Traversal is inherited from RegionVisitor - see
    BooleanChainRegionPass's docstring for why a hand-rolled `_visit`
    of this shape would silently skip SwitchRegion bodies.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)
        self._fold_sequence(node)

    def _fold_sequence(self, region: SequenceRegion):
        region.children = [
            c for c in region.children
            if not (isinstance(c, BasicBlock) and not c.instructions)
        ]

        index = 0
        while index < len(region.children) - 1:
            block = region.children[index]
            if_region = region.children[index + 1]
            if self._try_fold(block, if_region):
                del region.children[index + 1]
                continue
            index += 1

    def _try_fold(self, block, if_region) -> bool:
        if not isinstance(block, BasicBlock) or not isinstance(if_region, IfRegion):
            return False
        if not block.instructions:
            return False

        condition = if_region.condition
        if condition is None:
            return False

        if if_region.else_body is not None:
            # A two-armed if/else is a genuinely different shape from
            # the no-else case below, and isn't handled by it: the
            # no-else logic treats then_body as a single value-
            # producing arm to merge against a "default" expression in
            # block - meaningless once there's a real else_body too
            # (two full arms, each possibly holding real, order-
            # sensitive statements like a console.log call, which must
            # stay as statements rather than be absorbed into a
            # ConditionalExpression operand). Bail explicitly;
            # two-armed folding isn't implemented here.
            return False

        # No-else case: don't assume block.instructions[-1] is the
        # default value - it may instead be the branch-condition-
        # computing instruction itself (e.g. `r4 = param1 > 100`
        # immediately preceding the terminator), with the real default
        # sitting earlier in the block (e.g. `r3 = 100`). Try each
        # dest_reg-bearing instruction from last to first, using the
        # first one whose register also has a matching arm - not
        # positional order.
        #
        # A register's default is its LAST write in the block. Once that
        # write has been considered (and, below, possibly rejected), an
        # earlier write to the same register is dead code and must not be
        # promoted to "the default" in its place.
        considered: set[int] = set()

        for last in reversed(block.instructions):
            if last.dest_reg is None or not isinstance(last.value, Expression):
                continue
            if last.dest_reg in considered:
                continue
            considered.add(last.dest_reg)
            then_arm = self._single_result(if_region.then_body, last.dest_reg)
            if then_arm is None:
                continue
            arm_block, arm_result, arm_value = then_arm
            default_expr = last.value
            arm_expr = arm_result.value

            # `dest = default; if (cond) dest = arm` runs `default`
            # unconditionally and BEFORE `cond`. As `cond ? arm : default`
            # it would run only when `cond` is false, and after `cond`: a
            # call in `default` (`r1 = f(x); if (!r1) ...`) would become
            # conditional. Only a `default` that cannot have an effect may
            # move.
            if has_side_effects(default_expr):
                continue

            # `if (r8 === undefined) r8 = "anon"` tests the very register it
            # defaults, and that read means the default's value. Folded as-is
            # the test would still name `r8` while its defining statement
            # moved inside the ternary, so `r8` would be read before anything
            # sets it. The default is pure (checked above): name it directly.
            test = negate_condition(condition)

            if _mentions_register(test, last.dest_reg):
                test = substitute_register(test, f"r{last.dest_reg}", default_expr)

            new_expr = ConditionalExpression(
                test=test,
                consequent=default_expr,
                alternate=arm_value,
            )
            last.value = new_expr

            # Something after the merge still names the register (`return r1`
            # after a defaulted parameter): the ternary's own statement must
            # keep printing, or that bare read dangles. (The readers that were
            # already handed the arm's value keep a copy of the ternary: it is
            # pure, and repointing them to the register is only sound where
            # nothing reassigned it in between.)
            named_later = _reads_register_by_name(
                self.cfg, last.dest_reg, max(last.entry.address, arm_result.entry.address),
            )

            reclaim_definition(
                self.cfg, self.graph.root, last, default_expr, arm_result,
                ignore_blocks={arm_block}, ignore_regions={if_region},
            )

            repoint_references(
                self.cfg,
                self.graph.root,
                arm_expr,
                new_expr,
                min_block_id=arm_block.id,
                exclude={arm_result, last},
            )

            if named_later:
                last.definition_used = False

            return True

        return False

    def _single_result(self, body: SequenceRegion, dest_reg: int):
        children = [
            c for c in body.children
            if not (isinstance(c, BasicBlock) and not c.instructions)
        ]
        if not children or not all(isinstance(c, BasicBlock) for c in children):
            return None  # only handle flat all-BasicBlock arms for now

        last_block = children[-1]
        if not last_block.instructions:
            return None

        result = last_block.instructions[-1]
        if result.dest_reg != dest_reg or not isinstance(result.value, Expression):
            return None
        if not result.definition_used:
            return None

        # Every instruction across the whole arm except this final
        # merge write must be non-observable as its own statement.
        # `.statement is not None` alone isn't sufficient: an
        # instruction can be independently observable (a call's side
        # effect, an assignment's mutation) without yet having been
        # promoted to its own .statement node at this point in the
        # pipeline - the Printer falls back to printing such
        # instructions as bare expression statements from .value
        # directly. Also reject by expression type, same as
        # BooleanChainRegionPass._is_pure, so a call sitting earlier
        # in the arm can't be silently absorbed into the folded
        # ConditionalExpression's operand tree.
        for blk in children:
            for instr in blk.instructions:
                if instr is result:
                    continue
                if instr.statement is not None:
                    return None
                if has_side_effects(instr.value):
                    return None
                # A printed array/object literal definition is pure, but the
                # merge write usually reads it by name (`r7[r2]`): absorbing
                # the arm would delete the only statement that builds it
                # (see `is_unfolded_literal_definition`).
                if is_unfolded_literal_definition(instr):
                    return None

        # Any other PRINTED definition is deleted with the arm too, and
        # whatever read its register by name would be left dangling: fold it
        # into the arm's value (`(r7 - 0.1379) / 7.787`) or refuse.
        absorbed = absorb_arm_definitions(
            self.cfg, [i for blk in children for i in blk.instructions], result,
        )

        if absorbed is None:
            return None

        return last_block, result, absorbed
