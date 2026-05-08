"""Tests for offset/delta unit handling in from_pint and _normalize_pint_unit_symbol.

Covers:
- Bug fix: _normalize_pint_unit_symbol stripping degree_/delta_degree_/delta_ prefixes
- Bug fix: from_pint with offset units (Celsius, Fahrenheit) via to_unit round-trip
- Bug fix: to_pint/to_unit support for offset and prefixed offset units
- Bug fix: cross-version from_pint raises helpful TypeError
"""

import importlib

import pint
import pytest

# -- Unit tests for _normalize_pint_unit_symbol --


@pytest.fixture(params=["v1", "v2"], ids=["pydantic-v1", "pydantic-v2"])
def static_module(request):
    if request.param == "v1":
        return importlib.import_module(
            "opensemantic.characteristics.quantitative.v1._static"
        )
    return importlib.import_module("opensemantic.characteristics.quantitative._static")


class TestNormalizePintUnitSymbol:
    """Unit tests for _normalize_pint_unit_symbol prefix stripping."""

    def test_delta_degree_celsius(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{26.85}{\delta\degree\Celsius}")
        assert result == "Celsius"

    def test_delta_degree_fahrenheit(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{80.33}{\delta\degree\Fahrenheit}")
        assert result == "Fahrenheit"

    def test_delta_degree_reaumur(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{21.48}{\delta\degree\Reaumur}")
        assert result == "Reaumur"

    def test_degree_celsius(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{26.85}{\degree\Celsius}")
        assert result == "Celsius"

    def test_degree_fahrenheit(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{80.33}{\degree\Fahrenheit}")
        assert result == "Fahrenheit"

    def test_degree_rankine(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{539.67}{\degree\Rankine}")
        assert result == "Rankine"

    def test_non_offset_unit_unchanged(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{1.0}{\meter}")
        assert result == "meter"

    def test_kilo_gram_unchanged(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{1.0}{\kilo\gram}")
        assert result == "kilo_gram"

    def test_dimensionless(self, static_module):
        norm = static_module._normalize_pint_unit_symbol
        result = norm(r"\SI[]{1.0}{}")
        assert result == "dimensionless"


# -- Integration tests for offset unit conversion --


@pytest.fixture(params=["v1", "v2"], ids=["pydantic-v1", "pydantic-v2"])
def package_module(request):
    if request.param == "v1":
        return importlib.import_module("opensemantic.characteristics.quantitative.v1")
    return importlib.import_module("opensemantic.characteristics.quantitative")


class TestOffsetUnitConversion:
    """Integration tests for to_unit/from_pint with offset temperature units."""

    def test_kelvin_to_celsius(self, package_module):
        pkg = package_module
        t = pkg.Temperature(value=300.0, unit=pkg.TemperatureUnit.kelvin)
        t2 = t.to_unit(pkg.TemperatureUnit.Celsius)
        assert isinstance(t2, pkg.Temperature)
        assert t2.unit == pkg.TemperatureUnit.Celsius
        assert abs(t2.value - 26.85) < 0.01

    def test_celsius_to_kelvin(self, package_module):
        pkg = package_module
        t = pkg.Temperature(value=100.0, unit=pkg.TemperatureUnit.Celsius)
        t2 = t.to_unit(pkg.TemperatureUnit.kelvin)
        assert isinstance(t2, pkg.Temperature)
        assert t2.unit == pkg.TemperatureUnit.kelvin
        assert abs(t2.value - 373.15) < 0.01

    def test_kelvin_to_milli_celsius(self, package_module):
        pkg = package_module
        t = pkg.Temperature(value=300.0, unit=pkg.TemperatureUnit.kelvin)
        t2 = t.to_unit(pkg.TemperatureUnit.milli_Celsius)
        assert isinstance(t2, pkg.Temperature)
        assert t2.unit == pkg.TemperatureUnit.milli_Celsius
        assert abs(t2.value - 26850.0) < 10.0

    def test_celsius_round_trip(self, package_module):
        pkg = package_module
        t1 = pkg.Temperature(value=25.0, unit=pkg.TemperatureUnit.Celsius)
        t_k = t1.to_unit(pkg.TemperatureUnit.kelvin)
        t2 = t_k.to_unit(pkg.TemperatureUnit.Celsius)
        assert abs(t2.value - 25.0) < 0.01
        assert t2.unit == pkg.TemperatureUnit.Celsius

    def test_from_pint_celsius_quantity(self, package_module):
        pkg = package_module
        ureg = pint.get_application_registry()
        # Create a pint quantity in degree_Celsius
        q = (300.0 * ureg.kelvin).to("degC")
        result = pkg.QuantityValue.from_pint(q, quantity_type=pkg.Temperature)
        assert isinstance(result, pkg.Temperature)
        assert result.unit == pkg.TemperatureUnit.Celsius
        assert abs(result.value - 26.85) < 0.01

    def test_from_pint_celsius_return_dict(self, package_module):
        pkg = package_module
        ureg = pint.get_application_registry()
        q = (300.0 * ureg.kelvin).to("degC")
        result = pkg.QuantityValue.from_pint(
            q, quantity_type=pkg.Temperature, return_dict=True
        )
        assert isinstance(result, dict)
        assert result["unit"] == pkg.TemperatureUnit.Celsius
        assert abs(result["value"] - 26.85) < 0.01
        assert "type" in result


# -- Cross-version compatibility tests --


class TestCrossVersionCompatibility:
    """Tests for v1/v2 interop: cross-version from_pint raises helpful errors."""

    @pytest.fixture
    def v1_pkg(self):
        return importlib.import_module("opensemantic.characteristics.quantitative.v1")

    @pytest.fixture
    def v2_pkg(self):
        return importlib.import_module("opensemantic.characteristics.quantitative")

    def test_v2_from_pint_rejects_v1_quantity_type(self, v1_pkg, v2_pkg):
        """v2 from_pint should reject a v1 class with a helpful TypeError."""
        ureg = pint.get_application_registry()
        q = 1.0 * ureg.meter
        with pytest.raises(TypeError, match="Do not mix v1 and v2"):
            v2_pkg.QuantityValue.from_pint(q, quantity_type=v1_pkg.Length)

    def test_v1_from_pint_rejects_v2_quantity_type(self, v1_pkg, v2_pkg):
        """v1 from_pint should reject a v2 class with a helpful TypeError."""
        ureg = pint.get_application_registry()
        q = 1.0 * ureg.meter
        with pytest.raises(TypeError, match="Do not mix v1 and v2"):
            v1_pkg.QuantityValue.from_pint(q, quantity_type=v2_pkg.Length)

    def test_issubclass_rejects_non_quantity_value(self, v2_pkg):
        """from_pint should still reject types that are not QuantityValue."""
        ureg = pint.get_application_registry()
        q = 1.0 * ureg.meter
        with pytest.raises(ValueError, match="not a subclass"):
            v2_pkg.QuantityValue.from_pint(q, quantity_type=str)
