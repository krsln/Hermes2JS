import importlib
import pkgutil
import hermes_decompiler

# Define Import_Handlers inside Handlers/__init__.py
# This makes Import_Handlers() accessible via:
#       from HermesAssembly2JS.Hermes2JS.Handlers import Import_AllHandlers
def Import_Handlers():
    package = hermes_decompiler.handlers
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package.__name__}.{module_name}")
