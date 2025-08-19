# Scope

## What's in the dictionaries?

- unit_name_to_osw_id.json serves as a mapping for the unit name used in the [UnitEnum](../src/opensemantic/characteristics/quantitative/_enum.py) to the OSW-ID
- osw_id_to_unit_name.json serves as a mapping for OSW-ID to the unit name used in the [UnitEnum](../src/opensemantic/characteristics/quantitative/_enum.py)
- osw_id_to_pint.json serves as a mapping for OSW-ID to a Pint unit registry compatible unit name

## What are they used for?

When data is exported to a file or stored in a database as JSON, the unit are not represented as plain text unit names, but as their identifiers (OSW-IDs). This allows a compact storage of the measurement data.

To be able to retrieve the unit names, e.g. to create a pandas DataFrame with Pint units, we have created the mappings. They will be available through the GitHub raw file system directly and thus can be looked up by any client quickly and without authentication.
