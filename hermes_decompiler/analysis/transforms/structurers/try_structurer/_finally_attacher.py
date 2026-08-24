from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.analysis.models import TerminatorThrow
from hermes_decompiler.analysis.models.regions import FinallyRegion, SequenceRegion, TryRegion
from hermes_decompiler.ir.expressions import Identifier
from ._predicates import strip_duplicate_run


class _FinallyAttacher:
    """
    Commits a recognized `finally` shaped handler into the region tree.

    Handles the two shapes Hermes compiles a try/finally into:

    - `attach`: the two-handler case (a real catch exists alongside
      it) - `_finally_matcher.find_finally_wrapper_target` already
      identified the wider handler as this try/catch's
      finally-wrapper; this installs it.
    - `maybe_reinterpret_as_finally`: the single-handler case (no
      catch in the source at all) - `_HandlerBuilder` had no choice
      but to build an ordinary catch out of the lone handler; this
      recognizes after the fact that it's really a `finally` and
      rewrites it in place.
    """

    def __init__(self, graph):
        self.graph = graph

    def attach(self, handler: dict, try_region: TryRegion, inner_handler: dict, cfg: CFG) -> None:

        finally_block: BasicBlock = handler["handler_block"]

        # Pull the block out of wherever it currently sits in the
        # region tree (it hasn't been touched yet - still a bare
        # top-level BasicBlock sibling of `try_region`).
        self.graph.extract_block(finally_block)

        # Drop the leading Catch binding - finally has no bound
        # exception parameter.
        if finally_block.instructions:
            first = finally_block.instructions[0]

            if first.dest_reg is not None and isinstance(first.value, Identifier):
                finally_block.instructions.pop(0)

        # Drop the trailing rethrow - real JS finally semantics already
        # guarantee the original exception propagates once the finally
        # body finishes, so an explicit throw here would be redundant.
        # Only strip it when it's provably a plain rethrow (the thrown
        # value is a bare identifier), to avoid discarding a throw with
        # real side effects. The instruction itself is only popped once
        # confirmed to be the terminator's actual carrier. - The same
        # invariant this codebase checks everywhere a terminator is
        # tied to a specific trailing instruction - so a real
        # value-producing instruction can never be mistaken for it.
        terminator = finally_block.terminator

        if isinstance(terminator, TerminatorThrow) and isinstance(terminator.value, Identifier):
            last = finally_block.instructions[-1] if finally_block.instructions else None
            if last is not None and last.terminator is terminator:
                finally_block.instructions.pop()
            finally_block.terminator = None

        # Hermes duplicates the finally code inline at every normal
        # exit point too (e.g., right before the catch's own return),
        # since it has no true finally construct. Now that we're
        # emitting a real `finally` clause, those inline copies must be
        # removed or the cleanup code would run twice at runtime.
        # Expression trees are register-free (registers only exist
        # while resolving values, not in the final AST), so `==`
        # reliably identifies the duplicated statements regardless of
        # which scratch registers each copy happened to use.
        finally_values = [
            instr.value
            for instr in finally_block.instructions
            if instr.value is not None
        ]

        strip_duplicate_run(try_region.try_body, finally_values)

        catch_region = try_region.catch

        if catch_region is not None:
            strip_duplicate_run(catch_region.body, finally_values)

        # Hermes may also place the duplicated finally sequence in the shared
        # continuation point following the normal completion of the inner
        # try/catch (its immediate post-dominator). This is the same copy that
        # allows `find_finally_wrapper_target` to identify the enclosing
        # finally wrapper.
        #
        # The continuation block is not part of `try_body` or `catch.body`;
        # it remains a sibling of the TryRegion in the region tree. It must
        # therefore be cleaned up separately to prevent the ``finally`` body from
        # being emitted twice.
        if cfg is not None and cfg.post_dominator_tree is not None:
            merge_block = cfg.post_dominator_tree.immediate_post_dominator(
                inner_handler["handler_block"]
            )
            if merge_block is not None:
                owner = self.graph.owner(merge_block)
                if owner is not None:
                    strip_duplicate_run(owner, finally_values)

        finally_body = SequenceRegion()
        self.graph.transfer([finally_block], finally_body)

        finally_region = FinallyRegion()
        finally_region.body = finally_body
        finally_body.parent = finally_region

        try_region.finally_ = finally_region

    @staticmethod
    def maybe_reinterpret_as_finally(try_region: TryRegion) -> None:
        """Reinterpret a lone catch as finally when it's really one.

        Handles the single-handler `try { } finally { }` case (no
        catch at all in the source): with nothing to pair against,
        `_HandlerBuilder` has no choice but to build an ordinary catch
        region out of it. If that "catch" body's last statement is a
        bare rethrow of its own bound exception - and there's at least
        one other statement before it (an empty `catch (e) { throw e; }`
        is a legitimate, if pointless, source and shouldn't be rewritten)
        - It's really a `finally` that had nowhere to attach to.

        Only handles a single straight-line block for now; a `finally`
        body with its own branching needs the fuller multi-block
        treatment `attach` performs for the two-handler case.
        """

        catch_region = try_region.catch

        if catch_region is None:
            return

        body = catch_region.body

        if len(body.children) != 1:
            return

        block = body.children[0]

        if not isinstance(block, BasicBlock):
            return

        if not isinstance(block.terminator, TerminatorThrow):
            return

        if not isinstance(block.terminator.value, Identifier):
            return

        if block.terminator.value.name != catch_region.exception:
            return

        if len(block.instructions) < 2:
            return

        # Only pop the trailing instruction once confirmed to be the
        # actual carrier of the throw terminator (see `attach` for why);
        # the terminator itself is always cleared, since the rethrow is
        # redundant under real finally semantics either way.
        if block.instructions[-1].terminator is block.terminator:
            block.instructions.pop()
        block.terminator = None

        # Same reasoning as `attach`: Hermes also duplicates the
        # `finally` code inline at the try body's own normal-completion
        # exit, not just at the handler. Missing this step leaves the
        # cleanup code printed - and actually running - twice.
        finally_values = [
            instr.value
            for instr in block.instructions
            if instr.value is not None
        ]

        strip_duplicate_run(try_region.try_body, finally_values)

        try_region.catch = None

        finally_region = FinallyRegion()
        finally_region.body = body
        body.parent = finally_region

        try_region.finally_ = finally_region
