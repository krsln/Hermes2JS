"""`RegisterReadIndex` answers exactly what the plain `_reads_register_by_name` scan answers.

`UnfoldedMergeRepairPass` asks "does code after this `if` read the register by name?" for every write it looks at, and
the plain scan walks the whole function each time (98/3523 `parseURL` spent 230 s of its render there). The pass now
asks an index built once; this renders functions with the pass's question answered BOTH ways and compares each answer.
"""

import importlib
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.shared import _repoint

pass_module = importlib.import_module(
    "hermes_decompiler.backend.transforms.region_passes.UnfoldedMergeRepairPass"
)
_DATA = Path(__file__).parent / "data"
_FIXTURES = (
    "folded_value_test_inside_a_loop_96_1927.hasm",
    "resumed_value_copied_into_an_object_literal_96_12207.hasm",
)


def test_every_answer_of_the_index_is_the_plain_scans(monkeypatch):
    compared = []
    original = pass_module.UnfoldedMergeRepairPass._named_after_the_if

    real_reads = _repoint.RegisterReadIndex.reads

    def recording(index, register, after_address, ignore_blocks=()):
        state.append((after_address, ignore_blocks))

        return real_reads(index, register, after_address, ignore_blocks)

    state = []

    def run(self, write, region_blocks):
        answer = original(self, write, region_blocks)
        after_address, ignored = state[-1]
        plain = _repoint._reads_register_by_name(
            self.cfg, write.dest_reg, after_address, root=self.graph.root, ignore_blocks=ignored
        )
        compared.append((answer, plain))

        return answer

    monkeypatch.setattr(_repoint.RegisterReadIndex, "reads", recording)
    monkeypatch.setattr(pass_module.UnfoldedMergeRepairPass, "_named_after_the_if", run)

    for name in _FIXTURES:
        hasm = (_DATA / name).read_text(encoding="utf-8")
        Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert compared, "the pass never asked the question"
    assert all(answer == plain for answer, plain in compared)
