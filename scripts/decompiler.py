#!/usr/bin/env python3
"""
decompiler.py
=============

Batch-driver for the Hermes .hbc -> JavaScript decompilation pipeline.

Walks an input directory of `section_<number>.hbc` files (produced by
`hermes_splitter.py`), runs each through `hermes2js.FileOps.ProcessFile`,
and writes results to an output directory.

This is a thin, hardened CLI wrapper around the existing `FileOps` module —
it does not change the conversion logic itself, only how the batch is run:

- input/output directories are configurable via CLI flags (no more editing
  the script to point at a different fixture set)
- per-file try/except so a single bad section doesn't abort the whole batch
- optional --start/--end range and --limit for partial/resumable runs
- --fail-fast to restore the "stop on first error" behavior if desired
- --dry-run to preview what would be processed without running the decompiler
- a run summary (success / failed / skipped counts, elapsed time) and a
  non-zero exit code if any file failed, for CI/script-friendly usage
- optional JSON report of per-file outcomes (--report)

Usage
-----
    python scripts/decompiler.py \\
        --input-dir apps/demo/fixtures/sections \\
        --output-dir apps/demo/fixtures/results

    # Only a specific range, stop on first failure, verbose logging
    python scripts/decompiler.py -i sections/ -o results/ --start 9594 --end 9600 --fail-fast -v

    # Preview only
    python scripts/decompiler.py -i sections/ -o results/ --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Optional

from hermes2js.FileOps import ProcessFile, GetFiles
from hermes2js.Logger import logger

DEFAULT_INPUT_DIR = "../apps/demo/fixtures/sections"
DEFAULT_OUTPUT_DIR = "../apps/demo/fixtures/results"


def resolve_dir(path_str: str, must_exist: bool) -> Path:
    path = Path(path_str)
    if must_exist and not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {path}")
    if must_exist and not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")
    return path


def run(
    input_dir: str,
    output_dir: str,
    start: Optional[int] = None,
    end: Optional[int] = None,
    limit: Optional[int] = None,
    fail_fast: bool = False,
    dry_run: bool = False,
    report_path: Optional[str] = None,
) -> int:
    """
    Execute the batch conversion. Returns a process exit code
    (0 = all succeeded, 1 = one or more files failed, 2 = setup error).
    """
    try:
        in_path = resolve_dir(input_dir, must_exist=True)
    except (FileNotFoundError, NotADirectoryError) as exc:
        logger.error(str(exc))
        return 2

    out_path = Path(output_dir)
    if not dry_run:
        out_path.mkdir(parents=True, exist_ok=True)

    kwargs = {}
    if start is not None:
        kwargs["start"] = start
    if end is not None:
        kwargs["end"] = end

    try:
        files = GetFiles(str(in_path), str(out_path), **kwargs)
    except Exception as exc:  # noqa: BLE001 - surface any FileOps error clearly
        logger.error(f"Failed to enumerate input files: {exc}")
        return 2

    if not files:
        logger.info("No .hbc files found.")
        return 0

    if limit is not None:
        files = files[:limit]

    logger.info(f"Found {len(files)} .hbc file(s) in {in_path}\n")

    succeeded: list[int] = []
    failed: list[dict] = []
    started_at = time.monotonic()

    for filename, section_index in files:
        file_path = os.path.join(str(in_path), filename)

        if dry_run:
            logger.info(f"[dry-run] would process section #{section_index}: {filename}")
            succeeded.append(section_index)
            continue

        logger.debug(f"Processing section #{section_index}: {filename}")
        try:
            ProcessFile(section_index, file_path, str(out_path))
            succeeded.append(section_index)
        except Exception as exc:  # noqa: BLE001 - one bad section must not kill the batch
            logger.error(f"Section #{section_index} ({filename}) failed: {exc}")
            failed.append({"section_index": section_index, "file": filename, "error": str(exc)})
            if fail_fast:
                logger.error("--fail-fast set: stopping after first failure.")
                break

    elapsed = time.monotonic() - started_at

    if report_path and not dry_run:
        report_file = Path(report_path)
        report_file.write_text(
            json.dumps(
                {
                    "input_dir": str(in_path),
                    "output_dir": str(out_path),
                    "total": len(files),
                    "succeeded": len(succeeded),
                    "failed": failed,
                    "elapsed_seconds": round(elapsed, 3),
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        logger.info(f"Report written: {report_file}")

    prefix = "[dry-run] " if dry_run else ""
    logger.info(
        f"{prefix}Conversion finished in {elapsed:.2f}s — "
        f"{len(succeeded)} succeeded, {len(failed)} failed (of {len(files)})"
    )

    return 1 if failed else 0


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="decompiler.py",
        description="Batch-convert Hermes .hbc sections to JavaScript.",
    )
    parser.add_argument(
        "-i", "--input-dir",
        default=DEFAULT_INPUT_DIR,
        help=f"Directory containing section_<number>.hbc files (default: {DEFAULT_INPUT_DIR})",
    )
    parser.add_argument(
        "-o", "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to write decompiled JS results (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument("--start", type=int, default=None, help="First section index to process (inclusive)")
    parser.add_argument("--end", type=int, default=None, help="Last section index to process (inclusive)")
    parser.add_argument("--limit", type=int, default=None, help="Process at most N files (after start/end filtering)")
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop on the first failed section instead of continuing the batch",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List the files that would be processed without running the decompiler",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Optional path to write a JSON summary report of the run",
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
        help="Suppress INFO-level output; only warnings/errors are shown",
    )
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Adjust the shared project logger's level without replacing its handlers."""
    if quiet:
        level = logging.WARNING
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.INFO  # sensible default: keep prior script's verbosity
    logger.setLevel(level)


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    logger.info("Starting .hbc to JavaScript conversion")

    if args.start is not None and args.end is not None and args.start > args.end:
        logger.error(f"--start ({args.start}) cannot be greater than --end ({args.end})")
        return 2

    try:
        return run(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            start=args.start,
            end=args.end,
            limit=args.limit,
            fail_fast=args.fail_fast,
            dry_run=args.dry_run,
            report_path=args.report,
        )
    except KeyboardInterrupt:
        logger.warning("Interrupted by user.")
        return 130


if __name__ == "__main__":
    sys.exit(main())