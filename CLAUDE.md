# CLAUDE.md

Project context for AI-assisted development of the Constructed Beings Ontology.

## What this project is

A formal ontology of **constructed beings** in fiction — entities that are *made*, not *born*. 332 YAML entries coded against a seven-property analytical schema, spanning Homer (~750 BCE) through 2025. The dataset accompanies the essay "Tears in Rain" at tearsinrain.ai.

## Repository structure

```
data/beings/          332 YAML entry files (the corpus)
data/boundary_cases/  Entries on the definitional edge
data/exclusions.yaml  Entities considered and excluded
schema/cb-schema.yaml Machine-readable schema definition
schema/validate.py    Python validator
schema/entry_template.yaml  Copy-paste template for new entries
analysis/analyze.py   Analysis script (generates all outputs)
analysis/influence_graph.yaml  Textual lineage graph
analysis/influence_graph.html  Interactive visualization
output/               Generated analysis outputs (do not hand-edit)
docs/                 Methodology, coding guide, boundary cases, bibliography
```

## Key commands

```bash
# Install dependencies
pip install -r requirements.txt

# Validate all entries
python schema/validate.py

# Validate a single entry
python schema/validate.py data/beings/<id>.yaml

# Validate the entry template
python schema/validate.py schema/entry_template.yaml

# Generate all analysis outputs
python analysis/analyze.py --all

# Individual analysis outputs
python analysis/analyze.py --table       # summary_table.md
python analysis/analyze.py --coverage    # property_coverage.md
python analysis/analyze.py --questions   # question_analysis.md
python analysis/analyze.py --timeline    # timeline_analysis.md
python analysis/analyze.py --metadata    # metadata_analysis.md
python analysis/analyze.py --graph       # influence_graph.html
```

## Schema overview

Each entry has **seven analytical properties** in two blocks:

- **The Being:** `interiority`, `autonomy`, `divergence`
- **The Lens:** `primary_question`, `epistemic_reach`, `knowability`, `knowing`

Plus **eleven metadata fields:** `source`, `year`, `medium`, `creator`, `substrate` (list), `motivation` (list), `presentation`, `embodiment`, `prominence`, `creator_relationship`, `tags` (list).

Top-level fields: `id`, `name`, `card`, `metadata`, `sequel_link`, `link_type`, `notes`.

## Controlled vocabularies (quick reference)

- **interiority:** none | claims | narrated | demonstrated | undecidable
- **autonomy:** none | designed | emergent | seized
- **divergence:** none | design | departure | observer
- **primary_question:** none | control | affection | purpose | rights | knowledge | identity
- **epistemic_reach:** none | behavioral | conversational | inspection
- **knowability/knowing:** absent | present | secondary | primary
- **medium:** poem | epic | folklore | play | opera | ballet | musical | novel | short-story | comics | film | television | video-game
- **substrate:** mechanical | biological | electrical | magical | cloned | linguistic
- **motivation:** service | knowledge | power | companionship | art | mirror | child | other
- **presentation:** masculine | feminine | androgynous | none | variable
- **embodiment:** embodied | disembodied | projected | virtual
- **prominence:** foundational | major | supporting | minor
- **creator_relationship:** servile | loyal | indifferent | resentful | rebellious | patricidal | absent
- **tags:** canonical | love-story | rebellion | turing-test | passing | creator-conflict | child-arc | military | comedy | horror | philosophical | ensemble-split
- **link_type:** sequel | adaptation | successor

## Coding principles

1. **Code what the text shows, not what you infer.** The schema describes the source work, not the being or audience reception.
2. **`none` vs `absent` are different zero states.** Being properties use `none` (the being doesn't have it). Knowability/knowing use `absent` (the story doesn't engage with the question).
3. **One entry per source text.** Films always split. TV/comics split only when card values meaningfully diverge.
4. **IDs are kebab-case** and match filenames: `data/beings/<id>.yaml`.
5. **Notes do the work citations used to do.** Flag uncertainty, explain close calls, cite scenes.
6. **Use the closest enum value and flag the mismatch** in notes if the fit is bad.

## Common tasks

### Adding a new constructed being

1. Copy `schema/entry_template.yaml` to `data/beings/<id>.yaml`
2. Code all seven card properties and eleven metadata fields
3. Write the `notes` field — explain close calls and distinctive features
4. Set `sequel_link` and `link_type` (or null)
5. Run `python schema/validate.py data/beings/<id>.yaml`
6. If the being is part of a lineage, check that `sequel_link` targets exist
7. Consider adding edges to `analysis/influence_graph.yaml`
8. Regenerate outputs: `python analysis/analyze.py --all`

### Reviewing or correcting an entry

1. Read the entry's current coding and notes
2. Read the source text (or watch the film/play the game)
3. Compare against SCHEMA.md definitions and docs/coding_guide.md decision tests
4. Edit the entry, update notes with re-coding rationale
5. Run validation and regenerate analysis

### Checking corpus stats

- Entry count: `ls data/beings/*.yaml | wc -l`
- Divergence count (knowability != knowing): check `output/question_analysis.md`
- Property distributions: check `output/property_coverage.md`
- Primary/primary cluster: check `output/timeline_analysis.md` section 4

## Files that should NOT be hand-edited

- `output/summary_table.md` — generated by `analyze.py --table`
- `output/property_coverage.md` — generated by `analyze.py --coverage`
- `output/question_analysis.md` — generated by `analyze.py --questions`
- `output/timeline_analysis.md` — generated by `analyze.py --timeline`
- `output/metadata_analysis.md` — generated by `analyze.py --metadata`
- `analysis/influence_graph.html` — generated by `analyze.py --graph`

These are regenerated from the corpus. Edit the YAML entries, then regenerate.

`output/classification_summary.md` IS hand-written interpretation and can be edited directly.

## Version

Current: **v2.4.5** (schema version in `schema/cb-schema.yaml`). See CHANGELOG.md for history.

## References

- Full schema reference: SCHEMA.md
- Coding judgment calls: docs/coding_guide.md
- Boundary case rationale: docs/boundary_cases.md
- Contribution guidelines: CONTRIBUTING.md
- Methodology and reliability: docs/methodology.md
- Bibliography of source texts: docs/bibliography.md
