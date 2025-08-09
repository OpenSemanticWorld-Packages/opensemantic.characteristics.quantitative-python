import sys
from enum import Enum

if sys.version_info >= (3, 11):
    # Python 3.11 or higher
    from enum import EnumType
else:
    # Python < 3.11
    from enum import EnumMeta as EnumType

from typing import Dict, Union

import pint_pandas  # noqa: F401

unit_registry: Dict[str, list[EnumType]] = {}


def class_in_list(cls: Union[str, type], lst: list[type]) -> bool:
    cls_name = cls
    if isinstance(cls, UnitEnum):
        cls_name = cls.__name__
    names = [cls.__name__ for cls in lst]
    return cls_name in names


def move_matching_class_to_end(lst: list[type], cls_name: str) -> list:
    if not lst:
        return lst
    for item in lst:
        if item.__name__ == cls_name:
            lst.remove(item)
            lst.append(item)
    return lst


class UnitEnumMetaclass(EnumType):
    def __new__(cls, clsname, bases, attrs):
        # print(attrs["__qualname__"], attrs)
        class_instance = EnumType.__new__(cls, clsname, bases, attrs)
        for key, value in attrs.items():
            if key not in ["__module__", "__qualname__", "_generate_next_value_"]:
                # register all enum values in the unit_registry
                if key not in unit_registry.keys():
                    unit_registry[key] = []
                # if key in unit_registry and class_instance.__name__ == "Unit":
                #     # Make sure that the comparison here is according to
                #     #  _collection.py
                #     pass
                #     # warn(
                #     #     (
                #     #         f"Unit {key} already registered in "
                #     #         "unit_registry, skip registration."
                #     #     )
                #     # )
                # else:
                #     # Registers the class instance with a certain key, if it is not
                #     #  already present or was registered with the generic
                #     #  UnitEnum "Unit"
                #     unit_registry[key].append(class_instance)
                if not class_in_list(class_instance, unit_registry[key]):
                    unit_registry[key].append(class_instance)
                    # Move the most generic entry to the last position
                    move_matching_class_to_end(unit_registry[key], "Unit")

        return class_instance


class UnitEnum(str, Enum, metaclass=UnitEnumMetaclass):
    pass
