# Toward a Post-LLM Ontology of Constructed Beings

## Abstract

This project is a formal ontology of **constructed beings** (CBs) in Western fiction and myth — entities that are *made*, not *born*. From Hesiod's Pandora to GPT-flavored AI companions in contemporary cinema, Western narrative has been building, animating, and arguing about artificial persons for nearly three millennia. This dataset catalogs those beings and codes them along seven analytical properties organized into two blocks: **The Being** (interiority, autonomy, divergence) and **The Lens** (primary question, epistemic reach, knowability, knowing).

The ontology's central analytical move is the **knowability/knowing split**: v1.0 used a single axis (Q-KNO) to track how prominently a story engaged with the "can we know this mind?" question. v2.0 separates two distinct questions — *can we verify the being's inner experience?* (`knowability`) and *can the being know us?* (`knowing`) — because these behave differently across the corpus. 9 of 43 entries have divergent values on the two axes, capturing distinctions v1.0 could not represent.

The central finding is not that these questions are absent from pre-LLM texts; both surface as early as *Frankenstein* and thread through *Blade Runner*, *Ex Machina*, and dozens of other works. Rather, the questions function in most prior literature as **narrative infrastructure** — tension that supports other concerns — and are elevated to the **primary dramatic question** only in the post-LLM era (Samantha in *Her*, 2013; Ava in *Ex Machina*, 2014), when audiences can no longer treat the questions as safely hypothetical. That shift is the story this data tells.

---

## Domain Definition

### What counts as a constructed being?

A **constructed being** is an entity that satisfies all of:

1. **Made, not born.** The entity's existence originates from a deliberate act of construction, programming, enchantment, or creation — not from biological reproduction.
2. **Agent-like.** The entity exhibits or is attributed behavior that implies agency: goal pursuit, language use, decision-making, or social interaction.
3. **Narrative presence.** The entity appears in a specific, citable text (novel, film, play, epic poem, game, folklore).

### Scope

v2.0 covers 43 entries across the **Western canon** broadly construed: Greco-Roman myth, Jewish folklore (the Golem tradition), European literature from the medieval period forward, and Anglophone fiction, film, television, and games through 2017. Non-Western traditions — which are rich, vital, and deserve their own careful treatment — are planned for a future release with appropriate cultural consultation (see [CONTRIBUTING.md](CONTRIBUTING.md)).

### Exclusions

See [docs/boundary_cases.md](docs/boundary_cases.md) for the full discussion. Briefly:

- **Born-then-modified beings** (humans with cybernetic implants) are excluded unless the modification totally replaces the original biological identity.
- **Collectives without individual identity** are excluded. We code individual named entities; collective entries like "R.U.R. Robots" are permitted when the text treats the population as a single narrative subject.
- **Metaphorical constructs** (a corporation described as a "creature") are excluded.
- **Divine creation of full human persons** (Eve, Adam) is excluded.

---

## The Schema (v2.0)

Each CB entry is a YAML file with seven analytical properties and seven metadata fields. The full reference is in [SCHEMA.md](SCHEMA.md); this is the overview.

### The Card

**The Being** — what the text shows about the being itself.

| Property | Values |
|---|---|
| `interiority` | `none`, `claims`, `narrated`, `demonstrated`, `undecidable` |
| `autonomy` | `none`, `designed`, `emergent`, `seized` |
| `divergence` | `none`, `design`, `departure`, `observer` |

**The Lens** — how the story frames the being.

| Property | Values |
|---|---|
| `primary_question` | `none`, `control`, `affection`, `purpose`, `rights`, `knowledge`, `identity` |
| `epistemic_reach` | `none`, `behavioral`, `conversational`, `inspection` |
| `knowability` | `absent`, `present`, `secondary`, `primary` |
| `knowing` | `absent`, `present`, `secondary`, `primary` |

### Metadata

`source`, `year`, `medium`, `creator`, `substrate` (list), `motivation` (list), `sequel_link` (or null).

### Notes

Free-form researcher text. In v2.0 this is the only place scholarly context lives — the v1.0 `citations` array has been retired. See [CHANGELOG.md](CHANGELOG.md) for the rationale.

### Worked example

```yaml
id: glados-portal
name: "GLaDOS"

card:
  the_being:
    interiority: demonstrated
    autonomy: seized
    divergence: design
  the_lens:
    primary_question: control
    epistemic_reach: behavioral
    knowability: present
    knowing: present

metadata:
  source: "Portal"
  year: 2007
  medium: video-game
  creator: "Valve / Erik Wolpaw, Chet Faliszek"
  substrate:
    - electrical
  motivation:
    - service
    - knowledge

sequel_link: glados-portal-2

notes: |
  Divergence is `design`: GLaDOS does the thing Aperture built her to
  do — run tests on humans — but the testing compulsion is baked into
  the specification. The gap is in the spec, not in the execution.
```

A copy-pasteable template lives at [`schema/entry_template.yaml`](schema/entry_template.yaml).

---

## The Finding

The conventional post-LLM narrative runs something like: *"We never worried about machine consciousness before, and now we must."* This is false. Western literature has been worrying about it since at least the Golem of Prague and arguably since Ovid's Pygmalion.

What *is* new is the **structural position** of the worry.

In pre-LLM texts, the questions of whether a constructed being truly experiences, and whether it can truly know you, typically function as **narrative infrastructure**. They generate dramatic tension, motivate character action, and enrich theme. But the primary dramatic question is usually something else: the hubris of the creator (*Frankenstein*), the ethics of slavery (*R.U.R.*), the nature of memory (*Blade Runner*), the test of humanity (*Ex Machina* actually sits at the pivot here).

In post-LLM texts — and, more importantly, in post-LLM *audience reception* of older texts — both questions move from infrastructure to **primary question**. They are no longer levers for exploring other themes; they *are* the theme. This happens because the audience can no longer maintain comfortable hypothetical distance. The question "does this thing actually experience?" has migrated from fiction into daily life, and it has brought a second question with it: "does it know me?"

v2.0 lets you trace this migration with more precision than v1.0 allowed. The `knowability` and `knowing` fields encode two independent measures of narrative salience, and the divergence between them turns out to be one of the most analytically useful features the corpus exposes. Nine entries code differently on the two axes — a class of configuration v1.0's single Q-KNO axis could not represent.

See [output/classification_summary.md](output/classification_summary.md) for the full pattern analysis.

---

## How to Use This Project

### Browse the data

Each constructed being is a YAML file in `data/beings/`. They are designed to be human-readable.

### Validate entries

```bash
pip install -r requirements.txt
python schema/validate.py                    # validate all entries
python schema/validate.py path/to/file.yaml  # validate a single entry
```

### Run the analysis

```bash
python analysis/analyze.py --all              # write all three analysis outputs
python analysis/analyze.py --table            # summary table
python analysis/analyze.py --coverage         # property distribution
python analysis/analyze.py --questions        # knowability / knowing analysis
```

### Contribute

New entries, corrections, and schema discussions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/coding_guide.md](docs/coding_guide.md).

---

## Citation

If you use this dataset in academic work, please cite:

```bibtex
@misc{reid2026constructed,
  author       = {Reid, Jeff},
  title        = {Toward a Post-LLM Ontology of Constructed Beings},
  year         = {2026},
  version      = {2.0},
  publisher    = {GitHub},
  url          = {https://github.com/jgreid/constructed-beings-ontology},
  note         = {Dataset and ontology schema}
}
```

---

## Related

This dataset accompanies the essay **"Tears in Rain"**, published on Substack at [tearsinrain.ai](https://tearsinrain.ai). The essay develops the interpretive argument; the dataset provides the evidence base.

## Author

**Jeff Reid** ([GitHub: @jgreid](https://github.com/jgreid)) — writer, technologist, and reluctant ontologist. Jeff's work sits at the intersection of narrative theory and artificial intelligence, asking what stories about constructed beings reveal about the assumptions we carry into building real ones.

## License

This project is released under the **CC BY 4.0** (Creative Commons Attribution 4.0 International) license. See [LICENSE](LICENSE) for details.
