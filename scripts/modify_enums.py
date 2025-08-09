import json
import re
from pathlib import Path

from pint import application_registry

from opensemantic.characteristics.quantitative import QuantityValue

ureg = application_registry.get()


model_path = (
    Path(__file__).parents[1]
    / "src"
    / "opensemantic"
    / "characteristics"
    / "quantitative"
    / "_model.py"
)

print(model_path)


with model_path.open("r", encoding="utf-8") as file:
    content = file.read()

matches = []
pattern1 = (
    r'\s*([a-zA-Z\_]+)\s*=[\s\(]*"(Item\:OSW[a-f0-9]+(#OSW[a-f0-9]+)*)"[\s\)]*\s*'
)
#
# matches = re.findall(
#     pattern=r'([a-zA-Z\_]+)\s*=[\s\(]*"(Item\:OSW[a-f0-9]+(#OSW[a-f0-9]+)*)"[\s\)]*',
#     string=content,
#     flags=re.MULTILINE,
# )

unit_name_to_osw = {}
osw_to_unit_name = {}
duplicate_var_count = 0
duplicate_str_count = 0
for match in re.finditer(pattern1, content, flags=re.MULTILINE):
    start_pos = match.start()
    # Zeilennummer berechnen (1-basiert)
    line_number = content.count("\n", 0, start_pos) + 1
    groups = match.groups()
    full_match = match.group(0)
    matches.append((line_number, groups, full_match))
    # match.group(0)  # This will give you the full match
    var_name = match.group(1)
    # This will give you the first capturing group (the variable name)
    osw_id = match.group(2)
    # This will give you the second capturing group (the item string)
    if var_name not in unit_name_to_osw:
        unit_name_to_osw[var_name] = osw_id
    else:
        # print(f"Duplicate variable name found: {var_name}")
        duplicate_var_count += 1
    if osw_id not in osw_to_unit_name:
        osw_to_unit_name[osw_id] = var_name
    else:
        if osw_to_unit_name[osw_id] != var_name:
            duplicate_str_count += 1
            print(
                f"Duplicate string found with different variable names: {osw_id} "
                f"({osw_to_unit_name[osw_id]} vs {var_name})"
            )
        # print(f"Duplicate string found: {string}")

print(f"Found {len(unit_name_to_osw)} unique unit names.")
print(f"Found {len(osw_to_unit_name)} unique OSW IDs.")
print(f"Found {duplicate_var_count} duplicate variable names.")
print(f"Found {duplicate_str_count} duplicate OSW IDs with different variable names.")

# todo: make a mapping to latex

osw_to_pint = {}
for osw_id, var_name in osw_to_unit_name.items():
    pint_compatible = QuantityValue.get_pint_ureg_compatible_str(var_name)
    try:
        ureg[pint_compatible]
    except Exception as e:
        print(f"Incompatible string: {pint_compatible}; Exception:\n{e}")
        continue
    osw_to_pint[osw_id] = pint_compatible

new_content = content
pattern2 = (
    r'[ \t\f\v]*([a-zA-Z\_]+)\s*=[\s\(]*"(Item\:OSW[a-f0-9]+(#OSW[a-f0-9]+)*)"'
    r"\s*\)*\n+"
)
unit_enum_class_name = "Unit"
unit_literal_varname = "UnitLiteral"
unit_function_name = "unit"
# We need a second round to do the replacements
for match in re.finditer(pattern2, content, flags=re.MULTILINE):
    # This will give you the full match = the line(s) with the variable definition we
    #  want to replace
    full_match = match.group(0)
    # This will give you the first capturing group (the variable name):
    var_name = match.group(1)
    if not var_name:
        continue
    replacement = f"{var_name} = {unit_enum_class_name}.{var_name}"
    if full_match.endswith("\n"):
        # If the line starts with one or more newlines, we need to keep the newlines
        replacement += "\n" * (len(full_match) - len(full_match.rstrip("\n")))
    if full_match.startswith("\n"):
        # If the line starts with spaces, we need to keep the indentation
        replacement = "\n    " + replacement
    if full_match.startswith(" "):
        # If the line starts with spaces, we need to keep the indentation
        replacement = " " * (len(full_match) - len(full_match.lstrip())) + replacement
    # Replace the full match with the new replacement string
    new_content = new_content.replace(full_match, replacement)


collection_modulename = "_collection"
# Create a unit enum collection
collection = f"""from opensemantic.characteristics.quantitative._static import UnitEnum


class {unit_enum_class_name}(UnitEnum):
"""
for var_name, osw_id in unit_name_to_osw.items():
    collection += f'    {var_name} = "{osw_id}"\n'


string_helper_modulename = "_strings"
# Create a string helper
string_helper = f"""from typing import Literal
from opensemantic.characteristics.quantitative.{collection_modulename} import (
    {unit_enum_class_name}
)


{unit_literal_varname} = Literal[
"""
for var_name in unit_name_to_osw.keys():
    string_helper += f'    "{var_name}",\n'
string_helper += f"""]


def {unit_function_name}(name: {unit_literal_varname}) -> {unit_enum_class_name}:
    return getattr({unit_enum_class_name}, name)
"""

# Ensure the output directory exists
output_dir = Path(__file__).parents[1] / "data"
output_dir.mkdir(parents=True, exist_ok=True)

# Write the mappings to JSON files
with (output_dir / "osw_to_pint.json").open("w", encoding="utf-8") as file:
    json.dump(osw_to_pint, file, indent=4, ensure_ascii=False)
with (output_dir / "unit_name_to_osw.json").open("w", encoding="utf-8") as file:
    json.dump(unit_name_to_osw, file, indent=4, ensure_ascii=False)
with (output_dir / "osw_to_unit_name.json").open("w", encoding="utf-8") as file:
    json.dump(unit_name_to_osw, file, indent=4, ensure_ascii=False)
# Write the collection to a Python file
collection_path = model_path.parent / (collection_modulename + ".py")
with collection_path.open("w", encoding="utf-8") as file:
    file.write(collection)
# Write the stringhelper to a Python file
string_helper_path = model_path.parent / (string_helper_modulename + ".py")
with string_helper_path.open("w", encoding="utf-8") as file:
    file.write(string_helper)

# Make sure that the new model references the new collection file
if not re.findall(
    pattern=rf"{collection_modulename}[^\n]*{unit_enum_class_name}",
    string=new_content,
    flags=re.MULTILINE,
):
    new_content = (
        f"from opensemantic.characteristics.quantitative.{collection_modulename} "
        f"import {unit_enum_class_name}\n"
    ) + new_content

# Make replacements in the _model.py file
with model_path.open("w", encoding="utf-8") as file:
    file.write(new_content)

# Make additions to the __init__.py file
init_path = model_path.parent / "__init__.py"
with init_path.open("r", encoding="utf-8") as file:
    init_content = file.read()
with init_path.open("w", encoding="utf-8") as file:
    if not re.findall(
        pattern=rf"{collection_modulename}[^\n]*{unit_enum_class_name}",
        string=init_content,
        flags=re.MULTILINE,
    ):
        init_content = init_content + (
            f"from opensemantic.characteristics.quantitative.{collection_modulename} "
            f"import {unit_enum_class_name}  # noqa\n"
        )
    if not re.findall(
        pattern=rf"{string_helper_modulename}[^\n]*{unit_literal_varname}",
        string=init_content,
        flags=re.MULTILINE,
    ):
        init_content = init_content + (
            f"from opensemantic.characteristics.quantitative."
            f"{string_helper_modulename} import (  # noqa\n"
            f"    {unit_literal_varname},\n"
            f"    {unit_function_name}\n"
            ")\n"
        )
    file.write(init_content)
