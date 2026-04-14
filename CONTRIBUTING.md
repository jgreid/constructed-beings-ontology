# Contributing to the Constructed Beings Ontology

Thank you for your interest in contributing. This is a scholarly dataset, and contributions are treated as scholarly work — rigor matters, primary texts matter, and good-faith disagreement is not only tolerated but expected.

If you're new to the project, start with [SCHEMA.md](SCHEMA.md) (the definitive reference) and [docs/coding_guide.md](docs/coding_guide.md) (how to make the judgment calls).

---

## Ways to Contribute

### 1. Propose a new constructed being

The simplest contribution is to suggest a CB that should be in the dataset but isn't.

**Open a GitHub Issue** with:

- **Entity name** (e.g., "David 8")
- **Source text** (e.g., *Alien: Covenant*, Ridley Scott, 2017)
- **Year** of release / publication
- **One- or two-sentence argument for inclusion** — why this entity meets the three criteria (made not born, agent-like, narrative presence).

We'll triage and either code it or invite you to submit a coded entry.

### 2. Submit a coded entry

If you want to contribute a fully coded CB entry:

1. **Fork** this repository.
2. **Copy** [`schema/entry_template.yaml`](schema/entry_template.yaml) to `data/beings/<your-id>.yaml`. The filename should match the `id` field (kebab-case). For sequel-split entries, follow the `<being-slug>-<source-slug>` convention (e.g., `glados-portal-2`).
3. **Code all seven card properties** and all eleven metadata fields. Use `sequel_link` if the entry is part of a lineage; use `null` otherwise.
4. **Write the `notes` field** in prose. Capture what's distinctive, flag any uncertainty, and explain any close calls. This is where scholarly context lives — the schema has no structured citations array.
5. **Run validation:**
   ```bash
   python schema/validate.py data/beings/<your-id>.yaml
   ```
6. **Submit a pull request** with the new YAML file and a brief description explaining any non-obvious coding decisions. Reference scenes, passages, or design decisions you relied on.

### 3. Correct or refine an existing entry

If you think an existing entry is miscoded:

1. Open an issue. Cite the specific scene / passage / design decision that argues for a different coding.
2. Or submit a PR with the correction. Update the entry's `notes` field to explain the re-coding rationale.

Disagreements are welcome and expected. The ontology gets better when multiple readers push against the coding.

### 4. Improve the schema, validator, or analysis tools

If you see a missing property, an under-specified enum value, or a bug in the analysis scripts, open an issue or submit a PR.

Schema changes are a bigger commitment and warrant discussion first — breaking changes should be rare. See [CHANGELOG.md](CHANGELOG.md) for what past schema changes involved.

---

## Coding Guidelines

### Core principles

- **Code what the text shows, not what you infer.** The schema's enums are descriptive, not aspirational. If the film doesn't address a property, use the option that best reflects what the text actually does. Usually that's `none` for Being properties and `absent` for Knowability/Knowing.
- **Use the closest available value, and flag the mismatch.** If the closest option is a bad fit, say so in `notes`. Bad fits are information; they tell us where the schema is under-specified.
- **Use `notes` for context that matters.** The schema does not have a structured citations array. When a coding decision depends on a specific passage or scene, write it in `notes` in enough detail that a future editor can verify it.
- **Flag low confidence.** If you're coding from partial familiarity with the source, say so. "Flagged for re-review" is a respected state.

### Close calls and judgment calls

The [coding guide](docs/coding_guide.md) walks through the hard properties in detail: divergence, interiority, primary_question, knowability vs. knowing. Read it before making a judgment call on any of these.

### Boundary cases

Some entities sit on the boundary of the CB definition. The [boundary cases document](docs/boundary_cases.md) discusses these in detail and explains inclusion/exclusion decisions. If your proposed entity is a boundary case, reference that document in your issue or PR.

---

## Discussion Norms

This is an academic project. Disagreements about coding are **scholarly arguments**, not edit wars.

- **Cite the text.** "I think Frankenstein's Creature has full autonomy" is an opinion. "In Volume III, Chapter 7, the Creature independently formulates and executes a plan of revenge, makes moral arguments for his actions, and negotiates terms with his creator" is a scholarly claim.
- **Engage with the strongest version of the opposing view.** If someone codes a property differently than you would, assume they had a reason and ask about it before asserting they were wrong.
- **Acknowledge genuine ambiguity.** The schema has `undecidable` for interiority when the text deliberately leaves the question open, and `observer` for divergence when the gap is in perception. Use them when the text supports them.
- **Be collegial.** The usual expectations of respectful academic discourse apply. We are all here because we find these questions fascinating.

---

## Scope

### Medium

Use the `medium` value that matches the source text's format. The schema supports: `poem`, `epic`, `folklore`, `play`, `novel`, `short-story`, `comics`, `film`, `television`, `video-game`. Use `comics` for entries sourced from serialized comic narratives (Marvel, DC, manga, etc.) — do not use `short-story` for comics.

### Primary scope: Western canon

The ontology's primary scope is Western fiction and myth, broadly construed: Greco-Roman mythology, Jewish folklore, European literature from the medieval period forward, and Anglophone fiction, film, television, and games.

### Non-Western works (Western-known)

As of v2.2, the corpus includes selected non-Western works that have achieved wide recognition in Western pop culture — currently Japanese anime and manga entries (Astro Boy, Ghost in the Shell, Neon Genesis Evangelion, Ghost in the Shell: Stand Alone Complex). These entries use the existing schema categories (manga → `comics`, anime TV → `television`, anime films → `film`).

This pragmatic expansion does not replace the planned full non-Western expansion with appropriate cultural consultation. The existing seven-property schema was developed on Western texts and may need modification for traditions with different epistemologies.

### Future: Full non-Western expansion

We intend to expand systematically to non-Western traditions in a future release. That expansion will be done with appropriate cultural consultation — not by applying Western-derived categories to non-Western texts, but by working with scholars of those traditions to determine whether the property axes are appropriate, need modification, or need replacement.

If you are a scholar of non-Western constructed-being traditions and are interested in contributing to future planning, please open an issue or contact [Jeff Reid](https://github.com/jgreid) directly.

---

## Questions?

Open an issue or reach out to [@jgreid](https://github.com/jgreid) on GitHub.
