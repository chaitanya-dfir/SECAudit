import importlib
import pkgutil
import os

def load_all_checks():
    checks = []
    package_dir = os.path.dirname(__file__)
    for _, modname, _ in pkgutil.iter_modules([package_dir]):
        mod = importlib.import_module(f"modules.{modname}")
        if hasattr(mod, "CHECKS"):
            checks.extend(mod.CHECKS)
    return checks
