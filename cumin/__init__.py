from .cumin_py import load as cumin_load
import json

def loads(source: str):
    return json.loads(cumin_load(source))


__all__ = [
    "load",
]
