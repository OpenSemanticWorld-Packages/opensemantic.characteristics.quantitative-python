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
<summary>pint roundtrip test (v2): 1831 successful, 299 errors and 54 warnings (33 critical)</summary>

```
Error: Missing unit LengthUnit.astronomical_unit in pint
Error: Missing unit DimensionlessUnit.dec in pint
Error: Missing unit DimensionlessUnit.COUNT in unit_registry
Error: Missing unit DimensionlessUnit.flight in pint
Error: Missing unit DimensionlessUnit.heartbeat in pint
Error: Missing unit DimensionlessUnit.unknown in pint
Error: Missing unit DimensionlessUnit.unitless in pint
Error: Missing unit EnergyUnit.electron_volt in pint
Error: Missing unit EnergyUnit.kilo_electron_volt in pint
Error: Missing unit EnergyUnit.mega_electron_volt in pint
Error: Missing unit EnergyUnit.giga_electron_volt in pint
Error: Missing unit EnergyUnit.hour_volt_ampere in unit_registry
Error: Missing unit EnergyUnit.hour_kilo_volt_ampere in unit_registry
Error: Missing unit EnergyUnit.hour_kilo_watt in unit_registry
Error: Missing unit EnergyUnit.hour_mega_volt_ampere in unit_registry
Error: Missing unit EnergyUnit.hour_mega_watt in unit_registry
Error: Missing unit EnergyUnit.hour_tera_watt in unit_registry
Error: Missing unit GeneralizedCoordinateUnit.unitless in pint
Error: Missing unit TimeUnit.min_sidereal in pint
Error: Missing unit TimeUnit.h_sidereal in pint
Error: Missing unit TimeUnit.day_sidereal in pint
Error: Missing unit TimeUnit.tropical_year in pint
Error: Missing unit TimeUnit.a_sidereal in pint
Error: Missing unit AbsorptanceUnit.unitless in pint
Error: Missing unit PowerUnit.liter_mega_pascal_per_second in unit_registry
Error: Missing unit PowerUnit.hour_tera_watt_per_year in unit_registry
Error: Missing unit ReactivityUnit.unitless in pint
Error: Missing unit IsentropicExponentUnit.unitless in pint
Error: Missing unit DensityUnit.metric_ton_per_meter_cubed in pint
Error: Missing unit LeakageFactorUnit.unitless in pint
Error: Missing unit ChromaticityUnit.unitless in pint
Error: Missing unit InverseEnergyUnit.per_hour_per_volt_ampere in pint
Error: Missing unit InverseEnergyUnit.per_hour_per_kilo_volt_ampere in pint
Error: Missing unit MassPerAreaTimeUnit.micro_g_per_cm_squared_wk in pint
Error: Missing unit MassPerAreaTimeUnit.metric_ton_per_hectare_per_year in pint
Error: Missing unit PlaneAngleUnit.mil_NATO in pint
Error: Missing unit PlaneAngleUnit.rev in pint
Error: Missing unit AngularMomentumUnit.electron_volt_second in pint
Error: Missing unit ConductivityVarianceUnit.micro_siemens_squared_per_centi_meter_squared in unit_registry
Error: Missing unit NeutronYieldPerFissionUnit.unitless in pint
Error: Missing unit AngularImpulseUnit.electron_volt_second in pint
Error: Missing unit MassUnit.deci_metric_ton in pint
Error: Missing unit MassUnit.metric_ton in pint
Error: Missing unit MassUnit.mega_metric_ton in pint
Error: Missing unit StatisticalWeightUnit.unitless in pint
Error: Missing unit ShortRangeOrderParameterUnit.unitless in pint
Error: Missing unit ThermalUtilizationFactorUnit.unitless in pint
Error: Missing unit PowerFactorUnit.unitless in pint
Error: Missing unit PowerPerElectricChargeUnit.volt_per_micro_second in unit_registry
Error: Missing unit PowerPerAreaQuarticTemperatureUnit.watt_per_kelvin_to_the_fourth_per_meter_squared in pint
Error: Missing unit StandardAbsoluteActivityUnit.unitless in pint
Error: Missing unit MagneticAreaMomentUnit.electron_volt_per_tesla in pint
Error: Missing unit ResistivityUnit.meter_nano_ohm in unit_registry
Error: Missing unit ResistivityUnit.meter_micro_ohm in unit_registry
Error: Missing unit ResistivityUnit.meter_milli_ohm in unit_registry
Error: Missing unit ResistivityUnit.centi_meter_ohm in unit_registry
Error: Missing unit ResistivityUnit.kilo_meter_mega_ohm in unit_registry
Error: Missing unit DatasetOfBitsUnit.kibi_barn in pint
Error: Missing unit DatasetOfBitsUnit.mebi_barn in pint
Error: Missing unit DatasetOfBitsUnit.gigabit in unit_registry
Error: Missing unit DatasetOfBitsUnit.gibi_barn in pint
Error: Missing unit DatasetOfBitsUnit.tebi_barn in pint
Error: Missing unit DatasetOfBitsUnit.pebi_barn in pint
Error: Missing unit DatasetOfBitsUnit.exbi_barn in pint
Error: Missing unit ElectricChargePerMassUnit.milli_coulomb_per_kilo_gram in unit_registry
Error: Missing unit ElectricChargePerMassUnit.coulomb_per_kilo_gram in unit_registry
Error: Missing unit WarpingConstantUnit.meter_to_the_sixth in pint
Error: Missing unit WarpingConstantUnit.centi_meter_to_the_sixth in pint
Error: Missing unit AbsorbedDoseRateUnit.watt_per_kilo_gram in unit_registry
Error: Missing unit PowerPerAreaUnit.joule_per_centi_meter_squared_per_day in unit_registry
Critical Warning: HydraulicPermeability and Area have the same unit HydraulicPermeabilityUnit.deci_meter_squared
Critical Warning: SectionModulus and Volume1 have the same unit SectionModulusUnit.deci_meter_cubed
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.pico_gram_per_milli_liter
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.nano_gram_per_milli_liter
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.gram_per_deci_meter_cubed
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.milli_gram_per_milli_liter
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.gram_per_centi_meter_cubed
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.gram_per_milli_liter
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.kilo_gram_per_deci_meter_cubed
Critical Warning: NuclearQuadrupoleMoment and Area have the same unit NuclearQuadrupoleMomentUnit.deci_meter_squared
Critical Warning: BloodGlucoseLevelByMass and Density have the same unit BloodGlucoseLevelByMassUnit.pico_gram_per_milli_liter
Critical Warning: BloodGlucoseLevelByMass and Density have the same unit BloodGlucoseLevelByMassUnit.nano_gram_per_milli_liter
Critical Warning: BloodGlucoseLevelByMass and Density have the same unit BloodGlucoseLevelByMassUnit.milli_gram_per_milli_liter
Critical Warning: BloodGlucoseLevelByMass and Density have the same unit BloodGlucoseLevelByMassUnit.gram_per_milli_liter
Critical Warning: MassDensity and Density have the same unit MassDensityUnit.metric_ton_per_meter_cubed
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.pico_gram_per_milli_liter
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.nano_gram_per_milli_liter
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.gram_per_deci_meter_cubed
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.milli_gram_per_milli_liter
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.gram_per_centi_meter_cubed
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.gram_per_milli_liter
Critical Warning: MassConcentration and Density have the same unit MassConcentrationUnit.kilo_gram_per_deci_meter_cubed
Critical Warning: MassConcentrationOfWater and Density have the same unit MassConcentrationOfWaterUnit.gram_per_deci_meter_cubed
Critical Warning: MassConcentrationOfWater and Density have the same unit MassConcentrationOfWaterUnit.gram_per_centi_meter_cubed
Critical Warning: MassConcentrationOfWater and Density have the same unit MassConcentrationOfWaterUnit.kilo_gram_per_deci_meter_cubed
Critical Warning: MassConcentrationOfWaterVapour and Density have the same unit MassConcentrationOfWaterVapourUnit.gram_per_deci_meter_cubed
Critical Warning: MassConcentrationOfWaterVapour and Density have the same unit MassConcentrationOfWaterVapourUnit.gram_per_centi_meter_cubed
Critical Warning: MassConcentrationOfWaterVapour and Density have the same unit MassConcentrationOfWaterVapourUnit.kilo_gram_per_deci_meter_cubed
Critical Warning: MeanMassRange and BodyMassIndex have the same unit MeanMassRangeUnit.milli_gram_per_deci_meter_squared
Critical Warning: SurfaceDensity and BodyMassIndex have the same unit SurfaceDensityUnit.milli_gram_per_deci_meter_squared
Critical Warning: MassPerArea and BodyMassIndex have the same unit MassPerAreaUnit.milli_gram_per_deci_meter_squared
Critical Warning: IonicStrength and AmountOfSubstancePerMass have the same unit IonicStrengthUnit.micro_mole_per_kilo_gram
Critical Warning: ElectricChargeVolumeDensity and ElectricChargeDensity have the same unit ElectricChargeVolumeDensityUnit.coulomb_per_centi_meter_cubed
Critical Warning: ElectricChargeVolumeDensity and ElectricChargeDensity have the same unit ElectricChargeVolumeDensityUnit.coulomb_per_milli_meter_cubed
```

</details>

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
