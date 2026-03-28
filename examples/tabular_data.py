"""Tabular data: using TabularData with pandas DataFrames."""

from typing import List, Optional

from opensemantic import OswBaseModel
from opensemantic.characteristics.quantitative import (
    Area,
    Length,
    TabularData,
    Width,
)


# Define a row schema using typed quantity fields
class Measurement(OswBaseModel):
    length: Length
    width: Width
    area: Optional[Area] = None


# Define a tabular dataset
class MeasurementData(TabularData):
    rows: List[Measurement]


# Create some measurements
data = MeasurementData(
    rows=[
        Measurement(length=Length(value=1.0), width=Width(value=2.0)),
        Measurement(length=Length(value=3.0), width=Width(value=4.0)),
        Measurement(length=Length(value=5.0), width=Width(value=6.0)),
    ]
)

# Convert to a pint-enabled pandas DataFrame
df = data.to_df()
print("DataFrame with pint units:")
print(df)
print()

# Compute area as a vectorized operation (unit-aware)
df["area"] = df["length"] * df["width"]
print("After computing area:")
print(df)
print()

# Convert back to a typed data model
result = MeasurementData.from_df(df)
print(f"Rows: {len(result.rows)}")
for row in result.rows:
    print(
        f"  length={row.length.value}, width={row.width.value}, area={row.area.value}"
    )
