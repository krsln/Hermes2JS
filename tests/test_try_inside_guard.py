"""A `try` whose range starts behind a null guard and its setup belongs INSIDE the guard (98/2676 `flushSpawnedWork`).

Bytecode: `if (r9 === null) goto END; r4 = env[2].T; r1 = env[385]; env[385] = 2; r5.T = null; <range starts> ... finally`.
`TryStructurer` built the `try` around the whole guard `if`, so the `finally` also ran when `r9` was null and read `r4` and
`r1`, which the setup never set. The guard's test is not protected: the `try` goes into its `then` arm, behind the setup.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_try_sits_inside_the_null_guard():
    hasm = (_DATA / "try_after_guard_setup_98_2676.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2676, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "        try {\n            if (null !== r9) {" not in code
    assert "        if (null !== r9) {\n            r5 = r2[2];\n            r4 = r5.T;" in code
    assert "            try {\n                r10 = 0;" in code


def test_default_of_a_register_written_in_a_try_inside_the_arm_still_prints():
    """96/9338 `test`: `r1 = param1; ...; if (typeof param1 === "string") { try { r1 = new SemVer(...) } catch { return false } }; r11 = r1`.

    With the `try` inside the arm, its `catch` block lies at a higher address than the `r11 = r1` read behind the
    `if`, so the repair pass took the read for one BEFORE the arm's end and dropped `r1 = param1`: the path that skips
    the arm read an `r1` nothing assigned."""
    hasm = (_DATA / "try_in_arm_keeps_default_96_9338.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9338, strict=False), verbose=False, raw=False)

    assert "    r1 = param1;\n" in out
    assert 'if (r4 === "string") {\n                try {' in out
