#!/usr/bin/env python3
"""
Generate opcode_version_map.json from a local hermes-dec checkout.

This is a developer utility and is not used at runtime.
The generated JSON is committed to the repository.

Example:

python ./tests/tools/update_opcode_catalog.py \
    --hermes-dec ./vendor/hermes-dec \
    --output ./tests/data/opcode_version_map.json
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from collections import defaultdict
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate opcode version catalog from hermes-dec."
    )

    parser.add_argument(
        "--hermes-dec",
        type=Path,
        required=True,
        help="Path to the hermes-dec repository.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Destination JSON file.",
    )

    return parser.parse_args()


@contextmanager
def temporary_sys_path(path: Path) -> Iterator[None]:
    """
    Temporarily prepend a directory to ``sys.path`` while importing modules.
    """
    path_str = str(path)

    sys.path.insert(0, path_str)
    try:
        yield
    finally:
        try:
            sys.path.remove(path_str)
        except ValueError:
            pass


def discover_versions(opcodes_dir: Path) -> list[int]:
    """
    Discover all available Hermes bytecode versions.
    """
    versions: list[int] = []

    for path in sorted(opcodes_dir.glob("hbc*.py")):
        if path.name == "__init__.py":
            continue

        suffix = path.stem[3:]

        if suffix.isdigit():
            versions.append(int(suffix))

    if not versions:
        raise RuntimeError(
            f"No opcode definition files found in:\n{opcodes_dir}"
        )

    return versions


def load_module(module_name: str) -> ModuleType:
    """
    Import a Hermes opcode definition module.
    """
    sys.modules.pop(module_name, None)
    return importlib.import_module(module_name)


def build_catalog(
        src_dir: Path,
        versions: list[int],
) -> dict[str, list[int]]:
    """
    Build an opcode -> bytecode versions mapping.
    """
    version_map: defaultdict[str, set[int]] = defaultdict(set)

    with temporary_sys_path(src_dir):
        for version in versions:
            module = load_module(
                f"hermes_dec.parsers.hbc_opcodes.hbc{version}"
            )

            instructions = getattr(module, "_instructions", None)

            if not isinstance(instructions, list):
                raise RuntimeError(
                    f"hbc{version} does not expose '_instructions'."
                )

            if not instructions:
                raise RuntimeError(
                    f"hbc{version} contains no instructions."
                )

            for instruction in instructions:
                try:
                    name = instruction.name
                except AttributeError as exc:
                    raise RuntimeError(
                        f"Invalid instruction in hbc{version}: {instruction!r}"
                    ) from exc

                version_map[name].add(version)

    return {
        opcode: sorted(found_versions)
        for opcode, found_versions in sorted(version_map.items())
    }


def write_catalog(
        catalog: dict[str, list[int]],
        output: Path,
) -> None:
    """
    Write the generated opcode catalog to disk.
    """
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8") as fp:
        json.dump(
            catalog,
            fp,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
        )
        fp.write("\n")


def main() -> None:
    args = parse_args()

    hermes_dec = args.hermes_dec.expanduser().resolve()
    output = args.output.expanduser().resolve()

    src_dir = hermes_dec / "src"
    opcodes_dir = src_dir / "hermes_dec" / "parsers" / "hbc_opcodes"

    if not src_dir.is_dir():
        raise SystemExit(
            f"Could not find:\n{src_dir}"
        )

    if not opcodes_dir.is_dir():
        raise SystemExit(
            f"Could not find:\n{opcodes_dir}"
        )

    versions = discover_versions(opcodes_dir)
    catalog = build_catalog(src_dir, versions)

    write_catalog(catalog, output)

    print()
    print("Opcode catalog generated successfully.")
    print(f"Versions : {versions[0]}-{versions[-1]}")
    print(f"Opcodes  : {len(catalog)}")
    print(f"Output   : {output}")


if __name__ == "__main__":
    main()
