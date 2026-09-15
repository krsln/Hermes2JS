"""
Live cross-check of `BytecodeFileHeader.parse()` against the official
`hermesc` compiler's own `-dump-bytecode` report, for the bytecode
versions pinned in `tools/hermes/versions.json`.

Skipped (not failed) when the relevant hermesc isn't installed - install
it with `./tools/hermes/fetch_compiler.sh <version>` to run this for
real; see `tools/hermes/README.md`.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.oracle.HermescFileInfo import HermescFileInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
DUMP_SCRIPT = REPO_ROOT / "tools" / "hermes" / "dump_bytecode.sh"

# version -> bundle fixture already committed in this repo
BUNDLES = {
    96: REPO_ROOT / "apps" / "testy" / "96" / "index.android.bundle",
    98: REPO_ROOT / "apps" / "testy" / "98" / "index.android.bundle",
}


def _hermesc_installed(version: int) -> bool:
    compiler_dir = REPO_ROOT / "tools" / "hermes" / "compilers" / str(version)
    return any(compiler_dir.glob("node_modules/hermes-compiler/hermesc/*/hermesc"))


def _run_oracle_dump(version: int, bundle: Path, tmp_path: Path) -> str:
    output = tmp_path / f"oracle-{version}.hdump"
    subprocess.run(
        [str(DUMP_SCRIPT), str(version), str(bundle), str(output)],
        check=True, capture_output=True, text=True,
    )
    return output.read_text()


@pytest.mark.parametrize("version", sorted(BUNDLES))
def test_header_matches_hermesc_oracle(version: int, tmp_path: Path):
    bundle = BUNDLES[version]
    if not bundle.is_file():
        pytest.skip(f"fixture not found: {bundle}")
    if not _hermesc_installed(version):
        pytest.skip(
            f"hermesc {version} not installed - run "
            f"./tools/hermes/fetch_compiler.sh {version} first"
        )

    header = BytecodeFileHeader.parse(bundle.read_bytes())
    oracle = HermescFileInfo.parse(_run_oracle_dump(version, bundle, tmp_path))

    ours = {
        "version": header.version,
        "source_hash": header.source_hash.hex(),
        "function_count": header.function_count,
        "string_count": header.string_count,
        "bigint_count": header.bigint_count,
        "string_kind_count": header.string_kind_count,
        "regexp_count": header.regexp_count,
        "segment_id": header.segment_id,
        "cjs_module_count": header.cjs_module_count,
        "function_source_count": header.function_source_count,
        "static_builtins": header.options.static_builtins,
        "cjs_modules_statically_resolved": header.options.cjs_modules_statically_resolved,
    }

    for field, our_value in ours.items():
        expected = getattr(oracle, field)
        assert our_value == expected, f"{field}: ours={our_value!r} oracle={expected!r}"
