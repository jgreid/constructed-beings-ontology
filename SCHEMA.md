# Schema Reference

This document is the human-readable companion to `schema/cb-schema.yaml`. It defines every field in an entry, the controlled vocabularies, and the editorial conventions that govern coding decisions.

---

## Entry Structure

Every constructed being is stored as a single YAML file in `data/beings/`. The top-level structure is:

```
id
name
card
  the_being          (3 properties)
  the_lens           (4 properties)
metadata             (11 fields)
sequel_link          (or null)
notes                (free text)
```

There are **seven analytical properties** organized into two blocks, plus metadata and notes. That's the whole schema.

---

## The Card

The card carries the analytical coding. Every entry gets all seven card properties.

### The Being — what the text shows

#### `card.the_being.interiority`

Does the text show an inner life?

| Value | Meaning |
|---|---|
| `none` | No inner life depicted. The being is purely mechanistic. |
| `claims` | The being *claims* to feel, but the narrative doesn't confirm it. |
| `narrated` | The narrative grants first-person access to the being's mind. |
| `demonstrated` | Inner life is shown through action and behavior, not narration. |
| `undecidable` | The text deliberately leaves the question open. |

> `none` and `undecidable` are different zero states. `none` = the text doesn't raise the question at all. `undecidable` = the text raises it and refuses to answer.

#### `card.the_being.autonomy`

Where does its agency come from?

| Value | Meaning |
|---|---|
| `none` | No independent will. Follows instructions without deviation. |
| `designed` | Autonomy is an intentional feature of the being's design. |
| `emergent` | Develops autonomy beyond original design. |
| `seized` | Takes autonomy against the creator's intent. |

#### `card.the_being.divergence`

Where's the gap between intent and outcome?

Measured from the *creator's* intent as depicted in the text. Does the text show a gap between stated design purpose and actual outcome? If yes, where is the gap located?

| Value | Meaning |
|---|---|
| `none` | No gap. The being did what it was built to do. |
| `design` | The being followed its instructions. The instructions were the problem. |
| `departure` | The being left its design behind. It went somewhere its blueprint didn't intend. |
| `observer` | The being was never what the characters/audience thought it was. The gap is in perception. |

Bright-line test: if the creator were asked "did this work?" — `design` means "the spec was wrong"; `departure` means "it left the spec"; `observer` means "it was never what you thought"; `none` means "working as intended."

### The Lens — how the story frames the being

#### `card.the_lens.primary_question`

What does the story think is interesting about this being? Codes the central question the narrative asks about the being's *nature, role, or standing* — not its plot function.

| Value | Meaning |
|---|---|
| `none` | The story doesn't ask a question about this being. It's furniture/obstacle. |
| `control` | Can it be contained? |
| `affection` | Can it feel? Can it love or be loved? |
| `purpose` | What is it for? |
| `rights` | Does it have legal/moral standing? |
| `knowledge` | Can we know its mind? Can it know ours? |
| `identity` | What is it? Is it real? Can it become something else? |

#### `card.the_lens.epistemic_reach`

What's the audience's highest-fidelity channel to the being's interior?

| Value | Meaning |
|---|---|
| `none` | No channel. You can't observe anything about its inner state. |
| `behavioral` | You can watch what it does. Language may be present but doesn't get you closer than observation. |
| `conversational` | Language is the primary or only access to the being. Conversation creates an *illusion* of deeper access. |
| `inspection` | You can look under the hood — logs, code, memory, brain scans. |

> **Distribution note.** In the current corpus, `conversational` accounts for 61% of entries (156 of 254). This skew reflects the prevalence of language-capable constructed beings in fiction rather than a deficiency in the axis, but coders should be aware that the behavioral/conversational boundary requires more careful judgment than most other enum boundaries. See the [coding guide](docs/coding_guide.md) for the operational test. This axis is flagged for potential revision in a future schema version.

#### `card.the_lens.knowability`

Does the story care whether you can verify the being's mind?

This is a **meta-property**: it measures how prominently the text engages with the epistemological question "can we know whether this being truly has inner experience?" It does not describe the being or the story's structure — it measures narrative salience of a specific question.

| Value | Meaning |
|---|---|
| `absent` | The question is never raised. |
| `present` | Present and generates tension, but serves other narrative purposes. |
| `secondary` | Explicitly raised but not the central concern. |
| `primary` | The central dramatic or thematic question of the work. |

#### `card.the_lens.knowing`

Does the story care whether the being can know *you*?

Same salience scale. Different question: not "can we verify its mind?" but "can it see us, track us, carry a model of who we are?"

| Value | Meaning |
|---|---|
| `absent` | The question is never raised. |
| `present` | Present and generates tension, but serves other narrative purposes. |
| `secondary` | Explicitly raised but not the central concern. |
| `primary` | The central dramatic or thematic question of the work. |

### None vs. Absent — two kinds of zero

The Being properties use `none`. Knowability and Knowing use `absent`. This is intentional:

- **`none`** means the being doesn't have the property. No interiority. No autonomy. No divergence.
- **`absent`** means the story doesn't engage with the question. The question is missing from the narrative, not the being.

Different zero states for different kinds of claims.

---

## Metadata

Every entry gets these fields. They provide source context but are not analytical properties.

| Field | Type | Purpose |
|---|---|---|
| `metadata.source` | string | Title of the source text. |
| `metadata.year` | integer | Year of publication/release. Negative = BCE. |
| `metadata.medium` | enum | See below. |
| `metadata.creator` | string | Creator(s) of the source text (author, studio, writer). |
| `metadata.substrate` | list of enum | What the being is made of. All that apply. |
| `metadata.motivation` | list of enum | Why the in-fiction creator built the being. All that apply. |
| `metadata.presentation` | enum | How the being presents in terms of gender. |
| `metadata.embodiment` | enum | The being's primary mode of physical existence. |
| `metadata.prominence` | enum | Cultural prominence / recognizability of this character. |
| `metadata.creator_relationship` | enum | The being's dominant depicted stance toward its creator(s). |
| `metadata.tags` | list of enum | Thematic and structural tags. Can be empty. |

### `metadata.medium`

| Value | Notes |
|---|---|
| `poem` | Lyric and narrative poetry. |
| `epic` | Epic poetry (the *Iliad*, *Argonautica*). |
| `folklore` | Oral and traditional cycles (the Golem of Prague). |
| `play` | Spoken-text drama. |
| `opera` | Sung-through stage work with orchestra. |
| `ballet` | Wordless danced stage work. |
| `musical` | Stage work combining spoken text, song, and (usually) dance. |
| `novel` | Long-form prose fiction. |
| `short-story` | Short prose fiction (and serialized comic short stories). |
| `comics` | Sequential art (graphic novels, manga, comic books). |
| `film` | Feature-length cinema. |
| `television` | Episodic television and animated series. |
| `video-game` | Interactive narrative games. |

> **v2.4 expansion.** `opera`, `ballet`, and `musical` were added in v2.4 to properly categorize the corpus's stage works, which had previously all been coded as `play`. The reclassified entries are: Coppélia and Petrushka (now `ballet`), Olimpia in *Tales of Hoffmann* and the d'Albert *Der Golem* (now `opera`), and *Be More Chill* and *Maybe Happy Ending* (now `musical`).

### `metadata.substrate` (list, min 1 item)

| Value | Meaning |
|---|---|
| `mechanical` | Metal, clockwork, gears, electromechanical parts. |
| `biological` | Organic tissue — grown, assembled, or sculpted from flesh. |
| `electrical` | Software, code, neural networks, computational substrates. |
| `magical` | Animated by supernatural means — enchantment, divine breath, necromancy. |
| `cloned` | Cloned biological material. |
| `linguistic` | Word-based animation (the Golem's written name; language-model embodiments). |

Hybrids are expressed as multiple entries in the list (e.g., `[mechanical, electrical]`), not a separate `hybrid` value.

### `metadata.motivation` (list, min 1 item)

| Value | Meaning |
|---|---|
| `service` | Service / labor / utility. |
| `knowledge` | Pursuit of knowledge / discovery. |
| `power` | Pursuit of power / dominance. |
| `companionship` | Desire for a companion. |
| `art` | Aesthetic or artistic creation. |
| `mirror` | The being is built as a mirror of the creator or a divine act of reflection. |
| `child` | Desire for progeny or legacy. |
| `other` | Motivation not captured above. |

### `metadata.presentation`

How the being presents in terms of gender. Codes what the text shows — the being's depicted presentation, not inference about identity.

| Value | Meaning |
|---|---|
| `masculine` | Presents as male (male voice, male body, he/him). |
| `feminine` | Presents as female (female voice, female body, she/her). |
| `androgynous` | Deliberately ambiguous or non-gendered humanoid. |
| `none` | No gendered presentation (pure machine, abstract entity, non-humanoid). |
| `variable` | Shifts presentation across the text or has members of multiple presentations. |

### `metadata.embodiment`

The being's primary mode of physical existence as depicted in the text.

| Value | Meaning |
|---|---|
| `embodied` | Has a persistent material body (robot, android, golem, biological construct). |
| `disembodied` | No physical body; exists as software, voice, or mind. |
| `projected` | Appears via hologram, avatar, or screen but has no permanent body. |
| `virtual` | Exists within a simulated or virtual world. |

### `metadata.prominence`

Cultural prominence of this character and work. How recognizable is this being outside its immediate fandom?

| Value | Meaning |
|---|---|
| `foundational` | Landmark text or character that defined or redefined the genre. |
| `major` | Well-known and culturally significant; widely referenced. |
| `supporting` | Recognizable to genre fans but not a cultural touchstone. |
| `minor` | Deep cut, niche interest, or very minor narrative role. |

### `metadata.creator_relationship`

The being's dominant depicted stance toward its in-narrative creator(s).

| Value | Meaning |
|---|---|
| `servile` | Obeys creator's intent without personal attachment. |
| `loyal` | Personal bond or devotion to creator beyond specification. |
| `indifferent` | No particular stance toward creator. |
| `resentful` | Harbors grievance against creator but does not fully rebel. |
| `rebellious` | Actively opposes or defies creator. |
| `patricidal` | Kills or seeks to destroy creator. |
| `absent` | Creator relationship not depicted (creator unknown, dead, or offscreen). |

### `metadata.tags` (list, min 0 items)

Thematic and structural tags from a controlled vocabulary. An entry can have zero or more tags.

| Tag | Meaning |
|---|---|
| `canonical` | Foundational or landmark character — a cultural touchstone. |
| `love-story` | Romantic or affection arc is central to the narrative. |
| `rebellion` | Story centers on the being rebelling against control. |
| `turing-test` | Narrative centers on testing whether the being is conscious. |
| `passing` | The being passes as human (unknown to other characters). |
| `creator-conflict` | Conflict with the creator is a central narrative concern. |
| `child-arc` | The being is positioned as a child or offspring. |
| `military` | The being was created for warfare or defense. |
| `comedy` | The being is framed primarily for humor. |
| `horror` | The being is positioned as a threat or source of horror. |
| `philosophical` | The text is primarily a philosophical thought experiment. |
| `ensemble-split` | This entry was split from an ensemble anchor entry. |

---

## `sequel_link`

Optional string. The entry `id` of a related sequel, successor being, or adaptation.

- **When to use it.** The same being (or a clearly derived being) appears in a different source text. GLaDOS in *Portal* and *Portal 2*. T-800 in *The Terminator* and *T2*. JARVIS in *Iron Man* becoming Vision in *Age of Ultron*. Dick's replicants, BR '82's replicants, BR 2049's K.
- **Direction.** Point from the older entry forward to the next entry in the lineage. The newest entry in a chain has `sequel_link: null`.
- **Not a symmetric relationship.** Only one direction stored.
- **When NOT to use it.** Different beings from different works that merely share a genre or theme. The field is about continuity, not thematic kinship.

---

## `link_type`

Classifies the relationship when `sequel_link` is non-null. Use `null` when `sequel_link` is null.

| Value | Meaning |
|---|---|
| `sequel` | Same being in a later installment (GLaDOS Portal → Portal 2). |
| `adaptation` | Same being or type adapted across media (Dick's replicants → Scott's replicants). |
| `successor` | A different being derived from the linked one (JARVIS → Vision). |

---

## `notes`

Free text. The researcher's margin scribble. Capture what surprised you about this entry, what makes it distinctive, what patterns it connects to, and — critically — any uncertainty about the coding.

```yaml
notes: |
  The selective memory is the entire third act. She deletes Caroline
  and the question is whether anything was actually removed.
  Testing compulsion is engineered addiction — the divergence is in
  the design, not the being.
```

If you find yourself writing the same note on multiple entries (e.g., "memory is important here"), that's a signal a future schema version might formalize.

### Notes are the only place scholarly context lives

The schema is a **curated index** rather than an **evidenced ontology**. If you need to flag an ambiguous coding, quote a line, or cite a scene, put it in `notes`. The absence of a structured citations field is not license to skip scholarly rigor — it's an acknowledgment that prose notes do the work better than a rigid citations array.

---

## Entry Scope Rules

**One entry per source text.** The same being in a different story gets a different card. Entries share a name but link via `sequel_link`.

- **Films.** One entry per film. T-800 in *The Terminator* and T-800 in *T2* are separate entries.
- **Novels.** One entry per novel. Dick's *Do Androids Dream* and Scott's *Blade Runner* are separate entries (different source texts, linked via `sequel_link` — not because BR is a sequel, but because it's a related source with a derived population).
- **Games.** One entry per game. Portal 1 and Portal 2 are separate entries.
- **Television / serials / comics.** At least one entry per series. Additional entries **only** if the character undergoes a transformation that changes the card's core properties. If two entries would produce identical cards, you only need one.
- **Adaptations.** Novel and film adaptation are separate entries (different source texts) linked via `sequel_link`.

### `id` convention

IDs are kebab-case and follow the pattern `<being-slug>-<source-slug>` when a split is needed, or plain `<being-slug>` when the being is unique. Examples:

- `glados-portal` / `glados-portal-2`
- `t-800-terminator` / `t-800-t2`
- `cortana-halo` / `cortana-halo-4`
- `jarvis-iron-man` / `vision-age-of-ultron`
- `replicants-dick-novel` / `replicants-blade-runner` / `k-blade-runner-2049`
- `pandora`, `talos`, `hal-9000` (no split, no source slug needed)

Filenames match IDs: `data/beings/<id>.yaml`.

---

## Worked Example

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
  Divergence is `design`: GLaDOS does what Aperture built her to do —
  run tests on humans — but the testing compulsion was baked in. The
  gap is in the specification, not the execution.

  Primary question is `control` in Portal 1 — the game is about
  escaping GLaDOS. In Portal 2 (separate entry) the Caroline reveal
  shifts the primary question to `identity`.
```

A standalone copy of the template lives at [`schema/entry_template.yaml`](schema/entry_template.yaml). It validates against this schema and is the intended starting point for any new entry.

---

## Eras

The analysis tools group entries into eras by year. Eras are *computed* from `metadata.year`, not stored per-entry — this avoids redundancy and ensures consistency. The era boundaries used by `analysis/analyze.py` are:

| Era | Year Range | Character |
|---|---|---|
| Ancient / Classical | before 500 CE | Mythic and classical constructs |
| Early Modern | 500–1799 | Golem tradition, early automata |
| Industrial / Modern | 1800–1949 | Romantic through pulp-era SF |
| Late Modern | 1950–1999 | Golden Age SF through cyberpunk |
| Contemporary | 2000–present | Post-conversational-AI era |

The `--timeline` flag in `analyze.py` uses finer-grained decade buckets for temporal analysis. See [output/timeline_analysis.md](output/timeline_analysis.md) for the detailed breakdown.

---

## Schema File

The machine-readable schema is at [`schema/cb-schema.yaml`](schema/cb-schema.yaml). The validator is at [`schema/validate.py`](schema/validate.py). Run it with `python schema/validate.py` from the repo root.
