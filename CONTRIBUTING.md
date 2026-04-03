# Contributing to the Constructed Beings Ontology

Thank you for your interest in contributing. This is a scholarly dataset, and contributions are treated as scholarly work -- which means rigor matters, primary texts matter, and good-faith disagreement is not only tolerated but expected.

## Ways to Contribute

### 1. Propose a new constructed being

The simplest contribution is to suggest a CB that should be in the dataset but isn't.

**Open a GitHub Issue** with the following information:

- **Entity name** (e.g., "HAL 9000")
- **Source text** (e.g., *2001: A Space Odyssey*, Arthur C. Clarke, 1968)
- **Year** of first publication, release, or known composition
- **Brief argument for inclusion** -- why this entity meets the CB definition (made not born, agent-like, narrative presence). One or two sentences is fine.

We will triage the suggestion and either code it ourselves or invite you to submit a coded entry.

### 2. Submit a coded entry

If you want to contribute a fully coded CB entry:

1. **Fork** this repository.
2. **Create a YAML file** in `data/beings/` following the naming convention: `kebab-case-entity-name.yaml` (e.g., `hal-9000.yaml`).
3. **Code all properties** defined in [SCHEMA.md](SCHEMA.md). Entries use nested objects (`source`, `creator`, `being`, `relationship`) rather than flat top-level properties. Each entry must include a `citations` array with at least one citation to the primary text. Use the [coding guide](docs/coding_guide.md) for ambiguous cases.
4. **Run validation** to ensure your entry conforms to the schema:
   ```bash
   python schema/validate.py
   ```
5. **Submit a pull request** with:
   - The new YAML file
   - A brief PR description explaining any non-obvious coding decisions
   - Citations to the primary text for any contested properties

### 3. Correct or refine an existing entry

If you believe an existing entry is miscoded:

1. Open an issue explaining the disagreement, **citing the primary text**.
2. Or submit a PR with the correction and a clear rationale.

### 4. Improve the schema or tooling

If you see a gap in the property definitions, an edge case the schema doesn't handle, or a bug in the analysis scripts, issues and PRs are welcome.

## Coding Guidelines

### General principles

- **Code what the text says, not what you infer.** If the source text does not address a property, use `ambiguous` or `unknown` as appropriate. Do not project modern interpretations onto ancient texts without flagging this in the `notes` field.
- **Use the primary text as your authority.** Film adaptations and novelizations may diverge; code the specific version listed in `source_text`.
- **When in doubt, use `ambiguous`.** The `ambiguous` value is not a cop-out; it is a positive claim that the text is genuinely indeterminate on this property. This is often the most interesting coding.

### Ambiguous cases

The [coding guide](docs/coding_guide.md) provides worked examples for common ambiguous cases, including:

- Biologically manufactured beings (replicants, clones)
- Divine creations (where the "constructor" is God)
- Entities whose autonomy changes over the narrative
- Entities with multiple or hybrid substrates
- Properties not addressed in the source text

### Boundary cases

Some entities sit on the boundary of the CB definition. The [boundary cases document](docs/boundary_cases.md) discusses these in detail and explains inclusion/exclusion decisions. If your proposed entity is a boundary case, please reference this document in your issue or PR.

## Discussion Norms

This is an academic project. Disagreements about coding are **scholarly arguments**, not edit wars.

- **Cite the primary text.** "I think Frankenstein's creature has full autonomy" is an opinion. "In Volume III, Chapter 7, the creature independently formulates and executes a plan of revenge, makes moral arguments for his actions, and negotiates terms with his creator" is a scholarly claim.
- **Engage with the strongest version of the opposing view.** If someone codes a property differently than you would, assume they have a reason and ask about it before asserting they are wrong.
- **Acknowledge genuine ambiguity.** Many of the most important texts in this ontology are important precisely *because* they resist clean coding. If a disagreement cannot be resolved, the correct response is often to code the property as `ambiguous` and document the competing readings in the `notes` field.
- **Be collegial.** The usual expectations of respectful academic discourse apply. We are all here because we find these questions fascinating.

## Scope

### Version 1: Western canon

The current scope is Western fiction and myth, broadly construed: Greco-Roman mythology, Jewish folklore, European literature from the medieval period forward, and Anglophone fiction and film through 2025.

This is not a claim that the Western canon is the only or most important tradition for thinking about constructed beings. It is a practical scoping decision for a first release.

### Version 2: Non-Western traditions

We intend to expand to non-Western traditions in v2. This expansion will be done with appropriate cultural consultation -- not by applying Western-derived categories to non-Western texts, but by working with scholars of those traditions to determine whether the ontology's property axes are appropriate, need modification, or need replacement.

If you are a scholar of non-Western constructed-being traditions and are interested in contributing to v2 planning, please open an issue or contact [Jeff Reid](https://github.com/jgreid) directly.

## Questions?

Open an issue or reach out to [@jgreid](https://github.com/jgreid) on GitHub.
