"""Interoperability with pint: converting to/from pint.Quantity objects."""

import pint

from opensemantic.characteristics.quantitative import (
    Area,
    Diameter,
    Length,
    LengthUnit,
    QuantityValue,
)

# QuantityValue -> pint
length = Length(value=1.0, unit=LengthUnit.milli_meter)
q_pint = length.to_pint()
print(f"As pint: {q_pint}")
print(f"  magnitude: {q_pint.magnitude}, units: {q_pint.units}")

# pint -> QuantityValue (auto-detects the quantity type from the unit)
restored = QuantityValue.from_pint(q_pint)
name = type(restored).__name__
print(f"\nRestored: {name}(value={restored.value}, unit={restored.unit.name})")
assert length == restored

# Cast to a specific quantity type
diameter = QuantityValue.from_pint(q_pint, quantity_type=Diameter)
print(f"Cast to Diameter: {type(diameter).__name__}")

# Or use from_pint on the target class directly
diameter2 = Diameter.from_pint(q_pint)
print(f"Diameter.from_pint: {type(diameter2).__name__}")

# Arithmetic via pint — result type is inferred from the resulting unit
l1 = Length(value=2.0, unit=LengthUnit.meter)
l2 = Length(value=3.0, unit=LengthUnit.meter)
product = l1 * l2
print(f"\n2m * 3m = {product.value} {product.unit.name} ({type(product).__name__})")
assert isinstance(product, Area)

# Use return_dict=True to inspect the mapping without constructing an object
info = QuantityValue.from_pint(q_pint, return_dict=True)
print(
    f"\nfrom_pint dict: value={info['value']}, unit={info['unit'].name}, "
    f"type={info['quantity_type'].__name__}"
)

# Constructor shorthand: pass a pint.Quantity directly
ureg = pint.get_application_registry()
pq = 2.5 * ureg.meter
l3 = Length(pint_quantity=pq, quantity_type=Length)
print(f"\nFrom pint constructor: {l3.value} {l3.unit.name}")
