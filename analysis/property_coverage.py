#!/usr/bin/env python3
"""Analyze property coverage across all YAML being definitions."""

import os
import glob
from collections import Counter
import yaml
from tabulate import tabulate


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'beings')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'output', 'property_coverage.md')

# Properties to check: (display_name, dot_path)
PROPERTIES = [
    ('Name',              'name'),
    ('Source Title',      'source.title'),
    ('Year',              'source.year'),
    ('Medium',            'source.medium'),
    ('Tradition',         'source.tradition'),
    ('Reproductive Method', 'reproductive_method'),
    ('Creator Motivation', 'creator.motivation'),
    ('Creation Morality', 'creator.creation_morality'),
    ('Substrate',         'being.substrate'),
    ('Autonomy',          'being.autonomy'),
    ('Interiority',       'being.interiority'),
    ('Mortality',         'being.mortality'),
    ('Multiplicity',      'being.multiplicity'),
    ('Memory Persistence', 'being.memory_persistence'),
    ('Nonconsensual Transformation', 'being.nonconsensual_transformation'),
    ('Failure Mode',      'relationship.failure_mode'),
    ('Question',          'relationship.question'),
    ('Primary Question',  'relationship.question_primary'),
    ('Epistemic Reach',   'relationship.epistemic_reach'),
    ('Q-KNO Status',      'relationship.q_kno_status'),
    ('Narrative Role',    'narrative_role'),
]


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


def get_nested(data, dotpath):
    """Get a value from nested dicts using dot notation."""
    keys = dotpath.split('.')
    val = data
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            return None
        if val is None:
            return None
    return val


def main():
    beings = load_beings()
    total = len(beings)

    lines = []
    lines.append('# Property Coverage Report\n')
    lines.append(f'Total entries: **{total}**\n')

    for display_name, dotpath in PROPERTIES:
        counter = Counter()
        missing = []
        coded = 0

        for being in beings:
            value = get_nested(being, dotpath)
            entity_name = being.get('name', being.get('id', '(unknown)'))

            if value is None or value == '' or value == []:
                missing.append(entity_name)
            else:
                coded += 1
                if isinstance(value, list):
                    for v in value:
                        counter[str(v)] += 1
                else:
                    counter[str(value)] += 1

        lines.append(f'## {display_name}\n')
        lines.append(f'- **Coded:** {coded}/{total} entries\n')

        if counter:
            lines.append('- **Distribution:**\n')
            sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
            dist_parts = [f'{value}: {count}' for value, count in sorted_items]
            lines.append(f'  - {", ".join(dist_parts)}\n')

        if missing:
            lines.append(f'- **Missing ({len(missing)}):** {", ".join(missing)}\n')

        lines.append('')

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Output written to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
