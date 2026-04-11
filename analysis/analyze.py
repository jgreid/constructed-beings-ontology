#!/usr/bin/env python3
"""
Analyze the v2.0 constructed beings corpus.

Replaces the v1 scripts generate_table.py, property_coverage.py, and
question_analysis.py with a single entry point.

Usage:
    python analysis/analyze.py --table       # write output/summary_table.md
    python analysis/analyze.py --coverage    # write output/property_coverage.md
    python analysis/analyze.py --questions   # write output/question_analysis.md
    python analysis/analyze.py --all         # write all three
"""

import argparse
import glob
import os
import sys
from collections import Counter, defaultdict

import yaml
from tabulate import tabulate


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data", "beings")
OUTPUT_DIR = os.path.join(REPO_ROOT, "output")

SUMMARY_TABLE = os.path.join(OUTPUT_DIR, "summary_table.md")
COVERAGE_FILE = os.path.join(OUTPUT_DIR, "property_coverage.md")
QUESTIONS_FILE = os.path.join(OUTPUT_DIR, "question_analysis.md")


# ── Eras (used by question_analysis) ──────────────────────────────────────────

ERAS = [
    ("Ancient / Classical", None, 500),
    ("Early Modern",        500,  1800),
    ("Industrial / Modern", 1800, 1950),
    ("Late Modern",         1950, 2000),
    ("Contemporary",        2000, None),
]

SALIENCE_ORDER = ["absent", "present", "secondary", "primary"]


# ── I/O helpers ──────────────────────────────────────────────────────────────

def load_beings():
    beings = []
    for ext in ("*.yaml", "*.yml"):
        for filepath in sorted(glob.glob(os.path.join(DATA_DIR, ext))):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
            except (yaml.YAMLError, OSError) as exc:
                print(f"Warning: skipping {filepath}: {exc}", file=sys.stderr)
                continue
            if isinstance(data, dict):
                beings.append(data)
    return beings


def get_nested(data, dotpath, default=None):
    current = data
    for key in dotpath.split("."):
        if isinstance(current, dict):
            current = current.get(key, default)
            if current is default:
                return default
        else:
            return default
    return current


def fmt(value):
    if value is None or value == "":
        return ""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value)


def year_sort_key(being):
    year = get_nested(being, "metadata.year", 0)
    try:
        return int(year)
    except (TypeError, ValueError):
        return 0


def get_era(year):
    if year is None:
        return "Unknown"
    for name, start, end in ERAS:
        if (start is None or year >= start) and (end is None or year < end):
            return name
    return "Unknown"


# ── Analysis 1: summary table ────────────────────────────────────────────────

SUMMARY_COLUMNS = [
    ("Entity",           "name"),
    ("Source",           "metadata.source"),
    ("Year",             "metadata.year"),
    ("Medium",           "metadata.medium"),
    ("Interiority",      "card.the_being.interiority"),
    ("Autonomy",         "card.the_being.autonomy"),
    ("Divergence",       "card.the_being.divergence"),
    ("Primary Question", "card.the_lens.primary_question"),
    ("Epistemic Reach",  "card.the_lens.epistemic_reach"),
    ("Knowability",      "card.the_lens.knowability"),
    ("Knowing",          "card.the_lens.knowing"),
]


def write_summary_table(beings):
    beings_sorted = sorted(beings, key=year_sort_key)
    headers = [col[0] for col in SUMMARY_COLUMNS]
    rows = [
        [fmt(get_nested(b, dotpath)) for _, dotpath in SUMMARY_COLUMNS]
        for b in beings_sorted
    ]
    table = tabulate(rows, headers=headers, tablefmt="pipe")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(SUMMARY_TABLE, "w", encoding="utf-8") as f:
        f.write("# Constructed Beings Summary Table\n\n")
        f.write(f"Total entries: **{len(beings)}**. Sorted by year.\n\n")
        f.write(table)
        f.write("\n")
    print(f"Wrote {SUMMARY_TABLE}")


# ── Analysis 2: property coverage ────────────────────────────────────────────

COVERAGE_PROPERTIES = [
    ("Interiority",      "card.the_being.interiority"),
    ("Autonomy",         "card.the_being.autonomy"),
    ("Divergence",       "card.the_being.divergence"),
    ("Primary Question", "card.the_lens.primary_question"),
    ("Epistemic Reach",  "card.the_lens.epistemic_reach"),
    ("Knowability",      "card.the_lens.knowability"),
    ("Knowing",          "card.the_lens.knowing"),
    ("Medium",           "metadata.medium"),
    ("Substrate",        "metadata.substrate"),
    ("Motivation",       "metadata.motivation"),
]


def write_coverage(beings):
    total = len(beings)
    lines = ["# Property Coverage Report", ""]
    lines.append(f"Total entries: **{total}**.")
    lines.append("")
    lines.append(
        "This report counts the distribution of values for each v2.0 property. "
        "List-valued properties (substrate, motivation) count every token "
        "separately — hybrids contribute to each of their substrates."
    )
    lines.append("")

    for display, dotpath in COVERAGE_PROPERTIES:
        counter = Counter()
        coded = 0
        for being in beings:
            val = get_nested(being, dotpath)
            if val is None or val == "" or val == []:
                continue
            coded += 1
            if isinstance(val, list):
                for v in val:
                    counter[str(v)] += 1
            else:
                counter[str(val)] += 1

        lines.append(f"## {display}")
        lines.append("")
        lines.append(f"- **Coded:** {coded}/{total} entries")
        if counter:
            sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
            headers = [display, "Count"]
            rows = [[k, v] for k, v in sorted_items]
            lines.append("")
            lines.append(tabulate(rows, headers=headers, tablefmt="pipe"))
        lines.append("")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(COVERAGE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {COVERAGE_FILE}")


# ── Analysis 3: question / knowability / knowing ─────────────────────────────

def _salience_rank(value):
    try:
        return SALIENCE_ORDER.index(value)
    except ValueError:
        return -1


def write_questions(beings):
    total = len(beings)
    lines = ["# Question Analysis — v2.0", ""]
    lines.append(f"Total entries: **{total}**.")
    lines.append("")
    lines.append(
        "v2.0 replaces the single Q-KNO axis with two meta-properties: "
        "`knowability` (can we verify its mind?) and `knowing` (can it "
        "know us?). This report tracks both, plus the distribution of "
        "`primary_question`."
    )
    lines.append("")

    # ── Section 1: primary_question frequency ────────────────────────
    lines.append("## 1. Primary Question Frequency")
    lines.append("")
    q_counter = Counter()
    for being in beings:
        q = get_nested(being, "card.the_lens.primary_question")
        if q:
            q_counter[q] += 1
    rows = sorted(q_counter.items(), key=lambda x: (-x[1], x[0]))
    lines.append(tabulate(rows, headers=["Primary Question", "Count"], tablefmt="pipe"))
    lines.append("")

    # ── Section 2: primary_question by era ───────────────────────────
    lines.append("## 2. Primary Questions by Era")
    lines.append("")
    era_counters = defaultdict(Counter)
    for being in beings:
        q = get_nested(being, "card.the_lens.primary_question")
        if not q:
            continue
        year = get_nested(being, "metadata.year")
        era = get_era(year)
        era_counters[era][q] += 1
    era_order = [e[0] for e in ERAS] + ["Unknown"]
    for era_name in era_order:
        if era_name not in era_counters:
            continue
        lines.append(f"### {era_name}")
        lines.append("")
        sorted_qs = sorted(era_counters[era_name].items(), key=lambda x: (-x[1], x[0]))
        rows = [[q, c] for q, c in sorted_qs]
        lines.append(tabulate(rows, headers=["Primary Question", "Count"], tablefmt="pipe"))
        lines.append("")

    # ── Section 3: knowability distribution ──────────────────────────
    lines.append("## 3. Knowability Distribution")
    lines.append("")
    know_counter = Counter()
    for being in beings:
        v = get_nested(being, "card.the_lens.knowability")
        if v:
            know_counter[v] += 1
    rows = [[v, know_counter.get(v, 0)] for v in SALIENCE_ORDER]
    lines.append(tabulate(rows, headers=["Knowability", "Count"], tablefmt="pipe"))
    lines.append("")

    # ── Section 4: knowing distribution ──────────────────────────────
    lines.append("## 4. Knowing Distribution")
    lines.append("")
    knowing_counter = Counter()
    for being in beings:
        v = get_nested(being, "card.the_lens.knowing")
        if v:
            knowing_counter[v] += 1
    rows = [[v, knowing_counter.get(v, 0)] for v in SALIENCE_ORDER]
    lines.append(tabulate(rows, headers=["Knowing", "Count"], tablefmt="pipe"))
    lines.append("")

    # ── Section 5: knowability/knowing divergence ────────────────────
    lines.append("## 5. Knowability vs. Knowing Divergence")
    lines.append("")
    lines.append(
        "Entries where knowability and knowing have different values. "
        "v1's single Q-KNO axis could not distinguish these cases."
    )
    lines.append("")
    divergent = []
    for being in sorted(beings, key=year_sort_key):
        kab = get_nested(being, "card.the_lens.knowability")
        kin = get_nested(being, "card.the_lens.knowing")
        if kab != kin:
            divergent.append([
                get_nested(being, "name", ""),
                get_nested(being, "metadata.source", ""),
                get_nested(being, "metadata.year", ""),
                kab,
                kin,
            ])
    if divergent:
        lines.append(tabulate(
            divergent,
            headers=["Entity", "Source", "Year", "Knowability", "Knowing"],
            tablefmt="pipe",
        ))
    else:
        lines.append("(no divergent entries)")
    lines.append("")
    lines.append(f"**{len(divergent)} of {total} entries diverge.**")
    lines.append("")

    # ── Section 6: entries by knowability, sorted by year ────────────
    lines.append("## 6. Entries by Knowability (chronological)")
    lines.append("")
    groups = defaultdict(list)
    for being in beings:
        v = get_nested(being, "card.the_lens.knowability", "(unset)")
        groups[v].append(being)
    for v in SALIENCE_ORDER:
        entries = sorted(groups.get(v, []), key=year_sort_key)
        if not entries:
            continue
        lines.append(f"### knowability = {v}")
        lines.append("")
        rows = [
            [
                get_nested(b, "name", ""),
                get_nested(b, "metadata.source", ""),
                get_nested(b, "metadata.year", ""),
                get_nested(b, "card.the_lens.primary_question", ""),
            ]
            for b in entries
        ]
        lines.append(tabulate(
            rows,
            headers=["Entity", "Source", "Year", "Primary Q"],
            tablefmt="pipe",
        ))
        lines.append("")

    # ── Section 7: first appearance of each salience level ──────────
    lines.append("## 7. First Appearance of Each Salience Level")
    lines.append("")
    lines.append("For knowability and knowing, tracking the earliest year each level appears.")
    lines.append("")
    for label, dotpath in [
        ("Knowability", "card.the_lens.knowability"),
        ("Knowing",     "card.the_lens.knowing"),
    ]:
        first_seen = {}
        for being in sorted(beings, key=year_sort_key):
            v = get_nested(being, dotpath)
            if v not in first_seen and v in SALIENCE_ORDER:
                first_seen[v] = (
                    get_nested(being, "metadata.year", ""),
                    get_nested(being, "name", ""),
                )
        lines.append(f"### {label}")
        lines.append("")
        rows = []
        for level in SALIENCE_ORDER:
            if level in first_seen:
                year, name = first_seen[level]
                rows.append([level, year, name])
            else:
                rows.append([level, "—", "(not observed)"])
        lines.append(tabulate(rows, headers=["Level", "First Year", "Entity"], tablefmt="pipe"))
        lines.append("")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {QUESTIONS_FILE}")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CBO v2.0 analysis tools.")
    parser.add_argument("--table", action="store_true", help="Write summary_table.md")
    parser.add_argument("--coverage", action="store_true", help="Write property_coverage.md")
    parser.add_argument("--questions", action="store_true", help="Write question_analysis.md")
    parser.add_argument("--all", action="store_true", help="Write all outputs")
    args = parser.parse_args()

    if not (args.table or args.coverage or args.questions or args.all):
        parser.print_help()
        sys.exit(0)

    beings = load_beings()
    if not beings:
        print("No entries found in data/beings/", file=sys.stderr)
        sys.exit(1)

    if args.all or args.table:
        write_summary_table(beings)
    if args.all or args.coverage:
        write_coverage(beings)
    if args.all or args.questions:
        write_questions(beings)


if __name__ == "__main__":
    main()
