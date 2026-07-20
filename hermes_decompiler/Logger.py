"""
Centralized logging for hermes_decompiler.

Library code should NEVER call print() for diagnostics and should never
configure the root logger (that's the application's job). We attach a
NullHandler by default, so the library is silent unless the consuming
application explicitly wires up logging.

Usage in any module:

    from hermes_decompiler.Logger import get_logger
    logger = get_logger(__name__)

    logger.debug("Unparsed line: %s", line)
    logger.warning("Could not parse metadata segment: %s", segment)
    logger.error("Dispatch failed for opcode %s", opcode, exc_info=True)

Applications that want console output (e.g., a CLI script) should call
`logging.basicConfig(level=logging.INFO)` themselves, once, at startup -
importing this module must never do that on your behalf, since it would
silently reconfigure the *root* logger for the entire host application.
(The previous version of this file called basicConfig() at import time -
that antipattern has been removed.)
"""
import logging

_ROOT_NAME = "hermes_decompiler"

logging.getLogger(_ROOT_NAME).addHandler(logging.NullHandler())


def get_logger(module_name: str) -> logging.Logger:
    """Return a namespaced logger, e.g., hermes_decompiler.parsers.metadata_parser"""
    if module_name.startswith(_ROOT_NAME):
        return logging.getLogger(module_name)
    return logging.getLogger(f"{_ROOT_NAME}.{module_name}")


# Backwards-compatible module-level logger, matching the old
# `from hermes_decompiler.Logger import logger` usage (e.g., FileOps.py
# before this refactor). New code should prefer get_logger(__name__).
logger = get_logger(__name__)

logging.basicConfig(format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
logging.getLogger("hermes_decompiler").setLevel(logging.INFO)
