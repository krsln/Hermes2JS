import importlib
import logging
import pkgutil
import hermes_decompiler

logger = logging.getLogger(__name__)


class HandlerLoader:

    @classmethod
    def load(cls) -> None:
        """
        Import every opcode handler module found under the handler's package,
        including modules located in nested subpackages.
        """
        package = hermes_decompiler.handlers

        for _, module_name, is_package in pkgutil.walk_packages(
                package.__path__,
                package.__name__ + ".",
        ):
            if is_package:
                continue

            try:
                importlib.import_module(module_name)
                logger.debug("Loaded handler: %s", module_name)
            except (ImportError, ModuleNotFoundError):
                logger.exception("Failed to import handler: %s", module_name)

    # def _all_subclasses(cls):
    #     """Yield all subclasses recursively."""
    #     for subclass in cls.__subclasses__():
    #         yield subclass
    #         yield from _all_subclasses(subclass)
    #
    #
    # def get_all_handlers() -> list[Type[OpcodeHandler]]:
    #     """
    #     Return every registered OpcodeHandler implementation.
    #     """
    #     return list(_all_subclasses(OpcodeHandler))
