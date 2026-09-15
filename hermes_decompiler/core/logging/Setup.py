from __future__ import annotations

import logging
import logging.handlers

from .ColorFormatter import ColorFormatter

_ROOT = "hermes_decompiler"
_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"

logging.getLogger(_ROOT).addHandler(logging.NullHandler())


def get_logger(module_name: str) -> logging.Logger:
    """
    Return a logger inside the hermes_decompiler namespace.

    Example:
        get_logger(__name__)
    """

    if module_name.startswith(_ROOT):
        return logging.getLogger(module_name)

    return logging.getLogger(f"{_ROOT}.{module_name}")


def configure_logging(*, level: int = logging.INFO, use_color: bool | None = None) -> None:
    """
    Configure console logging for Hermes2JS CLI.

    Args:
        level: Root logger level.
        use_color: Whether to wrap each formatted line in ANSI color
            codes (see `ColorFormatter`). Defaults to `None`, which
            auto-detects: color is enabled only when the handler's
            stream is an interactive terminal (`isatty()`). Passing an
            explicit `True`/`False` overrides detection either way -
            e.g. a `--color`/`--no-color` CLI flag can still force it.
            Auto-detection matters because a bare `True` default here
            previously meant every redirected-to-file or piped run
            (`... > run.log`, CI log capture, `| tee`) got raw
            `\\033[...m` escape sequences baked into otherwise
            plain-text logs.
    """

    handler = logging.StreamHandler()

    if use_color is None:
        use_color = getattr(handler.stream, "isatty", lambda: False)()

    if use_color:
        formatter = ColorFormatter(_FORMAT, datefmt=_DATEFMT)
    else:
        formatter = logging.Formatter(_FORMAT, datefmt=_DATEFMT)

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
