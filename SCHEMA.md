# Schema Reference

This document is the human-readable companion to `schema/cb-schema.yaml`. It defines every property, its type, allowed values, and the meaning of each enumerated value. For the rationale behind each property -- *why* it is in the schema -- see [docs/property_definitions.md](docs/property_definitions.md).

---

## Entry Structure

Each constructed being is stored as a single YAML file in `data/beings/`. All properties listed below are **required** unless marked as optional.

---

## Properties

### `id`

| | |
|---|---|
| **Type** | `string` |
| **Format** | kebab-case (lowercase, hyphens, no spaces) |
| **Required** | Yes |
| **Example** | `frankensteins-creature` |

A unique identifier for the entity. Used as the filename (without extension) and for cross-references.

---

### `name`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `Frankenstein's Creature` |

The most commonly used name for the entity. Where multiple names exist (e.g., "Frankenstein's monster" vs. "the Creature"), prefer the name used in the primary source text.

---

### `source_text`

| | |
|---|---|
| **Type** | `string` |
| **Required** | Yes |
| **Example** | `Frankenstein; or, The Modern Prometheus (Mary Shelley)` |

The primary text in which the entity appears. Include author name in parentheses. For films, include director. For mythological entities, cite the specific textual source being coded (e.g., "Metamorphoses (Ovid)" rather than "Greek myth").

---

### `source_year`

| | |
|---|---|
| **Type** | `integer` |
| **Required** | Yes |
| **Example** | `1818` |

Year of first publication, release, or best scholarly estimate of composition. For ancient texts, use the conventional date. Negative values indicate BCE (e.g., `-8` for Ovid's *Metamorphoses*, completed around 8 CE; use `-700` for Hesiod).

---

### `tradition`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

The literary or mythic tradition to which the source text belongs.

| Value | Meaning |
|---|---|
| `greco-roman` | Greek and Roman mythology and literature |
| `jewish-folklore` | Jewish mystical and folkloric traditions (Golem narratives) |
| `medieval` | Medieval European literature and legend |
| `renaissance` | Renaissance-era literature and drama |
| `enlightenment-fiction` | Enlightenment through early Romantic literature (roughly 1700--1830) |
| `gothic` | Gothic fiction tradition |
| `early-sf` | Early science fiction, pre-Golden Age (roughly 1818--1937) |
| `golden-age-sf` | Golden Age science fiction (roughly 1938--1960) |
| `new-wave-sf` | New Wave and post-New Wave science fiction (roughly 1960--1985) |
| `modern-sf` | Modern science fiction (roughly 1985--2015) |
| `post-llm-sf` | Post-LLM era science fiction and narrative (roughly 2015--present) |
| `film` | Primarily a film (when the film is the primary text, not an adaptation) |
| `television` | Primarily a television series |
| `other` | Traditions not captured above |

---

### `substrate`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

What the entity is made of -- its physical or computational substrate.

| Value | Meaning |
|---|---|
| `mechanical` | Metal, clockwork, gears, electromechanical parts. The classic robot. |
| `biological` | Organic tissue, whether grown, assembled, or sculpted from flesh. Includes replicants and beings made from clay that the narrative treats as living tissue. |
| `digital` | Software, code, neural networks, or other purely computational substrates. No physical body, or body is incidental to identity. |
| `magical` | Animated by supernatural means -- enchantment, divine breath, necromancy. The substrate is secondary to the animating force. |
| `hybrid` | Explicitly combines two or more substrate types (e.g., a cyborg with both biological and mechanical components, where both are essential to identity). |
| `ambiguous` | The text does not clearly establish the substrate, or the substrate resists classification. |

---

### `autonomy`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

The degree of independent agency the entity demonstrates in the text.

| Value | Meaning |
|---|---|
| `none` | The entity has no independent will. It follows instructions or programming without deviation. A pure tool. |
| `instrumental` | The entity has limited autonomy in pursuit of assigned goals. It can choose *how* to accomplish tasks but not *which* tasks to pursue. |
| `emergent` | The entity develops or displays autonomy beyond its original design or instructions, but this autonomy is partial, unstable, or contested within the narrative. |
| `full` | The entity is narratively treated as a fully autonomous agent, capable of setting its own goals, making moral choices, and acting against its creator's wishes. |
| `ambiguous` | The text is genuinely indeterminate about the entity's level of autonomy, or the autonomy level is actively contested within the narrative. |

---

### `creator_relationship`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

How the creator relates to the created entity within the narrative.

| Value | Meaning |
|---|---|
| `master` | The creator treats the entity as property or a tool. The relationship is one of ownership and command. |
| `parent` | The creator relates to the entity as a parent to a child -- with nurture, responsibility, and emotional investment (even if imperfect). |
| `absent` | The creator is dead, gone, unknown, or otherwise absent from the narrative. The entity exists without a creator relationship to navigate. |
| `adversarial` | The creator and entity are in conflict. The relationship has broken down into opposition. |
| `collaborative` | The creator and entity work as partners or colleagues, with mutual respect. |
| `ambiguous` | The relationship is complex, shifting, or not clearly one of the above. |

---

### `moral_standing`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Whether the text grants the entity moral consideration -- i.e., whether harming or destroying it is treated as morally significant.

| Value | Meaning |
|---|---|
| `none` | The entity is treated as an object. Its destruction carries no more moral weight than breaking a tool. |
| `instrumental` | The entity has moral standing only insofar as it is useful or valued by someone. Destroying it is wrong because it belongs to someone, not because it matters in itself. |
| `contested` | The entity's moral standing is actively debated within the text. Characters disagree about whether it deserves moral consideration. This is often the most interesting value. |
| `full` | The text treats the entity as a full moral patient. Harming it is wrong for the same reasons harming a person is wrong. |
| `ambiguous` | The text does not clearly establish the entity's moral standing, or sends conflicting signals. |

---

### `inner_life`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Whether the text attributes subjective experience (qualia, feelings, consciousness) to the entity.

| Value | Meaning |
|---|---|
| `none` | The text does not attribute any inner experience to the entity. It is presented as purely mechanistic. |
| `implied` | The text hints at inner experience without confirming it. Behavioral cues suggest feeling, but the text maintains deniability. |
| `asserted` | Characters within the text (including the entity itself) assert that the entity has inner experience, but the narrative does not independently confirm this. |
| `demonstrated` | The text provides direct access to the entity's subjective experience (e.g., through narration from the entity's point of view that includes qualia, emotions, or phenomenal consciousness). |
| `ambiguous` | The text deliberately or inadvertently leaves the question of inner experience unresolved. |

---

### `q_kno_presence`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

Whether the **knowability question** -- "Can we determine whether this being has genuine subjective experience?" -- is raised in the text.

| Value | Meaning |
|---|---|
| `absent` | The text does not engage with the question of whether the entity's inner life is knowable. The entity either clearly has or clearly lacks inner life, and this is not treated as epistemically problematic. |
| `infrastructure` | The knowability question is present in the text and generates dramatic tension, but it serves other narrative purposes. It is a supporting concern, not the central question. |
| `primary` | The knowability question is the central dramatic or thematic concern of the text. The narrative is organized around the impossibility or difficulty of knowing whether the entity truly experiences. |
| `ambiguous` | The text engages with knowability in a way that resists classification as infrastructure or primary. |

---

### `q_kno_framing`

| | |
|---|---|
| **Type** | `enum` or `null` |
| **Required** | Only when `q_kno_presence` is not `absent` |

When the knowability question is present, how does the text frame it?

| Value | Meaning |
|---|---|
| `philosophical` | Framed as an epistemological or metaphysical problem. Characters or narration engage with it abstractly. |
| `emotional` | Framed as a matter of empathy, connection, or emotional recognition. "I feel that it feels" rather than "I can prove that it feels." |
| `pragmatic` | Framed as a practical problem with real-world consequences. "It doesn't matter whether it really feels; what matters is how we treat it." |
| `legal` | Framed in terms of rights, legal personhood, or institutional recognition. |
| `mixed` | The text uses multiple framings without a dominant one. |
| `ambiguous` | The framing resists classification. |

---

### `narrative_role`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

The primary narrative function of the constructed being within the story.

| Value | Meaning |
|---|---|
| `tool` | The entity functions primarily as an instrument or device. Its purpose is to serve. |
| `mirror` | The entity functions as a reflection of humanity -- its existence raises questions about what it means to be human. |
| `child` | The entity occupies the role of offspring or ward. The narrative focuses on creation, nurture, and the creator's responsibility. |
| `threat` | The entity is primarily a source of danger. The narrative focuses on containment, conflict, or survival. |
| `partner` | The entity functions as a companion, collaborator, or equal. |
| `other` | The narrative role does not fit the above categories. |

---

### `autonomy_trajectory`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

How the entity's autonomy changes over the course of the narrative.

| Value | Meaning |
|---|---|
| `static` | The entity's level of autonomy does not meaningfully change. |
| `ascending` | The entity gains autonomy over the course of the narrative -- from less to more independent. |
| `descending` | The entity loses autonomy -- from more to less independent (e.g., brought under control, lobotomized, enslaved). |
| `arc` | The entity's autonomy rises and then falls (or vice versa) over the narrative. |
| `ambiguous` | The trajectory is unclear or contested. |

---

### `destruction_or_fate`

| | |
|---|---|
| **Type** | `enum` |
| **Required** | Yes |

What happens to the entity by the end of the narrative.

| Value | Meaning |
|---|---|
| `survives` | The entity is intact and continuing to exist at the narrative's close. |
| `destroyed` | The entity is killed, deactivated, dismantled, or otherwise ended. |
| `transformed` | The entity undergoes a fundamental change in nature (e.g., becomes human, merges with another entity, transcends its original form). |
| `sacrificed` | The entity is destroyed, but its destruction is framed as a meaningful, voluntary, or redemptive act. |
| `ambiguous` | The entity's fate is left unclear or open to interpretation. |
| `unknown` | The narrative does not address the entity's ultimate fate. |

---

### `notes`

| | |
|---|---|
| **Type** | `string` |
| **Required** | No (optional) |

Free-text field for recording context, ambiguities, coding rationale, or competing interpretations. This field is especially important for entries where one or more properties are coded as `ambiguous` -- use it to explain *why* the ambiguity exists and what competing readings are in play.

---

## Example Entry

```yaml
id: frankensteins-creature
name: "Frankenstein's Creature"
source_text: "Frankenstein; or, The Modern Prometheus (Mary Shelley)"
source_year: 1818
tradition: gothic
substrate: biological
autonomy: full
creator_relationship: adversarial
moral_standing: contested
inner_life: demonstrated
q_kno_presence: infrastructure
q_kno_framing: emotional
narrative_role: mirror
autonomy_trajectory: ascending
destruction_or_fate: ambiguous
notes: >
  The Creature narrates his own experience in Volume II, providing direct
  access to his inner life (loneliness, desire for companionship, moral
  reasoning). This makes inner_life "demonstrated" rather than "asserted."
  However, Q-KNO functions as infrastructure rather than primary: the novel's
  central concern is Frankenstein's hubris and responsibility, not whether
  the Creature truly feels. The knowability question enables the moral
  argument but is not itself the main event. Fate is "ambiguous" because
  the Creature declares intent to self-immolate but is last seen drifting
  into darkness; the text does not confirm his death.
```

---

## Schema File

The machine-readable schema is located at `schema/cb-schema.yaml`. Validation scripts in `analysis/` use this schema to check that all entries conform to the definitions above.
