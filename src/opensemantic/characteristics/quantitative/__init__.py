from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "opensemantic.characteristics.quantitative"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

from opensemantic.characteristics.quantitative._model import *  # noqa

# Delete names from the namespace that are imported by wildcard but are unwanted.
# Tolerant of which typing/pydantic helpers a given generator version leaks.
for _unwanted in ("Any", "Field"):  # noqa
    globals().pop(_unwanted, None)
from opensemantic.characteristics.quantitative._collection import Unit  # noqa

# QuantityValue is the merged generated class (Characteristic + _static mixin)
# exported by the wildcard above; only TabularData is _static-only.
from opensemantic.characteristics.quantitative._static import TabularData  # noqa
