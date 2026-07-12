#!/usr/bin/env python3

from pathlib import Path
import argparse

from hermes2js.FileOps import GetFiles, ProcessFile
from hermes2js.Logger import logger


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Hermes .hbc sections to JavaScript."
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=Path,
        help="Directory containing .hbc section files.",
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="Directory where JavaScript files will be written.",
    )

    parser.add_argument(
        "--start",
        type=int,
        help="First section number to process.",
    )

    parser.add_argument(
        "--end",
        type=int,
        help="Last section number to process.",
    )

    args = parser.parse_args()

    input_dir = args.input.resolve()
    output_dir = args.output.resolve()

    logger.info("Starting .hbc to JavaScript conversion")

    if not input_dir.exists():
        logger.error("Input directory does not exist: %s", input_dir)
        raise SystemExit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    files = GetFiles(
        str(input_dir),
        str(output_dir),
        start=args.start,
        end=args.end,
    )

    if not files:
        logger.info("No .hbc files found.")
        return

    logger.info("Found %d .hbc files", len(files))

    for filename, section_index in files:
        file_path = input_dir / filename
        ProcessFile(section_index, str(file_path), str(output_dir))

    logger.info("Conversion completed successfully")


if __name__ == "__main__":
    main()