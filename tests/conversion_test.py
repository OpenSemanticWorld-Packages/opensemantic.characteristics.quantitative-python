import json

import pint


def test_addition(q_module):
    q = q_module
    q1 = q.Mobility(
        value=1.0,
        unit=q.MobilityUnit.meter_squared_per_second_per_volt,
    )

    q2 = q.Mobility(
        value=1.0,
        unit=q.MobilityUnit.centi_meter_squared_per_second_per_volt,
    )

    q3 = q1 + q2
    assert (
        q3.value == 1.0001
        and q3.unit == q.MobilityUnit.meter_squared_per_second_per_volt
    )


def test_quantity_value(q_module):
    q = q_module
    q1 = q.Length(value=1.0, unit=q.LengthUnit.milli_meter)

    q_json = json.loads(q1.json(exclude_none=True))
    assert q_json == {
        "type": ["Category:OSWee9c7e5c343e542cb5a8b4648315902f"],
        "value": 1.0,
        "unit": (
            "Item:OSWf101d25e944856e3bd4b4c9863db7de2"
            "#OSW322dec469be75aedb008b3ebff29db86"
        ),
    }

    q1 = q.Length(value=1.0, unit=q.LengthUnit.meter)

    q_json = json.loads(q1.json(exclude_none=True))
    assert q_json == {
        "type": ["Category:OSWee9c7e5c343e542cb5a8b4648315902f"],
        "value": 1.0,
        "unit": "Item:OSWf101d25e944856e3bd4b4c9863db7de2",
    }

    q_json = json.loads(q1.json(exclude_none=True, exclude_defaults=True))
    assert q_json == {"value": 1.0}


def test_pint(q_module):
    q = q_module
    q1 = q.Length(value=1.0, unit=q.LengthUnit.milli_meter)
    # transform to pint
    q_pint = q1.to_pint()
    # transform back to QuantityValue
    q_ = q.QuantityValue.from_pint(q_pint)
    assert q1 == q_

    q2 = q.Length(value=1.0, unit=q.LengthUnit.meter)
    q3 = q1 + q2
    assert q3 == q.Length(value=1.001, unit=q.LengthUnit.meter)

    q31 = q1 * q2
    assert q31 == q.Area(value=1000.0, unit=q.AreaUnit.milli_meter_squared)

    q41 = q.Area(value=1.0, unit=q.AreaUnit.meter_squared)
    q42 = q.Area(value=1.0, unit=q.AreaUnit.milli_meter_squared)
    # 'square_meter' is not a valid unit for pint, but 'square_meter' is
    q43 = q41 + q42
    assert q43 == q.Area(value=1.000001, unit=q.AreaUnit.meter_squared)

    q5 = q.Length(value=2.0, unit=q.LengthUnit.meter)
    q25 = q2 / q5  # Dimensionless(value=0.5, unit=DimensionLessUnit.dimensionless)
    # will envoke QuantityValue.from_pint(), which will call unit_registry[unit_symbol]
    _ = q.VoltageRatio(value=q25.value)


def test_full_inventory_test(q_module, static_module):
    q = q_module
    quantity_registry = static_module.quantity_registry
    # test all QuantityValue classes
    warning_count = 0
    critical_warning_count = 0
    error_count = 0
    success_count = 0
    qu_reg = {}
    # build a list of all UnitEnums per QuantityValue class
    for ue, qv in quantity_registry.items():
        if qv not in qu_reg:
            qu_reg[qv] = []
        qu_reg[qv].append(ue)

    for qv in qu_reg.keys():
        for ue in qu_reg[qv]:
            if isinstance(ue, str):
                try:
                    ue = getattr(q, ue)
                except AttributeError:
                    continue
            for u in ue:
                q1 = qv(value=1.0, unit=u)

                try:
                    q_pint = q1.to_pint()
                    q_ = q.QuantityValue.from_pint(q_pint)
                    if q1 != q_:
                        warning_count += 1
                        if type(q1) is not type(q_):
                            print(
                                (
                                    f"Critical Warning: {q1.__class__.__name__} "
                                    f"and {q_.__class__.__name__} "
                                    f"have the same unit {u}"
                                )
                            )
                            critical_warning_count += 1
                        elif q1.unit != q_.unit:
                            print(f"Warning: {q1.unit} was normalized to {q_.unit}")
                        elif q1.value != q_.value:
                            print(f"Warning: Rounding error: {q1.value} vs {q_.value}")
                        else:
                            print(f"Warning: Unknown error: {q1} vs {q_}")
                    else:
                        success_count += 1
                except Exception as e:
                    if isinstance(e, pint.errors.UndefinedUnitError):
                        print(f"Error: Missing unit {u} in pint")
                    elif isinstance(e, KeyError):
                        print(f"Error: Missing unit {u} in unit_registry")
                    else:
                        print(f"Error {e.__class__}: {q1}")
                    error_count += 1
    print(
        (
            f"{success_count} successful, "
            f"{error_count} errors and {warning_count} warnings "
            f"({critical_warning_count} critical)"
        )
    )


if __name__ == "__main__":
    import opensemantic.characteristics.quantitative.v1._model as q
    from opensemantic.characteristics.quantitative.v1._static import quantity_registry

    class _FakeModule:
        pass

    _q = _FakeModule()
    _q.__dict__.update(vars(q))
    _q.QuantityValue = q.QuantityValue

    class _FakeStatic:
        pass

    _s = _FakeStatic()
    _s.quantity_registry = quantity_registry

    test_addition(_q)
    test_pint(_q)
    test_full_inventory_test(_q, _s)
    test_quantity_value(_q)
