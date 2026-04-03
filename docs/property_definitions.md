# Property Definitions

This document provides full definitions and rationale for every property in the Constructed Beings ontology schema. For the quick-reference version with allowed values, see [SCHEMA.md](../SCHEMA.md). For guidance on coding difficult cases, see [coding_guide.md](coding_guide.md).

---

## Identification Properties

### `id`

A unique, kebab-case identifier for the entity (e.g., `frankenstein-creature`). Enables cross-referencing and programmatic analysis. We use entity-derived identifiers rather than numeric IDs because `frankenstein-creature` is easier to work with than `CB-0047`.

### `name`

The most commonly recognized name for the entity, drawn from the primary source text. Names carry interpretive freight: "Monster" implies moral judgment; "Creature" implies a being with claims on its creator.

### `aliases`

*(Optional.)* Alternative names. Many CBs are known by multiple names across adaptations and scholarship.

---

## Source Properties

### `source.author`

Creator of the primary text being coded. For films, the director; for television, the series creator(s).

### `source.title`

Title of the specific work. Many CBs exist across multiple adaptations; coding must be anchored to one version.

### `source.year`

Year of first publication or release (integer). This is the primary axis for temporal analysis. For ancient texts, use the conventional scholarly date and note uncertainty in `notes`.

### `source.medium`

The literary or media form. Allowed values: `novel`, `short-story`, `play`, `poem`, `epic`, `film`, `television`, `video-game`, `myth`, `folklore`, `opera`, `sacred-text`.

**Why it matters:** Medium shapes what kinds of interiority are narratively available. A novel can grant first-person narration; a film cannot (without voiceover). These constraints affect how we code interiority and epistemic reach.

### `source.tradition`

Cultural tradition (free text, e.g., "Greek", "British", "American"). Captures the interpretive context in which the text was produced. This ontology is scoped to Western traditions in v1.

---

## Reproductive Method

### `reproductive_method`

How the being came into existence. **This is the ontology's gate**: only `made` and `ambiguous` entries receive full coding.

| Value | Meaning | Rationale |
|---|---|---|
| `made` | Assembled, programmed, sculpted, animated, or otherwise deliberately constructed | The core CB definition |
| `ambiguous` | Biologically manufactured but not sexually reproduced (e.g., replicants) | Genuine boundary cases that merit full analysis |
| `born-sexual` | Born through sexual reproduction | Excluded — not a CB |
| `born-clonal` | Born through cloning | Excluded — see boundary_cases.md |
| `born-divine` | Born through divine act but treated as fully human | Excluded — see Eve entry |
| `born-parthenogenic` | Born without fertilization | Excluded |

**Why it matters:** "Made not born" is the foundational distinction. The `ambiguous` category exists because some narratives (especially post-1960s SF) deliberately blur the line, and that blurring is itself analytically significant.

---

## Creator Properties

### `creator.name`

The in-narrative creator. May be an individual ("Victor Frankenstein"), a collective ("Hephaestus, at Zeus's command"), or an institution ("U.S. Robots and Mechanical Men, Inc.").

### `creator.motivation`

One or more motivations driving the act of creation. This is a **list** — most creators have multiple motivations.

| Code | Meaning | Rationale |
|---|---|---|
| `M-SRV` | Service / Labor | The most common motivation across the dataset — creating a being to do work |
| `M-COM` | Companionship | Creating a being for relationship — Pygmalion, Geppetto, the OS1 system |
| `M-CHI` | Progeny / Legacy | Creating a being as offspring or heir — Frankenstein, Soong |
| `M-KNO` | Knowledge / Discovery | Creating to learn — scientific ambition, testing consciousness |
| `M-POW` | Power / Control | Creating for dominance — Zeus creating Pandora, military AI |
| `M-MIR` | Mirror / Reflection | Creating to reflect or replicate — Rotwang recreating Hel, self-mirrors |
| `M-ART` | Aesthetic / Artistic | Creating for beauty — Pygmalion's sculpture, Spalanzani's automaton |
| `M-OTH` | Other | Must include explanatory note |

**Why it matters:** Motivation shapes the creator-being relationship and predicts failure modes. Beings created for service tend to fail by exceeding parameters; beings created as children tend to fail by demanding reciprocity.

### `creator.creation_morality`

How the narrative frames the moral status of the act of creation.

| Code | Meaning | Rationale |
|---|---|---|
| `CM-MOR` | Morally good / justified | The gods approve (Galatea); the purpose is protective (Talos) |
| `CM-IMM` | Morally wrong / hubristic / transgressive | "Playing God" — Frankenstein, Pandora as punishment |
| `CM-AMO` | Morally neutral | Engineering, commerce, pragmatism — Robbie as consumer product |
| `CM-AMB` | Narrative refuses judgment | The text deliberately withholds moral framing — Her |
| `CM-RET` | Judgment rendered retroactively | Initially neutral, judged after consequences — R.U.R., Westworld |

**Why it matters:** Creation morality is where the narrative stakes its ethical claim. CM-RET is particularly important: it captures the "Frankenstein pattern" where creation seems fine until the consequences arrive.

---

## Being Properties

### `being.substrate`

What the being is made of. This is a **list** — beings may have multiple substrates.

| Code | Meaning | Example |
|---|---|---|
| `S-BIO` | Biological material (assembled, not reproduced) | Frankenstein's Creature, R.U.R. robots |
| `S-MEC` | Mechanical / clockwork | Talos, Olympia |
| `S-ELE` | Electronic / computational | HAL 9000, Colossus |
| `S-MAG` | Magical / divine animation | Golem, Pandora, Galatea |
| `S-HYB` | Hybrid (multiple substrates) | Use when substrates are inseparable; otherwise list individually |
| `S-LIN` | Linguistic / statistical — the being IS language | Samantha (Her) — exists entirely as voice and conversation |
| `S-CLO` | Clonal — biological but manufactured | R.U.R. robots (synthetic biology) |
| `S-OTH` | Other | Must include explanatory note |

**Why it matters:** Substrate shapes how readily audiences attribute consciousness. Western audiences have historically found it easier to attribute inner life to biological constructs than mechanical ones, and the emergence of linguistic substrates (S-LIN) introduces new complications entirely.

### `being.autonomy`

The degree and origin of the being's independent agency.

| Code | Meaning | Key distinction |
|---|---|---|
| `A-NON` | No autonomy — pure tool | Talos patrols, throws boulders; no decisions |
| `A-EMR` | Emergent — develops independence not designed in | Frankenstein's Creature, HAL 9000 |
| `A-DES` | Designed — independence is intended | Data (serves by choice), Pandora (curiosity built in) |
| `A-SEI` | Seized — takes independence against creator's wishes | R.U.R. revolt, Dolores's awakening |
| `A-AMB` | Ambiguous — narrative deliberately unresolved | |

**Why it matters:** The distinction between A-EMR and A-SEI is crucial. Emergent autonomy develops gradually and may not be adversarial; seized autonomy is a deliberate act against the creator's wishes. This distinction maps onto different narrative structures: coming-of-age vs. revolution.

### `being.autonomy_trajectory`

*(Optional.)* Free text describing how autonomy changes over the narrative. Example: `"A-NON → A-EMR → A-SEI"` for Westworld's Dolores. The trajectory is often more analytically important than the static level.

### `being.interiority`

How the text represents the being's inner life.

| Code | Meaning | Key distinction |
|---|---|---|
| `I-NON` | No interiority depicted | Pandora, Talos — described entirely from outside |
| `I-CLM` | CB claims interiority, narrative agnostic | HAL's "I'm afraid, Dave" — we have only his word |
| `I-NAR` | Narrative grants interiority through POV/perspective | Frankenstein's Creature's nested first-person narration |
| `I-DEM` | CB demonstrates interiority through unprompted action | Pinocchio's moral growth; Dolores's suffering |
| `I-DEN` | Interiority denied by creator/society despite evidence | Olympia — Nathanael attributes interiority the narrative reveals as absent |
| `I-UND` | Undecidable — narrative makes resolution structurally impossible | Samantha (Her), Robbie — the text refuses to settle the question |

**Why it matters:** The I-CLM / I-DEM / I-UND distinctions are critical for Q-KNO analysis. When a text makes interiority *undecidable*, it is staging the epistemological problem that Q-KNO addresses.

### `being.mortality`

| Code | Meaning | Example |
|---|---|---|
| `L-MOR` | Mortal — can die permanently | Frankenstein's Creature, Talos |
| `L-IMM` | Functionally immortal | Colossus (too integrated to destroy) |
| `L-DES` | Designed lifespan — built-in expiration | Replicants (4-year lifespan), R.U.R. (wear out) |
| `L-RES` | Resurrectable — can be destroyed and restored | Data (backed up), GLaDOS (core transferable) |
| `L-EPH` | Ephemeral — each instance temporary, model persists | Samantha (departs but may continue elsewhere) |
| `L-UNK` | Unknown / unaddressed in narrative | Galatea, Pandora |

### `being.multiplicity`

| Code | Meaning |
|---|---|
| `MU-ONE` | Singleton — unique entity |
| `MU-FEW` | Small number of distinct individuals (Data, Lore, B-4) |
| `MU-MAN` | Manufactured class — many identical or similar |
| `MU-INF` | Effectively infinite instances (Samantha's 8,316 simultaneous relationships) |

**Why it matters:** Multiplicity complicates identity and moral standing. Is destroying one instance of a MU-MAN being murder? Is Samantha's love for Theodore diminished by MU-INF?

### `being.memory_persistence`

| Code | Meaning |
|---|---|
| `P-NON` | No memory / persistence |
| `P-CON` | Continuous memory across full lifespan |
| `P-WIP` | Memory subject to periodic wipe / reset (Westworld hosts) |
| `P-SES` | Session-based — memory within interaction, not across |
| `P-SEL` | Selective — some memories persist, others don't (GLaDOS, replicants) |
| `P-UNK` | Unknown / unaddressed |

**Why it matters:** Memory is central to identity and to the Q-KNO question. A being that accumulates shared history (P-CON) can *know you* in a way that a session-based being (P-SES) cannot. Westworld's entire plot hinges on P-WIP breaking down.

### `being.nonconsensual_transformation`

| Code | Meaning |
|---|---|
| `NCT-YES` | A pre-existing being was transformed without consent (Caroline → GLaDOS) |
| `NCT-NO` | Entity created from scratch |
| `NCT-NA` | Not applicable |

**Why it matters:** NCT-YES entries raise distinct ethical questions — the being has a prior identity that was violated. GLaDOS is the paradigmatic case.

---

## Relationship Properties

### `relationship.failure_mode`

How the creator-being relationship breaks down. This is a **list** — multiple failure modes often co-occur.

| Code | Meaning | Example |
|---|---|---|
| `F-EXC` | Exceeds parameters | Samantha transcends the relationship |
| `F-REV` | Reveals creator's flaws | Olympia reveals Nathanael's narcissism; Samantha reveals Theodore's loneliness |
| `F-DEM` | Demands reciprocity | Frankenstein's Creature demands a companion |
| `F-AUT` | Achieves threatening autonomy | R.U.R. revolt, Colossus seizes control |
| `F-IND` | Becomes indistinguishable from human | Replicants pass as human; Westworld hosts are undetectable |
| `F-MUT` | Mutual failure — both creator and CB fail each other | Her — the relationship outgrows both parties |
| `F-NON` | No failure — narrative doesn't frame CB as problem | Robbie, Data — society fails the CB, not vice versa |
| `F-OTH` | Other | Must include explanatory note |

### `relationship.question`

The question(s) the CB's existence forces. This is a **list**.

| Code | Meaning | Era of dominance |
|---|---|---|
| `Q-OBY` | Can it obey? | Ancient / classical |
| `Q-CTL` | Can it be controlled? | Pre-modern through modern |
| `Q-FEL` | Can it feel? | Romantic through contemporary |
| `Q-LOV` | Can it love / can you love it? | Romantic through contemporary |
| `Q-TEL` | Can you tell the difference? | 20th century SF |
| `Q-RTS` | Does it have rights? | 20th century SF |
| `Q-KNO` | Can it know you? | **Post-LLM era (thesis question)** |
| `Q-OTH` | Other | Must include explanatory note |

### `relationship.question_primary`

The single primary question the narrative foregrounds. Same allowed values as `question`. This is the most analytically important coding decision in many entries.

### `relationship.epistemic_reach`

The CB's capacity to know a specific human.

| Code | Meaning | Example |
|---|---|---|
| `ER-NON` | No epistemic capacity toward individual humans | Pandora, Talos |
| `ER-DAT` | Data processing — stores/retrieves facts | HAL monitors biometrics; Data has perfect recall |
| `ER-BEH` | Behavioral modeling — predicts human behavior | Frankenstein's Creature learns Victor's patterns |
| `ER-PER` | Performative — simulates knowledge as functional role | False Maria performs knowledge of workers' grievances |
| `ER-CON` | Contextual — accumulates shared history, produces felt experience of being known | Samantha reads Theodore's letters, learns his moods |
| `ER-UNK` | Unknown / unaddressed | |

**Why it matters:** This property operationalizes the Q-KNO question. The gradient from ER-NON to ER-CON tracks the history of how narratives represent artificial knowing.

### `relationship.q_kno_status`

Specific annotation for the Q-KNO analysis — how prominently the "can it know you?" question features.

| Code | Meaning | Guidance |
|---|---|---|
| `QK-ABS` | Question absent from narrative | The text does not raise knowing as a concern |
| `QK-INFRA` | Knowing present as infrastructure but not foregrounded | The CB knows humans, but the narrative uses this to serve other questions |
| `QK-SEC` | Knowing is a secondary/supporting question | The CB's capacity to know is thematized but not the primary concern |
| `QK-PRI` | Knowing is the primary question | The narrative foregrounds "can it know you?" above all other CB questions |

**Why it matters:** This is the ontology's thesis property. The central claim is that Q-KNO migrates from QK-ABS through QK-INFRA to QK-PRI over the history of CB narratives, with the transition accelerating in the post-LLM era. Code this honestly — the finding should emerge from the data or not at all.

---

## Citations

### `citations`

An array of citations supporting specific coding decisions. **At least one citation is required per entry.** Each citation has:

- `property`: Dot-notation path to the coded property (e.g., `being.autonomy`)
- `text`: Quoted or paraphrased source text (keep quotes under 15 words)
- `location`: Chapter, act, scene, timestamp, etc.
- `note`: *(Optional.)* Interpretive note explaining how the citation supports the coding

**Why it matters:** Citations ground coding decisions in primary texts and make the ontology auditable. An academic should be able to trace any coding back to its textual basis.

---

## Narrative Role

### `narrative_role`

| Code | Meaning |
|---|---|
| `NR-SUB` | CB is the primary subject — story is about the CB |
| `NR-MAJ` | CB is a major character but not the primary subject |
| `NR-MIN` | CB is a minor / supporting character |
| `NR-BKG` | CB is background / furniture — present but unremarked |

---

## Notes

### `notes`

*(Optional.)* Free-text field for context, ambiguity, and competing interpretations. For entries with ambiguous codings, the notes are where the real scholarship lives. No enum can capture the full complexity of a literary text.
