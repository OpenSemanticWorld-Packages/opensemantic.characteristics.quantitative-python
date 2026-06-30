<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/opensemantic.characteristics.quantitative.svg?branch=main)](https://cirrus-ci.com/github/<USER>/opensemantic.characteristics.quantitative)
[![ReadTheDocs](https://readthedocs.org/projects/opensemantic.characteristics.quantitative/badge/?version=latest)](https://opensemantic.characteristics.quantitative.readthedocs.io/en/stable/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/opensemantic.characteristics.quantitative.svg)](https://anaconda.org/conda-forge/opensemantic.characteristics.quantitative)
[![Monthly Downloads](https://pepy.tech/badge/opensemantic.characteristics.quantitative/month)](https://pepy.tech/project/opensemantic.characteristics.quantitative)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/opensemantic.characteristics.quantitative)
-->

[![PyPI-Server](https://img.shields.io/pypi/v/opensemantic.characteristics.quantitative.svg)](https://pypi.org/project/opensemantic.characteristics.quantitative/)
[![Coveralls](https://img.shields.io/coveralls/github/OpenSemanticWorld-Packages/opensemantic.characteristics.quantitative/main.svg)](https://coveralls.io/r/OpenSemanticWorld-Packages/opensemantic.characteristics.quantitative)
[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# opensemantic.characteristics.quantitative

> Library with Python models derived from the page package world.opensemantic.characteristics.quantitative

Quantities and units generated from [QUDT](https://www.qudt.org). [pint](https://pypi.org/project/ucumvert/) mapping was done with support from [ucumvert](https://pypi.org/project/ucumvert/)

## Usage

```python
from opensemantic.characteristics.quantitative import (
    Length, LengthUnit, Width, Area, AreaUnit, QuantityValue,
)

# Create typed quantity values
length = Length(value=1.0, unit=LengthUnit.meter)
width = Width(value=200, unit=LengthUnit.milli_meter)

# Arithmetic — units are tracked automatically via pint
area = length * width
print(area.value, area.unit.name)  # 200000.0 milli_meter_squared
assert isinstance(area, Area)

# Unit conversion
area_cm2 = area.to_unit(AreaUnit.centi_meter_squared)
print(area_cm2.value)  # 2000.0
assert area == area_cm2  # physical equality across units

# Addition with automatic unit conversion
l1 = Length(value=1.0, unit=LengthUnit.milli_meter)
l2 = Length(value=1.0, unit=LengthUnit.meter)
print((l1 + l2).value)  # 1.001 (in meters)

# pint interop: round-trip to/from pint.Quantity
q_pint = l1.to_pint()                    # -> 1.0 millimeter
restored = QuantityValue.from_pint(q_pint)  # -> Length(1.0, milli_meter)
assert l1 == restored

# JSON serialization (via oold's unified API)
print(l1.to_json())
# {'type': ['Category:OSWee9c7e5c...'], 'value': 1.0, 'unit': 'Item:OSWf101d25e...'}
```

### Round-tripping derived units

`from_pint` recovers a typed `QuantityValue` even when the exact unit symbol is
not in the registry - e.g. derived units (`watt`, `joule`, `ohm`) or composed
results such as `volt * ampere`. When the symbol is unknown it falls back to the
quantity's **dimensionality**, mapping it to a representative SI-coherent unit via
`DIMENSION_TO_UNIT` (generated into `_dimensions.py` by `scripts/post_process.py`):

```python
from opensemantic.characteristics.quantitative import (
    Voltage, VoltageUnit, ElectricCurrent, ElectricCurrentUnit, Power,
)

power = Voltage(value=3.7, unit=VoltageUnit.volt) * ElectricCurrent(
    value=2.0, unit=ElectricCurrentUnit.ampere
)
assert isinstance(power, Power)  # volt * ampere -> watt
```

### Compact export

`exclude_defaults=True` omits values left at their default (e.g. the default
unit) for a minimal, portable representation:

```python
length = Length(value=1.0, unit=LengthUnit.meter)
print(length.to_json(exclude_defaults=True))  # {'value': 1.0}
```

See [`examples/`](examples/) for more, including tabular data with pandas and a tensile test analysis.

## TODO: Unit Name Conflicts in `_collection.py`

18 unit member names appear in multiple `*Unit` enum classes with different OSW IDs.
The first occurrence goes into `_collection.py`; conflicting entries remain hardcoded in `_model.py`.
These likely stem from upstream QUDT modeling where the same unit name maps to different physical quantities.

| Name | Classes (conflicting OSW IDs) |
|---|---|
| `day` | TimeUnit vs HydraulicPermeabilityUnit |
| `kilo_newton` | ForceUnit vs TorquePerLengthUnit |
| `kilo_newton_per_meter` | EnergyPerAreaUnit vs ForcePerLengthUnit |
| `liter_per_meter_squared_per_second` | VolumetricFluxUnit vs VentilationRatePerFloorAreaUnit |
| `meter` | LengthUnit vs AreaPerLengthUnit vs VolumePerUnitAreaUnit |
| `meter_pascal` | StressIntensityFactorUnit vs UnknownUnit |
| `milli_newton_per_meter` | EnergyPerAreaUnit vs ForcePerLengthUnit |
| `minute` | TimeUnit vs PlaneAngleUnit |
| `newton` | ForceUnit vs TorquePerLengthUnit |
| `newton_per_meter` | EnergyPerAreaUnit vs ForcePerLengthUnit |
| `pH_value` | InductanceUnit vs BasicityUnit |
| `per_centi_meter` | InverseLengthUnit vs UnknownUnit |
| `per_day` | FrequencyUnit vs UnknownUnit vs MassSpecificBiogeochemicalRateUnit |
| `per_hour` | FrequencyUnit vs MassSpecificBiogeochemicalRateUnit |
| `per_meter` | InverseLengthUnit vs UnknownUnit |
| `per_meter_1` | InverseLengthUnit vs UnknownUnit |
| `per_minute` | FrequencyUnit vs RotationalFrequencyUnit |
| `year` | AreaUnit vs TimeUnit |

## Status

<details>
<summary>pint round-trip (full inventory): 0 unit_registry misses</summary>

`tests/conversion_test.py::test_full_inventory_test` round-trips every
`QuantityValue` x unit through `to_pint()` / `from_pint()` and now asserts
**zero `unit_registry` misses** (v2: 2089 ok / 282 errors; v1: 3181 ok / 442
errors). `from_pint` resolves every unit whose symbol pint can parse - derived
units fall back to the dimensionality map in `_dimensions.py`. The remaining
errors are all `UndefinedUnitError` (units pint itself does not define, e.g.
`astronomical_unit`, `electron_volt`, `metric_ton`, sidereal time units); the
critical warnings are units shared by several quantities of the same
dimensionality (value + unit still round-trip, but the class may resolve to a
sibling).

</details>

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
