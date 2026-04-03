#!/usr/bin/env python3
"""Generate a markdown summary table from all YAML being definitions."""

import os
import glob
import yaml
from tabulate import tabulate


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'beings')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'output', 'summary_table.md')


def load_beings():
    """Load all YAML files from the beings data directory."""
    beings = []
    for ext in ('*.yaml', '*.yml'):
        pattern = os.path.join(DATA_DIR, ext)
        for filepath in sorted(glob.glob(pattern)):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data is not None:
                    beings.append(data)
    return beings


def get_nested(data, dotpath, default=''):
    """Get a value from nested dicts using dot notation (e.g. 'source.year')."""
    keys = dotpath.split('.')
    val = data
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            return default
        if val is None:
            return default
    return val


def fmt(value):
    """Format a value for table display."""
    if value is None or value == '':
        return ''
    if isinstance(value, list):
        return ', '.join(str(v) for v in value)
    return str(value)


# Columns: (display_name, dot_path)
COLUMNS = [
    ('Entity',           'name'),
    ('Source',           'source.title'),
    ('Year',             'source.year'),
    ('Medium',           'source.medium'),
    ('Motivation',       'creator.motivation'),
    ('Substrate',        'being.substrate'),
    ('Autonomy',         'being.autonomy'),
    ('Interiority',      'being.interiority'),
    ('Mortality',        'being.mortality'),
    ('Multiplicity',     'being.multiplicity'),
    ('Memory',           'being.memory_persistence'),
    ('Failure Mode',     'relationship.failure_mode'),
    ('Primary Question', 'relationship.question_primary'),
    ('Epistemic Reach',  'relationship.epistemic_reach'),
    ('Q-KNO Status',     'relationship.q_kno_status'),
]


def main():
    beings = load_beings()

    # Sort by year
    def sort_key(b):
        y = get_nested(b, 'source.year', 0)
        try:
            return int(y)
        except (ValueError, TypeError):
            return 0

    beings.sort(key=sort_key)

    headers = [col[0] for col in COLUMNS]
    rows = []
    for being in beings:
        row = [fmt(get_nested(being, col[1])) for col in COLUMNS]
        rows.append(row)

    table_md = tabulate(rows, headers=headers, tablefmt='pipe')

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('# Constructed Beings Summary Table\n\n')
        f.write(table_md)
        f.write('\n')

    print(f"Output written to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
