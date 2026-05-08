import sys

if sys.version_info >= (3, 11):
    # Python 3.11 or higher
    from enum import EnumType
else:
    # Python < 3.11
    from enum import EnumMeta as EnumType

import re
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, overload

import pandas as pd

# pip install pint
import pint
import pint_pandas  # noqa: F401
from oold.model.v1 import LinkedBaseModelMetaClass as ModelMetaclass
from pydantic.v1 import Field, create_model
from pydantic.v1.fields import FieldInfo

from opensemantic.characteristics.quantitative.v1._collection import Unit
from opensemantic.characteristics.quantitative.v1._enum import UnitEnum, unit_registry
from opensemantic.v1 import OswBaseModel

# import pint_pandas

# from osw.model.entity import Characteristic # pip install pint-pandas

QV = TypeVar("QV", bound="QuantityValue")

_SI_PREFIX_FACTORS = {
    "quetta": 1e30,
    "ronna": 1e27,
    "yotta": 1e24,
    "zetta": 1e21,
    "exa": 1e18,
    "peta": 1e15,
    "tera": 1e12,
    "giga": 1e9,
    "mega": 1e6,
    "kilo": 1e3,
    "hecto": 1e2,
    "deca": 1e1,
    "deci": 1e-1,
    "centi": 1e-2,
    "milli": 1e-3,
    "micro": 1e-6,
    "nano": 1e-9,
    "pico": 1e-12,
    "femto": 1e-15,
    "atto": 1e-18,
    "zepto": 1e-21,
    "yocto": 1e-24,
    "ronto": 1e-27,
    "quecto": 1e-30,
}

_EXPONENT_WORDS = {
    "2": "squared",
    "3": "cubed",
    "4": "to_the_fourth",
    "5": "to_the_fifth",
    "6": "to_the_sixth",
    "7": "to_the_seventh",
    "8": "to_the_eighth",
    "9": "to_the_ninth",
}


def _normalize_pint_unit_symbol(raw: str) -> str:
    """Normalize a pint LaTeX-formatted unit symbol to match x-enum-varnames.

    Extracts the unit part from pint's LaTeX output, replaces backslashes with
    underscores, and converts exponent digits to words (e.g. ``2`` -> ``squared``).
    """
    # Handle pint's \tothe{N} pattern before extracting the unit block
    raw = re.sub(
        r"\\tothe\{(\d+)\}",
        lambda m: "\\" + _EXPONENT_WORDS.get(m.group(1), "to_the_" + m.group(1)),
        raw,
    )
    unit_symbol = raw.split("{")[-1].replace("}", "")
    unit_symbol = unit_symbol.replace("\\", "_").strip("_")
    # Pint formats offset/delta units with degree_ and delta_degree_ prefixes
    # (e.g. \degree\Celsius -> degree_Celsius, \delta\degree\Celsius ->
    # delta_degree_Celsius). Strip them to match the registry key
    # (just "Celsius", "Fahrenheit", etc.).
    if unit_symbol.startswith("delta_degree_"):
        unit_symbol = unit_symbol[len("delta_degree_") :]
    elif unit_symbol.startswith("degree_"):
        unit_symbol = unit_symbol[len("degree_") :]
    elif unit_symbol.startswith("delta_"):
        unit_symbol = unit_symbol[len("delta_") :]
    if not unit_symbol:
        return "dimensionless"
    unit_symbol = re.sub(
        r"(\d+)",
        lambda m: _EXPONENT_WORDS.get(m.group(1), "to_the_" + m.group(1)),
        unit_symbol,
    )
    return unit_symbol


class Characteristic(OswBaseModel):
    """
    Elementary building block for object data schemas. Can inherit, reuse and/or define custom properties from other Characteristcs. Properties can have literal values or other complex values (objects) described by other Characteristics.
    """  # noqa: E501

    class Config:
        schema_extra = {
            "@context": [{"type": {"@id": "@type", "@type": "@id"}}],  # noqa: E501
            "uuid": "93ccae36-2435-42ce-ac6c-951450a81d47",  # noqa: E501
            "title": "Characteristic",  # noqa: E501
            "title*": {"en": "Characteristic", "de": "Charakteristik"},  # noqa: E501
            "description": "Elementary building block for object data schemas. Can inherit, reuse and/or define custom properties from other Characteristcs. Properties can have literal values or other complex values (objects) described by other Characteristics. ",  # noqa: E501
            "description*": {
                "en": "Elementary building block for object data schemas. Can inherit, reuse and/or define custom properties from other Characteristcs. Properties can have literal values or other complex values (objects) described by other Characteristics. ",  # noqa: E501
                "de": "Elementarer Baustein für Objekt-Datenschema. Kann Attribute von anderen Charakteristiken erben, übernehmen und/oder eigene definieren. Attribute können als Werte sowohl Literale als auch komplexe Objekte haben die von anderen Charakteristiken beschrieben werden.  ",  # noqa: E501
            },
        }

    type: Optional[List[str]] = Field(
        ["Category:OSW93ccae36243542ceac6c951450a81d47"],
        min_items=1,
        options={"hidden": True},
        propertyOrder=-1010,
        title="Types/Categories",
        title_={"de": "Typen/Kategorien"},
    )
    # @classmethod
    # def get_cls_iri(cls) -> str:
    #    # return default
    # should be optional:
    # uuid: UUID = Field(default_factory=uuid4, options={"hidden": True}, title="UUID")


ureg = pint.get_application_registry()

quantity_registry: Dict[EnumType, ModelMetaclass] = {}


class QuantityValueMetaclass(ModelMetaclass):
    def __new__(cls, clsname, bases, attrs):
        class_instance = super().__new__(cls, clsname, bases, attrs)
        # print(attrs["__qualname__"], attrs)
        if "unit" in attrs and attrs["unit"] is not None:
            # print(attrs["__annotations__"]["unit"].__dict__)#, attrs["unit"].__dict__)
            # print(attrs["unit"].__dict__["__objclass__"])
            # print(attrs["__annotations__"]["unit"].__args__[0])
            # register the mapping between the unit enum and the quantity class

            unit_field_type = None
            # check if FieldInfo was used for annotation
            if type(attrs["unit"]) is FieldInfo:
                # handle type annotation str value "<classname> | None"
                if isinstance(attrs["__annotations__"]["unit"], str):
                    _types = [
                        t.strip() for t in attrs["__annotations__"]["unit"].split("|")
                    ]
                else:
                    _types = attrs["__annotations__"]["unit"].__args__
                # select the first type != None
                for _type in _types:
                    if _type is not None and _type != "None":
                        unit_field_type = _type
                        break
            else:
                unit_field_type = attrs["unit"].__dict__["__objclass__"]
            quantity_registry[unit_field_type] = class_instance
        return class_instance


class QuantityValue(Characteristic, metaclass=QuantityValueMetaclass):
    """
    A Quantity Value expresses the magnitude and kind of a quantity and is given by the product of a numerical value n and a unit of measure u (from qudt).
    """  # noqa: E501

    class Config:
        schema_extra = {
            "$comment": "Autogenerated section - do not edit. Generated from Category:Category Category:OSWffe74f291d354037b318c422591c5023",  # noqa: E501
            "uuid": "40829379-0663-4af9-92cf-9a1b18d772cf",
            "title": "QuantityValue",
            "title*": {"en": "Quantity Value"},
            "description": "A Quantity Value expresses the magnitude and kind of a quantity and is given by the product of a numerical value n and a unit of measure u (from qudt).",  # noqa: E501
            "description*": {
                "en": "A Quantity Value expresses the magnitude and kind of a quantity and is given by the product of a numerical value n and a unit of measure u (from qudt)."  # noqa: E501
            },
            "defaultProperties": ["type", "unit"],
            "@context": [
                "/wiki/Category:OSW93ccae36243542ceac6c951450a81d47?action=raw&slot=jsonschema",  # noqa: E501
                {"unit": "Property:HasUnit", "value": "Property:HasValue"},
            ],
            "$defs": {},
        }

    type: Optional[Any] = ["Category:OSW4082937906634af992cf9a1b18d772cf"]
    value: float = Field(
        ...,
        options={"grid_columns": 4},
        title="value",
        title_={"en": "Value", "de": "Wert"},
    )
    # unit: Optional[UnitEnum] = Field(
    # unit: Optional[Union[UnitEnum, Unit]] = Field(
    unit: Optional[Unit] = Field(
        None,
        options={"grid_columns": 4},
        title="unit",
        title_={"en": "Unit", "de": "Einheit"},
    )

    # @validator("unit", pre=True)
    @classmethod
    def accept_any_unit_enum(cls, v):
        # Get the expected enum class for this QuantityValue
        expected_enum = cls.__fields__["unit"].type_
        # Not required anymore if QuantityValue.unit is typed Unit
        if expected_enum == UnitEnum:
            # If the generic QuantityValue is used, all Unit members are valid
            expected_enum = Unit
        if isinstance(v, expected_enum):
            # Returns the enum as is - causes Error because the validator of unit
            # won't find any Member in UnitEnum --> The unit field type must be changed
            return v
        # Also accept other UnitEnum types, map by name
        if isinstance(v, UnitEnum):
            try:
                return getattr(expected_enum, v.name)
            except KeyError:
                raise ValueError(
                    f"Unit '{v.name}' is not a valid member of {expected_enum}."
                )
        # # Optional: String to Enum
        # if isinstance(v, str):
        #     try:
        #         return expected_enum[v]
        #     except KeyError:
        #         raise ValueError(f"Unit '{v}' ist not valid for {expected_enum}.")
        return v

    # fmt: off
    @overload
    def __init__(self, value: float, unit: Optional[UnitEnum]) -> None:
        ...

    @overload
    def __init__(self, v: float, u: Optional[UnitEnum]) -> None:
        ...

    @overload
    def __init__(self, quantity_value: "QuantityValue") -> None:
        ...

    @overload
    def __init__(
        self, pint_quantity: pint.Quantity, quantity_type: Type["QuantityValue"]
    ) -> None:
        ...

    # @overload
    # def __init__(self, **data: Any) -> None:
    #     ...
    # fmt: on

    def __init__(self, *args, **kwargs) -> None:
        if "v" in kwargs and "u" in kwargs:
            # support for v, u as keyword arguments
            kwargs["value"] = kwargs.pop("v")
            kwargs["unit"] = kwargs.pop("u")
            # will raise error if alias and original names are mixed
        elif "v" in kwargs and "u" not in kwargs and "unit" not in kwargs:
            kwargs["value"] = kwargs.pop("v")
        elif (
            len(args) == 2
            and isinstance(args[0], float)
            and isinstance(args[1], UnitEnum)
        ):
            # support for float, UnitEnum as positional arguments
            raise AttributeError(
                "QuantityValue.__init__() takes either a pint.Quantity and "
                "QuantityValue subclass as positional arguments, or a QuantityValue "
                "as positional arguments, but not a float and UnitEnum. These are "
                "keyword arguments only!"
            )
        elif (
            len(args) == 2
            and isinstance(args[0], pint.Quantity)
            and issubclass(args[1], QuantityValue)
        ):
            # support for pint.Quantity and Type[QuantityValue] as positional arguments
            qv_dict = QuantityValue.from_pint(
                quantity=args[0], simplify=True, quantity_type=args[1], return_dict=True
            )
            kwargs["value"] = qv_dict["value"]
            kwargs["unit"] = qv_dict["unit"]

        elif "pint_quantity" in kwargs and "quantity_type" in kwargs:
            # support for pint.Quantity and Type[QuantityValue] as keyword arguments
            qv_dict = QuantityValue.from_pint(
                quantity=kwargs.pop("pint_quantity"),
                simplify=True,
                quantity_type=kwargs.pop("quantity_type"),
                return_dict=True,
            )
            kwargs["value"] = qv_dict["value"]
            kwargs["unit"] = qv_dict["unit"]
        elif "pint_quantity" in kwargs and "quantity_type" not in kwargs:
            raise ValueError(
                "If 'pint_quantity' is provided, a 'quantity_type' to cast to must "
                "also be provided."
            )
        elif len(args) == 1 and len(kwargs) == 0 and isinstance(args[0], QuantityValue):
            # support for QuantityValue as positional argument
            kwargs = args[0].dict()
        elif "quantity_value" in kwargs:
            # support for QuantityValue as keyword argument
            quantity_value = kwargs.pop("quantity_value")
            kwargs["value"] = quantity_value.value
            kwargs["unit"] = quantity_value.unit

        # Validate unit here manually, since we allow alias "u" for "unit" we cant
        #  use the @validator(unit, pre=True) alone ("v" is not registered as field)
        if "unit" in kwargs.keys():
            kwargs["unit"] = self.accept_any_unit_enum(kwargs["unit"])
        # Finally call the init
        super().__init__(**kwargs)

    @classmethod
    def get_pint_ureg_compatible_str(cls, string: str) -> str:
        pint_unit_name = string.replace("_", " ")
        # SI prefixes, see https://en.wikipedia.org/wiki/Metric_prefix
        prefixes = [
            "quetta",
            "ronna",
            "yotta",
            "zetta",
            "exa",
            "peta",
            "tera",
            "giga",
            "mega",
            "kilo",
            "hecto",
            "deca",
            "deci",
            "centi",
            "milli",
            "micro",
            "nano",
            "pico",
            "femto",
            "atto",
            "zepto",
            "yocto",
            "ronto",
            "quecto",
        ]

        for prefix in prefixes:
            pint_unit_name = pint_unit_name.replace(prefix + " ", prefix)
        pint_unit_name = pint_unit_name.strip(" ")
        if pint_unit_name.split(" ")[0] == "per":
            pint_unit_name = pint_unit_name.replace("per", "1 /")
        # Make sure unit names like Celsius and Ohm don't break the ureg access
        pint_unit_name = pint_unit_name.lower()
        if pint_unit_name == "number":
            pint_unit_name = "dimensionless"
        return pint_unit_name

    def to_pint(self) -> pint.Quantity:
        pint_unit_name = QuantityValue.get_pint_ureg_compatible_str(self.unit.name)

        # Use Quantity() constructor instead of multiplication to support
        # offset units (e.g. degree_Celsius) where value * ureg(unit) fails
        # with OffsetUnitCalculusError.
        try:
            return ureg.Quantity(self.value, ureg(pint_unit_name).units)
        except pint.errors.OffsetUnitCalculusError:
            # Prefixed offset unit (e.g. millicelsius). Pint cannot apply
            # SI prefixes to offset units, so we scale to the base offset
            # unit manually.
            for prefix, factor in _SI_PREFIX_FACTORS.items():
                if pint_unit_name.startswith(prefix):
                    base_unit = pint_unit_name[len(prefix) :]
                    try:
                        return ureg.Quantity(self.value * factor, ureg(base_unit).units)
                    except Exception:
                        continue
            raise

    # fmt: on
    @classmethod
    @overload
    def from_pint(
        cls: Type[QV],
        quantity: pint.Quantity,
        simplify: bool = ...,
        quantity_type: Optional[Type[QV]] = ...,
        strict: bool = ...,
        return_dict: bool = False,
    ) -> QV: ...

    @classmethod
    @overload
    def from_pint(
        cls: Type[QV],
        quantity: pint.Quantity,
        simplify: bool = ...,
        quantity_type: Optional[Type[QV]] = ...,
        strict: bool = ...,
        return_dict: bool = True,
    ) -> Dict[str, Any]: ...

    # fmt: off

    @classmethod
    def from_pint(
        cls: Type[QV],
        quantity: pint.Quantity,
        simplify: bool = True,
        quantity_type: Optional[Type[QV]] = None,
        strict: bool = False,
        return_dict: bool = False,
    ) -> Union[QV, Dict[str, Any]]:
        """Constructs a QuantityValue from a pint.Quantity. If no specific
        QuantityValue child class is provided via quantity_type, the generic type
        'QuantityValue' will be used instead. If strict mode is active, a more specific
        type must be derivable from the unit or must be provided.

        Parameters
        ----------
        quantity
            The pint.Quantity to process
        simplify
            If the units should be simplified before trying to derive the
            QuantityValue type based on the unit
        quantity_type
            QuantityValue type that should be cast to. Provide if you don't want to
            rely on deriving the type based on the unit
        strict
            Whether deriving the QuantityValue type based on the unit may fall back
            to the non-specific type.
        return_dict
            Returns a dictionary instead of an instance of QuantityValue

        Returns
        -------
        result
            Instance of QuantityValue or a corresponding dictionary, containing the
            attributes of the instance as keys.
        """

        # see also
        # https://pint.readthedocs.io/en/stable/getting/tutorial.html#simplifying-units
        # unit_symbol = "{:~P}".format(quantity.units)
        if quantity_type:
            if not issubclass(quantity_type, QuantityValue):
                if any(c.__name__ == "QuantityValue" for c in quantity_type.__mro__):
                    raise TypeError(
                        f"Provided quantity_type '{quantity_type}' from module "
                        f"'{quantity_type.__module__}' is not compatible with "
                        f"QuantityValue from '{QuantityValue.__module__}'. "
                        f"Do not mix v1 and v2 classes."
                    )
                raise ValueError(
                    f"Provided quantity_type '{quantity_type}' is not a "
                    f"subclass of QuantityValue."
                )

        def class_logic(unit_class_):
            if cls != QuantityValue:
                # If the class is not the generic QuantityValue, it must be a subclass
                #  of QuantityValue, so we can use it directly.
                quantity_class_ = cls
            elif unit_class_ == Unit:
                # If the unit_class is the generic Unit, we can use the generic
                #  QuantityValue class directly.
                quantity_class_ = QuantityValue
            else:
                # In any other case, we need to look up the quantity class in the
                #  quantity_registry based on the unit_class.
                quantity_class_ = quantity_registry.get(
                    unit_class_,
                    quantity_registry.get(unit_class_.__qualname__, None),
                )
            if quantity_type is not None:
                # If a specific quantity type is provided, use it instead of the
                #  (derived) default one
                quantity_class_ = quantity_type
            if quantity_class_ is None and strict is False:
                raise ValueError(
                    "quantity_class could not be determined and was not provided via "
                    "quantity_type parameter. With strict mode enabled, no fallback is "
                    "available. Consider to run with strict=False or providing a "
                    "target quantity_type."
                )
            if quantity_class_ is None:
                # Fallback to the generic QuantityValue class if no specific
                # quantity_class could be determined
                quantity_class_ = QuantityValue
            return quantity_class_

        def original(quantity_: pint.Quantity):
            """Derives a LaTeX-formatted string from  a pint.Quantity and returns a
            numeric value along with unit and QuantityValue type."""
            if simplify:
                value = (
                    f"{quantity_:9f#Lx}"  # 9f => round to 8 digits, '#' => simplify
                    # the unit
                )
            else:
                value = f"{quantity_:9fLx}"
            # e.g. \SI[]{1.0}{\kilo\gram\meter\per\ampere\squared\per\second\squared}
            unit_symbol = _normalize_pint_unit_symbol(value)
            # simplifying the unit may change the scale
            numeric_value = float(value.split("{")[1].split("}")[0])
            # Selecting the first entry for the key in the registry:
            unit_class = unit_registry[unit_symbol][0]
            quantity_class = class_logic(unit_class)
            if return_dict:
                return {
                    "value": numeric_value,
                    "unit": unit_class[unit_symbol],
                    "quantity_type": quantity_class,
                    "type": quantity_class.__fields__["type"].default,
                }
            return quantity_class(value=numeric_value, unit=unit_class[unit_symbol])

        def altered(quantity_: pint.Quantity):
            """Converts a pint.Quantity to base units (removing prefixes),
            and derives a LaTeX-formatted string and returns an adjusted numeric
            value along with unit and QuantityValue type."""
            # Convert to base units to remove prefixes
            base_quantity = quantity_.to_base_units()

            # Format the numeric value and unit separately
            numeric_value = base_quantity.magnitude
            unit_latex = f"{base_quantity.units:Lx}"
            if simplify:
                unit_latex = f"{base_quantity.units:#Lx}"

            unit_symbol = _normalize_pint_unit_symbol(unit_latex)
            # Selecting the first entry for the key in the registry:
            unit_class = unit_registry[unit_symbol][0]
            quantity_class = class_logic(unit_class)
            if return_dict:
                return {
                    "value": numeric_value,
                    "unit": unit_class[unit_symbol],
                    "quantity_type": quantity_class,
                    "type": quantity_class.__fields__["type"].default,
                }
            return quantity_class(value=numeric_value, unit=unit_class[unit_symbol])

        try:
            return original(quantity)
        except KeyError:
            return altered(quantity)

    def to_base(self) -> "QuantityValue":
        """Converts the QuantityValue to its base unit."""
        pint_quantity = self.to_pint().to_base_units()
        return QuantityValue.from_pint(
            pint_quantity, simplify=False, quantity_type=self.__class__)

    def to_unit(self, unit: Union[UnitEnum, str]) -> "QuantityValue":
        """Converts the QuantityValue to the specified unit."""

        if isinstance(unit, UnitEnum):
            unit_str = QuantityValue.get_pint_ureg_compatible_str(unit.name)
        elif isinstance(unit, str):
            # Assuming the string is a valid unit from the pint unit registry
            unit_str = QuantityValue.get_pint_ureg_compatible_str(unit)
        else:
            raise ValueError(
                f"Invalid unit type: {type(unit)}. Must be UnitEnum or str.")

        pint_quantity = self.to_pint()
        try:
            pint_quantity = pint_quantity.to(unit_str)
        except pint.errors.OffsetUnitCalculusError:
            # Target is a prefixed offset unit (e.g. millicelsius). Pint
            # cannot convert to prefixed offset units, so we convert to the
            # base offset unit and scale manually.
            for prefix, factor in _SI_PREFIX_FACTORS.items():
                if unit_str.startswith(prefix):
                    base_unit = unit_str[len(prefix):]
                    try:
                        base_result = pint_quantity.to(base_unit)
                        return self.__class__(
                            value=base_result.magnitude / factor, unit=unit
                        )
                    except Exception:
                        continue
            raise
        return QuantityValue.from_pint(
            quantity=pint_quantity, simplify=False, quantity_type=self.__class__)

    def __neg__(self) -> "QuantityValue":
        return QuantityValue.from_pint(-self.to_pint(), quantity_type=self.__class__)

    def __pos__(self) -> "QuantityValue":
        return QuantityValue.from_pint(
            +self.to_pint(), quantity_type=self.__class__)

    def __abs__(self) -> "QuantityValue":
        return QuantityValue.from_pint(
            abs(self.to_pint()), quantity_type=self.__class__)

    def __add__(self, other: "QuantityValue") -> "QuantityValue":
        res_pint = self.to_pint() + other.to_pint()
        return QuantityValue.from_pint(res_pint, quantity_type=self.__class__)

    def __sub__(self, other: "QuantityValue") -> "QuantityValue":
        res_pint = self.to_pint() - other.to_pint()
        return QuantityValue.from_pint(res_pint, quantity_type=self.__class__)

    # * operator
    def __mul__(self, other: Union["QuantityValue", float, int]) -> "QuantityValue":
        if not isinstance(other, (float, int)):
            other = other.to_pint()
        res_pint = self.to_pint() * other
        return QuantityValue.from_pint(res_pint)

    # / operator
    def __truediv__(self, other: Union["QuantityValue", float, int]) -> "QuantityValue":
        if not isinstance(other, (float, int)):
            other = other.to_pint()
        res_pint = self.to_pint() / other
        return QuantityValue.from_pint(res_pint)

    def __floordiv__(self, other: "QuantityValue") -> "QuantityValue":
        """Floor division is supported by pint only for dimensionless quantities and
        quantities with the same dimension"""
        if isinstance(other, QuantityValue):
            other = other.to_pint()
        return QuantityValue.from_pint(self.to_pint() // other)

    def __mod__(self, other: "QuantityValue") -> "QuantityValue":
        """Modulo is supported by pint only for dimensionless quantities and
        quantities with the same dimension"""
        if isinstance(other, QuantityValue):
            other = other.to_pint()
        return QuantityValue.from_pint(self.to_pint() % other)

    def __pow__(self, other: Union[int, float, "QuantityValue"]) -> "QuantityValue":
        # todo: test if supported with dimensionless unit / quantity as exponent
        if isinstance(other, QuantityValue):
            other = other.to_pint()
        return QuantityValue.from_pint(self.to_pint() ** other)

    def __eq__(self, other: "QuantityValue") -> bool:
        return self.to_pint() == other.to_pint()

    def __ne__(self, other: "QuantityValue") -> bool:
        return self.to_pint() != other.to_pint()

    def __ge__(self, other: "QuantityValue") -> bool:
        return self.to_pint() >= other.to_pint()

    def __gt__(self, other: "QuantityValue") -> bool:
        return self.to_pint() > other.to_pint()

    def __le__(self, other: "QuantityValue") -> bool:
        return self.to_pint() <= other.to_pint()

    def __lt__(self, other: "QuantityValue") -> bool:
        return self.to_pint() < other.to_pint()


QuantityValue.update_forward_refs()


class TabularData(OswBaseModel):
    rows: List[Characteristic]  # convention for tabular data is a list of rows

    # consider https://stackoverflow.com/questions/51505504/pandas-nesting-dataframes # noqa: E501
    # consider https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.attrs.html # noqa: E501

    def to_df(self) -> pd.DataFrame:
        series = []
        row_class = self.__class__.__fields__["rows"].type_
        for attr in row_class.__fields__.keys():
            if attr == "type":
                continue
            q_name = QuantityValue.get_pint_ureg_compatible_str(
                row_class.__fields__[attr].type_.__fields__["unit"].default.name
            )
            # q_pint = ureg[q_name]
            s = pd.Series(
                [
                    (
                        getattr(m, attr).to_pint().to(q_name).magnitude
                        if getattr(m, attr, None) is not None
                        else None
                    )
                    for m in self.rows
                ],
                dtype="pint[" + q_name + "]",
                name=attr,
            )
            series.append(s)
        rows = {s.name: s for s in series}
        return pd.DataFrame(rows)

    @classmethod
    def from_df(cls, df: pd.DataFrame):
        rows = []
        row_class = OswBaseModel
        if "rows" in cls.__fields__:
            row_class = cls.__fields__["rows"].type_

        additional_fields = {}
        for key in df.columns:
            # print(df[key].pint.__dict__)
            if key not in row_class.__fields__.keys():
                # raise ValueError(f"Column '{key}' not found in '{row_class.__name__}'") # noqa: E501
                quantity = QuantityValue.from_pint(
                    1 * getattr(df.dtypes, key).units
                ).__class__
                # todo: preserve quantity_type
                additional_fields[key] = (quantity, ...)

        if len(additional_fields) > 0:
            row_class = create_model(
                row_class.__name__ + "Extended", **additional_fields, __base__=row_class
            )
            cls = create_model(
                cls.__name__ + "Extended",
                **{"rows": (List[row_class], ...)},
                __base__=cls,
            )

        # convert all columns to the default unit
        for attr in row_class.__fields__.keys():
            if attr == "type":
                continue
            q_name = QuantityValue.get_pint_ureg_compatible_str(
                row_class.__fields__[attr].type_.__fields__["unit"].default.name
            )
            q_pint = ureg(q_name)
            df[attr] = df[attr].pint.to(q_pint)

        for i, row in df.iterrows():
            # create a dictionary with the values of the row
            # using the column names as keys
            d = {key: {"value": row[key].magnitude} for key in df.columns}
            m = row_class(**d)
            rows.append(m)
        return cls(rows=rows)
