#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import argparse
import json
import logging
import re
from dataclasses import dataclass, field
from typing import Optional
from hermes_decompiler.core.logging import configure_logging, get_logger

log = get_logger(__name__)

DEFAULT_SEPARATOR = "==============="
FUNCTION_HEADER_RE = re.compile(
    r'^\[Function #(?P<number>\d+)\s+"(?P<name>[^"]*)"\s+of\s+\d+\s+bytes]'
)
# Anything outside this set is replaced with '_' when building filenames.
SAFE_CHARS_RE = re.compile(r"[^A-Za-z0-9_\-.]")
MAX_FILENAME_LEN = 150  # keep well under common OS limits (255), room for suffixes


@dataclass
class Section:
    """A single extracted section (one function, or an anonymous chunk)."""

    index: int
    start_line: int
    end_line: int
    function_number: Optional[str] = None
    function_name: Optional[str] = None
    lines: list[str] = field(default_factory=list)

    @property
    def is_function(self) -> bool:
        return self.function_number is not None

    def base_filename(self) -> str:
        if self.is_function:
            name = self.function_name or "anonymous"
            raw = f"function_{self.function_number}_{name}"
        else:
            raw = f"section_{self.index}"
        return sanitize_filename(raw)


def sanitize_filename(name: str, max_len: int = MAX_FILENAME_LEN) -> str:
    """Collapse unsafe characters and enforce a sane max length."""
    cleaned = SAFE_CHARS_RE.sub("_", name).strip("._") or "section"
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len].rstrip("._") or "section"
    return cleaned


# def unique_path(directory: Path, filename: str, extension: str) -> Path:
#     """Return a non-colliding path, appending _1, _2, ... on duplicates."""
#     candidate = directory / f"{filename}{extension}"
#     if not candidate.exists():
#         return candidate
#     n = 1
#     while True:
#         candidate = directory / f"{filename}_{n}{extension}"
#         if not candidate.exists():
#             return candidate
#         n += 1


def iter_sections(input_path: Path, separator: str):
    """
    Lazily yield Section objects by scanning the input file line by line.
    Keeps memory bounded to a single section's worth of lines at a time.
    """
    index = 0
    start_line = 1
    current_number: Optional[str] = None
    current_name: Optional[str] = None
    buffer: list[str] = []
    line_no = 0

    with input_path.open("r", encoding="utf-8", errors="replace") as f:
        for line_no, raw_line in enumerate(f, start=1):
            stripped = raw_line.rstrip("\n\r")

            if stripped == separator:
                if buffer:
                    yield Section(
                        index=index,
                        start_line=start_line,
                        end_line=line_no - 1,
                        function_number=current_number,
                        function_name=current_name,
                        lines=buffer,
                    )
                    index += 1
                buffer = []
                current_number = None
                current_name = None
                start_line = line_no + 1
                continue

            buffer.append(raw_line)

            if current_number is None:
                match = FUNCTION_HEADER_RE.match(stripped)
                if match:
                    current_number = match.group("number")
                    current_name = match.group("name") or None

    if buffer:
        yield Section(
            index=index,
            start_line=start_line,
            end_line=line_no,
            function_number=current_number,
            function_name=current_name,
            lines=buffer,
        )


def split_file(
        input_file: str,
        output_dir: str,
        separator: str = DEFAULT_SEPARATOR,
        extension: str = ".hbc",
        manifest_path: Optional[str] = None,
        dry_run: bool = False,
) -> int:
    """
    Split `input_file` into per-section files under `output_dir`.

    Returns the number of sections written. Raises on unrecoverable errors
    (missing input file, unwritable output directory, etc.).
    """
    in_path = Path(input_file)
    if not in_path.is_file():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    out_dir = Path(output_dir)
    if not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)
    elif not out_dir.exists():
        log.debug("Dry-run: output directory %s does not exist yet (would be created).", out_dir)

    manifest_entries = []
    written = 0

    for section in iter_sections(in_path, separator):
        base_name = section.base_filename()

        if dry_run:
            log.info(
                "[dry-run] section #%d (lines %d-%d) -> %s%s%s",
                section.index,
                section.start_line,
                section.end_line,
                base_name,
                extension,
                " [function]" if section.is_function else "",
            )
            written += 1
            continue

        # out_path = unique_path(out_dir, base_name, extension)
        out_path = out_dir / f"{base_name}{extension}"
        try:
            out_path.write_text("".join(section.lines), encoding="utf-8")
        except OSError as exc:
            log.error("Failed to write %s: %s", out_path, exc)
            continue

        log.info("Created: %s", out_path)
        written += 1

        manifest_entries.append(
            {
                "index": section.index,
                "output_file": str(out_path),
                "start_line": section.start_line,
                "end_line": section.end_line,
                "function_number": section.function_number,
                "function_name": section.function_name,
            }
        )

    if manifest_path and not dry_run:
        manifest_file = Path(manifest_path)
        manifest_file.write_text(
            json.dumps(
                {
                    "input_file": str(in_path),
                    "output_dir": str(out_dir),
                    "section_count": written,
                    "sections": manifest_entries,
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        log.info("Manifest written: %s", manifest_file)

    return written


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="split_output_file.py",
        description="Split a Hermes bytecode disassembly (.hbc) into one file per function.",
    )
    parser.add_argument("-i", "--input", required=True, help="Path to the input .hbc file")
    parser.add_argument("-o", "--output", required=True, help="Output directory for split sections")
    parser.add_argument(
        "--separator",
        default=DEFAULT_SEPARATOR,
        help=f"Section separator line (default: {DEFAULT_SEPARATOR!r})",
    )
    parser.add_argument(
        "--extension",
        default=".hbc",
        help="File extension for output sections (default: .hbc)",
    )
    parser.add_argument(
        "--manifest",
        default=None,
        help="Optional path to write a JSON manifest describing all sections",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the split without writing any files",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v for INFO, -vv for DEBUG)",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress all output except errors",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.quiet:
        level = logging.ERROR
    elif args.verbose >= 2:
        level = logging.DEBUG
    elif args.verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING

    configure_logging(level=level, use_color=True)

    try:
        count = split_file(
            input_file=args.input,
            output_dir=args.output,
            separator=args.separator,
            extension=args.extension,
            manifest_path=args.manifest,
            dry_run=args.dry_run,
        )
    except FileNotFoundError as exc:
        log.error(str(exc))
        return 1
    except OSError as exc:
        log.error("I/O error: %s", exc)
        return 1
    except Exception as exc:  # noqa: BLE001 - top-level safety net for CLI use
        log.error("Unexpected error: %s", exc)
        return 2

    if not args.quiet:
        prefix = "[dry-run] " if args.dry_run else ""
        print(f"✅ {prefix}Total sections: {count}")

    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
