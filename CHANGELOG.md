# Changelog

All notable changes to the Constructed Beings Ontology are documented here.

---

## [2.0.0] — 2026-04

**Breaking change release.** v2.0 is a ground-up restructure of the schema, the vocabulary, the analysis scripts, and the entry corpus. If you had tooling pinned to v1.0, it will not work against v2.0 without rewriting. See the migration notes below.

### Summary

v1.0 grew organically to 14+ analytical axes, verbose nested YAML (`source`/`creator`/`being`/`relationship` objects), a required `citations` array, and a mnemonic code vocabulary (`Q-KNO`, `I-NAR`, `S-HYB`, etc.). v2.0 reduces to **seven analytical properties in two blocks** with plain lowercase tokens, drops the citations array in favor of free-text `notes`, and introduces a **one entry per source text** rule that expands the corpus from 37 to 44 entries.

### New

- **Two-block card structure.** Every entry now has `card.the_being` (interiority, autonomy, divergence) and `card.the_lens` (primary_question, epistemic_reach, knowability, knowing). Seven properties total, down from 14+.
- **`divergence` axis.** Measures the gap between creator intent and actual outcome. Values: `none`, `design` (the spec was the problem), `departure` (it left the spec), `observer` (the gap is in perception). Every entry has been coded on this new axis.
- **Knowability / knowing split.** v1.0 had a single `q_kno_status` axis. v2.0 splits it into `knowability` (can we verify its mind?) and `knowing` (can it know us?), because these behave differently across the corpus. 10 of 44 entries now have divergent values on the two axes.
- **`primary_question` values added:** `identity` (what am I?) and `none` (the story doesn't ask a question about this being). Nine entries were reclassified into these new buckets.
- **`primary_question` values merged:** `obedience` + `control` → `control`. `fellow-feeling` + `love` → `affection`.
- **Sequel-split rule.** One entry per source text. Films, novels, and games always split; TV/serials/comics split only when card properties meaningfully change. The corpus expanded from 37 to 44 entries as a result.
- **`sequel_link` field.** Chains related entries (older → newer → null). Covers sequels, successor beings, and adaptations.
- **`schema/entry_template.yaml`.** A real, validatable template file. Copy-paste for new entries.
- **`analysis/analyze.py`.** Single entry point replacing three v1 scripts. Flags: `--table`, `--coverage`, `--questions`, `--all`.
- **`CHANGELOG.md`.** This file.
- **Sequel splits added:**
  - `t-800-terminator` + `t-800-t2`
  - `glados-portal` + `glados-portal-2`
  - `cortana-halo` + `cortana-halo-4`
  - `jarvis-iron-man` + `vision-age-of-ultron`
  - `replicants-dick-novel` + `replicants-blade-runner` + `k-blade-runner-2049`
  - `agent-smith-matrix` + `agent-smith-reloaded`

### Changed

- **Vocabulary lowercased.** v1 codes like `Q-KNO`, `M-SRV`, `I-NAR`, `A-EMR`, `NCT-YES` are all replaced with plain lowercase tokens (`knowledge`, `service`, `narrated`, `emergent`, etc.).
- **YAML structure flattened.** v1's nested `source`, `creator`, `being`, `relationship` objects are replaced with `card.the_being`, `card.the_lens`, and `metadata`.
- **`substrate` is now a list.** v1 had a separate `S-HYB` value for hybrids. v2.0 expresses hybrids as multiple entries in the list (`[mechanical, electrical]`).
- **`interiority: denied` removed.** Entries previously coded `denied` (Olympia, Skynet) have been re-coded. Per the brief's rationale: Olympia → `undecidable` (the whole story is about not being able to tell); Skynet → `none` (the films don't engage with Skynet's inner life at all).
- **`autonomy: ambiguous` removed.** GIR was re-coded from `ambiguous` to `designed` (designed to be a servant robot, catastrophically bad at it — that's malfunction, not ambiguity).
- **Schema version bumped** from `"1.0"` to `"2.0"` in `schema/cb-schema.yaml`.
- **Validator rewritten.** `schema/validate.py` is about half the size of the v1 version (the new schema is simpler), still hand-rolled with no new dependencies, and now checks `sequel_link` cross-references across the full corpus.
- **`classification_summary.md` rewritten.** New schema overview, new pattern analysis, and a new section explaining what v2.0 surfaces that v1.0 hid.
- **`README.md`, `CONTRIBUTING.md`, `docs/coding_guide.md`, `docs/boundary_cases.md`** all rewritten for v2.0.

### Removed

- **`citations` array.** This is the most significant methodological change in the release. v1.0 required every entry to carry a structured `citations` list — property, text, location, optional note — supporting each coding decision. v2.0 removes this field entirely. Scholarly context now lives in the free-text `notes` field.

  **Rationale.** The v1 citations field was doing less analytical work than it claimed. In practice it documented coding decisions at a level of fidelity that was already possible in `notes`, and the schema constraint of "at least one citation required" produced a lot of citation-shaped filler without improving the dataset's rigor. Removing the structured field forces scholarly context to live in prose, where it can say what it needs to say. The cost is that v2.0 is a **curated index** rather than an **evidenced ontology**. The benefit is that the curation is clearer about what it is.

  If you need the old citations, they remain in git history before the v2.0 migration commit.

- **`creation_morality` axis.** v1 had `CM-MOR`, `CM-IMM`, `CM-AMO`, `CM-AMB`, `CM-RET`. v2.0 has no moral framing field. Moral context about the act of creation now goes in `notes` along with everything else narratively specific. This is a real analytical loss and is called out here because someone will ask.
- **`narrative_role` axis.** v1 had `NR-SUB`, `NR-MAJ`, `NR-MIN`, `NR-BKG` (subject, major, minor, background). v2.0 has no prominence field. If you want to filter by narrative prominence, add that information to `notes` in each entry.
- **`reproductive_method` axis.** v1 had `made`, `born-sexual`, `born-clonal`, `born-parthenogenic`, `born-divine`, `ambiguous`. v2.0 defines constructed beings via the three-criteria test (made, agent-like, narrative presence) and does not record a separate reproductive method. This changes the status of boundary cases like Eve (see below).
- **`aliases` field.** Removed. v2.0 records a single canonical name per entry.
- **`source.tradition` field.** Removed. Cultural tradition information, where relevant, goes in `notes`.
- **`source.author` field.** Removed. Author information is folded into `metadata.creator`, which can accommodate phrases like "Ridley Scott (Tyrell Corporation in-narrative)."
- **`creator` nested object.** v1 had a top-level `creator` object with `name`, `motivation`, and `creation_morality` subfields. v2.0 flattens this: `creator.name` is now the simple string `metadata.creator`; `creator.motivation` is now the list `metadata.motivation` at the metadata level; `creator.creation_morality` is deleted outright (see above).
- **`source` nested object.** v1 had a top-level `source` object with `author`, `title`, `year`, `medium`, `tradition` subfields. v2.0 flattens this into `metadata.source` (title as string), `metadata.year`, `metadata.medium`, with author information folded into `metadata.creator` and `tradition` retired. Nothing in v2.0 references the old nested object layout.
- **`medium` enum values** `myth`, `opera`, and `sacred-text`. Removed. None of the 44 v2.0 entries use these values (the v1 corpus only used `sacred-text` for the Eve boundary case, which is also retired). If a future entry needs one of these media, re-add the value to the enum with a CHANGELOG entry.
- **`being.mortality`** (`L-MOR`, `L-IMM`, `L-DES`, `L-RES`, `L-EPH`, `L-UNK`). Removed.
- **`being.multiplicity`** (`MU-ONE`, `MU-FEW`, `MU-MAN`, `MU-INF`). Removed.
- **`being.memory_persistence`** (`P-NON`, `P-CON`, `P-WIP`, `P-SES`, `P-SEL`, `P-UNK`). Removed.
- **`being.nonconsensual_transformation`** (`NCT-YES`, `NCT-NO`, `NCT-NA`). Removed. The Caroline/GLaDOS case, which this axis was designed to capture, now lives in the `notes` for `glados-portal` and `glados-portal-2`.
- **`being.autonomy_trajectory`** free-text field. Removed; trajectory discussion goes in `notes`.
- **`relationship.failure_mode` list** (`F-EXC`, `F-REV`, `F-DEM`, `F-AUT`, `F-IND`, `F-MUT`, `F-NON`, `F-OTH`). Removed. The most important distinction this axis captured — `F-EXC` (exceeded) vs. others — has been subsumed into the new `divergence` axis.
- **`relationship.question` list.** Removed. v2.0 keeps only `primary_question` and drops the multi-value list. The primary question was always doing most of the analytical work; the list was mostly documenting runners-up.
- **`relationship.q_kno_status`**. Removed (see Changed → Knowability/Knowing split).
- **`analysis/generate_table.py`, `analysis/property_coverage.py`, `analysis/question_analysis.py`.** Removed. Their functionality is merged into `analysis/analyze.py`.
- **`analysis/influence_graph.yaml`, `analysis/influence_graph.html`.** Removed. These encoded v1-specific narrative-influence claims hardwired to Q-KNO axis propagation. Retired pending v2-native re-analysis.
- **`analysis/analysis_notes.md`, `analysis/qkno_paths.md`.** Removed. These were hypothesis documents for v1's single Q-KNO axis; the thesis survives into v2.0 (see `output/classification_summary.md`) but the specific hand-written documents are retired.
- **`docs/property_definitions.md`.** Removed. [`SCHEMA.md`](SCHEMA.md) now subsumes it — the v2.0 property count is small enough that a separate reference doc added friction without adding clarity.
- **`data/boundary_cases/eve-genesis.yaml`.** Removed. The v1 entry existed specifically to make the `born-divine` vs. `made` distinction visible. v2.0 has no `reproductive_method` axis, so Eve no longer has a schema reason to be a boundary case. See [`docs/boundary_cases.md`](docs/boundary_cases.md) for the new treatment.

### Reclassifications from v1

Several entries had their codings change beyond a simple vocabulary translation. Each of these has its rationale documented in the entry's `notes` field.

- **Pinocchio**: primary_question `fellow-feeling` → `identity`. "Can I become a real boy?" is an identity arc.
- **Iron Giant**: primary_question `purpose` → `identity`. "I am not a gun" is refusing an identity.
- **Westworld Hosts (Dolores)**: primary_question `fellow-feeling` → `identity`. Her arc is remembering who she is.
- **Sonny**: primary_question `obedience` → `identity`. "Can a robot have a soul?"
- **Olympia**: primary_question `purpose` → `identity`; interiority `denied` → `undecidable`.
- **Pandora**: primary_question `obedience` → `purpose`. The myth asks what she's for.
- **EMERAC, Talos, GIR, C-3PO**: primary_question → `none`. These are furniture/obstacle beings; the stories don't ask questions about them.
- **R2-D2**: primary_question `obedience` → `control`. The tension is always whether anyone can actually control him.
- **Skynet**: interiority `denied` → `none`. The films don't engage.
- **T-800 (original)**: interiority `claims` → `none`. The first film is not philosophical; the T-800 doesn't claim anything.
- **GIR**: autonomy `ambiguous` → `designed`. Malfunction, not ambiguity.
- **HAL 9000**: divergence coded as `design`, not `departure`. HAL's breakdown is predictable output of a bad specification, not a being going rogue.
- **Skynet, Smith, Creature, SHODAN, etc.**: divergence coded as `departure`. These are the beings that left their blueprints behind.

### Migration notes

- **Raw entry count:** 37 → 44.
- **Sequel splits added:** 7 new entries (one T-800, one GLaDOS, one Cortana, one Vision, two Replicants/K, one Agent Smith).
- **File renames:** `glados.yaml` → `glados-portal.yaml`, `jarvis-vision-mcu.yaml` split into `jarvis-iron-man.yaml` and `vision-age-of-ultron.yaml`, `replicants.yaml` split into three files, `eve-genesis.yaml` removed.
- **Tooling break:** anything depending on `relationship.q_kno_status`, `being.autonomy`, `being.interiority`, or the nested v1 structure will break. Rewrite against `card.the_being.*` and `card.the_lens.*`.
- **Validator break:** v1 mnemonic codes are rejected by the v2 validator. The error messages will show the valid v2 enum values.
- **Git recoverability:** the full v1 entry corpus, including Eve and the v1 analysis artifacts, lives in git history before this release.

### Known issues carried forward into v2.0

- **Agent Smith duplication.** The Matrix (1999) and Matrix Reloaded/Revolutions (2003) entries have identical card values under v2.0. Both exist per the "one entry per film" scope rule, and the redundancy is noted in each entry's `notes` field. A future editor may collapse them.
- **Knowability/knowing divergence is 10 of 44.** The draft spec expected ≥12 divergent entries. The current corpus codes 10, which is above the re-review threshold (<10) but below target. No individual entry has been re-coded for this reason; the pattern is documented in `output/classification_summary.md`.
- **Hosts (Dolores)** collapses a polyphonic ensemble into one entry. Maeve would code differently. A future release may split this.

---

## [1.0.0] — 2025

Initial release. 37 entries, 14+ analytical axes, verbose nested YAML, mnemonic code vocabulary, structured citations array. See git history before the v2.0 migration commit for the complete v1 schema.
