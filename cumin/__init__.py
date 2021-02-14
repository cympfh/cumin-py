from .cumin_py import load as cumin_load
import json

def loads(source: str):
    """Load cumin from String"""
    return json.loads(cumin_load(source))


def load(filepath: str):
    """Load cumin from File"""
    return loads(open(filepath).read())


__all__ = [
    "load",
    "loads",
]
