#!/usr/bin/env python3
"""
Analyze the constructed beings corpus.

Single entry point for all analysis outputs.

Usage:
    python analysis/analyze.py --table       # write output/summary_table.md
    python analysis/analyze.py --coverage    # write output/property_coverage.md
    python analysis/analyze.py --questions   # write output/question_analysis.md
    python analysis/analyze.py --graph       # render analysis/influence_graph.html
    python analysis/analyze.py --all         # all of the above
"""

import argparse
import glob
import html
import json
import os
import sys
from collections import Counter, defaultdict

import yaml
from tabulate import tabulate


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data", "beings")
OUTPUT_DIR = os.path.join(REPO_ROOT, "output")
ANALYSIS_DIR = os.path.join(REPO_ROOT, "analysis")

INFLUENCE_GRAPH_YAML = os.path.join(ANALYSIS_DIR, "influence_graph.yaml")
INFLUENCE_GRAPH_HTML = os.path.join(ANALYSIS_DIR, "influence_graph.html")

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
        "This report counts the distribution of values for each property. "
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
    lines = ["# Question Analysis", ""]
    lines.append(f"Total entries: **{total}**.")
    lines.append("")
    lines.append(
        "The schema tracks two meta-properties: "
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
        "A single-axis approach could not distinguish these cases."
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


# ── Analysis 4: influence graph renderer ─────────────────────────────────────

EDGE_COLORS = {
    "adapts":   "#3b82f6",  # blue
    "sequel":   "#8b5cf6",  # purple
    "inherits": "#64748b",  # slate
    "inverts":  "#f59e0b",  # amber
    "elevates": "#10b981",  # emerald
}

MEDIUM_COLORS = {
    "poem":         "#e11d48",
    "epic":         "#db2777",
    "folklore":     "#9333ea",
    "play":         "#7c3aed",
    "novel":        "#2563eb",
    "short-story":  "#0284c7",
    "film":         "#059669",
    "television":   "#d97706",
    "video-game":   "#dc2626",
}


def render_influence_graph(beings):
    """Render analysis/influence_graph.html from influence_graph.yaml."""
    if not os.path.exists(INFLUENCE_GRAPH_YAML):
        print(f"Skipping graph: {INFLUENCE_GRAPH_YAML} not found", file=sys.stderr)
        return

    with open(INFLUENCE_GRAPH_YAML, "r", encoding="utf-8") as f:
        graph = yaml.safe_load(f)

    edges_data = graph.get("edges", [])
    edge_types = graph.get("edge_types", {})

    # Index beings by id
    by_id = {b["id"]: b for b in beings}

    # Build participating-node set
    participating_ids = set()
    for e in edges_data:
        participating_ids.add(e["from"])
        participating_ids.add(e["to"])

    missing = [eid for eid in participating_ids if eid not in by_id]
    if missing:
        print(
            f"WARNING: influence graph references missing ids: {missing}",
            file=sys.stderr,
        )

    # Build vis.js node array — one node per participating being.
    # Sort by (year, id) so equal-year entries have a deterministic order
    # (sets are hash-randomized; year alone is not a stable sort key).
    nodes = []
    for bid in sorted(participating_ids, key=lambda x: (year_sort_key(by_id.get(x, {})), x)):
        b = by_id.get(bid)
        if not b:
            continue
        year = get_nested(b, "metadata.year", 0)
        medium = get_nested(b, "metadata.medium", "")
        interiority = get_nested(b, "card.the_being.interiority", "")
        autonomy = get_nested(b, "card.the_being.autonomy", "")
        divergence = get_nested(b, "card.the_being.divergence", "")
        primary_q = get_nested(b, "card.the_lens.primary_question", "")
        know_ab = get_nested(b, "card.the_lens.knowability", "")
        know_ing = get_nested(b, "card.the_lens.knowing", "")
        tooltip = (
            f"<b>{html.escape(b['name'])}</b><br>"
            f"<i>{html.escape(get_nested(b, 'metadata.source', ''))}</i> ({year})<br>"
            f"medium: {medium}<br>"
            f"interiority: {interiority}<br>"
            f"autonomy: {autonomy}<br>"
            f"divergence: {divergence}<br>"
            f"primary_q: {primary_q}<br>"
            f"knowability: {know_ab}<br>"
            f"knowing: {know_ing}"
        )
        nodes.append({
            "id": bid,
            "label": f"{b['name']}\n{year}",
            "title": tooltip,
            "group": medium,
            "year": year,
        })

    # Build vis.js edge array
    edges = []
    for e in edges_data:
        edges.append({
            "from": e["from"],
            "to": e["to"],
            "label": e["type"],
            "title": html.escape((e.get("note") or "").strip().replace("\n", " ")),
            "color": {"color": EDGE_COLORS.get(e["type"], "#888"), "highlight": EDGE_COLORS.get(e["type"], "#888")},
            "arrows": "to",
            "font": {"size": 10, "align": "middle", "color": "#333"},
            "smooth": {"type": "curvedCW", "roundness": 0.15},
        })

    # Build legend HTML
    legend_rows = []
    for t, desc in edge_types.items():
        color = EDGE_COLORS.get(t, "#888")
        legend_rows.append(
            f'<tr><td><span class="swatch" style="background:{color}"></span></td>'
            f'<td><b>{html.escape(t)}</b></td>'
            f'<td>{html.escape(desc.strip())}</td></tr>'
        )
    legend_html = "\n".join(legend_rows)

    medium_legend_rows = []
    for m, c in MEDIUM_COLORS.items():
        medium_legend_rows.append(
            f'<tr><td><span class="swatch" style="background:{c}"></span></td>'
            f'<td>{html.escape(m)}</td></tr>'
        )
    medium_legend_html = "\n".join(medium_legend_rows)

    total_edges = len(edges_data)
    total_nodes = len(nodes)
    orphans = sorted(set(by_id) - participating_ids)
    orphan_html = ", ".join(html.escape(o) for o in orphans) if orphans else "(none)"

    # vis.js options — group-color by medium, physics on, directed
    groups = {m: {"color": {"background": c, "border": "#1e293b"}} for m, c in MEDIUM_COLORS.items()}

    nodes_json = json.dumps(nodes, ensure_ascii=False)
    edges_json = json.dumps(edges, ensure_ascii=False)
    groups_json = json.dumps(groups)

    template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CBO — Influence Graph</title>
<script src="https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    margin: 0;
    background: #f8fafc;
    color: #1e293b;
  }
  header {
    padding: 1.2em 2em 0.8em 2em;
    border-bottom: 1px solid #e2e8f0;
    background: white;
  }
  h1 { margin: 0 0 0.2em 0; font-size: 1.4em; }
  header p { margin: 0.2em 0; color: #475569; font-size: 0.9em; }
  #graph {
    width: 100%;
    height: 72vh;
    background: white;
    border-bottom: 1px solid #e2e8f0;
  }
  .legends {
    display: flex;
    gap: 2em;
    padding: 1em 2em 2em 2em;
    background: white;
    flex-wrap: wrap;
  }
  .legend { flex: 1; min-width: 300px; }
  .legend h2 { font-size: 1em; margin: 0 0 0.5em 0; color: #334155; }
  .legend table { border-collapse: collapse; font-size: 0.85em; width: 100%; }
  .legend td { padding: 0.2em 0.5em; vertical-align: top; }
  .swatch {
    display: inline-block;
    width: 14px;
    height: 14px;
    border: 1px solid #64748b;
    border-radius: 2px;
  }
  footer {
    padding: 1em 2em;
    font-size: 0.8em;
    color: #64748b;
    background: #f1f5f9;
  }
  footer code { background: white; padding: 1px 4px; border-radius: 3px; }
</style>
</head>
<body>

<header>
  <h1>Constructed Beings Ontology — Influence Graph</h1>
  <p>{TOTAL_EDGES} edges across {TOTAL_NODES} nodes. Each edge represents a judgment call about how one work's constructed-being properties propagate into a later work. Rendered from <code>analysis/influence_graph.yaml</code>.</p>
</header>

<div id="graph"></div>

<div class="legends">

  <div class="legend">
    <h2>Edge types</h2>
    <table>
      {EDGE_LEGEND}
    </table>
  </div>

  <div class="legend">
    <h2>Medium (node color)</h2>
    <table>
      {MEDIUM_LEGEND}
    </table>
  </div>

  <div class="legend">
    <h2>Orphans ({ORPHAN_COUNT})</h2>
    <p style="font-size: 0.85em; color: #64748b;">Nodes not connected to any edge in the current graph. These are acknowledged analytical outliers.</p>
    <p style="font-size: 0.85em;"><code>{ORPHANS}</code></p>
  </div>

</div>

<footer>
  Hover a node for its card values. Hover an edge for the influence rationale.
  Drag to pan, scroll to zoom. Regenerate with <code>python analysis/analyze.py --graph</code>.
</footer>

<script>
  const nodes = new vis.DataSet(__NODES__);
  const edges = new vis.DataSet(__EDGES__);
  const groups = __GROUPS__;

  const container = document.getElementById("graph");
  const data = { nodes, edges };
  const options = {
    nodes: {
      shape: "box",
      margin: 8,
      font: { size: 12, color: "white", face: "system-ui", multi: true, align: "center" },
      borderWidth: 1,
      widthConstraint: { minimum: 80, maximum: 140 },
    },
    edges: {
      width: 1.5,
      selectionWidth: 3,
      arrows: { to: { scaleFactor: 0.7 } },
    },
    groups: groups,
    physics: {
      enabled: true,
      solver: "forceAtlas2Based",
      forceAtlas2Based: {
        gravitationalConstant: -60,
        centralGravity: 0.008,
        springLength: 180,
        springConstant: 0.04,
        damping: 0.6,
      },
      stabilization: { iterations: 300 },
    },
    interaction: {
      hover: true,
      tooltipDelay: 100,
      navigationButtons: true,
      keyboard: true,
    },
  };
  new vis.Network(container, data, options);
</script>

</body>
</html>
"""

    out = (
        template
        .replace("{TOTAL_EDGES}", str(total_edges))
        .replace("{TOTAL_NODES}", str(total_nodes))
        .replace("{EDGE_LEGEND}", legend_html)
        .replace("{MEDIUM_LEGEND}", medium_legend_html)
        .replace("{ORPHAN_COUNT}", str(len(orphans)))
        .replace("{ORPHANS}", orphan_html)
        .replace("__NODES__", nodes_json)
        .replace("__EDGES__", edges_json)
        .replace("__GROUPS__", groups_json)
    )

    with open(INFLUENCE_GRAPH_HTML, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {INFLUENCE_GRAPH_HTML}")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CBO analysis tools.")
    parser.add_argument("--table", action="store_true", help="Write summary_table.md")
    parser.add_argument("--coverage", action="store_true", help="Write property_coverage.md")
    parser.add_argument("--questions", action="store_true", help="Write question_analysis.md")
    parser.add_argument("--graph", action="store_true", help="Render analysis/influence_graph.html")
    parser.add_argument("--all", action="store_true", help="Write all outputs")
    args = parser.parse_args()

    if not (args.table or args.coverage or args.questions or args.graph or args.all):
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
    if args.all or args.graph:
        render_influence_graph(beings)


if __name__ == "__main__":
    main()
