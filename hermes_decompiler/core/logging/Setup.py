from __future__ import annotations

import logging
import logging.handlers

from .ColorFormatter import ColorFormatter

_ROOT = "hermes_decompiler"
_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"

logging.getLogger(_FORMAT).addHandler(logging.NullHandler())


def get_logger(module_name: str) -> logging.Logger:
    """
    Return a logger inside the hermes_decompiler namespace.

    Example:
        get_logger(__name__)
    """

    if module_name.startswith(_ROOT):
        return logging.getLogger(module_name)

    return logging.getLogger(f"{_ROOT}.{module_name}")


def configure_logging(*, level: int = logging.INFO, use_color: bool = True, ) -> None:
    """
    Configure console logging for Hermes2JS CLI.
    """

    handler = logging.StreamHandler()

    if use_color:
        formatter = ColorFormatter(_FORMAT)
    else:
        formatter = logging.Formatter(_FORMAT)

    handler.setFormatter(formatter)

    logger = logging.getLogger(_ROOT)

    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


def logging_test() -> None:
    logger = logging.getLogger(_ROOT)
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
