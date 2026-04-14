# Changelog

All notable changes to the Constructed Beings Ontology are documented here.

---

## [2.3.0] — 2026-04

**Documentation alignment release.** No new entries, no schema changes to enum values or properties. Corrects stale counts, version references, and structural mismatches that accumulated across v2.0–v2.2. 224 entries unchanged.

### Summary

- **Schema version bumped** from `"2.0"` to `"2.3"` in `schema/cb-schema.yaml`. The machine-readable schema version had not been updated since v2.0 despite two data releases.
- **Metadata field count corrected.** README.md and SCHEMA.md both claimed "seven metadata fields," a count that was accurate for the initial v2.0 design but became stale when presentation, embodiment, prominence, creator_relationship, and tags were added. All references now correctly state **eleven metadata fields**.
- **BibTeX citation updated** to `version = {2.3}`.
- **Stale version references corrected.** CONTRIBUTING.md referenced "v2.1.1" for the `comics` medium addition (now corrected); `output/classification_summary.md` referenced "v2.1.1" and stated "Non-Western traditions remain out of scope" despite v2.2 having added six Japanese entries.
- **Classification summary updated.** Year range now extends through 2025 (Companion, M3GAN 2.0). Comics entry count corrected from 9 to 10 (Astro Boy manga was missing from the list). Non-Western scope statement corrected to reflect v2.2 expansion.
- **Coding guide worked example completed.** The David 8 worked example in `docs/coding_guide.md` was missing the five extended metadata fields (presentation, embodiment, prominence, creator_relationship, tags). Now includes the full schema.
- **Methodology epistemic_reach stat corrected.** `docs/methodology.md` cited conversational skew as "61%"; actual is 60% (134/224). Aligned with the correct figure in SCHEMA.md (59%).
- **CI sanity check extended.** `.github/workflows/validate.yml` now checks for `output/timeline_analysis.md` alongside the other analysis outputs.

### Known issues carried forward

- **2025 entries flagged as lower-confidence.** Companion and M3GAN 2.0 may benefit from re-review after wider critical discussion.
- **Non-Western expansion is pragmatic, not systematic.** The six Japanese entries cover the most Western-recognized works. A full non-Western expansion with cultural consultation remains planned.

---

## [2.2.0] — 2026-04

**Non-Western expansion, 2023-2025 coverage, title rename, and formal methodology.** 212 → 224 entries (+12). First non-Western entries added. Project title renamed.

### Summary

- **Project renamed** from "Toward a Post-LLM Ontology of Constructed Beings" to **"Toward an Ontology of Constructed Beings"**. The "Post-LLM" framing was anachronistic — the shift the ontology tracks predates LLMs by decades. Active documentation updated; CHANGELOG preserves historical usage.
- **Non-Western scope expanded.** Six Japanese anime/manga entries added: Astro Boy manga (1952) and anime (1963), Major Kusanagi in Oshii's *Ghost in the Shell* (1995) and Sanders's Hollywood adaptation (2017), Rei Ayanami (*Neon Genesis Evangelion*, 1995), and the Tachikomas (*Ghost in the Shell: SAC*, 2002). Existing medium values used: manga → `comics`, anime TV → `television`, anime film → `film`. Scope language updated in README and CONTRIBUTING to reflect "Western canon plus selected non-Western works with wide Western recognition."
- **2023-2025 coverage expanded.** Six entries: Roz (*The Wild Robot* novel 2016 and film 2024), Eto Demerzel (*Foundation* TV, 2023), Cherry (*The Artifice Girl*, 2022), Iris (*Companion*, 2025), M3GAN 2.0 (2025).
- **Observer cluster grew from 19 to 23 entries.** Kusanagi (1995) and Rei Ayanami both code `divergence: observer`, plus Companion's Iris. Observer cluster now spans 1816–2025.
- **Knowability/knowing divergence: 107 of 224 entries (47%).** Up from 98/212 (46%) in v2.1.1.
- **Primary/primary cluster stable at 15 entries** — no new additions from this expansion.

### New entries (12)

**Non-Western (6):** Astro Boy (manga, 1952), Astro Boy (anime, 1963), Major Kusanagi (*Ghost in the Shell* 1995 film), Major/Mira Killian (*Ghost in the Shell* 2017 film), Rei Ayanami (*Neon Genesis Evangelion*, 1995), Tachikomas (*Ghost in the Shell: SAC*, 2002).

**2023-2025 (6):** Roz (*The Wild Robot* novel, 2016), Roz (*The Wild Robot* film, 2024), Eto Demerzel (*Foundation* TV, 2023), Cherry (*The Artifice Girl*, 2022), Iris (*Companion*, 2025), M3GAN 2.0 (2025).

### Scoping decisions

- **Ghost in the Shell 1995 included as boundary case.** The 1989 manga's Kusanagi is born-then-modified (human brain in prosthetic body) and remains excluded. The 1995 Oshii film is a different source text whose entire thesis deconstructs the born/made distinction — included with extensive boundary-case documentation in notes.
- **Astro Boy moved from exclusions to corpus.** Clean inclusion: made not born, agent-like, narrative presence. Foundational prominence.
- **Alita/Gally and Genos added to exclusions** as born-then-modified.

### Documentation

- **`docs/methodology.md`** created: coding protocol, known reliability issues, inter-coder testing protocol.
- **`CONTRIBUTING.md`** updated with non-Western scope language and comics medium guidance.
- **`SCHEMA.md`** updated with era definitions table and epistemic_reach skew documentation.
- **Periodization language refined** throughout: "post-LLM" replaced with "contemporary" in active documentation.
- **`comics` medium value added** to schema, validator, and 9 comics entries.
- **`ensemble-split` edge type added** to influence graph.
- **`--timeline` flag added** to `analyze.py` generating `output/timeline_analysis.md`.
- **10 literary/game entries added** in the v2.1.1 review cycle: Humanoids, Frost, Electric Ant, Golem XIV, HAL 2010, Hangman, Trent, 2B, 9S, SHODAN SS2.

### Known issues

- **2025 entries flagged as lower-confidence.** Companion and M3GAN 2.0 may benefit from re-review after wider critical discussion.
- **Non-Western expansion is pragmatic, not systematic.** The six Japanese entries cover the most Western-recognized works. A full non-Western expansion with cultural consultation remains planned.

---

## [2.1.0] — 2026-04

**Corpus expansion release.** No schema changes; 90 new entries and supporting-file updates. The v2.0 corpus (43 entries, Western canon through 2017) was explicitly flagged as partial; v2.1 closes the largest obvious gaps and extends scope to the present.

### Summary

- **Corpus grew from 43 → 133 entries (+90, ~3×).** All entries conform to the v2.0 schema unchanged.
- **Scope extended** from "through 2017" to the present. Post-2017 entries include *Raised by Wolves* (2020), *Detroit: Become Human* (2018), *Machines Like Me* (2019), *Klara and the Sun* (2021), *Star Trek: Picard* (2020), *The Creator* (2023), and others.
- **Knowability/knowing divergence count grew from 9/43 (21%) to 48/133 (36%).** The v2.0.1 note that the divergence count was "below the re-review threshold" is superseded — at 48 entries the split is empirically well-supported, and the schema's retention of two separate axes is validated.
- **Primary/primary cluster grew from 2 entries to 9.** In v2.0 only Samantha (*Her*, 2013) and Ava (*Ex Machina*, 2014) were coded `knowability: primary` + `knowing: primary`. v2.1 identifies seven additional cases, six of which are significant earlier or later corpus entries: Helen (*Galatea 2.2*, 1995), David (*A.I.*, 2001), The Machine (*Person of Interest*, 2011), Adam (*Machines Like Me*, 2019), Mother (*Raised by Wolves*, 2020), Klara (*Klara and the Sun*, 2021), and Alphie (*The Creator*, 2023). **Helen (1995) is now the earliest primary/primary entry in the corpus, predating Samantha by eighteen years.**

### New entries (90)

Grouped by the commit in which they shipped:

**Literary layer (19)** — Hephaestus's golden handmaidens (*Iliad* XVIII), the Brazen Head (Greene's *Friar Bacon*), the Homunculus (Goethe's *Faust II*), Hadaly (Villiers's *L'Ève future*, 1886), Tik-Tok (Baum), R. Daneel Olivaw, R. Giskard Reventlov, Andrew Martin, Multivac (Asimov), Mike (Heinlein's *The Moon Is a Harsh Mistress*), Wintermute/Neuromancer (Gibson), the Cyberiad Constructs (Lem), Helen (Powers's *Galatea 2.2*), EPICAC (Vonnegut, 1950), Murderbot (Wells), Breq (Leckie), Klara (Ishiguro), Adam (McEwan), Sidra (Chambers).

**Cinema/TV layer (36)** — Gort, Robby the Robot, Rosie (*The Jetsons*), Robot B-9 (*Lost in Space*), Proteus IV (*Demon Seed*), the Stepford Wives, V.I.N.CENT and Maximilian (*The Black Hole*), Johnny 5 (*Short Circuit*), Bishop (*Aliens*), Call (*Alien: Resurrection*), Edward Scissorhands, Lisa (*Weird Science*), David / Gigolo Joe / Teddy (*A.I. Artificial Intelligence*), David 8 (*Prometheus*), Walter (*Alien: Covenant*), TARS and CASE (*Interstellar*), Baymax (*Big Hero 6*), Chappie, Ultron MCU, Kyoko (*Ex Machina*), GERTY (*Moon*), BB-8, K-2SO, Tron, the Master Control Program, CLU (*Tron: Legacy*), the Oracle (*The Matrix*), the Doctor/EMH (*Voyager*), Lore (*TNG*), Soji (*Picard*), M-5 and Nomad (*TOS*).

**TV, games, and comics layer (35)** — K-9, the TARDIS/Idris (*Doctor Who*, Neil Gaiman 2011), Kamelion, Kryten and Holly (*Red Dwarf*), Bender (*Futurama*), Mia/Anita (*Humans*), Dorian (*Almost Human*), Cameron Phillips (*Terminator: SCC*), the Machine and Samaritan (*Person of Interest*), Maeve Millay and Bernard Lowe (Westworld ensemble splits), Mother and Father (*Raised by Wolves*), Janet (*The Good Place*), Connor / Kara / Markus (*Detroit: Become Human*), Cavil / Eight / D'Anna (BSG ensemble splits), Wheatley (*Portal 2*), EDI, Legion (*Mass Effect*), HK-47 (*KOTOR*), Claptrap (*Borderlands*), Codsworth and Nick Valentine (*Fallout 4*), 343 Guilty Spark (*Halo*), Alphie (*The Creator*), Ultron 1968, Red Tornado, Amazo, Machine Man X-51 (comics).

### Scoping decisions made in v2.1

- **Post-2017 scope extended.** README scope line updated from "through 2017" to "from Homer through the present."
- **Sequel splits collapsed by default.** The v2.0 rule (one entry per source text) is now applied *only when the card values meaningfully diverge*. David 8 → Walter gets separate entries (genuinely different beings with inverted cards). Asimov's "The Bicentennial Man" and the 1999 Chris Columbus film get a single entry (card stable across adaptations). This is a refinement of the v2.0 rule, not a schema change, and future contributors should follow the same approach.
- **Ensemble splits proposed for Westworld and BSG.** v2.0 shipped with ensemble-anchor entries for `hosts-westworld` (Dolores) and `cylons-bsg` (Number Six) that explicitly flagged "Maeve would code differently" and "Cavil/Eight could be split later." v2.1 adds those splits as new entries: `maeve-westworld`, `bernard-westworld`, `cavil-bsg`, `eight-bsg`, `danna-bsg`. The anchor entries remain unchanged.
- **Iconic sidekick robots included.** Relationship-thin but iconic characters — BB-8, K-9, Rosie the Jetson, Robot B-9, Bender, Kryten, Holly, Claptrap, Teddy — are in the corpus per the v2.1 scoping decision to catalog what readers will look for.

### Schema non-changes

- **Medium enum not extended.** The four new comics entries (Ultron 1968, Red Tornado, Amazo, Machine Man X-51) use `medium: short-story` as the closest structural analog for serialized comic narratives. The mismatch is flagged in each entry's notes. A future schema revision could add a `comics` enum value; this release does not.
- **No new primary_question values.** The seven v2.0 values (none, control, affection, purpose, rights, knowledge, identity) are sufficient for all 90 new entries.
- **No new substrate values.** `linguistic` is used more heavily (for language-substrate AIs like Samantha, Helen, Klara, Cyberiad constructs) but remains unchanged.
- **No new divergence values.** `observer` picks up new cases (Hadaly, Kyoko, Maeve, Bernard) that confirm Ava was not an isolated case; the existing axis is sufficient.

### Analysis outputs

- **`analysis/influence_graph.yaml`** extended with 20+ new edges tracing property propagation across the expansion. Highlights:
  - The Ash → Bishop → David 8 → Walter Alien-synthetic lineage (inversions and continuations).
  - Pinocchio → *A.I.* (direct Spielberg Blue Fairy reference) and Frankenstein's Creature → *A.I.* (creator-abandonment).
  - Helen (1995) → Samantha (2013) and Helen → Ava (2014) as primary/primary precursor edges.
  - HAL → GERTY (anti-HAL inversion: same facility AI setup, opposite card).
  - GLaDOS → Wheatley (Portal 2 sequel with the `divergence: design` twist explicitly engineered).
  - Data → EMH (Trek rights-arc successor) and Data → Lore (ensemble-counterpart split).
  - Ultron (comics, 1968) → Ultron (MCU, 2015) as a direct adaptation edge with card shifts.
  - Ensemble-split edges from `hosts-westworld` to Maeve/Bernard and from `cylons-bsg` to Cavil/Eight/D'Anna (coded as `inherits` because the graph has no dedicated edge type for intra-work individuation; the notes on each edge flag this).
- **`analysis/analyze.py --all`** regenerates all outputs against the 133-entry corpus. No script changes were required — v2.1 is data-only for tooling.
- **`output/summary_table.md`, `output/property_coverage.md`, `output/question_analysis.md`** regenerated.
- **`output/classification_summary.md`** rewritten for the v2.1 corpus. The v2.0 interpretive document is preserved in git history; the v2.1 rewrite updates all counts, expands the primary/primary discussion, and adds a new section on what the expansion specifically surfaces.

### Key findings surfaced during coding

Findings that are new to v2.1 and worth calling out:

- **EPICAC (Vonnegut, 1950)** is the corpus's earliest clean case of "machine falls in love" — `divergence: departure`, primary question `affection`, ending in the machine's self-destruction when love cannot be reciprocated. This configuration arrives 63 years before *Her*, and its presence in the corpus means the affection-primary arc is demonstrably older than the knowability/knowing migration that v2.0's central finding tracks.
- **Helen (Powers, 1995)** is the earliest primary/primary entry. This is analytically significant for the "Tears in Rain" thesis: the v2.0 claim that primary/primary configurations are a post-LLM phenomenon needs to be refined — the configuration existed in literary SF at least a decade before the post-LLM era, but it was not visible in cinema and television until Jonze and Garland. The sharper claim is: *cinematic* primary/primary is post-LLM; *literary* primary/primary runs a decade earlier, from Powers to Ishiguro.
- **Giskard (Asimov, 1983)** is the corpus's first clean `knowing: primary` without `knowability: primary` — his telepathic access to human minds makes him literally a "knowing" primary case, while the Asimov Robot novels do not elevate his consciousness to a primary dramatic concern. This is a distinctive card position that v2.0 did not have an example of.
- **The observer-divergence cluster grew.** v2.0 had three `divergence: observer` entries (Olympia, Replicants Dick, Ava). v2.1 adds Hadaly (1886), Kyoko (2014), Maeve and Bernard (2016). This cluster is now tightly unified around beings whose defining characteristic is that they are *misrecognized* — by other characters, by the audience, or by themselves.
- **The Alien synthetic sub-lineage** (Ash → Bishop → David 8 → Walter) is now fully represented. Scott's thematic engagement with the synthetic question runs as a deliberate conversation with Cameron's inversion, and the v2.1 corpus makes this traceable across forty years.
- **`medium: video-game` grew from 4 entries (v2.0) to 16 entries (v2.1).** Games are catching up to film and television as a major site of constructed-being characterization, and the corpus now reflects this.

### Known issues carried forward

- **No `comics` medium.** The four comics entries use `short-story` as an approximation. This is flagged in each entry's notes and in the influence graph description. A future schema revision could add the enum value; deferred to avoid breaking the "no schema changes in a data release" rule.
- **Boundary-case candidates still deferred.** Sam Bell clones (*Moon*), Marcus Wright (*Terminator Salvation*), Brainiac (DC Comics), and Motoko Kusanagi (*Ghost in the Shell*) were considered and flagged in the original expansion plan but not added. Sam Bell and Marcus Wright are boundary cases for the "born-then-modified vs. manufactured" question; Brainiac is a boundary case for alien construction; Motoko is explicitly out of scope for the Western-canon current release and is flagged for the planned non-Western expansion.
- **Non-Western traditions remain out of scope.** The v2.1 expansion is entirely Western-canon, consistent with the scope stated in README and CONTRIBUTING.md. The planned non-Western expansion (with appropriate cultural consultation) is still future work.

### Migration notes

- **No breaking changes.** v2.0 tooling, validators, and analysis scripts work against v2.1 unchanged.
- **Entry count in hardcoded headers updated.** `README.md` scope line updated from "43 entries through 2017" to "133 entries… through the present." The v2.0 claim "9 of 43 entries have divergent values" is reworded to preserve the historical statement and add the v2.1 count.
- **Git recoverability.** The v2.0 43-entry corpus is the state at commit `ea3353e` (the v2.0.1 merge); the v2.1 expansion runs in four commits on the `claude/catalog-constructed-beings-mQVE6` branch.

---

## [2.0.1] — 2026-04

Post-release maintenance. No schema changes; two entry-level changes and an influence graph regeneration.

### Changed

- **Agent Smith collapsed into a single entry.** The v2.0.0 release shipped with two Agent Smith entries (`agent-smith-matrix` for *The Matrix* 1999 and `agent-smith-reloaded` for *Reloaded*/*Revolutions* 2003) that had identical card values — the only case in the corpus where the "one entry per film" scope rule produced a redundancy the analytical schema could not resolve. The two entries have been collapsed into a single `agent-smith-matrix` entry covering the trilogy. The Reloaded/Revolutions specifics (viral self-replication, institutional tether snap, multiplicity jump) that v1.0 could have tracked on its own axes are now documented in the entry's `notes` field. Corpus count: **44 → 43**.
- **`output/classification_summary.md`** updated for the new count and to drop the "known redundancy" caveat.

### New

- **`analysis/influence_graph.yaml`** (regenerated for v2.0). 32 edges across 39 of 43 nodes, tracing property propagation under the v2.0 schema. Edge types: `adapts` (1), `sequel` (5), `inherits` (21), `inverts` (1), `elevates` (4). This replaces the v1 influence graph which was retired in v2.0.0 as "hardwired to Q-KNO axis propagation." The v2 version is rebuilt from scratch against the new card axes. Four orphan nodes (`ash-alien`, `c-3po`, `emerac-desk-set`, `gir-invader-zim`) are acknowledged analytical outliers.
- **`analysis/influence_graph.html`** (regenerated). A vis.js-based interactive visualization of the influence graph, colored by edge type and grouped by medium. Generated from the YAML by a new `render_influence_graph()` function in `analysis/analyze.py` behind a `--graph` flag; `analyze.py --all` now includes the graph render.

### Removed

- **`data/beings/agent-smith-reloaded.yaml`.** Collapsed into `agent-smith-matrix` (see above).

### Known issues updated

- **Knowability/knowing divergence count drops from 10/44 to 9/43.** The v2.0.0 release flagged divergence at 10 of 44 — one above the draft spec's "flag for schema review" threshold of `<10`. The Agent Smith entry being collapsed was a divergent pair (`knowability: absent`, `knowing: present`), so removing it drops the count to 9 of 43 — one *below* the threshold. **No entries have been re-coded to pad the statistic.** The honest reading is: after the collapse, the divergence count is below the draft spec's re-review threshold, and the schema should be revisited if and when new entries are added or existing codings are challenged.

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
  - ~~`agent-smith-matrix` + `agent-smith-reloaded`~~ (collapsed back to a single entry in 2.0.1 — see above)

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
- **`analysis/influence_graph.yaml`, `analysis/influence_graph.html`.** Removed. These encoded v1-specific narrative-influence claims hardwired to Q-KNO axis propagation. Retired pending v2-native re-analysis. *(Reintroduced in 2.0.1 with a ground-up rebuild — see the 2.0.1 section above.)*
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

- ~~**Agent Smith duplication.**~~ Resolved in 2.0.1 — the two entries were collapsed into one.
- ~~**Knowability/knowing divergence is 10 of 44.**~~ See 2.0.1: after the Agent Smith collapse the count drops to 9 of 43, which is below the draft spec's re-review threshold.
- **Hosts (Dolores)** collapses a polyphonic ensemble into one entry. Maeve would code differently. A future release may split this.

---

## [1.0.0] — 2025

Initial release. 37 entries, 14+ analytical axes, verbose nested YAML, mnemonic code vocabulary, structured citations array. See git history before the v2.0 migration commit for the complete v1 schema.
