from typing import Any, List, Optional
from uuid import UUID

from osw.model.static import OswBaseModel
from pydantic.v1 import Field


from uuid import uuid4
from typing import Type, TypeVar
from osw.model.static import OswBaseModel, Ontology

from datetime import datetime
from enum import Enum, EnumType
import json
from os import times
from pprint import pprint
from re import A
from typing import Any, Dict, Optional, List, Union
from uuid import UUID, uuid4
from annotated_types import Le
from inflect import unit
from numpy import test
from pydantic import Field
from pydantic.v1 import BaseModel, create_model
from pydantic.v1.main import ModelMetaclass
from pydantic.v1.fields import FieldInfo

# pip install pint
import pint
from pint import UnitRegistry
import pandas as pd
#import pint_pandas

from osw.model.entity import Characteristic # pip install pint-pandas

unit_registry: Dict[str, EnumType] = {}

class UnitEnumMetaclass(EnumType):
    def __new__(cls, clsname, bases, attrs):
        #print(attrs["__qualname__"], attrs)
        class_instance = EnumType.__new__(cls, clsname, bases, attrs)
        for key, value in attrs.items():
            if key not in ["__module__", "__qualname__", "_generate_next_value_"]:
                # register all enum values in the unit_registry
                unit_registry[key] = class_instance
        return class_instance

class UnitEnum(str, Enum, metaclass=UnitEnumMetaclass):
    pass

class Characteristic(OswBaseModel):
    """
    Elementary building block for object data schemas. Can inherit, reuse and/or define custom properties from other Characteristcs. Properties can have literal values or other complex values (objects) described by other Characteristics.
    """

    type: Optional[List[str]] = Field(
        ["Category:OSW93ccae36243542ceac6c951450a81d47"],
        min_items=1,
        title="Types/Categories",
    )
    #uuid: UUID = Field(default_factory=uuid4, title="UUID") # should be optional

ureg = UnitRegistry()

quantity_registry: Dict[EnumType, ModelMetaclass] = {}



class QuantityValueMetaclass(ModelMetaclass):
    def __new__(cls, clsname, bases, attrs):
        class_instance =  ModelMetaclass.__new__(cls, clsname, bases, attrs)
        #print(attrs["__qualname__"], attrs)
        if "unit" in attrs and attrs["unit"] is not None:
            #print(attrs["__annotations__"]["unit"].__dict__)#, attrs["unit"].__dict__)
            #print(attrs["unit"].__dict__["__objclass__"])
            #print(attrs["__annotations__"]["unit"].__args__[0])
            # register the mapping between the unit enum and the quantity class
            
            unit_field_type = None
            # check if FieldInfo was used for annotation
            if type(attrs["unit"]) == FieldInfo:
                _types = attrs["__annotations__"]["unit"].__args__
                # select the first type != None
                for _type in _types:
                    if _type is not None:
                        unit_field_type = _type
                        break
            else:
                unit_field_type = attrs["unit"].__dict__["__objclass__"]
            quantity_registry[unit_field_type] = class_instance
        return class_instance

class QuantityValue(Characteristic, metaclass=QuantityValueMetaclass):
    """
    A Quantity Value expresses the magnitude and kind of a quantity and is given by the product of a numerical value n and a unit of measure u (from qudt).
    """

    type: Optional[Any] = ["Category:OSW4082937906634af992cf9a1b18d772cf"]
    value: float = Field(..., title="value")
    #unit: Optional[str] = Field(None, title="unit")    
    #value: float
    unit: Optional[UnitEnum] = None
    
    def to_pint(self) -> pint.Quantity:
        pint_unit_name = self.unit.name.replace("_", " ")
        # SI prefixes, see https://en.wikipedia.org/wiki/Metric_prefix
        prefixes = [
            "quetta", "ronna", "yotta", "zetta", "exa", "peta", "tera", 
            "giga", "mega", "kilo", "hecto", "deca", "deci", "centi",
            "milli", "micro", "nano", "pico", "femto", "atto",
            "zepto", "yocto", "ronto", "quecto"
        ]

        for prefix in prefixes:
            pint_unit_name = pint_unit_name.replace(prefix + " ", prefix)
        if pint_unit_name.split(" ")[0] == "per":
            pint_unit_name = pint_unit_name.replace("per", "1 /")
        return self.value * ureg[pint_unit_name]
       
    @classmethod 
    def from_pint(self, quantity: pint.Quantity):
        #unit_symbol = "{:~P}".format(quantity.units)
        value = f"{quantity:9f#Lx}" # 9f => round to 8 digits, '#' => simplify the unit
        # e.g. \SI[]{1.0}{\kilo\gram\meter\per\ampere\squared\per\second\squared}
        # select the last curly brace
        unit_symbol = value.split("{")[-1].replace("}", "")
        # replace backslashes with underscores
        unit_symbol = unit_symbol.replace("\\", "_").strip("_")
        #nummeric_value = quantity.magnitude # simplify the unit may change the scale
        nummeric_value = float(value.split("{")[1].split("}")[0])
        unit_class = unit_registry[unit_symbol]
        quantity_class = quantity_registry[unit_class]
        return quantity_class(
            value=nummeric_value, 
            unit=unit_class[unit_symbol]
        )
    
    def __add__(self, other: "QuantityValue") -> "QuantityValue":
        res_pint = self.to_pint() + other.to_pint()
        return self.from_pint(res_pint)
    
    def __sub__(self, other: "QuantityValue") -> "QuantityValue":
        res_pint = self.to_pint() - other.to_pint()
        return self.from_pint(res_pint)
    
    def __mul__(self, other: "QuantityValue") -> "QuantityValue":
        res_pint = self.to_pint() * other.to_pint()
        return self.from_pint(res_pint)
