"""Basic usage: creating quantities, arithmetic, unit conversion, and JSON export."""

import json

from opensemantic.characteristics.quantitative import (
    Area,
    AreaUnit,
    Length,
    LengthUnit,
    Width,
)

# Create typed quantity values
length = Length(value=1.0, unit=LengthUnit.meter)
width = Width(value=200, unit=LengthUnit.milli_meter)

print(f"Length: {length.value} {length.unit.name}")
print(f"Width:  {width.value} {width.unit.name}")

# Arithmetic — units are tracked automatically via pint
area = length * width
print(f"\nArea = length * width: {area.value} {area.unit.name}")
assert isinstance(area, Area)

# Unit conversion
area_cm2 = area.to_unit(AreaUnit.centi_meter_squared)
print(f"Area in cm²: {area_cm2.value} {area_cm2.unit.name}")
assert area == area_cm2  # physical equality

# Convert to SI base units
area_base = area.to_base()
print(f"Area in base units: {area_base.value} m²")

# Addition with automatic unit conversion
l1 = Length(value=1.0, unit=LengthUnit.milli_meter)
l2 = Length(value=1.0, unit=LengthUnit.meter)
l3 = l1 + l2
print(f"\n1 mm + 1 m = {l3.value} {l3.unit.name}")

# Comparison operators
print(f"1 mm < 1 m: {l1 < l2}")
print(f"1 mm == 1 m: {l1 == l2}")

# JSON serialization via oold's unified to_json() API
print("\nJSON (via to_json):")
print(json.dumps(l1.to_json(), indent=2))
