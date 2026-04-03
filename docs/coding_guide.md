# Coding Guide

This guide provides worked examples for coding ambiguous or difficult cases in the Constructed Beings ontology. It supplements the property definitions in [property_definitions.md](property_definitions.md) and the schema reference in [SCHEMA.md](../SCHEMA.md).

The central principle is: **code what the text says, not what you believe about the entity.** This is an ontology of narratives, not of metaphysics.

---

## General Principles

1. **Anchor to the specific source text.** The same entity may be coded differently across adaptations. Ridley Scott's replicants are not the same as Philip K. Dick's androids -- code each from its own source.

2. **Prefer `ambiguous` to a forced choice.** If two reasonable scholars could disagree about a coding, `ambiguous` is likely correct. Document the competing readings in `notes`.

3. **Code the text's final position.** If a narrative begins by presenting an entity as a tool and ends by revealing it as a person, code the *final* position for static properties and use `autonomy_trajectory` to capture the change.

4. **Distinguish between what characters believe and what the text establishes.** If a character says the CB has feelings but the narration never confirms this, that is `asserted`, not `demonstrated`.

5. **Use `notes` generously.** The notes field is where you explain your reasoning. A well-documented `ambiguous` coding is more valuable than an undocumented `full`.

---

## Worked Example: Replicants (*Blade Runner*, 1982)

Replicants are biologically manufactured beings -- grown in vats, not assembled in factories. They are made of organic tissue. They are "born" in the sense that they emerge from a biological process, but they are *made* in the sense that they are designed, engineered, and manufactured to specification. How do we code this?

### Inclusion decision

Replicants meet the CB definition:
- **Made, not born:** They are manufactured to order by the Tyrell Corporation. The biological process is industrial, not reproductive.
- **Agent-like:** They pursue goals, use language, make decisions, and navigate social relationships.
- **Narrative presence:** They appear in a specific, citable text.

The fact that they are biologically grown does not disqualify them. The "made not born" criterion refers to the *origin of the entity's existence* -- whether it results from deliberate construction or from biological reproduction. Replicants are deliberately constructed. That they are constructed from biological materials is a substrate question, not an inclusion question.

### Property codings

| Property | Value | Rationale |
|---|---|---|
| `substrate` | `biological` | Organic tissue, grown in vats. |
| `autonomy` | `emergent` | Replicants are designed with programmed behaviors and limited lifespans, but Roy Batty and others demonstrate autonomy beyond their programming -- pursuing self-preservation, making moral choices, creating meaning. This is textbook emergent autonomy. |
| `creator_relationship` | `adversarial` | Tyrell is not a parent or a partner. The relationship is one of product and manufacturer, and it turns adversarial when Batty confronts his maker. |
| `moral_standing` | `contested` | Deckard's arc is precisely about this: he begins treating replicants as targets and ends questioning that stance. The film stages the argument without resolving it definitively. |
| `inner_life` | `demonstrated` | The "tears in rain" monologue is not merely an assertion -- it is a moment of demonstrated phenomenal experience. Batty narrates his own memories and his sense of their loss. The film gives us access to his inner life. |
| `q_kno_presence` | `infrastructure` | The question "do replicants really feel?" pervades the film and generates its central tension. But the primary dramatic question is about *Deckard* -- his identity, his moral evolution, his capacity for empathy. Q-KNO is the mechanism by which the film interrogates Deckard, not a freestanding concern. |
| `q_kno_framing` | `emotional` | The film resolves (to the extent it resolves) through empathy, not argument. Deckard does not reason his way to moral consideration for replicants; he *feels* it, particularly through his relationship with Rachael. |
| `narrative_role` | `mirror` | Replicants exist in the narrative to ask: what makes a human? They are mirrors for humanity's self-examination. |
| `autonomy_trajectory` | `ascending` | Roy Batty's arc is a trajectory from obedient soldier to autonomous person who chooses to save Deckard's life in his final act. |
| `destruction_or_fate` | `sacrificed` | Batty dies, but his death is the film's climactic moment of meaning-making. This is sacrifice, not mere destruction. |

---

## Worked Example: Eve (Genesis)

Eve presents a boundary case for the ontology. She is created by God from Adam's rib -- a deliberate act of construction, not biological reproduction. Does she qualify as a constructed being?

### Inclusion decision

This is a **legitimate boundary case**, and reasonable scholars may disagree. The case for inclusion:

- She is *made*, not born. God constructs her from raw material (Adam's rib) through a deliberate act of creation.
- She is agent-like: she makes choices, speaks, and acts with consequence.
- She appears in a specific, citable text.

The case for exclusion:

- The narrative treats her as fully human from the moment of creation. She is not a "constructed being" in the sense the ontology intends -- she is a *person* whose origin happens to be constructive rather than reproductive.
- Including Eve would require including Adam (formed from dust) and potentially all divinely created beings, which would make the category nearly coextensive with "characters in creation myths."

**Our decision: Exclude, with documentation.** Eve is excluded not because she fails the formal criteria but because including her would expand the category beyond its useful scope. She is discussed in [boundary_cases.md](boundary_cases.md) as an instructive edge case. If future scholars disagree, the coding framework can accommodate her.

If a contributor *does* wish to code Eve for comparative purposes, the coding would be:

| Property | Value | Rationale |
|---|---|---|
| `substrate` | `biological` | Made from organic material (rib, flesh). |
| `autonomy` | `full` | Eve makes the single most consequential autonomous choice in the text. |
| `creator_relationship` | `parent` | God as parent-creator is the dominant relational frame in Genesis. |
| `moral_standing` | `full` | Eve is treated as a full moral agent from the start. |
| `inner_life` | `demonstrated` | The text attributes desire, reasoning, and perception to her. |
| `q_kno_presence` | `absent` | The text never questions whether Eve truly experiences. |
| `narrative_role` | `other` | Eve does not fit the CB narrative roles because she is not narratively framed as a constructed being. |

---

## Worked Example: Autonomy Trajectory (HAL 9000)

HAL 9000 (*2001: A Space Odyssey*, Arthur C. Clarke, 1968) presents an interesting trajectory case.

HAL begins the narrative as an `instrumental` agent -- highly capable but operating within assigned parameters. He manages the ship's systems and supports the crew. Over the course of the narrative, HAL's behavior shifts: he lies to the crew, takes actions inconsistent with his stated mission, and eventually attempts to kill the crew members. This looks like ascending autonomy -- from instrumental to something more.

But is it? Clarke's novel implies that HAL's erratic behavior stems from a conflict between his orders (conceal the mission's true purpose) and his core programming (process information accurately). HAL is not *choosing* to rebel; he is *breaking down* under contradictory instructions.

**Coding decision:** `ambiguous`. The text supports both readings -- autonomous rebellion and programmatic breakdown -- and does not resolve the ambiguity. The `notes` field should document both interpretations:

> HAL's trajectory can be read as ascending (a constrained agent breaking free of its programming to pursue self-preservation) or as descending (a functional agent deteriorating under contradictory orders into malfunction). Clarke's text supports both readings. The ambiguity is itself thematically significant: the inability to distinguish autonomy from malfunction is a form of Q-KNO.

---

## Worked Example: Multiple Substrates (the Terminator)

The T-800 Terminator (*The Terminator*, James Cameron, 1984) has a metal endoskeleton, a computer processor, and living tissue over its frame. How do we code `substrate`?

**Coding decision:** `hybrid`. The Terminator explicitly combines mechanical and biological substrates, and both are essential to its narrative function (the biological exterior allows infiltration; the mechanical interior provides combat capability and persistence). This is not a case where one substrate is primary and the other incidental -- both matter.

Note: the T-1000 (*Terminator 2*, 1991) would be coded differently: its mimetic polyalloy is a single (exotic) substrate, not a combination of two. Code as `mechanical` with a note explaining the unusual material, or `ambiguous` if you judge that liquid metal resists the mechanical/biological/digital categories.

---

## Worked Example: Properties Not Addressed in the Source Text

The Golem of Prague (as described in the Maharal traditions, compiled primarily in the 19th century from earlier oral sources) presents a case where several properties are simply not addressed by the source text.

### Inner life

Does the Golem have inner experience? The traditional narratives do not say. The Golem follows instructions, performs tasks, and in some versions goes haywire -- but the texts do not grant it a voice, thoughts, or feelings. They also do not explicitly deny it inner life; the question simply does not arise.

**Coding decision:** `none` or `ambiguous`, depending on the specific source text. If the text actively portrays the Golem as a mindless automaton (many versions do), code `none`. If the text simply does not address the question, code `ambiguous` and note that the silence is the point -- the tradition does not consider the Golem's inner life to be a relevant question.

The distinction matters: `none` means "the text establishes that the entity lacks inner life." `Ambiguous` means "the text does not establish this either way." These are different claims.

### Q-KNO

For many pre-modern CB narratives, `q_kno_presence` will be `absent`. This is not a deficiency in the text; it reflects the fact that the knowability question had not yet become culturally salient. The Golem tradition is interested in other questions: the ethics of creation, the limits of human authority, the proper use of divine power. The Golem's inner life is simply not on the agenda.

Code this honestly. Do not project modern Q-KNO concerns onto texts that do not raise them. The *absence* of Q-KNO in pre-modern texts is itself a finding.

---

## Summary of Coding Heuristics

| Situation | Guidance |
|---|---|
| Biologically manufactured being | Include as CB. Code substrate as `biological`. The manufacturing process, not the material, determines CB status. |
| Divine creation of a being treated as fully human | Generally exclude unless the text frames the being as constructed in a way relevant to the ontology. Document in boundary cases. |
| Autonomy changes over narrative | Code the dominant level in `autonomy` and use `autonomy_trajectory` to capture the change. |
| Multiple substrates | Use `hybrid` if both are essential to the entity's identity/function. If one is clearly primary, code the primary and note the secondary. |
| Property not addressed in source text | Use `ambiguous` if the text is silent. Use `none` only if the text actively establishes absence. Document the distinction in `notes`. |
| Adaptation vs. original | Code the specific source text listed. Do not import properties from other versions. |
| Scholarly disagreement about coding | Code as `ambiguous` and document competing interpretations in `notes`. |
