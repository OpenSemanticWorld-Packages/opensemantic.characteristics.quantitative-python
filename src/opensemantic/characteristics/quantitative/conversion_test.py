import opensemantic.characteristics.quantitative._model as q

q1 = q.Mobility(
    value=1.0,
    unit=q.MobilityUnit.meter_squared_per_second_per_volt,
)

q2 = q.Mobility(
    value=1.0,
    unit=q.MobilityUnit.centi_meter_squared_per_second_per_volt,
)

q3 = q1 + q2
assert q3.value == 1.0001 and q3.unit == q.MobilityUnit.meter_squared_per_second_per_volt

