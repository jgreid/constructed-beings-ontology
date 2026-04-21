# Classification Summary

**405 constructed beings** coded under the current schema across 2,800 years of fiction, from Homer's golden handmaidens of Hephaestus (~750 BCE) through Bong Joon-ho's *Mickey 17*, the Russo brothers' *The Electric State*, and *Tron: Ares* (2025), with stage works from W.S. Gilbert's *Pygmalion and Galatea* (1871) and Stravinsky/Fokine's *Petrushka* (1911) through *Maybe Happy Ending* (Broadway, 2024). The corpus spans mass-culture schlock (*Robot Monster*, 1953; *Chopping Mall*, 1986), horror-doll canon (Chucky, Annabelle, the Toulon puppets), Western-consumed anime (Lain, Chi, Vivy, Rouge), and post-ChatGPT AI imaginaries (the Entity, AIA, Sunny, Mrs. Davis). Release v2.4.4 completed a canonical-gap repair (+77 entries covering classical automata, Golden-Age SF shorts, Toy Story, expanded Star Trek, and anime), and v2.4.5 ran a self-audit that retracted 4 entries and corrected 6 codings without a schema change.

For the machine-readable table and the raw analysis outputs, see:

- [summary_table.md](summary_table.md) — all 405 entries with full card properties
- [property_coverage.md](property_coverage.md) — distribution of every schema enum
- [question_analysis.md](question_analysis.md) — detailed breakdown of the knowability/knowing split
- [../analysis/influence_graph.html](../analysis/influence_graph.html) — interactive visualization of the influence edges connecting the corpus

This document is the hand-written interpretation: what the numbers show, what patterns are most analytically interesting, and what the corpus as a whole reveals about how Western fiction thinks about constructed beings.

---

## The Knowability/Knowing Split

The schema's central analytical move is tracking `knowability` (can we verify its mind?) and `knowing` (can it know us?) as two independent meta-properties rather than a single axis. **210 of 405 entries (52%) have divergent values on the two axes**, confirming that these are genuinely independent analytical dimensions. The divergence rate has stabilized across the v2.4 expansion releases (v2.0: 21%; v2.1: 36%; v2.2: 47%; v2.4: 51%; v2.4.3: 53%; v2.4.5: 52%) — the split's analytical structure has been confirmed with each expansion, and the rate is now holding as the corpus broadens.

Notable divergent entries include:

- **Giskard** (Asimov, 1983) codes `knowability: secondary, knowing: primary`. His telepathic ability to read human minds makes him literally a knowing-primary case — the only one in the corpus where the primary status derives from the being's own built-in capacity rather than from the story's epistemological frame.
- **The Oracle** (*The Matrix*, 1999) codes `knowability: present, knowing: primary`. Her function in the simulation is to know the humans well enough to unbalance the Architect's deterministic model.
- **Janet** (*The Good Place*, 2016) codes `knowability: secondary, knowing: primary`. A Janet is definitionally omniscient within her neighborhood, and the show's most affecting moments are about what she does with that knowledge.
- **Hadaly** (*L'Ève future*, 1886) codes `knowability: primary, knowing: present`. Villiers's novel is the corpus's earliest primary-knowability entry, pre-dating *Her* by 127 years and *Galatea 2.2* by 109.

## The Divergence Axis

`divergence` measures the gap between creator intent and actual outcome, with four values: `none`, `design`, `departure`, `observer`.

| Divergence | Count | Exemplars |
|---|---:|---|
| `departure` | 196 | Creature, R.U.R. Robots, Skynet, SHODAN, Smith, Iron Giant, WALL-E, Daneel, Wintermute, David 8, Ultron MCU, Helen, Mother, Klara, Frost, Golem XIV, The Hangman, 9S, Petrushka, Niska, Dolores, AIDA, Max 404, Edgar, Ulysses, Chucky, Toulon's Puppets, SID 6.7, Stitchpunks, Pilgrims, STEM, Jung_E, Mickey 17, Ares, the Entity, AIA |
| `none` | 56 | Pandora, Galatea, False Maria, Data, Ash, Sonny, Robby, Gort, Bishop, TARS, BB-8, K-9, Dorian, HAL 9000 (2010), Huyang, Alpha Hatsuseno, Bubo, Isla |
| `design` | 52 | HAL, Marvin, VIKI, Talkie Toaster, GLaDOS ×2, Wheatley, Walter, GERTY, Brazen Head, Multivac, Proteus IV, The Humanoids, 2B, Robot Santa, Butter Robot, Mr. Meeseeks, Arthur (After the Blast), Gog, Protectors (Chopping Mall), M.A.R.K. 13, Educators (Class of 1999), Gunslinger (1973), Devs Machine |
| `observer` | 28 | Olympia, Coppélia, Olimpia, Hadaly, Replicants (Dick), Ava, Kyoko, Maeve, Bernard, Garson Poole, Trent, the Sons (A Number), the Cleon Dynasty, Walter Prime, Mrs. Davis, Iris (*Companion*) |

The **`design` cluster** (52 entries, +9 since v2.4) is a distinctive category: beings that do exactly what their creators specified, where the specification is the problem. Wheatley is one of the clearest examples — Aperture literally built him to be stupid, and the catastrophe is that the built-in stupidity escalates when his scope expands. The v2.4.2 schlock-cinema expansion adds the cluster's clearest B-movie instances (Gog, the Protectors in *Chopping Mall*, M.A.R.K. 13, the DRB Educators, the *Westworld* 1973 Gunslinger) — all beings doing exactly what they were built to do at catastrophic scale, which is the design cluster's defining structure.

The **`observer` cluster** (28 entries) is tightly thematically unified: all are cases where the being is *misrecognized* — by other characters, by the audience, or by themselves. Hadaly (1886) is the earliest 19th-century entry, Olympia (1816) and Coppélia (1870) frame the cluster's pre-1900 footprint, and Iris from *Companion* (2025) joins as the cluster's most recent addition — the constructed-being who discovers she has been misrecognizing herself all along.

---

## The Primary/Primary Cluster

Entries coded `knowability: primary` + `knowing: primary` — stories where both epistemological questions are the central dramatic concern:

| Year | Entity | Source | Primary Q |
|---:|:---|:---|:---|
| 1961 | Harey | *Solaris* (Lem) | knowledge |
| 1981 | Golem XIV | *Golem XIV* (Lem) | knowledge |
| 1995 | Helen | *Galatea 2.2* (Powers) | knowledge |
| 1998 | Lain | *Serial Experiments Lain* | identity |
| 2001 | David | *A.I. Artificial Intelligence* | affection |
| 2003 | Atom | *Pluto* (Urasawa) | identity |
| 2010 | The Digients | *The Lifecycle of Software Objects* (Chiang) | rights |
| 2011 | The Machine | *Person of Interest* | control |
| 2013 | Ash (reconstructed) | *Black Mirror*, "Be Right Back" | affection |
| 2013 | Samantha | *Her* | knowledge |
| 2014 | Ava | *Ex Machina* | knowledge |
| 2014 | Walter (Prime) | *Marjorie Prime* (play) | identity |
| 2016 | Dolores | *Westworld* | rights |
| 2017 | Joi | *Blade Runner 2049* | affection |
| 2017 | Walter (Prime, film) | *Marjorie Prime* (Almereyda film) | identity |
| 2018 | Lacia | *Beatless* | control |
| 2019 | Adam | *Machines Like Me* (McEwan) | rights |
| 2020 | J1, J2, J3 | *Archive* | identity |
| 2020 | Mother | *Raised by Wolves* | affection |
| 2020 | The Devs Machine | *Devs* | knowledge |
| 2021 | Klara | *Klara and the Sun* (Ishiguro) | affection |
| 2021 | Yang | *After Yang* | knowledge |
| 2023 | Alphie | *The Creator* | affection |
| 2023 | Mrs. Davis | *Mrs. Davis* | control |
| 2023 | The Entity | *M:I — Dead Reckoning / Final Reckoning* | control |
| 2024 | AIA | *Afraid* | control |
| 2025 | Mickey 17 | *Mickey 17* | identity |

Four patterns are visible.

**First: the configuration is older than contemporary cinema.** Harey in Lem's *Solaris* (1961) is the earliest primary/primary entry, followed by Golem XIV (Lem, 1981) and Helen in *Galatea 2.2* (Powers, 1995). All three are literary — the configuration existed in novels decades before cinema adopted it. *Cinematic* primary/primary begins with Jonze and Garland in 2013–2014, coinciding with conversational AI assistants entering daily life. The rise of LLMs has since accelerated the shift, but it did not originate it.

**Second: anime has been inside the primary/primary cluster since 1998.** The v2.4.2 anime expansion reveals that *Serial Experiments Lain* (1998) is the earliest screen-medium primary/primary entry in the corpus — fifteen years before *Her* and *Ex Machina*. Urasawa's *Pluto* (2003) follows, and *Beatless* (2018) adds the first `primary_question: control` anime case. Japanese SF animation was doing primary/primary work a generation before Western cinema caught up to it.

**Third: the control sub-cluster is the 2023–2024 growth area.** *Mrs. Davis* (2023), *The Entity* (2023/2025), and *AIA* (2024) all code `primary_question: control` at primary/primary. This is the post-LLM cultural cluster: mass audiences now treat AI-as-geopolitical-actor as the live analytical question, and the films that stage it do so at maximum knowability/knowing intensity. The *Entity* entry is the most culturally-prominent single instance, but the pattern is visible across three distinct 2023–24 properties — an emerging register, not a one-off.

**Fourth: the primary_question axis spans seven of eight possible values inside the primary/primary cluster.** The 27 entries include:

- `knowledge` (7): Harey, Golem XIV, Helen, Samantha, Ava, Yang, Devs Machine
- `affection` (7): David, Ash (Be Right Back), Joi, Mother, Klara, Alphie, (none new from v2.4.3)
- `identity` (6): Lain, Atom (Pluto), Walter Prime (play), Walter Prime (film), J1/J2/J3, Mickey 17
- `rights` (3): The Digients, Adam, Dolores
- `control` (4): The Machine, Mrs. Davis, The Entity, AIA
- (plus Lacia, control, 2018)

The **identity-primary sub-cluster** is the v2.4.2/2.4.3 growth area and has now matched the affection-primary cluster in size. The contemporary shift is about *elevation of the identity question to primary/primary intensity*, which Lain (1998) and Pluto (2003) anticipated in anime before Western cinema arrived there.

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

### Theater is the corpus's longest medium-bridge

The v2.4 stage-works expansion makes the corpus's longest direct lineage between two stage works traceable: 422 years from Robert Greene's *Friar Bacon and Friar Bungay* (1589, the Brazen Head) to Robert Askins's *Hand to God* (2011, Tyrone). Both are coded with `interiority` in the `claims`/`undecidable` cluster and `primary_question: identity`. The Brazen Head's prophetic utterances and Tyrone's unresolved animation are the same dramatic move staged in early-modern English and contemporary American idioms.

The Coppélia → Petrushka → R.U.R. lineage (1870 → 1911 → 1920) traces the puppet-with-soul tradition end to end. Coppélia codes `interiority: none` (she is unambiguously a doll); Petrushka codes `interiority: demonstrated` (he is unambiguously a soul); the R.U.R. Robots inherit Petrushka's interiority and elevate it to species-level rebellion. The 41 years between Coppélia and Petrushka contain ballet's discovery that the puppet-with-soul is a richer subject than the soul-mistaken-for-puppet.

### The post-Siri/Alexa cluster is now visible in serial TV as well as film

The v2.4 expansion confirms what v2.3 left implicit: post-2011 TV is where the constructed-being question is being most actively staged. Mrs. Davis (2023) joins *Person of Interest*'s Machine and Samaritan as a benevolent-surveillance LLM-shaped entity; the Cleon Dynasty (2021–) joins *Foundation*'s Demerzel as the dynastic-clone-identity case; *Lower Decks*'s AGIMUS, Badgey, and Peanut Hamper (2020–24) constitute the corpus's first explicit comedic engagement with the TOS evil-computer tradition as canon. The "post-Siri/Alexa cluster" is no longer a film-only phenomenon — serial TV has acquired the patience to stage these questions across multiple seasons.

### `undecidable` interiority now clusters around the post-LLM register

The v2.4.3 expansion brings the corpus's `undecidable` interiority count to 28, and the cluster is no longer a set of isolated philosophical outliers. The 2023–2025 additions — the Entity (*Mission: Impossible*), Regus Patoff (*The Consultant*), Lacia (*Beatless*), Iris (*Companion*) — share a specific structural pattern: the work deliberately refuses audience grounds to adjudicate whether the being experiences. This is the schema's response to a cultural register that has shifted since ChatGPT's public availability: "can we tell the difference between simulation and experience" has moved from an academic thought experiment to a live public question, and the films/series that stage it now decline to settle it. The cluster includes Hoffmann's Olympia (1816), Villiers's Hadaly (1886), Lang's False Maria (1927) — `undecidable` has always been available — but the density of 2013–2025 additions (Samantha, Ava, Her, Ash Be Right Back, Real Steel, Hand to God, Screamers, Lacia, Entity, Patoff, Iris, Companion) constitutes a distinct contemporary pattern worth analytical attention.

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
| Lain | *Serial Experiments Lain* | 1998 | demonstrated | seized | departure | identity | **primary** | **primary** |
| Chi | *Chobits* | 2001 | demonstrated | seized | departure | affection | **primary** | present |
| Atom | *Pluto* (Urasawa) | 2003 | demonstrated | seized | departure | identity | **primary** | **primary** |
| Sharon Apple | *Macross Plus* | 1994 | demonstrated | seized | departure | affection | **primary** | present |
| Jung_E | *Jung_E* | 2023 | demonstrated | seized | departure | identity | **primary** | present |
| Mrs. Davis | *Mrs. Davis* | 2023 | demonstrated | seized | observer | control | **primary** | **primary** |
| The Entity | *M:I — Dead Reckoning* | 2023 | undecidable | seized | departure | control | **primary** | **primary** |
| AIA | *Afraid* | 2024 | demonstrated | seized | departure | control | **primary** | **primary** |
| Mickey 17 | *Mickey 17* | 2025 | demonstrated | seized | departure | identity | **primary** | **primary** |

Primary/primary entries are bolded on the knowability/knowing columns.

---

## Methodology Notes

- **The schema's seven analytical card properties are unchanged since v2.0.** Every entry is coded against the same seven-property card and the same validator. The `metadata.medium` enum has been incrementally expanded (v2.1.1 added `comics`; v2.4 added `opera`, `ballet`, `musical`); these are non-breaking enum additions. See [CHANGELOG.md](../CHANGELOG.md) for schema history.
- **Flagged entries.** Several entries are flagged as lower-confidence in their `notes` fields: Maximilian (*The Black Hole*), Kamelion (*Doctor Who*), Amazo (DC), the Cyberiad Constructs (Lem), the *Detroit: Become Human* protagonists, and the 2025 entries Companion and M3GAN 2.0. Flagging is a respected state — lower-confidence cards are coded conservatively and the notes make the uncertainty explicit.
- **Comics entries.** Nine comics entries (Ultron 1968, Red Tornado, Amazo, Machine Man X-51, Brainiac, Metal Men, Sentinels, Jocasta, Jim Hammond) now use `medium: comics`, a value added in v2.1.1 to resolve the previous `short-story` approximation.
- **Ensemble splits are documented relations, not replacements.** The Maeve/Bernard/Cavil/Eight/D'Anna entries are splits *from* existing ensemble-anchor entries, not replacements. The influence graph records the split relationships as `ensemble-split` edges, distinguishing intra-work individuation from inter-work literary influence.
- **Anime/manga expansion (v2.4.2).** The corpus now includes 20+ anime and manga entries spanning 1952–2024 (Tezuka's Astro Boy through Urasawa's *Pluto*, *Lain*, *Chobits*, *Beatless*, *Vivy*, *Metallic Rouge*, etc.) reflecting works widely consumed in Western markets. The `out-of-scope` exclusion in `data/exclusions.yaml` was revised in v2.4.2 to formalize this scope opening. Non-Western texts without substantial Western distribution remain out-of-scope pending consultation.
- **Horror-doll lineage (v2.4.2).** Seven entries cover the magically-animated-artifact horror tradition (Chucky, Toulon's Puppets, Obelisk Dolls, Demonic Toys, Billy, Annabelle, Slappy), all coded with substrate `[magical, mechanical]` consistent with the Prague Golem and Tyrone. This admits the horror-doll subgenre as legitimate constructed beings rather than eliding the category.
- **Schlock/B-movie coverage (v2.4.2).** Thirty entries covering low-budget and direct-to-video SF cinema across seven decades (Ro-Man 1953 through Subservience 2024) repair a previously-acknowledged thin spot.
- **Bad-TV sidekicks (v2.4.3).** Ten pre-1990s TV android entries (Hymie, Rhoda Miller, Fembots, Yoyo, Muffit II, Andy, Dr. Theopolis, Automan & Cursor, Eve Edison, Maximillion) repair the pre-1990 American-network-TV android slot.
- **Post-ChatGPT streaming/cinema (v2.4.3).** Nine entries covering the 2020–2025 cultural shift in AI depiction (Devs Machine, The Entity, AIA, Sunny, Regus Patoff, Cosmo, Mickey 17, Ares, Rouge Redstar).
- **Canonical-gap repair (v2.4.4).** 77 entries added to close acknowledged gaps in the canon: classical automata (Celedones, Pygmalion-adjacent), the Golden-Age SF short-story chassis (Asimov's positronic shorts including Cutie/Speedy/Herbie, del Rey's Helen O'Loy, Bradbury's Mechanical Hound and Electric Grandmother, Vonnegut's Salo, Dick's Impostor and Second Variety), the Toy Story franchise (Woody/Buzz/Forky), expanded Star Trek (the Questor Tapes precursor, Moriarty, Zora, Chopper), additional anime, and several video-game entries (Weapon, NieR individuations). No schema change.
- **Self-audit (v2.4.5).** Four entries added in v2.4.4 were retracted to `data/exclusions.yaml` on scope grounds (Alphonse Elric as born-then-modified; Hayt as a boundary-deferred cloned-body-plus-conditioning case; the Khalkotauroi as within-source collective; Doraemon as failing the Western-distribution test), and six coding errors in v2.4.4 entries were corrected. No entries added; no schema change. See CHANGELOG.md for the full retraction rationale.
- **Harey (1961), Golem XIV (1981), Helen (1995), and EPICAC (1950) are the most analytically significant entries for the central thesis.** They relocate familiar findings earlier in the corpus timeline: the knowability/knowing questions' migration to primary narrative status begins with Lem in 1961, not with cinema in 2013. The affection arc (EPICAC, 1950) is far older than contemporary cinema suggests. Literary SF — particularly Polish literary SF — reached the primary/primary configuration decades before cinema.
