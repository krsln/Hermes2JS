import importlib
import pkgutil
import HermesAssembly2JS.Hermes2JS


def Import_Handlers():
    package = HermesAssembly2JS.Hermes2JS.Handlers
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package.__name__}.{module_name}")
