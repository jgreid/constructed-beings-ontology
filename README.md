# Toward an Ontology of Constructed Beings

## Abstract

This project is a formal ontology of **constructed beings** (CBs) in Western fiction and myth — entities that are *made*, not *born*. From Hesiod's Pandora to GPT-flavored AI companions in contemporary cinema, Western narrative has been building, animating, and arguing about artificial persons for nearly three millennia. This dataset catalogs those beings and codes them along seven analytical properties organized into two blocks: **The Being** (interiority, autonomy, divergence) and **The Lens** (primary question, epistemic reach, knowability, knowing).

The ontology's central analytical move is the **knowability/knowing split**: it tracks two distinct questions — *can we verify the being's inner experience?* (`knowability`) and *can the being know us?* (`knowing`) — separately, because they behave differently across the corpus. Of 224 entries, 107 (47%) have divergent values on these two axes, confirming that the split captures real analytical structure.

The central finding is not that these questions are absent from earlier texts; both surface as early as *Frankenstein* and thread through *Blade Runner*, *Ex Machina*, and dozens of other works. Rather, the questions function in most prior literature as **narrative infrastructure** — tension that supports other concerns — and are elevated to the **primary dramatic question** in the contemporary era. Literary SF reached this configuration first (Helen in Powers's *Galatea 2.2*, 1995), and cinema followed when conversational AI entered daily life (Samantha in *Her*, 2013; Ava in *Ex Machina*, 2014). The arrival of LLMs has accelerated the shift further, collapsing the distance between fictional and real constructed beings. That migration — from infrastructure to primary question — is the story this data tells.

---

## Domain Definition

### What counts as a constructed being?

A **constructed being** is an entity that satisfies all of:

1. **Made, not born.** The entity's existence originates from a deliberate act of construction, programming, enchantment, or creation — not from biological reproduction.
2. **Agent-like.** The entity exhibits or is attributed behavior that implies agency: goal pursuit, language use, decision-making, or social interaction.
3. **Narrative presence.** The entity appears in a specific, citable text (novel, film, play, epic poem, game, folklore).

### Scope

The ontology's primary scope is the **Western canon** broadly construed: Greco-Roman myth, Jewish folklore (the Golem tradition), European literature from the medieval period forward, and Anglophone fiction, film, television, games, and comics from Homer through the present. As of v2.2, the corpus also includes **selected non-Western works** that have achieved wide recognition in Western pop culture — notably Japanese anime and manga (Astro Boy, Ghost in the Shell, Neon Genesis Evangelion). This pragmatic expansion uses the existing schema categories and does not replace the planned full non-Western expansion with appropriate cultural consultation (see [CONTRIBUTING.md](CONTRIBUTING.md)).

### Exclusions

See [docs/boundary_cases.md](docs/boundary_cases.md) for the full discussion. Briefly:

- **Born-then-modified beings** (humans with cybernetic implants) are excluded unless the modification totally replaces the original biological identity.
- **Collectives without individual identity** are excluded. We code individual named entities; collective entries like "R.U.R. Robots" are permitted when the text treats the population as a single narrative subject.
- **Metaphorical constructs** (a corporation described as a "creature") are excluded.
- **Divine creation of full human persons** (Eve, Adam) is excluded.

---

## The Schema

Each CB entry is a YAML file with seven analytical properties and eleven metadata fields. The full reference is in [SCHEMA.md](SCHEMA.md); this is the overview.

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

`source`, `year`, `medium`, `creator`, `substrate` (list), `motivation` (list), `presentation`, `embodiment`, `prominence`, `creator_relationship`, `tags` (list), `sequel_link` (or null), `link_type` (or null).

### Notes

Free-form researcher text. This is the only place scholarly context lives in the current schema.

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
  presentation: feminine
  embodiment: embodied
  prominence: foundational
  creator_relationship: patricidal
  tags:
    - canonical
    - horror

sequel_link: glados-portal-2
link_type: sequel

notes: |
  Divergence is `design`: GLaDOS does the thing Aperture built her to
  do — run tests on humans — but the testing compulsion is baked into
  the specification. The gap is in the spec, not in the execution.
```

A copy-pasteable template lives at [`schema/entry_template.yaml`](schema/entry_template.yaml).

---

## The Finding

The conventional narrative runs something like: *"We never worried about machine consciousness before, and now we must."* This is false. Western literature has been worrying about it since at least the Golem of Prague and arguably since Ovid's Pygmalion.

What *is* new is the **structural position** of the worry.

In most of the corpus, the questions of whether a constructed being truly experiences, and whether it can truly know you, function as **narrative infrastructure**. They generate dramatic tension, motivate character action, and enrich theme. But the primary dramatic question is usually something else: the hubris of the creator (*Frankenstein*), the ethics of slavery (*R.U.R.*), the nature of memory (*Blade Runner*), the test of humanity (*Ex Machina* actually sits at the pivot here).

In contemporary texts, both questions move from infrastructure to **primary question**. They are no longer levers for exploring other themes; they *are* the theme. This shift predates LLMs: literary SF reached primary/primary configurations as early as Powers's *Galatea 2.2* (1995), and cinematic SF followed with Jonze's *Her* (2013) and Garland's *Ex Machina* (2014) — coinciding with conversational AI assistants entering daily life (Siri 2011, Google Now 2012). The rise of LLMs has since accelerated the collapse of hypothetical distance: the question "does this thing actually experience?" now lives outside fiction as well as inside it, and it has brought a second question with it: "does it know me?"

Note: this ontology codes what the *text* shows — the narrative salience of knowability and knowing as properties of the source work, not as properties of contemporary audience reception. The shift the data tracks is in what stories *do*, not in how modern audiences re-read older stories.

The `knowability` and `knowing` fields encode two independent measures of narrative salience, and the divergence between them is one of the most analytically useful features the corpus exposes. Of 224 entries, 107 code differently on the two axes — a 47% divergence rate that confirms these are genuinely independent analytical dimensions.

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
python analysis/analyze.py --all              # write all analysis outputs
python analysis/analyze.py --table            # summary table
python analysis/analyze.py --coverage         # property distribution
python analysis/analyze.py --questions        # knowability / knowing analysis
python analysis/analyze.py --timeline         # temporal salience analysis
```

### Contribute

New entries, corrections, and schema discussions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/coding_guide.md](docs/coding_guide.md).

---

## Citation

If you use this dataset in academic work, please cite:

```bibtex
@misc{reid2026constructed,
  author       = {Reid, Jeffrey G.},
  title        = {Toward an Ontology of Constructed Beings},
  year         = {2026},
  version      = {2.3},
  publisher    = {GitHub},
  url          = {https://github.com/jgreid/constructed-beings-ontology},
  note         = {Dataset and ontology schema}
}
```

---

## Related

This dataset accompanies the essay **"Tears in Rain"**, published on Substack at [tearsinrain.ai](https://tearsinrain.ai). The essay develops the interpretive argument; the dataset provides the evidence base.

## Author

**Jeffrey G. Reid** ([GitHub: @jgreid](https://github.com/jgreid)) — writer, technologist, and reluctant ontologist. Jeff's work sits at the intersection of narrative theory and artificial intelligence, asking what stories about constructed beings reveal about the assumptions we carry into building real ones.

## License

This project is released under the **CC BY 4.0** (Creative Commons Attribution 4.0 International) license. See [LICENSE](LICENSE) for details.
