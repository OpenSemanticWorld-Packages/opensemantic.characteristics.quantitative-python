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

# Delete names from the namespace that are imported by wildcard but are unwanted
del Any, Optional, Field  # noqa
from opensemantic.characteristics.quantitative._collection import Unit  # noqa
from opensemantic.characteristics.quantitative._static import (  # noqa
    QuantityValue,
    TabularData,
)
from opensemantic.characteristics.quantitative._strings import UnitLiteral, unit  # noqa
