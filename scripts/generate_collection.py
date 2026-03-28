"""Generate _collection.py from _model.py and update _model.py to use Unit.xxx.value.

Parses all FooUnit(Enum) classes in _model.py, extracts unit enum members,
generates _collection.py with a single Unit(UnitEnum) class containing all
unique values, and rewrites _model.py to reference Unit.xxx.value instead
of hardcoded strings.

Applies to both v1 and v2 (root) pydantic versions.

Usage:
    python scripts/generate_collection.py          # both v1 and v2
    python scripts/generate_collection.py v1       # v1 only
    python scripts/generate_collection.py v2       # v2 only
"""

import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / (
    "src/opensemantic/characteristics/quantitative"
)

_V1_PKG = "opensemantic.characteristics.quantitative.v1"
_V2_PKG = "opensemantic.characteristics.quantitative"

VERSIONS = {
    "v1": {
        "model": SRC / "v1" / "_model.py",
        "collection": SRC / "v1" / "_collection.py",
        "import_enum": f"from {_V1_PKG}._enum import UnitEnum",
        "import_collection": f"from {_V1_PKG}._collection import Unit",
        "anchor": f"from {_V1_PKG}._static import UnitEnum as Enum",
    },
    "v2": {
        "model": SRC / "_model.py",
        "collection": SRC / "_collection.py",
        "import_enum": f"from {_V2_PKG}._enum import UnitEnum",
        "import_collection": f"from {_V2_PKG}._collection import Unit",
        "anchor": f"from {_V2_PKG}._static import UnitEnum as Enum",
    },
}


def parse_collection(text: str) -> dict[str, str]:
    """Extract existing unit members from _collection.py (Unit(UnitEnum) class)."""
    units: dict[str, str] = {}
    in_class = False
    pending_name = None

    for line in text.splitlines():
        if re.match(r"^class Unit\(UnitEnum\):", line):
            in_class = True
            continue
        if in_class and line and not line[0].isspace():
            break
        if not in_class:
            continue

        m = re.match(r'^\s+(\w+)\s*=\s*"(Item:OSW[^"]+)"', line)
        if m:
            units[m.group(1)] = m.group(2)
            pending_name = None
            continue
        m = re.match(r"^\s+(\w+)\s*=\s*\(\s*$", line)
        if m:
            pending_name = m.group(1)
            continue
        if pending_name:
            m = re.match(r'^\s+"(Item:OSW[^"]+)"', line)
            if m:
                units[pending_name] = m.group(1)
                pending_name = None

    return units


def parse_model(text: str):
    """Extract unit enum members with hardcoded "Item:OSW..." values from _model.py.

    Returns
    -------
    all_units : dict[str, str]
        Mapping of member_name -> "Item:OSW..." value (insertion-ordered,
        first occurrence wins).
    """
    all_units: dict[str, str] = {}
    in_unit_enum = False
    pending_name = None

    for line in text.splitlines():
        if re.match(r"^class \w+Unit\((?:Enum|UnitEnum)\):", line):
            in_unit_enum = True
            continue

        if (
            in_unit_enum
            and line
            and not line[0].isspace()
            and not line.startswith('"""')
        ):
            in_unit_enum = False
            pending_name = None

        if not in_unit_enum:
            continue

        # Single-line: name = "Item:OSW..."
        m = re.match(r'^\s+(\w+)\s*=\s*"(Item:OSW[^"]+)"', line)
        if m:
            all_units.setdefault(m.group(1), m.group(2))
            pending_name = None
            continue

        # Multi-line start: name = (
        m = re.match(r"^\s+(\w+)\s*=\s*\(\s*$", line)
        if m:
            pending_name = m.group(1)
            continue

        # Multi-line value: "Item:OSW..."
        if pending_name:
            m = re.match(r'^\s+"(Item:OSW[^"]+)"', line)
            if m:
                all_units.setdefault(pending_name, m.group(1))
                pending_name = None
                continue

    return all_units


def generate_collection(all_units: dict[str, str], import_enum: str) -> str:
    """Build the content of _collection.py."""
    lines = [import_enum, "", "", "class Unit(UnitEnum):"]

    for name, value in all_units.items():
        if len(f'    {name} = "{value}"') <= 88:
            lines.append(f'    {name} = "{value}"')
        else:
            lines.append(f"    {name} = (")
            lines.append(f'        "{value}"')
            lines.append("    )")

    lines.append("")  # trailing newline
    return "\n".join(lines)


def rewrite_model(
    text: str,
    all_units: dict[str, str],
    import_collection: str,
    anchor: str,
) -> str:
    """Replace hardcoded unit string values with Unit.xxx.value in _model.py."""
    if import_collection not in text:
        text = text.replace(anchor, anchor + "\n" + import_collection)

    # Build reverse lookup: "Item:OSW..." -> member name
    value_to_name: dict[str, str] = {}
    for name, value in all_units.items():
        if value not in value_to_name:
            value_to_name[value] = name

    result_lines = []
    lines = text.splitlines(keepends=True)
    i = 0
    in_unit_enum = False

    while i < len(lines):
        line = lines[i]

        if re.match(r"^class \w+Unit\((?:Enum|UnitEnum)\):", line):
            in_unit_enum = True
            result_lines.append(line)
            i += 1
            continue

        if (
            in_unit_enum
            and line.rstrip()
            and not line[0].isspace()
            and not line.startswith('"""')
        ):
            in_unit_enum = False

        if not in_unit_enum:
            result_lines.append(line)
            i += 1
            continue

        # Single-line: name = "Item:OSW..."
        m = re.match(r'^(\s+)(\w+)\s*=\s*"(Item:OSW[^"]+)"(.*)$', line)
        if m:
            indent, name, value, rest = m.groups()
            unit_name = value_to_name.get(value)
            if unit_name:
                result_lines.append(f"{indent}{name} = Unit.{unit_name}.value{rest}\n")
            else:
                result_lines.append(line)
            i += 1
            continue

        # Multi-line: name = (\n    "Item:OSW..."\n    )
        m = re.match(r"^(\s+)(\w+)\s*=\s*\(\s*$", line)
        if m and i + 2 < len(lines):
            indent, name = m.groups()
            val_line = lines[i + 1]
            close_line = lines[i + 2]
            vm = re.match(r'^\s+"(Item:OSW[^"]+)"', val_line)
            cm = re.match(r"^\s+\)", close_line)
            if vm and cm:
                value = vm.group(1)
                unit_name = value_to_name.get(value)
                if unit_name:
                    result_lines.append(f"{indent}{name} = Unit.{unit_name}.value\n")
                    i += 3
                    continue

        result_lines.append(line)
        i += 1

    return "".join(result_lines)


def process_version(version: str):
    cfg = VERSIONS[version]
    model_path = cfg["model"]
    collection_path = cfg["collection"]

    if not model_path.exists():
        print(f"[{version}] Skipping — {model_path} not found")
        return

    rel = model_path.relative_to(SRC.parent)
    print(f"[{version}] Processing {rel}")
    text = model_path.read_text(encoding="utf-8")

    # 1. Parse existing _collection.py (if any), then merge new hardcoded entries
    existing_units: dict[str, str] = {}
    if collection_path.exists():
        coll_text = collection_path.read_text(encoding="utf-8")
        existing_units = parse_collection(coll_text)
    new_units = parse_model(text)

    # Merge: existing first, then new hardcoded (first occurrence wins)
    all_units: dict[str, str] = {}
    all_units.update(existing_units)
    for name, value in new_units.items():
        all_units.setdefault(name, value)

    print(
        f"[{version}] {len(existing_units)} existing + {len(new_units)} from model "
        f"= {len(all_units)} unique unit members"
    )

    # 2. Generate _collection.py
    collection_content = generate_collection(all_units, cfg["import_enum"])
    collection_path.write_text(collection_content, encoding="utf-8")
    print(f"[{version}] Wrote {collection_path.relative_to(SRC.parent)}")

    # 3. Rewrite _model.py
    new_model = rewrite_model(text, all_units, cfg["import_collection"], cfg["anchor"])
    model_path.write_text(new_model, encoding="utf-8")
    print(f"[{version}] Rewrote {model_path.relative_to(SRC.parent)}")

    # 4. Verify
    remaining = parse_model(new_model)
    hardcoded = {k: v for k, v in remaining.items() if v.startswith("Item:OSW")}
    if hardcoded:
        print(
            f"[{version}] {len(hardcoded)} members with name conflicts remain hardcoded"
        )
    else:
        print(f"[{version}] All unit enum members now reference Unit.xxx.value")


def main():
    versions = sys.argv[1:] if len(sys.argv) > 1 else ["v1", "v2"]
    for v in versions:
        if v not in VERSIONS:
            print(f"Unknown version: {v}. Use 'v1' or 'v2'.")
            sys.exit(1)
    for v in versions:
        process_version(v)
        print()


if __name__ == "__main__":
    main()
