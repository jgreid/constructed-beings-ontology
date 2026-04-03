# Schema Reference

This document is the human-readable companion to `schema/cb-schema.yaml`. It defines every property, its type, allowed values, and the meaning of each enumerated code. For the rationale behind each property -- *why* it is in the schema -- see [docs/property_definitions.md](docs/property_definitions.md).

---

## Entry Structure

Each constructed being is stored as a single YAML file in `data/beings/`. The top-level structure is:

```
id
name
aliases          (optional)
source           (object)
reproductive_method
creator          (object)
being            (object)
relationship     (object)
narrative_role
citations        (array)
notes            (optional)
```

All properties are **required** unless marked as optional.

---

## Properties

### `id`

| | |
|---|---|
| **Type** | `string` |
| **Format** | kebab-case (lowercase, hyphens, no spaces) |
| **Required** | Yes |
| **Example** | `frankenstein-creature` |

A unique identifier for the entity. Used as the filename (without extension) and for cross-references.

---

### `name`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `The Creature` |

The most commonly used name for the entity. Where multiple names exist, prefer the name used in the primary source text.

---

### `aliases`

| | |
|---|---|
| **Type** | `list` of `string` |
| **Required** | No (optional) |
| **Example** | `["Frankenstein's Monster", "The Wretch", "The Daemon"]` |

Alternative names or titles by which the entity is known.

---

## `source` (object)

Metadata about the work in which the entity appears. This is a **nested object**, not a flat field.

### `source.author`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `Mary Shelley` |

Author or originator of the source work.

### `source.title`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `Frankenstein; or, The Modern Prometheus` |

Title of the source work.

### `source.year`

| | |
|---|---|
| **Type** | `integer` |
| **Required** | Yes |
| **Example** | `1818` |

Year of first publication or release. Negative values indicate BCE.

### `source.medium`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Literary or media form of the source work.

| Value | Meaning |
|---|---|
| `novel` | Novel |
| `short-story` | Short story |
| `play` | Play / drama |
| `poem` | Poem |
| `epic` | Epic (long-form verse narrative) |
| `film` | Film |
| `television` | Television series |
| `video-game` | Video game |
| `myth` | Myth |
| `folklore` | Folklore |
| `opera` | Opera |
| `sacred-text` | Sacred or religious text |

### `source.tradition`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `British` |

Cultural or literary tradition to which the source text belongs (free text, e.g. "Western", "Greek", "Jewish", "British").

---

## `reproductive_method`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

How the being came into existence. For constructed beings, the value is almost always `made`; the `born-*` values exist for completeness.

| Value | Meaning |
|---|---|
| `made` | Artificially constructed, assembled, or manufactured |
| `born-sexual` | Born through sexual reproduction |
| `born-clonal` | Born through cloning |
| `born-parthenogenic` | Born through parthenogenesis |
| `born-divine` | Born through divine act |
| `ambiguous` | Origin method is unclear or contested |

---

## `creator` (object)

Information about the in-narrative creator of the being.

### `creator.name`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `Victor Frankenstein` |

Name of the in-narrative creator.

### `creator.motivation`

| | |
|---|---|
| **Type** | `list` of `enum` (min 1 item) |
| **Required** | Yes |

One or more motivations driving the creator. Multiple values are allowed.

| Code | Mnemonic | Meaning |
|---|---|---|
| `M-SRV` | Service | Service / labor / utility |
| `M-COM` | Companionship | Companionship |
| `M-CHI` | Child | Desire for progeny / legacy |
| `M-KNO` | Knowledge | Pursuit of knowledge / discovery |
| `M-POW` | Power | Pursuit of power / control |
| `M-MIR` | Mirror | Miracle / divine act / reflection |
| `M-ART` | Artistic | Aesthetic or artistic creation |
| `M-OTH` | Other | Other motivation |

### `creator.creation_morality`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Moral framing of the act of creation within the narrative.

| Code | Mnemonic | Meaning |
|---|---|---|
| `CM-MOR` | Moral | The act of creation is framed as morally good or sanctioned |
| `CM-IMM` | Immoral | The act is framed as morally wrong, transgressive, or hubristic |
| `CM-AMO` | Amoral | The act is framed as morally neutral |
| `CM-AMB` | Ambiguous | The narrative refuses clear moral judgment |
| `CM-RET` | Retroactive | Moral judgment is applied retroactively, after consequences unfold |

---

## `being` (object)

Properties of the constructed being itself.

### `being.substrate`

| | |
|---|---|
| **Type** | `list` of `enum` (min 1 item) |
| **Required** | Yes |

Physical or metaphysical substrate(s) of the being. Multiple values are allowed for hybrid beings.

| Code | Mnemonic | Meaning |
|---|---|---|
| `S-BIO` | Biological | Organic tissue -- grown, assembled, or sculpted from flesh |
| `S-MEC` | Mechanical | Metal, clockwork, gears, electromechanical parts |
| `S-ELE` | Electronic | Software, code, neural networks, or purely computational substrates |
| `S-MAG` | Magical | Animated by supernatural means -- enchantment, divine breath, necromancy |
| `S-HYB` | Hybrid | Explicitly combines two or more substrate types |
| `S-LIN` | Linguistic | Linguistic or statistical -- word-based animation |
| `S-CLO` | Clonal | Cloned biological material |
| `S-OTH` | Other | Substrate not captured above |

### `being.autonomy`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Degree and origin of the being's autonomous agency.

| Code | Mnemonic | Meaning |
|---|---|---|
| `A-NON` | None | No independent will; follows instructions without deviation |
| `A-EMR` | Emergent | Develops autonomy beyond original design; partial, unstable, or contested |
| `A-DES` | Designed | Autonomy is an intentional feature of the being's design |
| `A-SEI` | Seized | The being seizes or claims autonomy against the creator's intent |
| `A-AMB` | Ambiguous | The text is genuinely indeterminate about the being's autonomy |

### `being.autonomy_trajectory`

| | |
|---|---|
| **Type** | `string` |
| **Required** | No (optional) |

Free-text note on how the being's autonomy changes over the narrative arc.

### `being.interiority`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

How the text represents the being's inner life (subjective experience, consciousness).

| Code | Mnemonic | Meaning |
|---|---|---|
| `I-NON` | None | No interiority depicted; the being is presented as purely mechanistic |
| `I-CLM` | Claims | The being claims interiority, but it is unverified by the narrative |
| `I-NAR` | Narrated | Narrative grants interiority via point-of-view access |
| `I-DEM` | Demonstrated | Interiority is demonstrated through action and behavior |
| `I-DEN` | Denied | Interiority is denied by the narrative despite evidence |
| `I-UND` | Undecidable | The text leaves the question of interiority deliberately unresolved |

### `being.mortality`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Mortality status or fate of the being.

| Code | Mnemonic | Meaning |
|---|---|---|
| `L-MOR` | Mortal | The being is mortal; its body is destructible and death is final |
| `L-IMM` | Immortal | The being is immortal or functionally undying |
| `L-DES` | Designed lifespan | The being has a designed lifespan or expiration date |
| `L-RES` | Resurrectable | The being can be resurrected, rebooted, or restored after death |
| `L-EPH` | Ephemeral | The being is short-lived by design |
| `L-UNK` | Unknown | Mortality status is unknown or unaddressed |

### `being.multiplicity`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Whether the being is singular or one of many.

| Code | Mnemonic | Meaning |
|---|---|---|
| `MU-ONE` | One | Unique individual |
| `MU-FEW` | Few | Small number of copies |
| `MU-MAN` | Many | Many copies |
| `MU-INF` | Infinite | Infinite or unbounded copies |

### `being.memory_persistence`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

How the being's memories persist across time.

| Code | Mnemonic | Meaning |
|---|---|---|
| `P-NON` | None | No persistent memory |
| `P-CON` | Continuous | Continuous, unbroken memory |
| `P-WIP` | Wiped | Memory subject to wipes or resets |
| `P-SES` | Session | Session-based memory only |
| `P-SEL` | Selective | Selective memory -- some memories persist, others do not |
| `P-UNK` | Unknown | Memory persistence is unknown or unaddressed |

### `being.nonconsensual_transformation`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Whether the being underwent transformation without consent (e.g., a living person converted into a constructed being against their will).

| Code | Mnemonic | Meaning |
|---|---|---|
| `NCT-YES` | Yes | The being was transformed without consent |
| `NCT-NO` | No | No nonconsensual transformation |
| `NCT-NA` | Not applicable | Not applicable (e.g., the being was never a living person) |

---

## `relationship` (object)

Properties describing the creator-being relationship and the narrative questions it raises.

### `relationship.failure_mode`

| | |
|---|---|
| **Type** | `list` of `enum` (min 1 item) |
| **Required** | Yes |

How the creator-being relationship breaks down (if it does). Multiple values are allowed.

| Code | Mnemonic | Meaning |
|---|---|---|
| `F-EXC` | Exceeds | The being exceeds its intended parameters |
| `F-REV` | Reveals | The being reveals the creator's flaws |
| `F-DEM` | Demands | The being demands reciprocity or recognition |
| `F-AUT` | Autonomy | The being achieves an autonomy the creator finds threatening |
| `F-IND` | Indistinguishable | The being becomes indistinguishable from human |
| `F-MUT` | Mutual | Mutual failure or mutual destruction |
| `F-NON` | None | No failure -- the relationship remains intact |
| `F-OTH` | Other | Other failure mode |

### `relationship.question`

| | |
|---|---|
| **Type** | `list` of `enum` (min 1 item) |
| **Required** | Yes |

Central questions the narrative raises about the being. Multiple values are allowed.

| Code | Mnemonic | Meaning |
|---|---|---|
| `Q-OBY` | Obedience | Should the being obey? |
| `Q-CTL` | Control | Can the being be controlled? |
| `Q-FEL` | Fellow-feeling | Does the being have genuine feelings / empathy? |
| `Q-LOV` | Love | Can the being love or be loved? |
| `Q-TEL` | Telos | What is the being's purpose? |
| `Q-RTS` | Rights | Does the being have rights? |
| `Q-KNO` | Knowledge | Can we know the being's inner state? (Epistemic question) |
| `Q-OTH` | Other | Other question |

### `relationship.question_primary`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

The single most central question from the `question` list. Uses the same codes as `relationship.question`.

### `relationship.epistemic_reach`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

How much access the narrative gives into the being's mind.

| Code | Mnemonic | Meaning |
|---|---|---|
| `ER-NON` | None | No epistemic access to the being's inner state |
| `ER-DAT` | Data | Data or outputs only |
| `ER-BEH` | Behavioral | Observable behavior -- the being is read through its actions |
| `ER-PER` | Perceptual | Perceptual access -- the narrative shows the being's sensory experience |
| `ER-CON` | Consciousness | Full consciousness access -- the narrative enters the being's mind |
| `ER-UNK` | Unknown | Epistemic reach is unknown or unaddressed |

### `relationship.q_kno_status`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Prominence of the knowledge/epistemics question (Q-KNO) in the narrative.

| Code | Mnemonic | Meaning |
|---|---|---|
| `QK-ABS` | Absent | The knowledge question is not raised |
| `QK-INFRA` | Infrastructural | The question is present and generates tension, but serves other narrative purposes |
| `QK-SEC` | Secondary | The question is raised but is not the central concern |
| `QK-PRI` | Primary | The knowledge question is the central dramatic or thematic concern |

---

## `narrative_role`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Prominence of the constructed being in the source narrative.

| Code | Mnemonic | Meaning |
|---|---|---|
| `NR-SUB` | Subject | Subject or protagonist of the narrative |
| `NR-MAJ` | Major | Major character |
| `NR-MIN` | Minor | Minor character |
| `NR-BKG` | Background | Background or world-building element |

---

## `citations` (array)

| | |
|---|---|
| **Type** | `list` of `object` (min 1 item) |
| **Required** | Yes |

An array of textual citations supporting the coding decisions. Each citation is an object with the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `property` | `string` | Yes | Dot-notation path to the property being cited (e.g. `being.autonomy`, `creator.motivation`) |
| `text` | `string` | Yes | Short quotation or paraphrase from the source (keep under 15 words) |
| `location` | `string` | Yes | Chapter, page, timestamp, or other locator in the source |
| `note` | `string` | No | Optional explanatory note on how the citation supports the coding |

---

## `notes`

| | |
|---|---|
| **Type** | `string` |
| **Required** | No (optional) |

Free-form editorial or analytical notes. Use YAML block scalar syntax (`>` or `|`) for multi-line text. This field is especially important for entries where one or more properties are coded with ambiguous values -- use it to explain *why* the ambiguity exists and what competing readings are in play.

---

## Worked Example

The following is the complete entry for the Creature from *Frankenstein* (`data/beings/frankenstein-creature.yaml`):

```yaml
id: frankenstein-creature
name: "The Creature"
aliases:
  - "Frankenstein's Monster"
  - "The Wretch"
  - "The Daemon"
  - "Adam"

source:
  author: "Mary Shelley"
  title: "Frankenstein; or, The Modern Prometheus"
  year: 1818
  medium: novel
  tradition: British

reproductive_method: made

creator:
  name: "Victor Frankenstein"
  motivation:
    - M-KNO
    - M-CHI
    - M-POW
  creation_morality: CM-RET

being:
  substrate:
    - S-BIO
  autonomy: A-EMR
  autonomy_trajectory: >
    The Creature progresses from helpless newborn-like confusion to independent
    language-learner to moral philosopher to deliberate antagonist. Each stage
    is shaped by experience (especially rejection), not by design. His autonomy
    grows in direct proportion to Victor's abandonment.
  interiority: I-NAR
  mortality: L-MOR
  multiplicity: MU-ONE
  memory_persistence: P-CON
  nonconsensual_transformation: NCT-NO

relationship:
  failure_mode:
    - F-DEM
    - F-REV
    - F-AUT
  question:
    - Q-FEL
    - Q-RTS
    - Q-LOV
  question_primary: Q-FEL
  epistemic_reach: ER-BEH
  q_kno_status: QK-INFRA

narrative_role: NR-SUB

citations:
  - property: creator.motivation
    text: "A new species would bless me as its creator and source"
    location: "Volume I, Chapter 4"
    note: "Victor's godlike ambition — supports M-CHI and M-POW coding."

  - property: being.interiority
    text: "I am malicious because I am miserable"
    location: "Volume II, Chapter 9 (Creature's narrative)"
    note: "Direct first-person articulation of inner state — supports I-NAR."

  - property: relationship.failure_mode
    text: "I will be with you on your wedding-night"
    location: "Volume II, Chapter 9"
    note: "The Creature's threat demonstrates his power over Victor — supports F-AUT, F-REV."

  - property: being.autonomy
    text: "I ought to be thy Adam, but I am rather the fallen angel"
    location: "Volume II, Chapter 7 (Creature's narrative)"
    note: "Self-identification via Paradise Lost shows emergent moral reasoning — supports A-EMR."

notes: >
  The Creature is the foundational case for the constructed being who demands
  recognition. Shelley's nested narrative structure is itself an argument about
  interiority — by giving the Creature his own voice, she forces the reader to
  confront his personhood before returning to Victor's dehumanizing perspective.
```

---

## Schema File

The machine-readable schema is located at `schema/cb-schema.yaml`. Validation scripts in `analysis/` use this schema to check that all entries conform to the definitions above.
