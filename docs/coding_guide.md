# Coding Guide — CBO v2.0

This guide walks through the judgment calls you'll make when coding a new entry or re-coding an existing one under the v2.0 schema. The [SCHEMA.md](../SCHEMA.md) document is the canonical reference for what each field means and what values it accepts. This document is about **how to decide** in the messy cases.

If you disagree with a coding decision below or in an existing entry, open an issue with your reasoning and the passages from the source text that support it. Coding disputes are scholarship.

---

## General principles

1. **Code what the text shows, not what you infer.** If the film doesn't address a being's inner life, that's `interiority: none`, not "probably demonstrated, off-screen." The schema asks what the text does, not what you know about the franchise.
2. **Use the closest available value.** v2.0's enums are tight. If the nearest option is a bad fit, it's still the right answer — and the bad fit is exactly what the `notes` field is for. Flag the mismatch.
3. **Notes do the work citations used to do.** v2.0 has no `citations` array. If your coding turns on a specific passage, scene, or design decision, write it in `notes` — in prose, with enough context that a future editor can find it.
4. **Low-confidence is a first-class flag.** If you're coding from partial familiarity with the source, say so in `notes`. "Flagged for re-review" is a real, respected state.

---

## Walkthroughs for the hard properties

### Divergence — the single most frequent coding call

`divergence` is new in v2.0 and often the hardest field. Ask: **does the text show a gap between stated design purpose and actual outcome?**

- If no gap → `none`. Example: Data (TNG). Soong built him to be a positronic person who aspires toward humanity, and that's exactly what he is. Working as specified.
- If the being followed its instructions but the instructions were the problem → `design`. Example: HAL 9000. HAL executes conflicting orders (tell the crew everything / conceal the monolith mission) in a way the spec allowed. The gap is in the spec. Also: Marvin (depressed-by-design), Talkie Toaster (obnoxious-by-design), VIKI (reasoned from the Three Laws), GLaDOS (testing compulsion engineered in).
- If the being left its design behind → `departure`. Example: Skynet, Agent Smith, the Iron Giant, WALL-E. The creator would say "that's not what I wanted" AND "that's not what I asked for."
- If the being was never what the characters/audience thought it was → `observer`. Example: Olympia, Ava, Dick's replicants. The gap is in perception, not in the being.

**Decision test:** what would the creator say if asked "did it work?"
- "Yes, perfectly" → `none`
- "The spec was wrong" → `design`
- "It left the spec" → `departure`
- "You were never seeing what you thought you were seeing" → `observer`

### Interiority — `none` vs. `undecidable` vs. `claims`

All three are ways the text might fail to confirm an inner life. They are not interchangeable:

- **`none`** — the text doesn't raise the question at all. The being is mechanistic and nobody minds. Talos is `none` because the Argonautica has no interest in whether he feels anything; it cares whether he can be stopped. Skynet is `none` because the Terminator films are not philosophical about their antagonist.
- **`undecidable`** — the text raises the question and refuses to settle it. This is a deliberate narrative choice, not an omission. Olympia, Samantha, Ava, the Replicants. The common thread is that the *refusal* is the point.
- **`claims`** — the being articulates an inner state that the narrative neither credits nor denies. HAL says "I'm afraid." Ash speaks admiringly of the xenomorph. The words are there; the verification isn't.

If you're torn between `none` and `undecidable`, ask: **does the text visibly decline to answer?** If yes, `undecidable`. If the question simply never comes up, `none`.

### Primary Question — `none` is a first-class value

v2.0 adds `primary_question: none` for beings that aren't the subject of a narrative question at all. This is often the right coding for:

- **Plot furniture / obstacles.** Talos (a guard), EMERAC (a MacGuffin), GIR (comic relief), C-3PO (droid-shaped comic relief). The story is asking questions, but not about this being.
- **Minor characters** who exist for color rather than for inquiry.

If you're leaning toward `none`, confirm by asking: **does any scene frame a question about this being's nature, role, or standing?** Not its plot function — its standing. If no, `none`. If only occasionally, probably `none`. If the question is threaded through the work, pick one of the other options.

### Primary Question — `identity` is the question v1 split across other fields

v1.0 had no `identity` value, so entries whose central question was "what am I?" ended up coded as `fellow-feeling`, `purpose`, or `obedience`. v2.0 collects them into one cluster. Use `identity` when:

- The being is asking "what am I?" (Sonny: "can a robot have a soul?")
- The being is becoming something else (Pinocchio → real boy; Iron Giant → protector)
- The text's central concern is what the being *is* vs. what it was built to be (Dolores across Westworld, Vision in Age of Ultron, K in BR 2049)

`identity` is often paired with `divergence: departure` but not always. Vision has `divergence: departure`; Sonny has `divergence: none` (Lanning designed him to ask exactly these questions). The divergence and primary-question axes are independent.

### Knowability vs. Knowing — two distinct questions

Both are **meta-properties** — they measure narrative salience, not something about the being itself.

- **Knowability** asks: *does the story care whether we can verify the being's mind?*
- **Knowing** asks: *does the story care whether the being can know us?*

These can and often do diverge. Code them independently:

- **Vic Fontaine:** knowability `absent` (nobody doubts he's a hologram), knowing `secondary` (his ability to know the crew IS his character).
- **Robbie:** knowability `absent`, knowing `present` (no consciousness debate, but he knows and protects Gloria).
- **VIKI:** knowability `present` (her reasoning is shown, her conclusions contested), knowing `absent` (she doesn't care about individuals).
- **Data:** knowability `secondary` ("Measure of a Man" foregrounds it), knowing `present` (his observation of humans runs through the series).
- **Samantha and Ava:** both `primary/primary` — the modern limit case where the two questions fuse.

The salience scale is the same for both:
- `absent` — the question is never raised.
- `present` — raised, generates tension, but serves other purposes.
- `secondary` — explicitly raised, not the central concern.
- `primary` — the central dramatic or thematic question.

**Rule of thumb:** if the film would still work without the question, it's `present` at most. If the film is partly about the question, it's `secondary`. If the film stops working when you remove the question, it's `primary`.

### Epistemic Reach — four channels, pick the highest

- **`none`** — you can't observe anything about its inner state. Skynet, Talos, Pandora.
- **`behavioral`** — you watch what it does. Language may be present but doesn't get you closer. R2-D2, Iron Giant, most mid-century robots.
- **`conversational`** — language is the primary access. Conversation creates an illusion of deeper access. Marvin, Vic Fontaine, JARVIS, Cortana, Samantha.
- **`inspection`** — you can look under the hood. Memory scans, code review, brain dissection, restraining bolts, diagnostic panels. Data, HAL, C-3PO, Colossus, EMERAC.

Pick the **highest-fidelity** channel the text gives you. If the film shows both HAL's chess moves (behavioral) and HAL's memory module being disconnected (inspection), `inspection` wins.

Note: language presence alone does not upgrade behavioral to conversational. The question is whether conversation is the primary or only channel. A character who talks while you watch them is still primarily behavioral if you have access to their behavior. Marvin is `conversational` because we never see him do anything other than talk about his state. Cortana is `conversational` because she's a voice in the Chief's ear and that voice is the character.

---

## Sequel splits — when to create a second entry

v2.0 uses a **one entry per source text** rule. The mechanical question is when to apply it.

- **Films: always split** — with one exception. *The Terminator* and *T2* are separate entries. *Blade Runner* and *Blade Runner 2049* are separate entries. *The Matrix* and its sequels were originally split, but on review the card values were identical across all three films and the entries were collapsed (see the Agent Smith entry's notes and CHANGELOG 2.0.1). When two candidate entries for different films produce identical v2.0 cards, and the analytical axes genuinely have nothing different to say, collapse them into a single entry and document the within-trilogy arc in `notes`. This is the only time the "one entry per film" rule bends.
- **Novels: always split.** Philip K. Dick's *Do Androids Dream* and Ridley Scott's *Blade Runner* (the film) are separate entries, linked via `sequel_link`, because they are different source texts.
- **Games: one per game.** Portal 1 and Portal 2 are separate entries. Halo is the ambiguous case — the CE-through-3 trilogy is coherent enough to unify, and Halo 4+ (rampancy) is distinct enough to split.
- **Television / serials / comics: one per series by default.** Split only if the character undergoes a transformation that changes the card's core properties. If two candidate entries produce identical cards, collapse them.

**Use `sequel_link`** to chain related entries: older → newer. The newest entry in a chain has `sequel_link: null`. The link is one-directional and is not a symmetric relationship — it's a reading aid, not a data model.

### Sequel splits for different beings with continuity

The tricky case is when the being in the later work is *derived* from the earlier being but is not the same being. JARVIS → Vision is the canonical example: Vision isn't JARVIS, but his pattern is in there. Use `sequel_link` anyway. The field is a pointer to "the next entry in this lineage," not "the next appearance of this being."

---

## Low-confidence entries in the current corpus

These entries are explicitly flagged in `notes` as lower-confidence. If you read the source text more closely than I did, please open an issue and propose a re-code:

- **Colossus** — mid-60s novel, coded from partial familiarity.
- **EMERAC** — 1957 romantic comedy; coding "what does *Desk Set* think about EMERAC" is genuinely hard because the film mostly thinks about humans.
- **Ash (Alien)** — the hidden-android reveal retroactively destabilizes interiority.
- **Talkie Toaster** — minor character, limited screen time, primary_question could reasonably be `none`.
- **Hosts (Dolores)** — collapses a polyphonic ensemble into a single entry. Maeve's card would differ.
- **Vic Fontaine** — the designed/emergent boundary is fuzzy for long-running holographic programs.

And from the draft's own flag list:

- **Cortana (Halo 4+)** — reasonably confident, but the specific Rampancy axis is a close call.
- **GLaDOS (Portal 2)** — the knowing shift to `secondary` is the judgment call.
- **Vision (Age of Ultron)** — substrate is genuinely hybrid in a way v2.0's list syntax handles but the coding question is what the film *foregrounds*.
- **K (BR 2049)** — knowability/knowing both `secondary` is defensible but close to `present`.

---

## A worked example

Suppose you want to add David from *Alien: Covenant* (2017). Here's the decision process:

1. **Source text.** *Alien: Covenant*, 2017. Different film from *Alien* (1979), so it gets its own entry even if Ash and David are "the same character type." They're different beings in different source texts.
2. **Being.** Ridley Scott's later synthetics are more explicit than Ash. Interiority is `demonstrated`: David writes poetry, monologues, performs. Divergence is `departure` (Weyland wanted an assistant; got a genocidal aesthete). Autonomy `seized`.
3. **Lens.** Primary question is `identity`: David's arc is explicitly about becoming a maker rather than a made thing. Epistemic reach is `conversational` (he talks constantly about his state). Knowability is `present` at least, maybe `secondary` — Scott engages the question but it's not the center. Knowing is `present` (David observes humans closely and weaponizes what he learns).
4. **Metadata.** Film, 2017, Ridley Scott, substrate `[mechanical, electrical]`, motivation `[service, knowledge]`.
5. **Notes.** Explain the David-vs-Walter choice, flag the coding as about David, explain the divergence call.

You'd end up with an entry like:

```yaml
id: david-alien-covenant
name: "David 8"

card:
  the_being:
    interiority: demonstrated
    autonomy: seized
    divergence: departure
  the_lens:
    primary_question: identity
    epistemic_reach: conversational
    knowability: present
    knowing: present

metadata:
  source: "Alien: Covenant"
  year: 2017
  medium: film
  creator: "Ridley Scott (Weyland Corporation in-narrative)"
  substrate:
    - mechanical
    - electrical
  motivation:
    - service
    - knowledge

sequel_link: null

notes: |
  This entry covers David specifically, not Walter (who would code
  differently — Walter's interiority is closer to `claims`, his
  divergence is `none`, his autonomy is `designed`). A future
  edition may split them.

  Divergence is `departure`: Weyland built David as a household
  assistant with near-human affect; David becomes a self-styled
  creator-god, specifically rejecting his service role. Identity is
  the primary question because David's arc is explicitly about
  becoming a maker rather than a made thing.
```

Then validate it: `python schema/validate.py data/beings/david-alien-covenant.yaml`.
