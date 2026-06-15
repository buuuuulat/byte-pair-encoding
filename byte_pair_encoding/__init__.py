import importlib.metadata

try:
    __version__ = importlib.metadata.version("byte_pair_encoding")
except importlib.metadata.PackageNotFoundError:
    pass
