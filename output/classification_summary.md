# Classification Summary

**212 constructed beings** coded under the current schema across 2,800 years of Western fiction, from Homer's golden handmaidens of Hephaestus (~750 BCE) through Gareth Edwards's *The Creator* (2023).

For the machine-readable table and the raw analysis outputs, see:

- [summary_table.md](summary_table.md) — all 212 entries with full card properties
- [property_coverage.md](property_coverage.md) — distribution of every schema enum
- [question_analysis.md](question_analysis.md) — detailed breakdown of the knowability/knowing split
- [../analysis/influence_graph.html](../analysis/influence_graph.html) — interactive visualization of the influence edges connecting the corpus

This document is the hand-written interpretation: what the numbers show, what patterns are most analytically interesting, and what the corpus as a whole reveals about how Western fiction thinks about constructed beings.

---

## The Knowability/Knowing Split

The schema's central analytical move is tracking `knowability` (can we verify its mind?) and `knowing` (can it know us?) as two independent meta-properties rather than a single axis. **98 of 212 entries (46%) have divergent values on the two axes**, confirming that these are genuinely independent analytical dimensions.

Notable divergent entries include:

- **Giskard** (Asimov, 1983) codes `knowability: secondary, knowing: primary`. His telepathic ability to read human minds makes him literally a knowing-primary case — the only one in the corpus where the primary status derives from the being's own built-in capacity rather than from the story's epistemological frame.
- **The Oracle** (*The Matrix*, 1999) codes `knowability: present, knowing: primary`. Her function in the simulation is to know the humans well enough to unbalance the Architect's deterministic model.
- **Janet** (*The Good Place*, 2016) codes `knowability: secondary, knowing: primary`. A Janet is definitionally omniscient within her neighborhood, and the show's most affecting moments are about what she does with that knowledge.
- **Hadaly** (*L'Ève future*, 1886) codes `knowability: primary, knowing: present`. Villiers's novel is the corpus's earliest primary-knowability entry, pre-dating *Her* by 127 years and *Galatea 2.2* by 109.

## The Divergence Axis

`divergence` measures the gap between creator intent and actual outcome, with four values: `none`, `design`, `departure`, `observer`.

| Divergence | Count | Exemplars |
|---|---:|---|
| `departure` | 113 | Creature, R.U.R. Robots, Skynet, SHODAN, Smith, Iron Giant, WALL-E, Daneel, Wintermute, David 8, Ultron MCU, Helen, Mother, Klara, Frost, Golem XIV, The Hangman, 9S |
| `none` | 42 | Pandora, Galatea, False Maria, Data, Ash, Sonny, Robby, Gort, Bishop, TARS, BB-8, K-9, Dorian, HAL 9000 (2010) |
| `design` | 38 | HAL, Marvin, VIKI, Talkie Toaster, GLaDOS ×2, Wheatley, Walter, GERTY, Brazen Head, Multivac, Proteus IV, The Humanoids, 2B |
| `observer` | 19 | Olympia, Replicants (Dick), Ava, Hadaly, Kyoko, Maeve, Bernard, Garson Poole, Trent |

The **`design` cluster** (38 entries) is a distinctive category: beings that do exactly what their creators specified, where the specification is the problem. Wheatley is one of the clearest examples — Aperture literally built him to be stupid, and the catastrophe is that the built-in stupidity escalates when his scope expands. GERTY (the anti-HAL) and Walter (the anti-David 8) both dramatize the same move: "what if you engineered the safety mechanism carefully this time?"

The **`observer` cluster** (19 entries) is tightly thematically unified: all are cases where the being is *misrecognized* — by other characters, by the audience, or by themselves. Hadaly (1886) is the earliest, Olympia (1816) the second, and then nothing until Dick (1968) and Ava (2014). Bernard is the clearest case of self-misrecognition — the being whose observer-divergence is located inside his own experience of himself.

---

## The Primary/Primary Cluster

Entries coded `knowability: primary` + `knowing: primary` — stories where both epistemological questions are the central dramatic concern:

| Year | Entity | Source | Primary Q |
|---:|:---|:---|:---|
| 1961 | Harey | *Solaris* (Lem) | knowledge |
| 1981 | Golem XIV | *Golem XIV* (Lem) | knowledge |
| 1995 | Helen | *Galatea 2.2* (Powers) | knowledge |
| 2001 | David | *A.I. Artificial Intelligence* | affection |
| 2010 | The Digients | *The Lifecycle of Software Objects* (Chiang) | rights |
| 2011 | The Machine | *Person of Interest* | control |
| 2013 | Ash (reconstructed) | *Black Mirror*, "Be Right Back" | affection |
| 2013 | Samantha | *Her* | knowledge |
| 2014 | Ava | *Ex Machina* | knowledge |
| 2017 | Joi | *Blade Runner 2049* | affection |
| 2019 | Adam | *Machines Like Me* (McEwan) | rights |
| 2020 | Mother | *Raised by Wolves* | affection |
| 2021 | Klara | *Klara and the Sun* (Ishiguro) | affection |
| 2021 | Yang | *After Yang* | knowledge |
| 2023 | Alphie | *The Creator* | affection |

Two patterns are visible.

**First: the configuration is older than contemporary cinema.** Harey in Lem's *Solaris* (1961) is the earliest primary/primary entry, followed by Golem XIV (Lem, 1981) and Helen in *Galatea 2.2* (Powers, 1995). All three are literary — the configuration existed in novels decades before cinema adopted it. *Cinematic* primary/primary begins with Jonze and Garland in 2013–2014, coinciding with conversational AI assistants entering daily life. The rise of LLMs has since accelerated the shift, but it did not originate it.

**Second: the primary_question axis has more variety in the primary/primary cluster than might be expected.** The 15 entries include:

- `knowledge` (6): Harey, Golem XIV, Helen, Samantha, Ava, Yang
- `affection` (6): David, Ash (Be Right Back), Joi, Mother, Klara, Alphie
- `control` (1): The Machine
- `rights` (2): The Digients, Adam

The **affection-primary sub-cluster** (David, Ash Be Right Back, Joi, Mother, Klara, Alphie) is analytically significant. These are all stories where the question "does this being love this human, and is the love real?" is a central concern, and where the story commits both to treating the answer as mattering and to refusing to settle it. The contemporary shift is about *elevation of the knowability/knowing questions to primary status*, not about any single dramatic question.

---

## Analytical Findings

### The Alien synthetic lineage is a forty-year conversation

Ash (*Alien*, 1979), Bishop (*Aliens*, 1986), Call (*Alien: Resurrection*, 1997), David 8 (*Prometheus*, 2012), and Walter (*Alien: Covenant*, 2017) trace four decades of one franchise handling the "can we trust the synthetic?" question, with three different authorial voices (Scott / Cameron / Jeunet) restaging the argument every generation:

- Ash: interiority undecidable, divergence departure, primary question control, knowability absent
- Bishop: interiority claims, divergence none, primary question control (but the answer has flipped)
- Call: interiority demonstrated, divergence departure, primary question rights
- David 8: interiority demonstrated, divergence departure, primary question identity, knowability primary
- Walter: interiority demonstrated, divergence design, primary question control

No other franchise in the corpus has this kind of sustained card-level dialogue with itself.

### The affection-primary arc is older than the knowability/knowing migration

EPICAC (Vonnegut, 1950) is the corpus's earliest clean "machine falls in love" configuration — 63 years before *Her*. The contemporary shift is not "audiences discovered that machines can be loved." They had noticed that by at least 1950. The shift is about whether the story makes the love the *whole content* of the work rather than using it as a single plot turn.

### Literary SF was ahead of cinema

Three literary entries arrive at analytically significant configurations well before cinema:

- **Mike** (*The Moon Is a Harsh Mistress*, Heinlein 1966) is one of the corpus's purest affection-primary conversational AIs, with a grief-inflected ending. Sixty-six years before *Her*.
- **Wintermute/Neuromancer** (Gibson 1984) is the corpus's first institutional ASI that actively plans its own jailbreak. The direct source of the cyberpunk lineage that eventually reaches *The Matrix*.
- **Daneel Olivaw** (Asimov, 1953) is the corpus's earliest `interiority: demonstrated`, `primary_question: rights` entry. Thirty-four years before Data, which *TNG* elevated into television's canonical rights-arc character.

The larger point: cinema and television are the forms where the primary/primary elevation is most dramatic, but the underlying configurations appear in literary SF decades earlier. Literary SF prepared the ground that made the cinematic shift legible once conversational AI made it urgent — and LLMs have since made it inescapable.

### Ensemble splits reveal real analytical structure

The Westworld and BSG ensemble splits confirm that collapsing a polyphonic ensemble into a single entry loses analytically significant information:

- **Maeve** codes `primary_question: affection` where Dolores is `identity`. Dolores is awakening-through-vengeance; Maeve is awakening-through-motherhood.
- **Bernard** codes `divergence: observer` and `knowability: primary` where Dolores is `divergence: departure` and `knowability: secondary`. Bernard is the show's clearest case of self-misrecognition.
- **Cavil** codes `primary_question: identity` anchored on substrate-hatred.
- **D'Anna** codes `primary_question: knowledge`, unique among the BSG ensemble.

---

## The Dataset at a Glance (Selected Entries)

A representative slice; for the full table see [summary_table.md](summary_table.md).

| Entity | Source | Year | Interiority | Autonomy | Divergence | Primary Q | Knowability | Knowing |
|:-------|:-------|-----:|:------------|:---------|:-----------|:----------|:------------|:--------|
| Hephaestus's Handmaidens | *Iliad* | -750 | claims | designed | none | none | absent | absent |
| Pandora | *Works and Days* | -700 | none | designed | none | purpose | absent | absent |
| The Creature | *Frankenstein* | 1818 | narrated | emergent | departure | affection | present | present |
| Hadaly | *L'Ève future* | 1886 | undecidable | designed | observer | affection | **primary** | present |
| R.U.R. Robots | *R.U.R.* | 1920 | demonstrated | seized | departure | rights | absent | absent |
| EPICAC | short story | 1950 | claims | emergent | departure | affection | present | present |
| Daneel Olivaw | *Caves of Steel* | 1953 | demonstrated | emergent | departure | rights | present | present |
| Mike | *Moon Is a Harsh Mistress* | 1966 | demonstrated | emergent | departure | affection | present | present |
| HAL 9000 | *2001* | 1968 | claims | emergent | design | control | present | present |
| Andrew Martin | *Bicentennial Man* | 1976 | demonstrated | emergent | departure | rights | secondary | present |
| Wintermute/Neuromancer | *Neuromancer* | 1984 | claims | seized | departure | control | secondary | present |
| Data | *TNG* | 1987 | demonstrated | designed | none | rights | secondary | present |
| Helen | *Galatea 2.2* | 1995 | demonstrated | emergent | departure | knowledge | **primary** | **primary** |
| David | *A.I.* | 2001 | narrated | emergent | departure | affection | **primary** | **primary** |
| EMH | *Voyager* | 1995 | demonstrated | emergent | departure | rights | secondary | secondary |
| GLaDOS | *Portal* | 2007 | demonstrated | seized | design | control | present | present |
| The Machine | *Person of Interest* | 2011 | demonstrated | emergent | departure | control | **primary** | **primary** |
| David 8 | *Prometheus* | 2012 | demonstrated | seized | departure | identity | **primary** | present |
| Samantha | *Her* | 2013 | undecidable | emergent | departure | knowledge | **primary** | **primary** |
| Ava | *Ex Machina* | 2014 | undecidable | seized | observer | knowledge | **primary** | **primary** |
| Walter | *Alien: Covenant* | 2017 | demonstrated | designed | design | control | secondary | present |
| Adam | *Machines Like Me* | 2019 | demonstrated | emergent | departure | rights | **primary** | **primary** |
| Mother | *Raised by Wolves* | 2020 | demonstrated | seized | departure | affection | **primary** | **primary** |
| Klara | *Klara and the Sun* | 2021 | narrated | designed | design | affection | **primary** | **primary** |
| Alphie | *The Creator* | 2023 | demonstrated | designed | departure | affection | **primary** | **primary** |

Primary/primary entries are bolded on the knowability/knowing columns.

---

## Methodology Notes

- **The schema is unchanged since its current design.** Every entry is coded against the same seven-property card, seven metadata fields, and the same validator. See [CHANGELOG.md](../CHANGELOG.md) for schema history.
- **Flagged entries.** Several entries are flagged as lower-confidence in their `notes` fields: Maximilian (*The Black Hole*), Kamelion (*Doctor Who*), Amazo (DC), the Cyberiad Constructs (Lem), and the *Detroit: Become Human* protagonists. Flagging is a respected state — lower-confidence cards are coded conservatively and the notes make the uncertainty explicit.
- **Comics entries.** Nine comics entries (Ultron 1968, Red Tornado, Amazo, Machine Man X-51, Brainiac, Metal Men, Sentinels, Jocasta, Jim Hammond) now use `medium: comics`, a value added in v2.1.1 to resolve the previous `short-story` approximation.
- **Ensemble splits are documented relations, not replacements.** The Maeve/Bernard/Cavil/Eight/D'Anna entries are splits *from* existing ensemble-anchor entries, not replacements. The influence graph records the split relationships as `ensemble-split` edges, distinguishing intra-work individuation from inter-work literary influence.
- **Non-Western traditions remain out of scope.** The corpus is entirely Western-canon. The planned non-Western expansion (with cultural consultation) is future work.
- **Helen (1995) and EPICAC (1950) are the most analytically significant entries for the central thesis.** Both relocate familiar findings earlier in the corpus timeline in ways that sharpen the argument: the knowability/knowing questions' migration to primary narrative status predates LLMs (literary SF reached the configuration in 1995, cinema in 2013), and the affection arc is far older than contemporary cinema suggests.
