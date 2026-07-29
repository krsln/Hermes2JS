from __future__ import annotations

import logging


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\033[36m",
        logging.INFO: "\033[32m",
        logging.WARNING: "\033[33m",
        logging.ERROR: "\033[31m",
        logging.CRITICAL: "\033[41m",
    }

    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)

        color = self.COLORS.get(record.levelno)

        if color is None:
            return message

        return f"{color}{message}{self.RESET}"
