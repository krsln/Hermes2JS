#!/usr/bin/env python3
import argparse
import logging
from pathlib import Path

from hermes_decompiler.core.Exceptions import OpcodeDispatchError, NoHandlerError
from hermes_decompiler.core.io import FileOperations
from hermes_decompiler.core.logging import configure_logging, get_logger

logger = get_logger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Hermes .hbc sections to JavaScript."
    )

    LOG_LEVELS = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    DESC_INPUT = "Directory containing .hbc section files."
    DESC_OUTPUT = "Directory where JavaScript files will be written."
    DESC_START = "First section number to process."
    DESC_END = "Last section number to process."
    DESC_STRICT = "Fail on first opcode error."
    DESC_NO_VERBOSE = "Disable source comments."
    DESC_NO_RAW = "Disable raw files."
    DESC_LOG_LEVEL = "Logging verbosity."

    parser.add_argument("-i", "--input", required=True, type=Path, help=DESC_INPUT)
    parser.add_argument("-o", "--output", required=True, type=Path, help=DESC_OUTPUT)
    parser.add_argument("--start", type=int, help=DESC_START)
    parser.add_argument("--end", type=int, help=DESC_END)
    parser.add_argument("--strict", action="store_true", help=DESC_STRICT)
    parser.add_argument("--no-verbose", action="store_false", dest="verbose", help=DESC_NO_VERBOSE)
    parser.add_argument("--no-raw", action="store_false", dest="raw", help=DESC_NO_RAW)
    parser.add_argument("--log-level", default="INFO", choices=LOG_LEVELS, help=DESC_LOG_LEVEL)

    parser.set_defaults(verbose=True)
    parser.set_defaults(raw=True)

    args = parser.parse_args()

    input_dir = args.input.resolve()
    output_dir = args.output.resolve()

    # configure_logging(level=logging.DEBUG, use_color=True)
    configure_logging(level=LOG_LEVELS[args.log_level], use_color=True)
    # logging_test()

    logger.info("Starting .hbc to JavaScript conversion. Verbose: %s | Strict: %s", args.verbose, args.strict)

    if not input_dir.exists():
        logger.error("Input directory does not exist: %s", input_dir)
        raise SystemExit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    files = FileOperations.get_section_files(
        str(input_dir),
        str(output_dir),
        start=args.start,
        end=args.end,
    )

    if not files:
        logger.info("No .hbc files found.")
        return

    logger.info("Found %d .hbc files", len(files))
    logger.info("input \t%s", input_dir)
    logger.info("output \t%s", output_dir)

    successful = 0
    failed = 0

    for filename, section_index in files:
        file_path = input_dir / filename

        try:
            result = FileOperations.process_section(
                section_index, str(file_path), str(output_dir),
                args.verbose, args.raw, args.strict,
            )
        except (OpcodeDispatchError, NoHandlerError) as e:
            logger.error("Batch stopped in strict mode at section #%s: %s", section_index, e)
            raise SystemExit(1)

        if result:
            successful += 1
        else:
            failed += 1

    logger.info("Conversion finished: %d succeeded, %d failed, %d total", successful, failed, len(files))

    if failed:
        logger.error("%d/%d sections failed - see errors above.", failed, len(files))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
