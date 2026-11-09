"""The package imports and exposes a version; nothing else exists yet."""

import importlib


def test_package_imports_and_has_version():
    module = importlib.import_module("skifer_engine")
    assert module.__version__ == "0.1.0.dev0"
