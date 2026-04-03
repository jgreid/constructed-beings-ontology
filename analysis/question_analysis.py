#!/usr/bin/env python3
"""Analyze the Q (question) and q_kno_status fields across all beings."""

import os
import glob
from collections import Counter, defaultdict
import yaml
from tabulate import tabulate


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'beings')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'output', 'question_analysis.md')

# Era definitions based on source year.
ERAS = [
    ('Ancient/Classical',  None, 500),
    ('Early Modern',       500,  1800),
    ('Industrial/Modern',  1800, 1950),
    ('Late Modern',        1950, 2000),
    ('Contemporary',       2000, None),
]

# Q-KNO transition ordering (from absent to primary).
QK_TRANSITION_ORDER = ['QK-ABS', 'QK-INFRA', 'QK-SEC', 'QK-PRI']


def load_beings():
    """Load all YAML files from the beings data directory."""
    beings = []
    for ext in ('*.yaml', '*.yml'):
        pattern = os.path.join(DATA_DIR, ext)
        for filepath in sorted(glob.glob(pattern)):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data is not None and isinstance(data, dict):
                        beings.append(data)
            except (yaml.YAMLError, OSError) as exc:
                print(f"Warning: skipping {filepath}: {exc}")
    return beings


def get_nested(data, dotpath, default=None):
    """Get a value from nested dicts using dot notation."""
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


def get_year(being):
    """Get the year as an integer, or None if not available."""
    y = get_nested(being, 'source.year')
    if y is None:
        return None
    try:
        return int(y)
    except (ValueError, TypeError):
        return None


def get_era(year):
    """Classify a year into an era."""
    if year is None:
        return 'Unknown'
    for era_name, start, end in ERAS:
        in_start = (start is None or year >= start)
        in_end = (end is None or year < end)
        if in_start and in_end:
            return era_name
    return 'Unknown'


def get_entity_name(being):
    """Get a human-readable name for a being entry."""
    return being.get('name', being.get('id', '(unknown)'))


def main():
    beings = load_beings()
    lines = []

    lines.append('# Question Analysis Report\n')
    lines.append(f'Total entries: **{len(beings)}**\n')

    # --- Section 1: Frequency of each Q value (all questions, not just primary) ---
    lines.append('## 1. Question Frequency (All Questions)\n')
    q_all_counter = Counter()
    for being in beings:
        questions = get_nested(being, 'relationship.question', [])
        if isinstance(questions, list):
            for q in questions:
                q_all_counter[str(q)] += 1
        elif questions:
            q_all_counter[str(questions)] += 1

    if q_all_counter:
        sorted_qs = sorted(q_all_counter.items(), key=lambda x: (-x[1], x[0]))
        headers = ['Question', 'Appearances']
        rows = [[q, count] for q, count in sorted_qs]
        lines.append(tabulate(rows, headers=headers, tablefmt='pipe'))
        lines.append('\n')

    # --- Section 1b: Primary question frequency ---
    lines.append('## 2. Primary Question Frequency\n')
    q_primary_counter = Counter()
    for being in beings:
        q = get_nested(being, 'relationship.question_primary')
        if q:
            q_primary_counter[str(q)] += 1

    if q_primary_counter:
        sorted_qs = sorted(q_primary_counter.items(), key=lambda x: (-x[1], x[0]))
        headers = ['Primary Question', 'Count']
        rows = [[q, count] for q, count in sorted_qs]
        lines.append(tabulate(rows, headers=headers, tablefmt='pipe'))
        lines.append('\n')
    else:
        lines.append('No primary question values found.\n')

    # --- Section 2: Questions by era ---
    lines.append('## 3. Primary Questions by Era\n')
    era_questions = defaultdict(Counter)
    for being in beings:
        q = get_nested(being, 'relationship.question_primary')
        if not q:
            continue
        year = get_year(being)
        era = get_era(year)
        era_questions[era][str(q)] += 1

    era_order = [e[0] for e in ERAS] + ['Unknown']
    for era_name in era_order:
        if era_name not in era_questions:
            continue
        lines.append(f'### {era_name}\n')
        sorted_qs = sorted(era_questions[era_name].items(), key=lambda x: (-x[1], x[0]))
        for q, count in sorted_qs:
            lines.append(f'- **{q}**: {count}')
        lines.append('')

    # --- Section 3: Entries by Q-KNO status, sorted by year ---
    lines.append('## 4. Q-KNO Status Pattern\n')
    kno_groups = defaultdict(list)
    for being in beings:
        status = get_nested(being, 'relationship.q_kno_status')
        if not status:
            status = '(unset)'
        kno_groups[str(status)].append(being)

    def year_sort_key(b):
        y = get_year(b)
        return y if y is not None else 99999

    # Present in transition order first, then any other statuses
    seen = set()
    ordered_statuses = []
    for s in QK_TRANSITION_ORDER:
        if s in kno_groups:
            ordered_statuses.append(s)
            seen.add(s)
    for s in sorted(kno_groups.keys()):
        if s not in seen:
            ordered_statuses.append(s)

    for status in ordered_statuses:
        entries = sorted(kno_groups[status], key=year_sort_key)
        lines.append(f'### {status}\n')
        headers = ['Entity', 'Source', 'Year', 'Primary Question']
        rows = []
        for b in entries:
            rows.append([
                get_entity_name(b),
                get_nested(b, 'source.title', ''),
                get_nested(b, 'source.year', ''),
                get_nested(b, 'relationship.question_primary', ''),
            ])
        lines.append(tabulate(rows, headers=headers, tablefmt='pipe'))
        lines.append('\n')

    # --- Section 4: Historical transition point analysis ---
    lines.append('## 5. Q-KNO Historical Transition Analysis\n')
    lines.append('Tracking the transition from QK-ABS (question absent) '
                 'through QK-INFRA (infrastructural) to QK-SEC (secondary) '
                 'to QK-PRI (primary).\n')

    transition_entries = []
    for being in beings:
        status = get_nested(being, 'relationship.q_kno_status')
        year = get_year(being)
        if status in QK_TRANSITION_ORDER and year is not None:
            transition_entries.append((year, str(status), being))

    transition_entries.sort(key=lambda x: x[0])

    if transition_entries:
        # Find first occurrence of each status
        first_seen = {}
        for year, status, being in transition_entries:
            if status not in first_seen:
                first_seen[status] = (year, get_entity_name(being))

        lines.append('**First appearance of each Q-KNO status:**\n')
        for status in QK_TRANSITION_ORDER:
            if status in first_seen:
                year, entity = first_seen[status]
                lines.append(f'- **{status}**: {year} ({entity})')
            else:
                lines.append(f'- **{status}**: not yet observed')
        lines.append('')

        # Full timeline
        lines.append('**Transition timeline:**\n')
        headers = ['Year', 'Entity', 'Q-KNO Status', 'Era']
        rows = []
        for year, status, being in transition_entries:
            rows.append([
                year,
                get_entity_name(being),
                status,
                get_era(year),
            ])
        lines.append(tabulate(rows, headers=headers, tablefmt='pipe'))
        lines.append('\n')

        # Identify transition boundaries
        status_years = defaultdict(list)
        for year, status, _ in transition_entries:
            status_years[status].append(year)

        lines.append('**Transition boundaries:**\n')
        for i in range(len(QK_TRANSITION_ORDER) - 1):
            s_from = QK_TRANSITION_ORDER[i]
            s_to = QK_TRANSITION_ORDER[i + 1]
            if s_from in status_years and s_to in status_years:
                last_from = max(status_years[s_from])
                first_to = min(status_years[s_to])
                lines.append(
                    f'- {s_from} -> {s_to}: '
                    f'transition occurs between {first_to} '
                    f'(first {s_to}) and {last_from} (last {s_from})'
                )
            elif s_to in status_years:
                first_to = min(status_years[s_to])
                lines.append(
                    f'- {s_from} -> {s_to}: '
                    f'{s_to} first appears at {first_to} '
                    f'(no {s_from} entries found)'
                )
            else:
                lines.append(
                    f'- {s_from} -> {s_to}: '
                    f'{s_to} not yet observed in data'
                )
        lines.append('')
    else:
        lines.append('No entries with both a recognized Q-KNO status and a year found.\n')

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Output written to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
