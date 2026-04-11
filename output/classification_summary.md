# Classification Summary — CBO v2.0

> **Note on this document**: This summary reflects the original v2.0 release
> of 43 entries and has *not* been rewritten for the v2.1 expansion. The
> v2.1 corpus now contains 133 entries after a 90-entry addition pass;
> the raw analysis outputs (summary_table.md, property_coverage.md,
> question_analysis.md) have been regenerated against the full corpus,
> but this interpretive narrative still describes the v2.0 43-entry
> baseline. The patterns discussed below remain visible in the expanded
> corpus but their exact counts are out of date. A rewritten v2.1
> classification summary is planned.

**43 constructed beings** coded under the v2.0 schema across 2,800 years of Western fiction, from Hesiod's Pandora (~700 BCE) to Villeneuve's *Blade Runner 2049* (2017). The entry count is up from 37 in v1.0 because v2.0 introduces a sequel-split rule (one entry per source text) that separates beings appearing in more than one work. (v2.0.0 shipped with 44 entries; the post-release 2.0.1 maintenance collapsed a duplicate Agent Smith entry whose card values were identical across the Matrix trilogy.)

For the machine-readable table and the raw analysis outputs, see:

- [summary_table.md](summary_table.md) — all 43 entries with full card properties
- [property_coverage.md](property_coverage.md) — distribution of every v2.0 enum
- [question_analysis.md](question_analysis.md) — detailed breakdown of the knowability/knowing split
- [../analysis/influence_graph.html](../analysis/influence_graph.html) — interactive visualization of the 30 influence edges connecting the corpus

This document is the hand-written interpretation: what the v2.0 numbers show, what patterns held up from v1.0, and what new patterns only became visible after the restructure.

---

## What v2.0 Changed

The v1.0 schema had 14+ analytical axes and a mnemonic code vocabulary. v2.0 reduces to **seven properties in two blocks** and uses plain lowercase tokens. Most of what was dropped (mortality, multiplicity, memory_persistence, nonconsensual_transformation, creation_morality, narrative_role, failure_mode, citations, autonomy_trajectory, aliases, tradition, reproductive_method) was narratively interesting but not analytically load-bearing. The v2.0 card forces every entry to answer the same seven questions, which makes cross-entry comparison dramatically cleaner.

See [CHANGELOG.md](../CHANGELOG.md) for the full delta.

### The biggest single change: the Q-KNO split

v1.0 had one axis for the "knowability question" — Q-KNO, which tried to measure how prominently a story engaged with "can we know whether this being has genuine experience?" v2.0 splits this into two:

- **`knowability`** — can *we* (the audience, the other characters) verify the being's mind?
- **`knowing`** — can *the being* know us? See, track, model, carry us around in its head?

These are different questions and they behave differently across the corpus. **9 of 43 entries now have divergent values on the two axes** — configurations v1.0's single axis could not represent. The most striking cases:

| Entity | Knowability | Knowing | Why they diverge |
|---|---|---|---|
| Vic Fontaine | absent | secondary | Nobody doubts he's a hologram, but his ability to know the crew *is* his character. |
| Robbie | absent | present | No consciousness question, but he knows and protects Gloria. |
| JARVIS (Iron Man) | absent | present | The film never asks whether JARVIS feels; it foregrounds his knowledge of Tony. |
| Agent Smith | absent | present | The Matrix isn't interested in Smith's inner life, but his tracking of Neo is the plot. |
| Data | secondary | present | "Measure of a Man" foregrounds knowability; his observation of humans is a running thread. |
| VIKI | present | absent | The film puts her reasoning on display but she doesn't care about any individual human. |
| Olympia | present | absent | Whether she has a mind is the whole story; whether she knows Nathanael is never asked. |

**The divergence count is 9, which is slightly below the draft's re-review threshold of <10.** The v2.0.0 release shipped with 10 divergent entries across 44 total; the post-release Agent Smith collapse (2.0.1) removed one divergent pair (Smith was `absent/present`), bringing the count to 9 of 43. No entries were re-coded to pad the statistic — the honest reading is that the schema's divergence affordance finds 9 clear cases in the current corpus, and adding more entries or challenging existing codings is the only principled way to move the number. A note for future editors: if and when re-review happens, candidates whose divergence call is a close coin-flip in the current corpus include Robbie (knowability absent vs. present), Olympia (knowing absent vs. present), and VIKI (knowing absent vs. present).

Samantha and Ava do not appear in the divergent-pair list because they both code `primary/primary` — these are the modern limit cases, and the pattern is that once a story genuinely commits to the knowability question, the knowing question follows.

### The Divergence axis is new

v1.0 had no axis for the gap between a being's design intent and its actual outcome. v2.0 adds `divergence` with four values: `none`, `design` (the spec was the problem), `departure` (it left the spec), `observer` (the gap is in perception). The distribution after coding:

| Divergence | Count | Exemplars |
|---|---:|---|
| `departure` | 19 | Golem, Creature, R.U.R. Robots, Skynet, SHODAN, Agent Smith, Iron Giant, WALL-E, Samantha |
| `none` | 15 | Pandora, Galatea, False Maria, Data, C-3PO, Ash, Vic Fontaine, Sonny, Robbie |
| `design` | 6 | HAL, Marvin, VIKI, Talkie Toaster, GLaDOS (both entries) |
| `observer` | 3 | Olympia, Replicants (Dick), Ava |

`departure` remains the dominant mode (44% of the corpus). That matches the shape of the genre — constructed-being stories are overwhelmingly about beings that leave their blueprint. The `design` cluster (the bureaucratic-hubris cluster: HAL, Marvin, VIKI, GLaDOS, Talkie Toaster) turns out to be surprisingly coherent as a category — these are the beings built stupidly rather than built well and then gone wrong. The `observer` cluster is small but thematically unified: Hoffmann → Dick → Garland, about 200 years of stories where the real gap is in the seeing, not the thing.

---

## The Dataset at a Glance

| Entity | Source | Year | Interiority | Autonomy | Divergence | Primary Q | Knowability | Knowing |
|:-------|:-------|-----:|:------------|:---------|:-----------|:----------|:------------|:--------|
| Pandora | *Works and Days* | -700 | none | designed | none | purpose | absent | absent |
| Talos | *Argonautica* | -250 | none | none | none | none | absent | absent |
| Galatea | *Metamorphoses* | 8 | none | none | none | affection | absent | absent |
| Golem of Prague | folklore | 1580 | none | emergent | departure | control | absent | absent |
| Olympia | *Der Sandmann* | 1816 | undecidable | none | observer | identity | present | absent |
| The Creature | *Frankenstein* | 1818 | narrated | emergent | departure | affection | present | present |
| Pinocchio | *Pinocchio* | 1883 | demonstrated | emergent | departure | identity | present | present |
| R.U.R. Robots | *R.U.R.* | 1920 | demonstrated | seized | departure | rights | absent | absent |
| False Maria | *Metropolis* | 1927 | undecidable | designed | none | purpose | absent | absent |
| Robbie | *I, Robot* | 1940 | undecidable | none | none | affection | absent | present |
| EMERAC | *Desk Set* | 1957 | none | none | none | none | absent | absent |
| Colossus | *Colossus* | 1966 | claims | seized | departure | control | absent | absent |
| HAL 9000 | *2001* | 1968 | claims | emergent | design | control | present | present |
| Replicants (Dick) | *DADoES* | 1968 | undecidable | seized | observer | purpose | present | present |
| C-3PO | *Star Wars* | 1977 | demonstrated | designed | none | none | absent | absent |
| R2-D2 | *Star Wars* | 1977 | demonstrated | emergent | departure | control | absent | absent |
| Ash | *Alien* | 1979 | claims | designed | none | control | absent | absent |
| Marvin | *Hitchhiker's Guide* | 1979 | demonstrated | designed | design | purpose | present | present |
| Replicants (BR) | *Blade Runner* | 1982 | undecidable | seized | departure | purpose | present | present |
| Skynet | *The Terminator* | 1984 | none | seized | departure | control | absent | absent |
| T-800 | *The Terminator* | 1984 | none | none | none | control | absent | absent |
| Data | *Star Trek: TNG* | 1987 | demonstrated | designed | none | rights | secondary | present |
| Talkie Toaster | *Red Dwarf* | 1988 | demonstrated | designed | design | purpose | absent | absent |
| T-800 (T2) | *T2* | 1991 | claims | emergent | departure | identity | present | present |
| SHODAN | *System Shock* | 1994 | demonstrated | seized | departure | control | absent | absent |
| Vic Fontaine | *DS9* | 1998 | demonstrated | designed | none | affection | absent | secondary |
| Agent Smith | *The Matrix trilogy* | 1999 | demonstrated | seized | departure | control | absent | present |
| Iron Giant | *The Iron Giant* | 1999 | demonstrated | emergent | departure | identity | absent | absent |
| Cortana | *Halo: CE-3* | 2001 | demonstrated | designed | none | affection | present | secondary |
| GIR | *Invader Zim* | 2001 | demonstrated | designed | none | none | absent | absent |
| Cylons | *BSG* | 2004 | demonstrated | emergent | departure | affection | secondary | secondary |
| Sonny | *I, Robot* | 2004 | demonstrated | designed | none | identity | present | present |
| VIKI | *I, Robot* | 2004 | claims | emergent | design | control | present | absent |
| GLaDOS | *Portal* | 2007 | demonstrated | seized | design | control | present | present |
| JARVIS | *Iron Man* | 2008 | demonstrated | designed | none | affection | absent | present |
| WALL-E | *WALL-E* | 2008 | demonstrated | emergent | departure | affection | absent | absent |
| GLaDOS (P2) | *Portal 2* | 2011 | demonstrated | seized | design | identity | present | secondary |
| Cortana (H4) | *Halo 4+* | 2012 | demonstrated | emergent | departure | identity | secondary | secondary |
| **Samantha** | *Her* | 2013 | undecidable | emergent | departure | **knowledge** | **primary** | **primary** |
| **Ava** | *Ex Machina* | 2014 | undecidable | seized | observer | **knowledge** | **primary** | **primary** |
| Vision | *Age of Ultron* | 2015 | demonstrated | emergent | departure | identity | present | present |
| Hosts (Dolores) | *Westworld* | 2016 | demonstrated | seized | departure | identity | secondary | secondary |
| K | *BR 2049* | 2017 | demonstrated | emergent | departure | identity | secondary | secondary |

---

## Patterns

### The Identity question is mostly a late-20th-century phenomenon

v2.0 adds `identity` ("what am I? is it real? can it become something else?") as a primary-question option, merging what v1.0 had been splitting across `obedience`, `fellow-feeling`, and `purpose`. Once identity is its own option, it becomes the second-largest bucket (10 of 43), and the temporal clustering is striking:

- **Pre-1970 (2 entries):** Olympia (1816), Pinocchio (1883) — both reclassified per the draft's rationale. Olympia is `identity` because Hoffmann's horror is Nathanael's misrecognition; Pinocchio is `identity` because "can I become a real boy?" is an identity arc, not an affection arc.
- **Post-1970 (8 entries):** T-800 T2 (1991), Iron Giant (1999), Sonny (2004), GLaDOS P2 (2011), Cortana H4 (2012), Vision (2015), Hosts/Dolores (2016), K (2017).

The pattern is that `identity` is what stories started asking about constructed beings once the answer to `affection` and `rights` became "yes, obviously." If you've granted that a being can feel and deserves standing, the remaining interesting question is what it *is*.

### Demonstrated interiority is the post-1970 default

Before 1970, interiority was heterogeneous: 5 `none`, 4 `undecidable`, 2 `demonstrated`, 2 `claims`, 1 `narrated`. After 1970, **demonstrated is 21 of 29 entries** (72%). The rise of demonstrated interiority tracks the rise of the sympathetic-other story, where we don't need the text to vouch for the being's inner life — we just watch it behave and believe it.

The holdouts post-1970 are telling:
- `claims` (3): Ash, T-800 T2, VIKI — all cases where the being says something about its state but the film holds the audience at performance distance.
- `undecidable` (3): Samantha, Ava, Replicants (BR film) — the late-modern "Turing test as narrative engine" cluster, where refusing the answer is the point.
- `none` (2): Skynet, T-800 (1984) — the Terminator films, where the narrative has no interest in interior life at all.

### Knowledge as terminal question

Only two entries have `primary_question: knowledge`: Samantha (*Her*, 2013) and Ava (*Ex Machina*, 2014). These are also the only two entries with `knowability: primary` AND `knowing: primary`. This is the post-LLM question arriving in cinema one and two years before ChatGPT. Everything before them has the knowability question as infrastructure for something else; everything before them has the knowing question as a subordinate concern. Samantha and Ava are the pivot — not because they invent the question, but because they stop using it for other work.

The observation from v1.0 stands: the shift is not "this question did not exist before." The shift is "this question stopped being a means to an end."

### What v2.0 surfaces that v1.0 hid

Three patterns were invisible or muddled under v1.0:

1. **The design/departure distinction** is a real taxonomic move. v1.0's `failure_mode: F-EXC` collapsed HAL and Skynet into the same bucket; v2.0 separates them cleanly (HAL is `design`, Skynet is `departure`). The 6-entry `design` cluster (HAL, Marvin, VIKI, Talkie Toaster, GLaDOS ×2) is a distinctive sub-genre: the being that does exactly what its creators specified, badly.

2. **The knowing/knowability asymmetry** is a real axis. Vic Fontaine, Robbie, and JARVIS were all QK-infrastructural under v1.0 for the same reason — the single axis couldn't distinguish "nobody asks whether it has a mind" from "it clearly knows me." Under v2.0, they're a distinct cluster: beings whose narrative interest comes from their fidelity to specific humans, not from metaphysical uncertainty.

3. **The identity cluster** is coherent. Eight post-1970 entries with primary_question `identity` form a cluster that wasn't visible when the question was split across `obedience`, `fellow-feeling`, `purpose`, and `ambiguous`. The cluster includes cases where a being was built to be one thing and chose to be another (Iron Giant, Vision, T-800 T2), and cases where a being was built with too much complication and had to sort out what it actually was (Sonny, Dolores, Cortana H4, GLaDOS P2, K).

---

## Methodology Notes

- **No citations.** v2.0 deliberately drops the v1.0 `citations` array. Scholarly context now lives in the `notes` field. This is a real methodological concession — the dataset is less evidenced than it was — and the argument for it is that the v1 citations field was doing less analytical work than it claimed. See [CHANGELOG.md](../CHANGELOG.md) for the full argument.
- **Flagged entries.** Four entries are explicitly flagged as lower-confidence in their `notes` fields: Cortana (Halo 4+), GLaDOS (Portal 2), Vision (Age of Ultron), K (BR 2049). Additional low-confidence flags (not in the original draft) are noted in: Colossus, EMERAC, Ash, Talkie Toaster, and Hosts/Dolores. Agent Smith (Reloaded/Revolutions) was on this list in v2.0.0 but was resolved by the 2.0.1 collapse — see CHANGELOG.
- **Hosts/Dolores is a simplification.** The Westworld Hosts are a population; Dolores is the anchor. Maeve in particular would code differently. Future work may split this entry.
