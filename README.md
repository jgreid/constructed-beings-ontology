# Toward a Post-LLM Ontology of Constructed Beings

## Abstract

This project is a formal ontology of **constructed beings** (CBs) in Western fiction and myth -- entities that are *made*, not *born*. From Hephaestus's golden handmaidens to GPT-flavored AI companions in contemporary fiction, Western narrative has been building, animating, and arguing about artificial persons for nearly three millennia. This dataset catalogs those beings and codes them along a consistent set of properties: substrate, autonomy, creator relationship, moral standing, and -- critically -- whether the text treats the question of the being's inner life as narratively central. We call that last property **Q-KNO** (the *knowability question*: can we determine whether this being has genuine experience?). The central finding is not that Q-KNO is absent from pre-LLM texts; it surfaces as early as *Frankenstein* and threads through *Blade Runner*, *Ex Machina*, and dozens of other works. Rather, Q-KNO exists in prior literature as **infrastructure** -- a tension that supports other narrative concerns -- and is elevated to a **primary dramatic question** only in the post-LLM era, when audiences can no longer treat it as safely hypothetical. That shift is the story this data tells.

## Domain Definition

### What counts as a constructed being?

A **constructed being** is an entity that satisfies all of the following:

1. **Made, not born.** The entity's existence originates from a deliberate act of construction, programming, enchantment, or creation -- not from biological reproduction.
2. **Agent-like.** The entity exhibits or is attributed behavior that implies agency: goal pursuit, language use, decision-making, or social interaction.
3. **Narrative presence.** The entity appears in a specific, citable text (novel, film, play, epic poem, sacred narrative treated as literary source).

### Scope

Version 1 covers the **Western canon** broadly construed: Greco-Roman myth, Jewish folklore (Golem traditions), European literature from the medieval period forward, and Anglophone fiction and film through 2025. Non-Western traditions -- which are rich, vital, and deserve their own careful treatment -- are planned for v2 with appropriate cultural consultation (see [CONTRIBUTING.md](CONTRIBUTING.md)).

### Exclusion criteria

- **Born-then-modified beings** (e.g., a human who receives cybernetic implants) are excluded unless the modification is so total that the original biological identity is narratively treated as replaced. See [docs/boundary_cases.md](docs/boundary_cases.md) for the full discussion.
- **Collectives without individual identity** (e.g., "the robots" as an undifferentiated mass) are excluded. We code individual named or individuated entities.
- **Metaphorical constructs** (e.g., a corporation described as a "creature") are excluded unless the text grants the entity literal agency.

## Properties

Each CB entry is coded along the following property axes. Brief definitions are given here; full definitions with rationale appear in [docs/property_definitions.md](docs/property_definitions.md).

Each entry has top-level fields (`id`, `name`, `aliases`, `reproductive_method`, `narrative_role`, `notes`) plus four nested property groups. Values use short mnemonic codes -- a few examples are shown below.

| Group | What it covers | Example codes |
|---|---|---|
| **`source`** | Author, title, year, medium, tradition | `medium`: `novel`, `film`, `myth` ... |
| **`creator`** | Creator name, motivation(s), creation morality | `motivation`: `M-SRV` (service), `M-KNO` (knowledge), `M-COM` (companionship) ... |
| **`being`** | Substrate, autonomy, interiority, mortality, multiplicity, memory, nonconsensual transformation | `substrate`: `S-BIO`, `S-MEC`, `S-ELE`, `S-MAG` ... ; `autonomy`: `A-NON`, `A-EMR`, `A-SEI` ... |
| **`relationship`** | Failure mode(s), central question(s), question\_primary, epistemic reach, Q-KNO status | `question`: `Q-KNO`, `Q-CTL`, `Q-RTS` ... ; `q_kno_status`: `QK-ABS`, `QK-INFRA`, `QK-PRI` ... |

Every coding is backed by a `citations` list linking each property to a specific passage in the source text.

For the complete schema specification, including all enum values and their definitions, see [SCHEMA.md](SCHEMA.md).

## The Finding

The conventional post-LLM narrative runs something like: *"We never worried about machine consciousness before, and now we must."* This is false. Western literature has been worrying about it since at least the Golem of Prague and arguably since Ovid's Pygmalion.

What *is* new is the **structural position** of the worry.

In pre-LLM texts, the question of whether a constructed being truly experiences -- whether its tears are "real" -- typically functions as **narrative infrastructure**. It generates dramatic tension, motivates character action, and enriches theme. But the primary dramatic question is usually something else: the hubris of the creator (*Frankenstein*), the ethics of slavery (*R.U.R.*), the nature of memory (*Blade Runner*), the test of humanity (*Ex Machina*).

In post-LLM texts -- and, more importantly, in post-LLM *audience reception* of older texts -- Q-KNO moves from infrastructure to **primary question**. It is no longer a lever for exploring other themes; it *is* the theme. This happens because the audience can no longer maintain comfortable hypothetical distance. The question "Does this thing actually experience?" has migrated from fiction into daily life.

This dataset lets you trace that migration quantitatively. The `relationship.question`, `relationship.question_primary`, and `relationship.q_kno_status` properties encode exactly where each text positions the knowability question, enabling systematic analysis across the full historical range.

## How to Use This Project

### Browse the data

Each constructed being is stored as a YAML file in `data/beings/`. You can read them directly -- they are designed to be human-readable.

### Run the analysis

Analysis scripts live in `analysis/`. To reproduce the core findings:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate a summary table of all beings
python analysis/generate_table.py

# Property coverage analysis
python analysis/property_coverage.py

# Q-KNO question analysis
python analysis/question_analysis.py
```

### Validate entries

```bash
# Validate all entries against the schema
python schema/validate.py
```

### Contribute

We welcome contributions -- new CB entries, corrections to existing codings, and improvements to the schema. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Citation

If you use this dataset in academic work, please cite:

```bibtex
@misc{reid2025constructed,
  author       = {Reid, Jeff},
  title        = {Toward a Post-LLM Ontology of Constructed Beings},
  year         = {2025},
  publisher    = {GitHub},
  url          = {https://github.com/jgreid/constructed-beings-ontology},
  note         = {Dataset and ontology schema}
}
```

## Related

This dataset accompanies the essay **"Tears in Rain"**, published on Substack at [tearsinrain.ai](https://tearsinrain.ai). The essay develops the interpretive argument; the dataset provides the evidence base.

## Author

**Jeff Reid** ([GitHub: @jgreid](https://github.com/jgreid)) -- writer, technologist, and reluctant ontologist. Jeff's work sits at the intersection of narrative theory and artificial intelligence, asking what stories about constructed beings reveal about the assumptions we carry into building real ones.

## License

This project is released under the **CC BY 4.0** (Creative Commons Attribution 4.0 International) license. See [LICENSE](LICENSE) for details.
