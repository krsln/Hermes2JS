from hermes_decompiler.cfg import CFGValidator
from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.cfg.CFGEdge import CFGEdge
from hermes_decompiler.cfg.ControlFlowGraph import ControlFlowGraph
from hermes_decompiler.cfg.EdgeKind import EdgeKind


class ControlFlowGraphBuilder:
    """
    Build edges between BasicBlocks.
    """

    @classmethod
    def build(cls, blocks: list[BasicBlock]) -> ControlFlowGraph:

        cfg = ControlFlowGraph.from_blocks(blocks)

        cls._connect(cfg)

        CFGValidator.validate(cfg)

        return cfg

    # Handlers whose `goto` edge represents "the condition, as already
    # polarity-baked into the emitted `if (...)` text, evaluated true".
    # See handlers/Jump/Jmp.py: JmpFalse.BuildCondition already wraps
    # the value in `!...`, so from the CFG's point of view every one of
    # these behaves identically - goto=TRUE_BRANCH, fallthrough=FALSE_BRANCH.
    _CONDITIONAL_HANDLERS = {
        "JmpTrue", "JmpTrueLong",
        "JmpFalse", "JmpFalseLong",
        "JmpUndefined", "JmpUndefinedLong",
        "JmpBuiltinIs", "JmpBuiltinIsLong",
        "JmpBuiltinIsNot", "JmpBuiltinIsNotLong",
        "JmpTypeOfIs",
    }

    @classmethod
    def _connect(cls, cfg: ControlFlowGraph):

        ordered = sorted(
            cfg,
            key=lambda block: block.start_addr,
        )

        for index, block in enumerate(ordered):

            if not block.instructions:
                continue

            last = block.instructions[-1]
            conditional = last.handler in cls._CONDITIONAL_HANDLERS

            #
            # explicit jump
            #

            if last.goto is not None:

                target = cfg.get_block(last.goto)

                if target is not None:
                    cls._connect_edge(
                        block,
                        target,
                        EdgeKind.TRUE_BRANCH if conditional else EdgeKind.UNCONDITIONAL,
                    )

            #
            # fallthrough
            #

            if cls._falls_through(last):

                if index + 1 < len(ordered):
                    cls._connect_edge(
                        block,
                        ordered[index + 1],
                        EdgeKind.FALSE_BRANCH if conditional else EdgeKind.FALLTHROUGH,
                    )

    @staticmethod
    def _connect_edge(
            source: BasicBlock,
            target: BasicBlock,
            kind: EdgeKind,
    ):

        edge = CFGEdge(
            source=source.id,
            target=target.id,
            kind=kind,
        )

        source.outgoing.append(edge)

        target.incoming.append(edge)

    @staticmethod
    def _falls_through(result) -> bool:
        """
        True if control can reach the next instruction in program order
        after this one.

        Ret/Throw/CompleteGenerator never fall through - they leave the
        function. Unconditional `Jmp`/`JmpLong` never fall through
        either - their `goto` edge (added above, kind=UNCONDITIONAL) is
        the *only* way out of the block; there is no "condition false"
        path to fall into.

        Conditional jumps (`JmpTrue`, `JmpFalse`, `JmpUndefined`,
        `JmpBuiltinIs`, `JmpBuiltinIsNot`, `JmpTypeOfIs`, and their
        `*Long` variants) DO fall through: the `goto` edge covers the
        "condition true" path (kind=TRUE_BRANCH), and the fallthrough
        edge added here covers the "condition false" / continuation
        path. Together they give exactly the two outgoing edges that
        IfRegion structuring depends on.

        BUG FIX (was): this previously only excluded {Ret, Throw,
        CompleteGenerator}, so a plain unconditional `Jmp` block ended
        up with BOTH a goto edge and a spurious fallthrough edge - two
        outgoing edges on a block that only ever has one real
        successor. That, in turn, made `IfRegion._is_if_header`'s
        `len(outgoing) == 2` check misfire on ordinary unconditional
        jumps (e.g. the "jump past the else branch" at the end of an
        if-block, or a loop's back-edge), producing false-positive
        if-headers with a bogus second branch.

        TODO: `SwitchImm` is a genuine multi-way branch and isn't
        handled here at all yet - it doesn't set `goto`, so today it
        falls into the `True` case below and gets a single spurious
        FALLTHROUGH edge to the next block, silently dropping every
        other case target. Needs a dedicated multi-edge connection
        (kind=UNCONDITIONAL per case, probably a new EdgeKind.SWITCH_CASE)
        before SwitchRegion structuring can be attempted.
        """

        non_falling = {
            "Ret",
            "Throw",
            "CompleteGenerator",
            "Jmp",
            "JmpLong",
        }

        return result.handler not in non_falling
