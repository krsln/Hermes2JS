"""A `return undefined` block that carries its own `ReturnStatement` is still falling off the end (F-178).

`flow_audit._bare_undefined_return` demanded that no instruction of the block print a statement, but the `Ret`
instruction carries the `ReturnStatement` itself, so no `return undefined` block ever qualified and every
`switch` whose `default` runs on into one (96/2103 `commitDeletionEffectsOnFiber`) counted a lost path. The count
sends a function through the retries, which may then adopt a worse tree for a loss that was never one.

    96/2103  the `default` body falls into the closing `return undefined`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.StructuralAnalyzer import StructuralAnalyzer

_DATA = Path(__file__).parent / "data"


def test_falling_into_the_closing_return_is_not_a_lost_path():
    counts = []
    original = StructuralAnalyzer.build

    def build(self):
        root = original(self)
        counts.append(getattr(self.cfg, "lost_edges", None))
        return root

    StructuralAnalyzer.build = build

    try:
        hasm = (_DATA / "switch_case_fallthrough_96_2103.hasm").read_text(encoding="utf-8")
        Decompiler.render(Decompiler.build_context(hasm, 2103, strict=False), verbose=False, raw=False)
    finally:
        StructuralAnalyzer.build = original

    # every attempt, the retries too: the one that was adopted lost a path that was never lost
    assert counts and max(counts) == 0
