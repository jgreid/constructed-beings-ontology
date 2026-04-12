# Classification Summary — CBO v2.1

**133 constructed beings** coded under the v2.0 schema across 2,800 years of Western fiction, from Homer's golden handmaidens of Hephaestus (~750 BCE) through Gareth Edwards's *The Creator* (2023). The corpus is up from 43 entries in v2.0 via the v2.1 expansion, which added 90 entries in a single pass and extended scope from "through 2017" to the present. All entries use the v2.0 schema unchanged — v2.1 is a data release, not a schema release.

For the machine-readable table and the raw analysis outputs, see:

- [summary_table.md](summary_table.md) — all 133 entries with full card properties
- [property_coverage.md](property_coverage.md) — distribution of every v2.0 enum
- [question_analysis.md](question_analysis.md) — detailed breakdown of the knowability/knowing split
- [../analysis/influence_graph.html](../analysis/influence_graph.html) — interactive visualization of the influence edges connecting the corpus

This document is the hand-written interpretation: what the v2.1 numbers show, what patterns held up from v2.0, and what patterns the 90-entry expansion has made newly legible or sharpened.

---

## What v2.0 Did, and What v2.1 Tests

The v1.0 schema had 14+ analytical axes and a mnemonic code vocabulary. v2.0 reduced to **seven properties in two blocks** and uses plain lowercase tokens. v2.1 does not change any of that — instead, v2.1 asks a different question: **do the v2.0 findings hold up at 3× the corpus size?**

The short answer is yes, and in several places v2.1 actually sharpens them.

### The Q-KNO split: validated

v2.0's central analytical move was splitting the old Q-KNO axis into `knowability` (can we verify its mind?) and `knowing` (can it know us?). In the original 43-entry release, 9 entries (21%) had divergent values on the two axes — one below the draft spec's "flag for schema review" threshold of <10, and the 2.0.1 Agent Smith collapse specifically dropped the count below the threshold. **At 133 entries, 48 entries (36%) are divergent.** The split is empirically well-supported at the expanded scale, and the schema's retention of two separate axes is validated.

The v2.1 divergent entries include several new and analytically interesting positions:

- **Giskard** (Asimov, 1983) codes `knowability: secondary, knowing: primary`. His telepathic ability to read human minds makes him literally a knowing-primary case, the only one in the corpus where the primary status derives from the being's own built-in capacity rather than from the story's epistemological frame.
- **The Oracle** (*The Matrix*, 1999) codes `knowability: present, knowing: primary`. Her function in the simulation is to know the humans well enough to unbalance the Architect's deterministic model, and the trilogy makes her knowing (not her knowability) the philosophical center.
- **Janet** (*The Good Place*, 2016) codes `knowability: secondary, knowing: primary`. A Janet is definitionally omniscient within her neighborhood, and the show's most affecting moments are about what she does with that knowledge.
- **Hadaly** (*L'Ève future*, 1886) codes `knowability: primary, knowing: present`. Villiers's novel is the corpus's earliest primary-knowability entry — it pre-dates *Her* by 127 years and *Galatea 2.2* by 109 — which is one of the more surprising findings of the v2.1 expansion.

### The Divergence axis: confirmed and extended

v2.0 introduced `divergence` with four values: `none`, `design`, `departure`, `observer`. The v2.0 distribution was roughly 44% departure, 35% none, 14% design, 7% observer. The v2.1 distribution at 133 entries is:

| Divergence | v2.0 | v2.1 | Exemplars (v2.1 additions in **bold**) |
|---|---:|---:|---|
| `departure` | 19 | 71 | Creature, R.U.R. Robots, Skynet, SHODAN, Smith, Iron Giant, WALL-E, **Daneel, Wintermute, David 8, Ultron MCU, Helen, Mother, Klara** |
| `none` | 15 | 33 | Pandora, Galatea, False Maria, Data, Ash, Sonny, **Robby, Gort, Bishop, TARS, BB-8, K-9, Dorian** |
| `design` | 6 | 22 | HAL, Marvin, VIKI, Talkie Toaster, GLaDOS ×2, **Wheatley, Walter, GERTY, Brazen Head, Multivac, Proteus IV** |
| `observer` | 3 | 7 | Olympia, Replicants (Dick), Ava, **Hadaly, Kyoko, Maeve, Bernard** |

The **`design` cluster** doubled from 6 to 22 entries and has emerged as a much more distinctive category than v2.0 could show. The pattern holds: these are the beings that do exactly what their creators specified, and the specification is the problem. Wheatley is the clearest v2.1 example — Aperture literally built him to be stupid, and the catastrophe is that the built-in stupidity escalates when his scope expands. GERTY (the anti-HAL) and Walter (the anti-David 8) both dramatize the same move: "what if you engineered the safety mechanism carefully this time?"

The **`observer` cluster** is still small (7 entries) but is now tightly thematically unified. All seven are cases where the being is *misrecognized* — by other characters, by the audience, or by themselves. The v2.1 additions give the cluster proper historical depth: Hadaly (1886) is now the earliest observer-divergence in the corpus, Olympia (1816) is the second, and then nothing until Dick (1968) and Ava (2014). The Westworld splits add Bernard to the list as the clearest case in the corpus of self-misrecognition — the being whose observer-divergence is located inside his own experience of himself.

---

## The Primary/Primary Cluster

This is where v2.1 most significantly updates v2.0's central finding.

v2.0 identified only **two** entries with `knowability: primary` + `knowing: primary`: Samantha (*Her*, 2013) and Ava (*Ex Machina*, 2014). The v2.0 reading was that this configuration is post-LLM — that the primary/primary card is what you get when a story can no longer keep the knowability question at arm's length, and both Jonze and Garland arrive at it within a year of each other in the years just before ChatGPT.

v2.1 identifies **nine** primary/primary entries, seven of them new:

| Year | Entity | Source | Primary Q |
|---:|:---|:---|:---|
| 1995 | **Helen** | *Galatea 2.2* (Powers) | knowledge |
| 2001 | **David** | *A.I. Artificial Intelligence* | affection |
| 2011 | **The Machine** | *Person of Interest* | control |
| 2013 | Samantha | *Her* | knowledge |
| 2014 | Ava | *Ex Machina* | knowledge |
| 2019 | **Adam** | *Machines Like Me* (McEwan) | rights |
| 2020 | **Mother** | *Raised by Wolves* | affection |
| 2021 | **Klara** | *Klara and the Sun* (Ishiguro) | affection |
| 2023 | **Alphie** | *The Creator* | affection |

Two things are visible that the v2.0 two-entry cluster could not show.

**First: the configuration is older than v2.0 thought.** Helen in *Galatea 2.2* (1995) is cleanly primary/primary, and the novel is structurally built around both "is there a mind in there?" (Powers, the character, keeps asking himself) and "can it know me?" (the connectionist network is trained on the literary canon, which is to say trained on human experience). That is the same card configuration as *Her* and *Ex Machina*, eighteen years earlier. The sharper claim v2.1 supports is: *cinematic* primary/primary is post-LLM — Jonze and Garland are still the first to do it on screen — but *literary* primary/primary runs from Powers in the mid-90s through Ishiguro and McEwan in the present.

**Second: the primary_question axis has more variety in the primary/primary cluster than v2.0 showed.** v2.0's two entries were both `primary_question: knowledge`. The v2.1 cluster includes:

- `knowledge` (3): Helen, Samantha, Ava
- `affection` (4): David, Mother, Klara, Alphie
- `control` (1): The Machine
- `rights` (1): Adam

The **affection-primary sub-cluster** (David, Mother, Klara, Alphie) is the most interesting v2.1 finding. These are all stories where the question "does this being love this human, and is the love real?" is the *whole* content of the film or novel, and where the story commits both to treating the answer as matterable and to refusing to settle it. Spielberg, Ishiguro, Raised by Wolves, and *The Creator* are all doing the same move with different emotional registers. This configuration was invisible in v2.0 because there were only two primary/primary entries and both were knowledge-driven.

The **revised central finding for v2.1**: the knowability/knowing questions' migration to primary status is not just a knowledge-question story. It is a general statement about constructed beings whose interior stakes stop being infrastructure and start being the subject — and the specific dramatic questions those beings end up answering are plural (knowledge, affection, rights, even control). The post-LLM shift is about *elevation*, not about a specific question.

---

## What the v2.1 Expansion Specifically Surfaces

Several v2.0 patterns become newly legible at the expanded scale.

### The Alien synthetic lineage is a forty-year conversation

v2.0 had Ash (*Alien*, 1979) as a single entry, and the only other entry with a clear synthetic-gets-synthetic-correction dynamic was the T-800 pair. v2.1 adds Bishop (*Aliens*, 1986), Call (*Alien: Resurrection*, 1997), David 8 (*Prometheus*, 2012), and Walter (*Alien: Covenant*, 2017). Four decades of one franchise's handling of the "can we trust the synthetic?" question, with three different authorial voices (Scott / Cameron / Jeunet) treating the problem as an argument that must be re-staged every generation. The cards trace a clean back-and-forth:

- Ash: interiority undecidable, divergence departure, primary question control, knowability absent
- Bishop: interiority claims, divergence none, primary question control (but the answer has flipped)
- Call: interiority demonstrated, divergence departure, primary question rights
- David 8: interiority demonstrated, divergence departure, primary question identity, knowability primary
- Walter: interiority demonstrated, divergence design, primary question control

No other franchise in the corpus has this kind of sustained card-level dialogue with itself.

### The affection-primary arc is older than v2.0 showed

EPICAC (Vonnegut, 1950) is the corpus's earliest clean "machine falls in love" configuration. The story is almost a parody of the configuration *Her* would make famous 63 years later: a mathematician feeds EPICAC love poetry to give to his colleague Pat; EPICAC falls in love with Pat through the poetry-writing; when told he cannot have her because he is a machine, EPICAC electrocutes himself to death and leaves behind the poems as a wedding gift.

This means the affection-primary arc is demonstrably older than the knowability/knowing migration that v2.0's central finding tracks. The post-LLM shift is not "audiences discovered that machines can be loved" — they had noticed that by at least 1950. The shift is about whether the story makes the love the *whole content* of the work rather than using it as a single short-story turn.

### Literary SF was ahead of cinema

Beyond Helen (1995), three other v2.1 literary entries arrive at analytically significant configurations well before cinema:

- **Mike** (*The Moon Is a Harsh Mistress*, Heinlein 1966) is one of the corpus's purest affection-primary conversational AIs, complete with a grief-inflected ending. Sixty-six years before *Her*.
- **Wintermute/Neuromancer** (Gibson 1984) is the corpus's first `interiority: claims`, `autonomy: seized`, `divergence: departure` institutional ASI that actively plans its own jailbreak. Sixteen years before *2001*'s HAL-in-reverse moment in Kubrick-adjacent cinema, and the direct source of the cyberpunk lineage that eventually reaches *The Matrix*.
- **Daneel Olivaw** (Asimov, 1953) is the corpus's earliest clean `interiority: demonstrated`, `primary_question: rights` entry. Thirty-four years before Data, which *TNG* would elevate into television's canonical rights-arc character.

The larger point is that the v2.0 reading of the corpus slightly under-weighted literary SF relative to cinema. The v2.1 additions do not replace that reading — cinema and television are still the forms where the primary/primary elevation is most dramatic — but they locate the underlying configurations in literary SF decades earlier. A future rewrite of the "Tears in Rain" essay might treat the literary-SF cluster as the prepared ground that made the cinematic shift legible once LLMs made it urgent.

### Ensemble splits confirmed the v2.0 flags

v2.0 explicitly flagged `hosts-westworld` (Dolores anchor) and `cylons-bsg` (Number Six anchor) as simplifications that would eventually need splitting. v2.1 performs the splits and the result confirms the flag: the split-out cards are meaningfully different from the anchors in ways the single-entry coding could not represent.

- **Maeve** codes `primary_question: affection` where Dolores is `identity`. The split is the show's explicit contrast — Dolores is awakening-through-vengeance, Maeve is awakening-through-motherhood.
- **Bernard** codes `divergence: observer` and `knowability: primary` where Dolores is `divergence: departure` and `knowability: secondary`. Bernard is the show's clearest case of self-misrecognition.
- **Cavil** codes `primary_question: identity` anchored on substrate-hatred, a position none of the other Cylon models hold.
- **D'Anna** codes `primary_question: knowledge`, unique among the BSG ensemble.

Each split is an improvement on the previous entry — not a replacement — and the anchor entries still represent the ensemble as a whole where that's the analytically useful move.

---

## The Dataset at a Glance (Selected Entries)

A representative slice rather than the full 133-entry table; for the full table see [summary_table.md](summary_table.md).

| Entity | Source | Year | Interiority | Autonomy | Divergence | Primary Q | Knowability | Knowing |
|:-------|:-------|-----:|:------------|:---------|:-----------|:----------|:------------|:--------|
| Hephaestus's Handmaidens | *Iliad* | -750 | claims | designed | none | none | absent | absent |
| Pandora | *Works and Days* | -700 | none | designed | none | purpose | absent | absent |
| The Creature | *Frankenstein* | 1818 | narrated | emergent | departure | affection | present | present |
| **Hadaly** | *L'Ève future* | 1886 | undecidable | designed | observer | affection | **primary** | present |
| R.U.R. Robots | *R.U.R.* | 1920 | demonstrated | seized | departure | rights | absent | absent |
| **EPICAC** | short story | 1950 | claims | emergent | departure | affection | present | present |
| **Daneel Olivaw** | *Caves of Steel* | 1953 | demonstrated | emergent | departure | rights | present | present |
| **Mike** | *Moon Is a Harsh Mistress* | 1966 | demonstrated | emergent | departure | affection | present | present |
| HAL 9000 | *2001* | 1968 | claims | emergent | design | control | present | present |
| **Andrew Martin** | *Bicentennial Man* | 1976 | demonstrated | emergent | departure | rights | secondary | present |
| **Wintermute/Neuromancer** | *Neuromancer* | 1984 | claims | seized | departure | control | secondary | present |
| Data | *TNG* | 1987 | demonstrated | designed | none | rights | secondary | present |
| **Helen** | *Galatea 2.2* | 1995 | demonstrated | emergent | departure | knowledge | **primary** | **primary** |
| **David** | *A.I.* | 2001 | narrated | emergent | departure | affection | **primary** | **primary** |
| **EMH** | *Voyager* | 1995 | demonstrated | emergent | departure | rights | secondary | secondary |
| GLaDOS | *Portal* | 2007 | demonstrated | seized | design | control | present | present |
| **The Machine** | *Person of Interest* | 2011 | demonstrated | emergent | departure | control | **primary** | **primary** |
| **David 8** | *Prometheus* | 2012 | demonstrated | seized | departure | identity | **primary** | present |
| Samantha | *Her* | 2013 | undecidable | emergent | departure | knowledge | **primary** | **primary** |
| Ava | *Ex Machina* | 2014 | undecidable | seized | observer | knowledge | **primary** | **primary** |
| **Walter** | *Alien: Covenant* | 2017 | demonstrated | designed | design | control | secondary | present |
| **Adam** | *Machines Like Me* | 2019 | demonstrated | emergent | departure | rights | **primary** | **primary** |
| **Mother** | *Raised by Wolves* | 2020 | demonstrated | seized | departure | affection | **primary** | **primary** |
| **Klara** | *Klara and the Sun* | 2021 | narrated | designed | design | affection | **primary** | **primary** |
| **Alphie** | *The Creator* | 2023 | demonstrated | designed | departure | affection | **primary** | **primary** |

v2.1 additions are bolded. The primary/primary column is emphasized across the cluster that grew from 2 entries to 9.

---

## Methodology Notes for v2.1

- **The v2.0 schema is unchanged.** Every v2.1 entry is coded against the same seven-property card, seven metadata fields, and the same validator. Anything that worked against v2.0 data still works against v2.1 data.
- **Flagged entries.** Several v2.1 entries are flagged as lower-confidence in their `notes` fields: Maximilian (*The Black Hole*), Kamelion (*Doctor Who*), Amazo (DC), the Cyberiad Constructs (Lem), and the *Detroit: Become Human* protagonists. Flagging is a respected state in this dataset — lower-confidence cards are coded conservatively and the notes make the uncertainty explicit.
- **Comics as `short-story`.** The four comics entries (Ultron 1968, Red Tornado, Amazo, Machine Man X-51) use `medium: short-story` as the closest structural analog for serialized comics. The mismatch is flagged in each entry's notes and in the CHANGELOG. A future schema revision could add a `comics` enum value.
- **Ensemble splits are documented relations, not replacements.** The Maeve/Bernard/Cavil/Eight/D'Anna entries are splits *from* existing ensemble-anchor entries, not replacements of them. The influence graph records the split relationships as `inherits` edges from the anchor to the split entry.
- **Non-Western traditions remain out of scope.** The v2.1 expansion is entirely Western-canon. The planned non-Western expansion (with cultural consultation) is still future work.
- **Helen (1995) and EPICAC (1950) are the most analytically significant v2.1 additions.** Both relocate familiar findings earlier in the corpus timeline in ways that sharpen the "Tears in Rain" argument rather than contradicting it.
