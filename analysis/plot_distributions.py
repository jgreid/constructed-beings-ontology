"""Generate bar-chart PNGs for every controlled vocabulary in the corpus.

One PNG per property is written to output/charts/. Bars are ordered by the
schema's canonical value order (not by count) so the "none/absent" zero state
always appears on the left where applicable.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

ROOT = Path(__file__).resolve().parent.parent
BEINGS = ROOT / "data" / "beings"
SCHEMA = ROOT / "schema" / "cb-schema.yaml"
OUT = ROOT / "output" / "charts"


SCALAR_FIELDS = [
    ("the_being.interiority", "Interiority"),
    ("the_being.autonomy", "Autonomy"),
    ("the_being.divergence", "Divergence"),
    ("the_lens.primary_question", "Primary Question"),
    ("the_lens.epistemic_reach", "Epistemic Reach"),
    ("the_lens.knowability", "Knowability"),
    ("the_lens.knowing", "Knowing"),
    ("metadata.medium", "Medium"),
    ("metadata.presentation", "Presentation"),
    ("metadata.embodiment", "Embodiment"),
    ("metadata.prominence", "Prominence"),
    ("metadata.creator_relationship", "Creator Relationship"),
    ("metadata.link_type", "Link Type"),
]

LIST_FIELDS = [
    ("metadata.substrate", "Substrate"),
    ("metadata.motivation", "Motivation"),
    ("metadata.tags", "Tags"),
]


def load_schema_enums() -> dict[str, list[str]]:
    with SCHEMA.open() as fh:
        schema = yaml.safe_load(fh)
    props = schema["properties"]
    enums: dict[str, list[str]] = {}
    enums["the_being.interiority"] = props["card"]["properties"]["the_being"]["properties"]["interiority"]["allowed"]
    enums["the_being.autonomy"] = props["card"]["properties"]["the_being"]["properties"]["autonomy"]["allowed"]
    enums["the_being.divergence"] = props["card"]["properties"]["the_being"]["properties"]["divergence"]["allowed"]
    enums["the_lens.primary_question"] = props["card"]["properties"]["the_lens"]["properties"]["primary_question"]["allowed"]
    enums["the_lens.epistemic_reach"] = props["card"]["properties"]["the_lens"]["properties"]["epistemic_reach"]["allowed"]
    enums["the_lens.knowability"] = props["card"]["properties"]["the_lens"]["properties"]["knowability"]["allowed"]
    enums["the_lens.knowing"] = props["card"]["properties"]["the_lens"]["properties"]["knowing"]["allowed"]
    meta = props["metadata"]["properties"]
    enums["metadata.medium"] = meta["medium"]["allowed"]
    enums["metadata.presentation"] = meta["presentation"]["allowed"]
    enums["metadata.embodiment"] = meta["embodiment"]["allowed"]
    enums["metadata.prominence"] = meta["prominence"]["allowed"]
    enums["metadata.creator_relationship"] = meta["creator_relationship"]["allowed"]
    enums["metadata.link_type"] = props["link_type"]["allowed"]
    enums["metadata.substrate"] = meta["substrate"]["items"]["allowed"]
    enums["metadata.motivation"] = meta["motivation"]["items"]["allowed"]
    enums["metadata.tags"] = meta["tags"]["items"]["allowed"]
    return enums


def load_entries() -> list[dict]:
    entries = []
    for path in sorted(BEINGS.glob("*.yaml")):
        with path.open() as fh:
            entries.append(yaml.safe_load(fh))
    return entries


def extract_scalar(entry: dict, dotted: str):
    head, _, tail = dotted.partition(".")
    if head == "metadata" and tail == "link_type":
        return entry.get("link_type")
    if head == "metadata":
        return entry["metadata"].get(tail)
    if head in ("the_being", "the_lens"):
        return entry["card"][head].get(tail)
    raise KeyError(dotted)


def extract_list(entry: dict, dotted: str) -> list[str]:
    head, _, tail = dotted.partition(".")
    assert head == "metadata"
    return entry["metadata"].get(tail) or []


def plot_bar(title: str, values: list[str], counts: list[int], total: int, out_path: Path, *, note: str | None = None) -> None:
    fig, ax = plt.subplots(figsize=(max(6, 0.55 * len(values) + 2), 4.2))
    bars = ax.bar(values, counts, color="#4C72B0", edgecolor="black", linewidth=0.6)
    for bar, count in zip(bars, counts):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            str(count),
            ha="center",
            va="bottom",
            fontsize=9,
        )
    ax.set_title(f"{title}  (n={total})")
    ax.set_ylabel("Entries" + (" (multi-valued)" if note == "list" else ""))
    ax.set_ylim(0, max(counts) * 1.15 if counts else 1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.xticks(rotation=30, ha="right")
    if note == "list":
        ax.text(
            1.0,
            1.02,
            "multi-valued — tokens sum > entry count",
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=8,
            color="#555",
        )
    plt.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    enums = load_schema_enums()
    entries = load_entries()
    total_entries = len(entries)

    written: list[Path] = []

    for dotted, label in SCALAR_FIELDS:
        values = list(enums[dotted])
        is_nullable = dotted == "metadata.link_type"
        counts: Counter = Counter()
        for entry in entries:
            v = extract_scalar(entry, dotted)
            if v is None and is_nullable:
                counts["<null>"] += 1
            else:
                counts[v] += 1
        labels = values + (["<null>"] if is_nullable and counts.get("<null>", 0) else [])
        bar_counts = [counts.get(v, 0) for v in labels]
        out_path = OUT / f"{dotted.replace('.', '__')}.png"
        plot_bar(label, labels, bar_counts, total_entries, out_path)
        written.append(out_path)

    for dotted, label in LIST_FIELDS:
        values = list(enums[dotted])
        counts = Counter()
        for entry in entries:
            for v in extract_list(entry, dotted):
                counts[v] += 1
        bar_counts = [counts.get(v, 0) for v in values]
        out_path = OUT / f"{dotted.replace('.', '__')}.png"
        plot_bar(label, values, bar_counts, total_entries, out_path, note="list")
        written.append(out_path)

    for path in written:
        print(f"Wrote {path.relative_to(ROOT)}")
    print(f"\n{len(written)} charts written to {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
