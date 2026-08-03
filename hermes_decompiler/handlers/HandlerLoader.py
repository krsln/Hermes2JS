from __future__ import annotations

import importlib
import logging
import pkgutil
from dataclasses import dataclass, field
from typing import List, Tuple

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class HandlerLoadReport:
    """
    Result of a `HandlerLoader.load()` call.

    Kept as an explicit object (rather than just logging) so callers -
    tests, a CLI `--check-handlers` command, CI - can assert on it
    directly instead of scraping log output.
    """

    loaded: List[str] = field(default_factory=list)
    failed: List[Tuple[str, BaseException]] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.failed

    def raise_if_failed(self) -> None:
        if not self.failed:
            return

        names = ", ".join(name for name, _ in self.failed)
        raise HandlerLoadError(
            f"{len(self.failed)} handler module(s) failed to import: {names}",
            self,
        )


class HandlerLoadError(RuntimeError):
    def __init__(self, message: str, report: HandlerLoadReport):
        super().__init__(message)
        self.report = report


class HandlerLoader:

    @classmethod
    def load(cls, *, strict: bool = True) -> HandlerLoadReport:
        """
        Import every opcode handler module found under the handlers
        package, including modules in nested subpackages, so their
        `OpcodeHandler` subclasses register themselves.

        strict:
            - True (default): a module that fails to import is a bug,
              not something to route around silently - a broken handler
              module means that opcode quietly falls back to
              `NoHandlerError` at dispatch time, with no clue why. Raises
              `HandlerLoadError` (which carries the full report) after
              attempting every module, so a single broken file doesn't
              hide failures in modules that would have imported fine.
            - False: best-effort - collects failures into the returned
              report instead of raising. Use this for tooling that wants
              to inspect *which* handlers are broken (e.g. a `--check`
              CLI command) without crashing on the first one.

        Returns a `HandlerLoadReport` either way (when strict=True and
        nothing failed, or after inspecting the report when strict=False).
        """
        package = importlib.import_module(__package__)
        report = HandlerLoadReport()

        for _, module_name, is_package in pkgutil.walk_packages(
                package.__path__,
                package.__name__ + ".",
        ):
            if is_package:
                continue

            try:
                importlib.import_module(module_name)
            except BaseException as exc:  # noqa: BLE001 - intentionally broad, see docstring
                print(module_name)
                raise
                logger.exception("Failed to import handler module: %s", module_name)
                report.failed.append((module_name, exc))
            else:
                logger.debug("Loaded handler module: %s", module_name)
                report.loaded.append(module_name)

        if strict:
            report.raise_if_failed()

        return report
