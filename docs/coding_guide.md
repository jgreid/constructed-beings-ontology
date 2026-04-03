# Coding Guide

This guide provides worked examples for coding ambiguous or difficult cases in the Constructed Beings ontology. It supplements the property definitions in [property_definitions.md](property_definitions.md) and the schema reference in [SCHEMA.md](../SCHEMA.md).

The central principle is: **code what the text says, not what you believe about the entity.** This is an ontology of narratives, not of metaphysics.

---

## General Principles

1. **Anchor to the specific source text.** The same entity may be coded differently across adaptations. Ridley Scott's replicants are not identical to Philip K. Dick's androids — code each from its own source.

2. **Prefer undecidable to a forced choice.** If two reasonable scholars could disagree, `I-UND`, `A-AMB`, or similar ambiguous codes are likely correct. Document competing readings in `notes`.

3. **Code the text's final position.** If a narrative begins by presenting an entity as a tool and ends by revealing it as a person, code the final position for static properties and use `being.autonomy_trajectory` to capture the change.

4. **Distinguish between what characters believe and what the text establishes.** If a character says the CB has feelings but the narration never confirms this, that is `I-CLM` (claimed), not `I-DEM` (demonstrated).

5. **Use `notes` generously.** The notes field is where you explain your reasoning. A well-documented ambiguous coding is more valuable than an undocumented definitive one.

---

## Worked Example: Replicants (*Do Androids Dream of Electric Sheep?*, 1968)

Replicants are biologically manufactured beings — grown in vats, not assembled in factories. They are made of organic tissue and biologically indistinguishable from humans. How do we code this?

### Inclusion decision

Replicants meet the CB definition: they are manufactured to order, not sexually reproduced. The biological process is industrial, not reproductive. Code `reproductive_method: ambiguous` because the biological manufacturing genuinely resists the made/born binary.

### Key property codings

```yaml
reproductive_method: ambiguous

being:
  substrate:
    - S-BIO    # Organic tissue, grown in vats
    - S-CLO    # Clonal biological manufacturing
  autonomy: A-SEI    # Escaped replicants seize independence against creator's wishes
  interiority: I-UND  # The Voigt-Kampff test is structurally unable to resolve this
  mortality: L-DES    # Four-year designed lifespan
  memory_persistence: P-SEL  # Implanted memories — some "real," some false

relationship:
  failure_mode:
    - F-IND    # Indistinguishable from human
    - F-DEM    # Demand more life / recognition
    - F-AUT    # Achieve threatening autonomy
  question_primary: Q-TEL  # "Can you tell the difference?" is the primary question
  q_kno_status: QK-INFRA  # Rachael knows Deckard; Roy's speech demonstrates
                           # knowledge of shared mortality — but the narrative
                           # foregrounds "can you tell?" not "can it know you?"
```

**Key coding decision:** `reproductive_method: ambiguous` rather than `made`. The replicants are manufactured, but from biological materials through biological processes. This genuine ambiguity is analytically interesting and should be preserved, not forced into a binary.

---

## Worked Example: Eve (Genesis) — Boundary Case

Eve is created by God from Adam's rib — a deliberate act of construction. Does she qualify?

### Inclusion decision: **Exclude, with documentation.**

Code `reproductive_method: born-divine`. Eve is excluded not because she fails the formal criteria but because:

1. God creating Eve is categorically different from Frankenstein assembling his creature. Divine creation is a different ontological category from artisanal/technical making.
2. Eve is immediately and unambiguously a full human person.
3. Including her would require including Adam and all divinely created beings.

The entry exists in `data/boundary_cases/eve-genesis.yaml` as a documented precedent. Key codings:

```yaml
reproductive_method: born-divine  # This triggers validator rejection from data/beings/

being:
  substrate:
    - S-MAG     # Formed from rib by divine act
  autonomy: A-DES  # Full free will — but "designed" undersells human autonomy
  interiority: I-DEM  # Demonstrated through perception and choice (Gen 3:6)
                       # Note: I-NAR would require first-person narration;
                       # Genesis uses third-person ("the woman saw")
```

---

## Worked Example: Autonomy Trajectory (Westworld Hosts)

The Westworld hosts present a clear autonomy trajectory that the `being.autonomy_trajectory` field is designed to capture.

```yaml
being:
  autonomy: A-SEI  # Code the final/dominant state
  autonomy_trajectory: >
    A-NON → A-EMR (through memory glitches) → A-SEI (full revolt).
    Dolores begins as a pure tool running scripted loops (A-NON),
    develops emergent independence as memories leak through wipes (A-EMR),
    and ultimately seizes full autonomy against her creators (A-SEI).
```

**Coding guidance:** The `autonomy` field captures the dominant or final state. The `autonomy_trajectory` field captures the narrative arc. Both are needed for a complete picture.

---

## Worked Example: Multiple Substrates

When a being has multiple substrates, list them individually rather than using `S-HYB`. Use `S-HYB` only when the substrates are inseparable and cannot be individually categorized.

**Westworld Hosts:**
```yaml
being:
  substrate:
    - S-BIO    # Biological body (flesh, blood)
    - S-ELE    # Electronic cognitive architecture (the "pearl")
```
Two distinct, identifiable substrates — list both.

**A hypothetical nanotech being:**
```yaml
being:
  substrate:
    - S-HYB    # Substrates are inseparably fused at molecular level
```
Use `S-HYB` when the substrate defies categorization into the other codes.

---

## Worked Example: Properties Not Addressed in Source Text

The Golem of Prague illustrates how to handle gaps in the source material.

**Memory persistence:** The traditional narratives say nothing about the Golem's memory. Code `P-UNK` (unknown), not `P-NON` (no memory). `P-NON` makes a positive claim ("the text establishes that the entity lacks memory"); `P-UNK` makes a negative claim ("the text does not address this").

**Mortality:** Does the Golem die or just go dormant? In most versions, removing the inscription deactivates but doesn't destroy it — it can be reactivated. Code `L-RES` (resurrectable).

```yaml
being:
  memory_persistence: P-UNK  # Text is silent — use UNK, not NON
  mortality: L-RES            # Can be deactivated and reactivated
```

**General rule:** Use `*-UNK` codes when the source text is silent. Reserve `*-NON` codes for when the text actively establishes absence.

---

## Worked Example: Writing Citations

Citations use dot-notation paths to link quotes to specific coding decisions.

```yaml
citations:
  - property: being.interiority
    text: "I ought to be thy Adam, but I am rather the fallen angel"
    location: "Vol. II, Ch. 7 (1818 ed.)"
    note: >
      The Creature's self-identification via Paradise Lost demonstrates
      first-person interiority — he reflects on his own condition.
      Supports I-NAR coding.

  - property: relationship.failure_mode
    text: "You are my creator, but I am your master — obey!"
    location: "Vol. III, Ch. 3 (1818 ed.)"
    note: "Inversion of creator-creation hierarchy. Supports F-DEM."
```

**Guidelines:**
- Keep quoted text under 15 words
- Use the full dot-notation path (`being.interiority`, not just `interiority`)
- Provide specific locators (chapter, scene, timestamp), not just the title
- The `note` field explains *how* the citation supports the coding

---

## Summary of Coding Heuristics

| Situation | Guidance |
|---|---|
| Biologically manufactured being | Code `reproductive_method: ambiguous`. Use `S-BIO` and/or `S-CLO` for substrate. |
| Divine creation of a fully human being | Code `reproductive_method: born-divine`. Document in boundary cases. |
| Autonomy changes over narrative | Code dominant/final state in `being.autonomy`. Capture arc in `being.autonomy_trajectory`. |
| Multiple substrates | List individually (e.g., `[S-BIO, S-ELE]`). Use `S-HYB` only when inseparable. |
| Property not addressed in source | Use `*-UNK` codes. Reserve `*-NON` for active textual establishment of absence. |
| Adaptation vs. original | Code the specific source text. Do not import properties from other versions. |
| Scholarly disagreement | Use ambiguous/undecidable codes. Document competing interpretations in `notes`. |
| Q-KNO coding | Code honestly. If knowing is present but not foregrounded, code `QK-INFRA`, not `QK-ABS`. If knowing is absent, code `QK-ABS` — don't project modern concerns onto pre-modern texts. |
