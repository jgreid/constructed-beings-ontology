"""Flag entries with potentially inconsistent classifications.

Rules are grounded in docs/coding_guide.md. Each rule produces a list of
flagged entries with a short rationale. Output is written to
output/consistency_audit.md.

These are *flags*, not verdicts. A flagged entry may still be coded
correctly — but it's a place a human reader should double-check.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BEINGS = ROOT / "data" / "beings"
OUT = ROOT / "output" / "consistency_audit.md"


def load_entries() -> list[dict]:
    entries = []
    for path in sorted(BEINGS.glob("*.yaml")):
        with path.open() as fh:
            d = yaml.safe_load(fh)
            d["_path"] = path
            entries.append(d)
    return entries


def b(entry: dict, field: str):
    return entry["card"]["the_being"][field]


def l(entry: dict, field: str):
    return entry["card"]["the_lens"][field]


def m(entry: dict, field: str):
    return entry["metadata"].get(field)


# --- rule definitions -------------------------------------------------------
#
# Each rule returns True when the entry should be flagged. The rationale
# string explains why the combination is suspicious.

RULES: list[tuple[str, str, callable]] = []


def rule(name: str, rationale: str):
    def decorator(fn):
        RULES.append((name, rationale, fn))
        return fn
    return decorator


@rule(
    "autonomy-none_but-divergence-departure",
    "autonomy=none means no depicted agency. Per the coding guide, `divergence=observer` is compatible (Olympia, Coppélia) because the gap is in perception — but `departure` requires the being to have left its design, which needs agency.",
)
def r1(e):
    return b(e, "autonomy") == "none" and b(e, "divergence") == "departure"


@rule(
    "autonomy-none_but-rebellious",
    "A being coded as having no autonomy cannot be rebellious or patricidal toward its creator.",
)
def r2(e):
    return b(e, "autonomy") == "none" and m(e, "creator_relationship") in (
        "rebellious",
        "patricidal",
        "resentful",
    )


@rule(
    "rebellious_but-divergence-none",
    "Rebellion/patricide against the creator usually implies leaving the design (divergence != none).",
)
def r3(e):
    return m(e, "creator_relationship") in ("rebellious", "patricidal") and b(e, "divergence") == "none"


@rule(
    "tag-rebellion_but-not-rebellious",
    "`rebellion` tag conflicts with a non-rebellious/patricidal creator relationship.",
)
def r4(e):
    tags = m(e, "tags") or []
    return "rebellion" in tags and m(e, "creator_relationship") not in ("rebellious", "patricidal")


@rule(
    "tag-love-story_but-not-affection",
    "`love-story` tag implies primary_question should be affection.",
)
def r5(e):
    tags = m(e, "tags") or []
    return "love-story" in tags and l(e, "primary_question") != "affection"


@rule(
    "tag-creator-conflict_but-loyal-or-servile",
    "`creator-conflict` tag is used broadly for narrative confrontation with the creator (V'Ger-style), but loyal/servile relationships are still worth a second look — the tag usually implies friction.",
)
def r6(e):
    tags = m(e, "tags") or []
    return "creator-conflict" in tags and m(e, "creator_relationship") in (
        "loyal",
        "servile",
    )


@rule(
    "tag-turing-test_but-knowability-absent",
    "`turing-test` tag implies the question of verifying the mind is at least present.",
)
def r7(e):
    tags = m(e, "tags") or []
    return "turing-test" in tags and l(e, "knowability") == "absent"


@rule(
    "tag-child-arc_but-no-child-motivation",
    "`child-arc` tag implies `child` should appear in motivation.",
)
def r8(e):
    tags = m(e, "tags") or []
    return "child-arc" in tags and "child" not in (m(e, "motivation") or [])


@rule(
    "interiority-none_but-question-identity",
    "A text that shows no interiority is unlikely to treat 'what am I?' as the primary question.",
)
def r9(e):
    return b(e, "interiority") == "none" and l(e, "primary_question") == "identity"


@rule(
    "interiority-none_but-knowing-salient",
    "`knowing` at primary/secondary implies some interior through which the being knows us.",
)
def r10(e):
    return b(e, "interiority") == "none" and l(e, "knowing") in ("primary", "secondary")


@rule(
    "epistemic-reach-none_but-interiority-visible",
    "`epistemic_reach=none` says we can't observe the being; interiority can't be demonstrated/narrated.",
)
def r11(e):
    return l(e, "epistemic_reach") == "none" and b(e, "interiority") in ("demonstrated", "narrated")


@rule(
    "knowing-primary_but-reach-none",
    "If the story's primary question is the being knowing us, we need some channel to observe it knowing.",
)
def r12(e):
    return l(e, "knowing") == "primary" and l(e, "epistemic_reach") == "none"


@rule(
    "question-rights_but-relationship-servile",
    "A rights question usually presupposes the being is not purely servile to its creator.",
)
def r13(e):
    return l(e, "primary_question") == "rights" and m(e, "creator_relationship") == "servile"


@rule(
    "substrate-biological-only_but-creator-relationship-absent",
    "Purely biological beings with no linguistic/electrical substrate tend to have present creators; worth double-checking `absent`.",
)
def r14(e):
    subs = m(e, "substrate") or []
    return subs == ["biological"] and m(e, "creator_relationship") == "absent"


@rule(
    "embodiment-virtual_but-not-electrical",
    "Virtual beings generally run on electrical/linguistic substrate; missing both is suspicious.",
)
def r15(e):
    if m(e, "embodiment") != "virtual":
        return False
    subs = set(m(e, "substrate") or [])
    return "electrical" not in subs and "linguistic" not in subs


# --- self-flagged entries ---------------------------------------------------

SELF_FLAG_PATTERNS = [
    r"\bflagged for re-?review\b",
    r"\blow[- ]confidence\b",
    r"\bfuture edition may\b",
    r"\buncertain\b",
    r"\bto verify\b",
    r"\bcould reasonably be\b",
    r"\bjudgment call\b",
    r"\bcoded from partial\b",
]

SELF_FLAG_RE = re.compile("|".join(SELF_FLAG_PATTERNS), re.IGNORECASE)


def self_flagged(e: dict) -> str | None:
    notes = e.get("notes") or ""
    m_ = SELF_FLAG_RE.search(notes)
    return m_.group(0) if m_ else None


# --- main -------------------------------------------------------------------


def run() -> int:
    entries = load_entries()
    entries_by_id = {e["id"]: e for e in entries}

    flags: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for rule_name, rationale, fn in RULES:
        for e in entries:
            if fn(e):
                flags[rule_name].append((e["id"], e["name"]))

    self_flags = []
    for e in entries:
        hit = self_flagged(e)
        if hit:
            self_flags.append((e["id"], e["name"], hit))

    # lineage check: walk each sequel chain and list card-value diffs.
    lineage_diffs: list[dict] = []
    inverted_links: list[dict] = []
    card_fields = [
        ("the_being", "interiority"),
        ("the_being", "autonomy"),
        ("the_being", "divergence"),
        ("the_lens", "primary_question"),
        ("the_lens", "epistemic_reach"),
        ("the_lens", "knowability"),
        ("the_lens", "knowing"),
    ]
    for e in entries:
        target_id = e.get("sequel_link")
        if not target_id:
            continue
        target = entries_by_id.get(target_id)
        if not target:
            lineage_diffs.append(
                {
                    "from_id": e["id"],
                    "to_id": target_id,
                    "broken": True,
                    "diffs": [],
                    "link_type": e.get("link_type"),
                }
            )
            continue

        # direction check: SCHEMA.md requires older → newer
        y_from = e["metadata"]["year"]
        y_to = target["metadata"]["year"]
        if y_to < y_from:
            inverted_links.append(
                {
                    "from_id": e["id"],
                    "from_name": e["name"],
                    "from_year": y_from,
                    "to_id": target["id"],
                    "to_name": target["name"],
                    "to_year": y_to,
                    "link_type": e.get("link_type"),
                }
            )

        diffs = []
        for block, field in card_fields:
            a = e["card"][block][field]
            c = target["card"][block][field]
            if a != c:
                diffs.append((field, a, c))
        if diffs:
            lineage_diffs.append(
                {
                    "from_id": e["id"],
                    "from_name": e["name"],
                    "to_id": target["id"],
                    "to_name": target["name"],
                    "link_type": e.get("link_type"),
                    "diffs": diffs,
                }
            )

    write_report(entries, flags, self_flags, lineage_diffs, inverted_links)
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


def write_report(entries, flags, self_flags, lineage_diffs, inverted_links):
    total = len(entries)
    all_flagged_ids: set[str] = set()
    for pairs in flags.values():
        all_flagged_ids.update(p[0] for p in pairs)

    lines: list[str] = []
    lines.append("# Consistency Audit\n")
    lines.append(f"Corpus: **{total} entries**. This report flags entries whose codings sit in tension with a rule derived from `docs/coding_guide.md` or the tag/field vocabularies. A flag is a prompt for a human review, not a verdict of miscoding — several combinations that look odd on paper are defensible in context.\n")
    lines.append(f"- **Rule-based flags:** {sum(len(v) for v in flags.values())} flag-instances across **{len(all_flagged_ids)} distinct entries**.")
    lines.append(f"- **Self-flagged in notes:** {len(self_flags)} entries.")
    lines.append(f"- **Lineage diffs:** {len(lineage_diffs)} sequel-link pairs with non-identical cards (including broken links if any).")
    lines.append(f"- **Inverted sequel_links:** {len(inverted_links)} pairs point newer → older, reversing the SCHEMA.md direction rule.\n")

    lines.append("## 1. Rule-based flags\n")
    for rule_name, rationale, _ in RULES:
        hits = flags.get(rule_name, [])
        lines.append(f"### `{rule_name}` — {len(hits)} entries\n")
        lines.append(f"*{rationale}*\n")
        if not hits:
            lines.append("_No entries flagged._\n")
            continue
        for eid, name in hits:
            lines.append(f"- **{name}** (`{eid}`)")
        lines.append("")

    lines.append("## 2. Self-flagged entries\n")
    lines.append("Entries whose own `notes` field contains hedging language (partial familiarity, judgment call, flagged-for-re-review, etc.). These were already marked by the coder as warranting a second look.\n")
    if not self_flags:
        lines.append("_None found._\n")
    else:
        lines.append("| Entry | Phrase |")
        lines.append("|---|---|")
        for eid, name, hit in sorted(self_flags, key=lambda t: t[0]):
            lines.append(f"| {name} (`{eid}`) | `{hit}` |")
        lines.append("")

    lines.append("## 3. Inverted sequel_links\n")
    lines.append("SCHEMA.md and `docs/coding_guide.md` both specify that `sequel_link` points from the older entry forward to the newer one (the newest in a chain has `sequel_link: null`). These pairs point the opposite way — they should be reversed (move the link to the older entry and set the younger entry's link to the next newer one, or null).\n")
    if not inverted_links:
        lines.append("_None found._\n")
    else:
        lines.append("| From (year) | → To (year) | link_type |")
        lines.append("|---|---|---|")
        for d in sorted(inverted_links, key=lambda x: x["from_year"]):
            lines.append(
                f"| {d['from_name']} (`{d['from_id']}`, {d['from_year']}) | {d['to_name']} (`{d['to_id']}`, {d['to_year']}) | `{d['link_type']}` |"
            )
        lines.append("")

    lines.append("## 4. Lineage diffs\n")
    lines.append("Pairs connected by `sequel_link` where at least one card value differs. Many of these are legitimate (a sequel that shifts the primary question), but sharp multi-field swings are worth checking.\n")
    broken = [d for d in lineage_diffs if d.get("broken")]
    if broken:
        lines.append("### Broken sequel links\n")
        for d in broken:
            lines.append(f"- `{d['from_id']}` → `{d['to_id']}` (link_type: `{d['link_type']}`): target does not exist.")
        lines.append("")
    real = [d for d in lineage_diffs if not d.get("broken")]
    real_sorted = sorted(real, key=lambda d: -len(d["diffs"]))
    lines.append(f"### Diff summary ({len(real)} pairs)\n")
    lines.append("| From | → To | link_type | # card fields changed |")
    lines.append("|---|---|---|---:|")
    for d in real_sorted:
        lines.append(
            f"| {d['from_name']} (`{d['from_id']}`) | {d['to_name']} (`{d['to_id']}`) | `{d['link_type']}` | {len(d['diffs'])} |"
        )
    lines.append("")
    lines.append("### Pairs with ≥4 card-field changes\n")
    heavy = [d for d in real_sorted if len(d["diffs"]) >= 4]
    if not heavy:
        lines.append("_None._\n")
    else:
        for d in heavy:
            lines.append(f"**{d['from_name']} (`{d['from_id']}`) → {d['to_name']} (`{d['to_id']}`)** (link_type: `{d['link_type']}`)")
            for field, a, c in d["diffs"]:
                lines.append(f"- `{field}`: `{a}` → `{c}`")
            lines.append("")

    lines.append("## 5. Findings & Recommendations\n")
    lines.append(
        "A sample of flagged entries was spot-checked against independent summaries "
        "(Wikipedia, Memory Alpha, published reviews) to separate genuine miscodings "
        "from defensible judgment calls. Headline findings below; the rest of the "
        "rule-based flags are judgment calls the coder thought through and documented "
        "in `notes`.\n"
    )
    lines.append("### Confirmed data bugs\n")
    lines.append(
        "- **7 inverted `sequel_link` directions** (see section 3). These are "
        "mechanical fixes: each pair should be reversed so the link flows older → newer. "
        "Examples include `galatea-gilbert → galatea` (Gilbert 1871 points back to Ovid 8 CE) "
        "and `atom-pluto → astro-boy-tezuka` (Pluto 2003 points back to Astro Boy 1952).\n"
    )
    lines.append("### Entries worth a closer re-read\n")
    lines.append(
        "- **Amazo** (`amazo-dc`). `creator_relationship: rebellious` + `divergence: none`. "
        "External check: in the original 1960 *Brave and the Bold* #30 debut, Amazo is "
        "Ivo's **obedient instrument** against the Justice League — he hunts and drains the "
        "League at Ivo's direction for an immortality serum. Rebellion-against-Ivo appears "
        "in later continuity. Either anchor the entry to the 1960 debut (then `creator_relationship` "
        "is `servile` or `loyal`) or acknowledge the later-continuity reading and add the "
        "`rebellion` tag to match.\n"
    )
    lines.append(
        "- **The Bride** (`bride-of-frankenstein`). `autonomy: none` + `divergence: departure`. "
        "The entry's own notes describe the Bride's refusal as *\"the most important act of agency "
        "in the film\"* — which is itself agency, arguing for `autonomy: seized` rather than `none`. "
        "Either the autonomy or the divergence reading needs to give.\n"
    )
    lines.append("### Rules that turned out to be too strict\n")
    lines.append(
        "- **`tag-love-story_but-not-affection` (19 entries).** Spot-checks on Samantha (*Her*), "
        "Woody (*Toy Story*), Guy (*Free Guy*), Walter (*Marjorie Prime*), and Galatea (Gilbert) "
        "show that the `love-story` tag is used for the presence of a romantic plot thread even "
        "when the analytical primary question is `identity`, `knowledge`, or `purpose`. This is a "
        "deliberate coding choice (the tag marks surface genre; `primary_question` marks the "
        "analytical core). Only entries where the romantic thread is also the central narrative "
        "question should flip to `affection` — Bride of Frankenstein, Galatea (Ovid), and Baymax "
        "do, and are coded that way.\n"
    )
    lines.append(
        "- **`tag-child-arc_but-no-child-motivation` (16 entries).** The `child-arc` tag marks "
        "the narrative shape (a being who grows up, learns, is parented), not the creator's "
        "original motivation for building it. Iron Giant, Baymax, Atom (*Real Steel*), Robbie and "
        "Teddy all have this shape without having been built as children. The rule should probably "
        "be dropped or reworded.\n"
    )
    lines.append(
        "- **`tag-creator-conflict_but-loyal-or-servile` (V'Ger).** V'Ger's creator-conflict is "
        "narrative-metaphysical (\"is there nothing more?\") rather than insurrectionary — the tag "
        "is being used for any dramatic encounter with the creator, not only for antagonism. The "
        "coding is defensible; the rule over-fires.\n"
    )
    lines.append("### Self-flagged entries worth external follow-up\n")
    lines.append(
        "Spot-checks on two self-flagged low-confidence entries returned clean:\n"
        "- **Colossus** (1966, D.F. Jones). The novel's verbal ambiguity about Colossus's "
        "inner life matches `interiority: claims`; its global takeover matches `divergence: departure` "
        "and `primary_question: control`. `knowability: absent` is defensible — the novel is a "
        "thriller about containment, not a question-of-mind narrative — though the ending's "
        "\"in time you will love me\" hint could push it to `present`.\n"
        "- **EMERAC** (1957, *Desk Set*). Wikipedia confirms EMERAC is an ENIAC pastiche used as "
        "a romantic-comedy MacGuffin, matching all seven card values and the metadata.\n"
    )
    lines.append(
        "The remaining 13 self-flagged entries (Ash, BB/Samantha, Booti, Hosts/Dolores, "
        "K/BR-2049, Mia, Regus Patoff, Stepford Wives, Talkie Toaster, Tyrone, Val & Aqua, "
        "Vic Fontaine, The Entity) were not externally spot-checked in this pass and remain "
        "candidates for future re-review.\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(run())
