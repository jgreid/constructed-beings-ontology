# Methodology

This document describes the coding methodology, known reliability issues, and protocols for testing inter-coder agreement.

---

## Coding Protocol

Each entry in the corpus is coded by a single researcher following these steps:

1. **Read the source text.** Film entries require watching the film; novel entries require reading the novel. Coding from summaries or secondary sources is discouraged and must be flagged in `notes`.
2. **Fill in all seven card properties and all metadata fields** using the controlled vocabularies in [SCHEMA.md](../SCHEMA.md).
3. **Write the `notes` field** with coding rationale, uncertainty flags, and any scholarly context that supports the decisions.
4. **Run the validator** to catch structural errors.
5. **Self-review** the entry against the [coding guide](coding_guide.md), checking each property against the decision tests.

### What the schema codes

The schema codes properties of the **source text**, not properties of the being or of audience reception. When a property is ambiguous, the question is "what does the text do?" — not "what do we think the being really is?" or "how do modern audiences interpret this?"

---

## Known Reliability Issues

### Properties with high expected agreement

- **`metadata.*` fields** — Source, year, medium, creator, substrate, embodiment are factual and should produce near-perfect agreement.
- **`interiority: none` vs. other values** — The bright line between "no inner life depicted" and "some inner life depicted" is clear.
- **`autonomy: none`** — "No independent will" is unambiguous when it applies.
- **`divergence: none`** — "Working as intended" is usually clear.

### Properties with lower expected agreement

- **`primary_question`** — The most judgment-heavy property. Seven values, thin boundaries between `affection` and `knowledge`, between `identity` and `rights`. The coding guide provides decision tests, but reasonable coders will disagree on entries where two questions are in tension. Expected agreement: 70–80%.
- **`divergence: design` vs. `departure`** — "The spec was wrong" vs. "it left the spec" can be a close call when the being follows instructions that have catastrophic emergent consequences. The decision test ("what would the creator say if asked 'did it work?'") helps but does not eliminate ambiguity. Expected agreement: 80–85%.
- **`knowability` and `knowing` salience levels** — The `present`/`secondary` boundary is the hardest to apply consistently. The rule of thumb ("would the film still work without the question?") helps but requires subjective judgment about narrative structure. Expected agreement: 75–85%.
- **`epistemic_reach: behavioral` vs. `conversational`** — The coding guide notes that "language presence alone does not upgrade behavioral to conversational," but applying this consistently is difficult. The `conversational` skew (60% of entries) reflects both the corpus composition and potential over-coding.

### Properties not expected to cause disagreement

- **`interiority: narrated` vs. `demonstrated`** — First-person access (narrated) vs. shown through action (demonstrated) is structurally clear.
- **`autonomy: designed` vs. `emergent` vs. `seized`** — These usually map cleanly to the source text's narrative.

---

## Inter-Coder Reliability Protocol

To test the reproducibility of coding decisions, the following protocol is recommended:

### Setup

1. **Select 5 entries** spanning different eras, media, and difficulty levels. Suggested:
   - One pre-1900 entry (e.g., Frankenstein's Creature, the Golem)
   - One mid-century entry (e.g., HAL 9000, Data)
   - One contemporary entry (e.g., Ava, Samantha)
   - One entry the coders have flagged as "hard" in `notes`
   - One entry the coders are unfamiliar with

2. **Ensure all coders have read the source text** (or watched the film/played the game).

3. **Provide each coder** with the blank entry template, the SCHEMA.md reference, and the coding guide. Do not provide existing codings.

### Procedure

1. Each coder independently completes all 7 card properties + metadata for each of the 5 entries.
2. Compare codings property-by-property.
3. For each disagreement, record:
   - The property and the two (or more) values chosen
   - The textual evidence each coder cited
   - Whether the disagreement is about the text or about the schema's definitions
4. Discuss disagreements and attempt to reach consensus. Document cases where consensus is not reached.

### Metrics

- **Per-property agreement rate**: percentage of entries where all coders chose the same value.
- **Cohen's kappa** (for 2 coders) or **Fleiss' kappa** (for 3+) on each property, to account for chance agreement.
- **Systematic disagreement patterns**: properties where the same pair of values are confused repeatedly (e.g., `present` vs. `secondary` on knowability).

### Reporting

Results should be documented with:
- The entries selected and the number of coders
- Per-property agreement rates and kappa scores
- Narrative discussion of the most productive disagreements
- Any schema revision suggestions that emerge from the process

---

## Limitations

- **Single-coder corpus.** The current corpus was coded by a single researcher. Inter-coder reliability has not yet been formally tested. This is acknowledged as a limitation.
- **Notes as the citation mechanism.** The absence of structured citations means that coding rationale varies in specificity across entries. Some entries have detailed scene-by-scene justification; others have brief notes.
- **Partial familiarity.** Some entries are coded from partial familiarity with the source text and are flagged as such in `notes`. These are candidates for re-coding by a coder with deeper familiarity.
