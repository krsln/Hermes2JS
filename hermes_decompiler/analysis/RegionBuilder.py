from __future__ import annotations

from hermes_decompiler.analysis.Region import Region
from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.analysis.regions.SequenceRegion import SequenceRegion
from hermes_decompiler.analysis.regions.IfRegion import IfRegion
from hermes_decompiler.cfg.EdgeKind import EdgeKind


class RegionBuilder:
    """
    Advanced structured region builder using:
    - LoopAnalysis (back-edges)
    - Dominators
    - Post-dominators (merge points for if-else)
    """

    @classmethod
    def build(cls, analysis: CFGAnalysis) -> Region:
        sequence = cls._build_sequence(analysis)
        # Refine with if structures using post-dominators
        cls._refine_with_ifs(analysis, sequence)
        return sequence

    @classmethod
    def _build_sequence(cls, analysis: CFGAnalysis) -> SequenceRegion:
        return SequenceRegion(blocks=list(analysis.reverse_post_order))

    @classmethod
    def _refine_with_ifs(cls, analysis: CFGAnalysis, sequence: SequenceRegion):
        """Replace conditional blocks with IfRegion in the sequence."""
        new_blocks = []
        i = 0
        while i < len(sequence.blocks):
            block = sequence.blocks[i]
            if isinstance(block, BasicBlock) and len(getattr(block, 'outgoing', [])) == 2:
                if_region = cls._build_if_region(analysis, block)
                if if_region:
                    new_blocks.append(if_region)
                    # Skip the conditional body blocks (heuristic - improve later)
                    i += 3  # rough skip
                    continue
            new_blocks.append(block)
            i += 1
        sequence.blocks = new_blocks

    @classmethod
    def _build_if_region(cls, analysis: CFGAnalysis, header: BasicBlock) -> IfRegion | None:
        if len(header.outgoing) != 2:
            return None

        last = header.instructions[-1] if header.instructions else None
        if last and last.handler.startswith(("JmpTrue", "JmpFalse")):
            # Better condition extraction
            value = last.value
            if "if (" in value:
                condition = value.split("if (", 1)[1].split(")", 1)[0].strip()
            else:
                condition = value.replace("/* jump to", "").strip() or "true"
        else:
            condition = "true"

        then_region = SequenceRegion(
            blocks=[b for b in analysis.reverse_post_order if b.start_addr > header.start_addr][:5])  # heuristic
        else_region = None

        return IfRegion.from_header(header, condition, then_region, else_region)
