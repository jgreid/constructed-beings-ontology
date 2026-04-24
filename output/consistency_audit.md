# Consistency Audit

Corpus: **405 entries**. This report flags entries whose codings sit in tension with a rule derived from `docs/coding_guide.md` or the tag/field vocabularies. A flag is a prompt for a human review, not a verdict of miscoding — several combinations that look odd on paper are defensible in context.

- **Rule-based flags:** 47 flag-instances across **46 distinct entries**.
- **Self-flagged in notes:** 15 entries.
- **Lineage diffs:** 28 sequel-link pairs with non-identical cards (including broken links if any).
- **Inverted sequel_links:** 7 pairs point newer → older, reversing the SCHEMA.md direction rule.

## 1. Rule-based flags

### `autonomy-none_but-divergence-departure` — 1 entries

*autonomy=none means no depicted agency. Per the coding guide, `divergence=observer` is compatible (Olympia, Coppélia) because the gap is in perception — but `departure` requires the being to have left its design, which needs agency.*

- **The Bride** (`bride-of-frankenstein`)

### `autonomy-none_but-rebellious` — 0 entries

*A being coded as having no autonomy cannot be rebellious or patricidal toward its creator.*

_No entries flagged._

### `rebellious_but-divergence-none` — 1 entries

*Rebellion/patricide against the creator usually implies leaving the design (divergence != none).*

- **Amazo** (`amazo-dc`)

### `tag-rebellion_but-not-rebellious` — 3 entries

*`rebellion` tag conflicts with a non-rebellious/patricidal creator relationship.*

- **The Clickers (R-Series)** (`clickers-creation-humanoids`)
- **Mike (Mycroft Holmes / HOLMES IV)** (`mike-heinlein`)
- **The SQUIP** (`squip-be-more-chill`)

### `tag-love-story_but-not-affection` — 19 entries

*`love-story` tag implies primary_question should be affection.*

- **Aigis** (`aigis-persona-3`)
- **Alice** (`alice-subservience`)
- **BB / Samantha** (`bb-deadly-friend`)
- **R. Dorothy Wayneright** (`dorothy-wayneright-big-o`)
- **EDI** (`edi-mass-effect`)
- **Galatea (Gilbert)** (`galatea-gilbert`)
- **The Golem (d'Albert opera)** (`golem-d-albert-opera`)
- **Guy** (`guy-free-guy`)
- **Harey (the Solaris visitor)** (`harey-solaris`)
- **J1, J2, J3** (`j-archive-2020`)
- **Walter (Prime) — film** (`marjorie-prime-film`)
- **Petrushka** (`petrushka-stravinsky`)
- **Pinocchio (Disney)** (`pinocchio-disney-1940`)
- **Quorra** (`quorra-tron-legacy`)
- **Salo** (`salo-sirens-of-titan`)
- **Samantha** (`samantha-her`)
- **Vivy / Diva** (`vivy-fluorite-eye`)
- **Walter (Prime)** (`walter-marjorie-prime-play`)
- **Woody** (`woody-toy-story`)

### `tag-creator-conflict_but-loyal-or-servile` — 3 entries

*`creator-conflict` tag is used broadly for narrative confrontation with the creator (V'Ger-style), but loyal/servile relationships are still worth a second look — the tag usually implies friction.*

- **Pinocchio (del Toro)** (`pinocchio-del-toro`)
- **Ragnarok (Clor)** (`ragnarok-civil-war`)
- **V'Ger** (`vger-tmp`)

### `tag-turing-test_but-knowability-absent` — 0 entries

*`turing-test` tag implies the question of verifying the mind is at least present.*

_No entries flagged._

### `tag-child-arc_but-no-child-motivation` — 16 entries

*`child-arc` tag implies `child` should appear in motivation.*

- **Arthur** (`arthur-after-the-blast`)
- **Atom** (`atom-real-steel`)
- **Baymax** (`baymax-big-hero-6`)
- **D-O** (`d-o-rise-of-skywalker`)
- **D.A.R.Y.L.** (`daryl-1985`)
- **Iris** (`iris-the-nether`)
- **The Iron Giant** (`iron-giant`)
- **Jack Pumpkinhead** (`jack-pumpkinhead-oz`)
- **Karen (Suit Lady)** (`karen-spider-man`)
- **Maximillion (Max)** (`maximillion-bionic-woman`)
- **Mega Man (Rock)** (`mega-man`)
- **Pascal** (`pascal-nier-automata`)
- **Robbie** (`robbie-asimov`)
- **The Scarecrow** (`scarecrow-oz`)
- **Teddy** (`teddy-ai`)
- **Woody** (`woody-toy-story`)

### `interiority-none_but-question-identity` — 0 entries

*A text that shows no interiority is unlikely to treat 'what am I?' as the primary question.*

_No entries flagged._

### `interiority-none_but-knowing-salient` — 1 entries

*`knowing` at primary/secondary implies some interior through which the being knows us.*

- **The Devs Machine** (`devs-machine`)

### `epistemic-reach-none_but-interiority-visible` — 1 entries

*`epistemic_reach=none` says we can't observe the being; interiority can't be demonstrated/narrated.*

- **GIR** (`gir-invader-zim`)

### `knowing-primary_but-reach-none` — 0 entries

*If the story's primary question is the being knowing us, we need some channel to observe it knowing.*

_No entries flagged._

### `question-rights_but-relationship-servile` — 2 entries

*A rights question usually presupposes the being is not purely servile to its creator.*

- **Gigolo Joe** (`gigolo-joe-ai`)
- **Kryten** (`kryten-red-dwarf`)

### `substrate-biological-only_but-creator-relationship-absent` — 0 entries

*Purely biological beings with no linguistic/electrical substrate tend to have present creators; worth double-checking `absent`.*

_No entries flagged._

### `embodiment-virtual_but-not-electrical` — 0 entries

*Virtual beings generally run on electrical/linguistic substrate; missing both is suspicious.*

_No entries flagged._

## 2. Self-flagged entries

Entries whose own `notes` field contains hedging language (partial familiarity, judgment call, flagged-for-re-review, etc.). These were already marked by the coder as warranting a second look.

| Entry | Phrase |
|---|---|
| Ash (`ash-alien`) | `Low-confidence` |
| BB / Samantha (`bb-deadly-friend`) | `Low-confidence` |
| Booti (`booti-buck-rogers`) | `Low-confidence` |
| Colossus (`colossus`) | `Low confidence` |
| EMERAC (`emerac-desk-set`) | `Low-confidence` |
| The Entity (`entity-mission-impossible`) | `uncertain` |
| Hosts (Dolores Abernathy) (`hosts-westworld`) | `Low-confidence` |
| K (Replicant) (`k-blade-runner-2049`) | `uncertain` |
| Mia (Anita) (`mia-humans`) | `to verify` |
| Regus Patoff (`regus-patoff-consultant`) | `uncertain` |
| The Stepford Wives (`stepford-wives`) | `to verify` |
| Talkie Toaster (`talkie-toaster-red-dwarf`) | `Low-confidence` |
| Tyrone (`tyrone-hand-to-god`) | `uncertain` |
| Val and Aqua (`val-aqua-heartbeeps`) | `Low-confidence` |
| Vic Fontaine (`vic-fontaine-ds9`) | `Low-confidence` |

## 3. Inverted sequel_links

SCHEMA.md and `docs/coding_guide.md` both specify that `sequel_link` points from the older entry forward to the newer one (the newest in a chain has `sequel_link: null`). These pairs point the opposite way — they should be reversed (move the link to the older entry and set the younger entry's link to the next newer one, or null).

| From (year) | → To (year) | link_type |
|---|---|---|
| Galatea (Gilbert) (`galatea-gilbert`, 1871) | Galatea (`galatea`, 8) | `adaptation` |
| The Golem (d'Albert opera) (`golem-d-albert-opera`, 1926) | The Golem of Prague (`golem-prague`, 1580) | `adaptation` |
| Atom (Pluto) (`atom-pluto`, 2003) | Astro Boy (Atom) (`astro-boy-tezuka`, 1952) | `adaptation` |
| The Creature (Nick Dear adaptation) (`creature-nick-dear-frankenstein`, 2011) | The Creature (`frankenstein-creature`, 1818) | `adaptation` |
| Walter (Prime) — film (`marjorie-prime-film`, 2017) | Walter (Prime) (`walter-marjorie-prime-play`, 2014) | `adaptation` |
| Ashley Too (`ashley-too-black-mirror`, 2019) | Cookie (digital copy) (`cookie-white-christmas`, 2014) | `successor` |
| Ares (`ares-tron-ares`, 2025) | CLU (`clu-tron-legacy`, 2010) | `successor` |

## 4. Lineage diffs

Pairs connected by `sequel_link` where at least one card value differs. Many of these are legitimate (a sequel that shifts the primary question), but sharp multi-field swings are worth checking.

### Diff summary (28 pairs)

| From | → To | link_type | # card fields changed |
|---|---|---|---:|
| T-800 (`t-800-terminator`) | T-800 (T2) (`t-800-t2`) | `sequel` | 7 |
| Galatea (Gilbert) (`galatea-gilbert`) | Galatea (`galatea`) | `adaptation` | 6 |
| The Gunslinger (`gunslinger-westworld-1973`) | Hosts (Dolores Abernathy) (`hosts-westworld`) | `successor` | 6 |
| HAL 9000 (`hal-9000`) | HAL 9000 (2010) (`hal-9000-2010`) | `sequel` | 6 |
| Robot Santa Claus (`robot-santa-futurama`) | Bender Bending Rodríguez (`bender-futurama`) | `successor` | 6 |
| The Claws (David, Variety I) (`claws-second-variety`) | Screamers (Second Variety Autonomous Weapons) (`screamers-1995`) | `adaptation` | 5 |
| The Golem (d'Albert opera) (`golem-d-albert-opera`) | The Golem of Prague (`golem-prague`) | `adaptation` | 5 |
| JARVIS (`jarvis-iron-man`) | Vision (`vision-age-of-ultron`) | `successor` | 5 |
| Replicants (`replicants-blade-runner`) | K (Replicant) (`k-blade-runner-2049`) | `sequel` | 5 |
| Ashley Too (`ashley-too-black-mirror`) | Cookie (digital copy) (`cookie-white-christmas`) | `successor` | 4 |
| Atom (Pluto) (`atom-pluto`) | Astro Boy (Atom) (`astro-boy-tezuka`) | `adaptation` | 4 |
| The Cleon Dynasty (Brother Dawn / Brother Day / Brother Dusk) (`cleons-foundation-tv`) | Eto Demerzel (`demerzel-foundation-tv`) | `successor` | 4 |
| Cortana (`cortana-halo`) | Cortana (Halo 4+) (`cortana-halo-4`) | `sequel` | 4 |
| The Creature (Nick Dear adaptation) (`creature-nick-dear-frankenstein`) | The Creature (`frankenstein-creature`) | `adaptation` | 4 |
| Dolores Abernathy (`dolores-westworld`) | Hosts (Dolores Abernathy) (`hosts-westworld`) | `successor` | 4 |
| Major Motoko Kusanagi (`kusanagi-gits-1995`) | Major / Mira Killian (`kusanagi-gits-2017`) | `adaptation` | 4 |
| Tik-Tok (`tik-tok-oz`) | Tik-Tok (Return to Oz) (`tik-tok-return-to-oz`) | `adaptation` | 4 |
| Ares (`ares-tron-ares`) | CLU (`clu-tron-legacy`) | `successor` | 3 |
| Calculon (`calculon-futurama`) | Bender Bending Rodríguez (`bender-futurama`) | `successor` | 3 |
| Pinocchio (Disney) (`pinocchio-disney-1940`) | Pinocchio (del Toro) (`pinocchio-del-toro`) | `adaptation` | 3 |
| SHODAN (`shodan-system-shock`) | SHODAN (System Shock 2) (`shodan-system-shock-2`) | `sequel` | 3 |
| Cortana (Halo 4+) (`cortana-halo-4`) | The Weapon (`weapon-halo-infinite`) | `successor` | 2 |
| GLaDOS (`glados-portal`) | GLaDOS (Portal 2) (`glados-portal-2`) | `sequel` | 2 |
| M3GAN (`m3gan`) | M3GAN 2.0 (`m3gan-2`) | `sequel` | 2 |
| Roz (ROZZUM unit 7134) (`roz-wild-robot-novel`) | Roz (ROZZUM unit 7134) (`roz-wild-robot`) | `adaptation` | 2 |
| Albertus Magnus's Android (`albertus-magnus-android`) | The Brazen Head (`brazen-head`) | `successor` | 1 |
| Pinocchio (`pinocchio`) | Pinocchio (Disney) (`pinocchio-disney-1940`) | `adaptation` | 1 |
| Replicants (`replicants-dick-novel`) | Replicants (`replicants-blade-runner`) | `adaptation` | 1 |

### Pairs with ≥4 card-field changes

**T-800 (`t-800-terminator`) → T-800 (T2) (`t-800-t2`)** (link_type: `sequel`)
- `interiority`: `none` → `claims`
- `autonomy`: `none` → `emergent`
- `divergence`: `none` → `departure`
- `primary_question`: `control` → `identity`
- `epistemic_reach`: `none` → `behavioral`
- `knowability`: `absent` → `present`
- `knowing`: `absent` → `present`

**Galatea (Gilbert) (`galatea-gilbert`) → Galatea (`galatea`)** (link_type: `adaptation`)
- `interiority`: `demonstrated` → `none`
- `autonomy`: `emergent` → `none`
- `divergence`: `departure` → `none`
- `primary_question`: `identity` → `affection`
- `epistemic_reach`: `conversational` → `none`
- `knowability`: `present` → `absent`

**The Gunslinger (`gunslinger-westworld-1973`) → Hosts (Dolores Abernathy) (`hosts-westworld`)** (link_type: `successor`)
- `interiority`: `none` → `demonstrated`
- `autonomy`: `designed` → `seized`
- `primary_question`: `control` → `identity`
- `epistemic_reach`: `behavioral` → `conversational`
- `knowability`: `absent` → `secondary`
- `knowing`: `absent` → `secondary`

**HAL 9000 (`hal-9000`) → HAL 9000 (2010) (`hal-9000-2010`)** (link_type: `sequel`)
- `interiority`: `claims` → `demonstrated`
- `autonomy`: `emergent` → `designed`
- `divergence`: `design` → `none`
- `primary_question`: `control` → `affection`
- `epistemic_reach`: `inspection` → `conversational`
- `knowability`: `present` → `secondary`

**Robot Santa Claus (`robot-santa-futurama`) → Bender Bending Rodríguez (`bender-futurama`)** (link_type: `successor`)
- `interiority`: `narrated` → `demonstrated`
- `autonomy`: `designed` → `seized`
- `divergence`: `design` → `departure`
- `primary_question`: `control` → `affection`
- `epistemic_reach`: `behavioral` → `conversational`
- `knowing`: `secondary` → `present`

**The Claws (David, Variety I) (`claws-second-variety`) → Screamers (Second Variety Autonomous Weapons) (`screamers-1995`)** (link_type: `adaptation`)
- `interiority`: `claims` → `undecidable`
- `primary_question`: `control` → `identity`
- `epistemic_reach`: `behavioral` → `conversational`
- `knowability`: `present` → `primary`
- `knowing`: `primary` → `present`

**The Golem (d'Albert opera) (`golem-d-albert-opera`) → The Golem of Prague (`golem-prague`)** (link_type: `adaptation`)
- `interiority`: `claims` → `none`
- `autonomy`: `seized` → `emergent`
- `primary_question`: `rights` → `control`
- `epistemic_reach`: `behavioral` → `none`
- `knowability`: `present` → `absent`

**JARVIS (`jarvis-iron-man`) → Vision (`vision-age-of-ultron`)** (link_type: `successor`)
- `autonomy`: `designed` → `emergent`
- `divergence`: `none` → `departure`
- `primary_question`: `affection` → `identity`
- `epistemic_reach`: `conversational` → `behavioral`
- `knowability`: `absent` → `present`

**Replicants (`replicants-blade-runner`) → K (Replicant) (`k-blade-runner-2049`)** (link_type: `sequel`)
- `interiority`: `undecidable` → `demonstrated`
- `autonomy`: `seized` → `emergent`
- `primary_question`: `purpose` → `identity`
- `knowability`: `present` → `secondary`
- `knowing`: `present` → `secondary`

**Ashley Too (`ashley-too-black-mirror`) → Cookie (digital copy) (`cookie-white-christmas`)** (link_type: `successor`)
- `autonomy`: `emergent` → `seized`
- `divergence`: `departure` → `observer`
- `primary_question`: `identity` → `rights`
- `knowing`: `secondary` → `present`

**Atom (Pluto) (`atom-pluto`) → Astro Boy (Atom) (`astro-boy-tezuka`)** (link_type: `adaptation`)
- `autonomy`: `seized` → `designed`
- `epistemic_reach`: `conversational` → `behavioral`
- `knowability`: `primary` → `absent`
- `knowing`: `primary` → `present`

**The Cleon Dynasty (Brother Dawn / Brother Day / Brother Dusk) (`cleons-foundation-tv`) → Eto Demerzel (`demerzel-foundation-tv`)** (link_type: `successor`)
- `divergence`: `observer` → `design`
- `primary_question`: `identity` → `control`
- `knowability`: `primary` → `secondary`
- `knowing`: `present` → `primary`

**Cortana (`cortana-halo`) → Cortana (Halo 4+) (`cortana-halo-4`)** (link_type: `sequel`)
- `autonomy`: `designed` → `emergent`
- `divergence`: `none` → `departure`
- `primary_question`: `affection` → `identity`
- `knowability`: `present` → `secondary`

**The Creature (Nick Dear adaptation) (`creature-nick-dear-frankenstein`) → The Creature (`frankenstein-creature`)** (link_type: `adaptation`)
- `interiority`: `demonstrated` → `narrated`
- `autonomy`: `seized` → `emergent`
- `primary_question`: `rights` → `affection`
- `knowability`: `primary` → `present`

**Dolores Abernathy (`dolores-westworld`) → Hosts (Dolores Abernathy) (`hosts-westworld`)** (link_type: `successor`)
- `primary_question`: `rights` → `identity`
- `epistemic_reach`: `inspection` → `conversational`
- `knowability`: `primary` → `secondary`
- `knowing`: `primary` → `secondary`

**Major Motoko Kusanagi (`kusanagi-gits-1995`) → Major / Mira Killian (`kusanagi-gits-2017`)** (link_type: `adaptation`)
- `interiority`: `undecidable` → `demonstrated`
- `epistemic_reach`: `conversational` → `inspection`
- `knowability`: `primary` → `secondary`
- `knowing`: `secondary` → `present`

**Tik-Tok (`tik-tok-oz`) → Tik-Tok (Return to Oz) (`tik-tok-return-to-oz`)** (link_type: `adaptation`)
- `interiority`: `none` → `claims`
- `primary_question`: `purpose` → `none`
- `epistemic_reach`: `inspection` → `conversational`
- `knowing`: `absent` → `present`

## 5. Findings & Recommendations

A sample of flagged entries was spot-checked against independent summaries (Wikipedia, Memory Alpha, published reviews) to separate genuine miscodings from defensible judgment calls. Headline findings below; the rest of the rule-based flags are judgment calls the coder thought through and documented in `notes`.

### Confirmed data bugs

- **7 inverted `sequel_link` directions** (see section 3). These are mechanical fixes: each pair should be reversed so the link flows older → newer. Examples include `galatea-gilbert → galatea` (Gilbert 1871 points back to Ovid 8 CE) and `atom-pluto → astro-boy-tezuka` (Pluto 2003 points back to Astro Boy 1952).

### Entries worth a closer re-read

- **Amazo** (`amazo-dc`). `creator_relationship: rebellious` + `divergence: none`. External check: in the original 1960 *Brave and the Bold* #30 debut, Amazo is Ivo's **obedient instrument** against the Justice League — he hunts and drains the League at Ivo's direction for an immortality serum. Rebellion-against-Ivo appears in later continuity. Either anchor the entry to the 1960 debut (then `creator_relationship` is `servile` or `loyal`) or acknowledge the later-continuity reading and add the `rebellion` tag to match.

- **The Bride** (`bride-of-frankenstein`). `autonomy: none` + `divergence: departure`. The entry's own notes describe the Bride's refusal as *"the most important act of agency in the film"* — which is itself agency, arguing for `autonomy: seized` rather than `none`. Either the autonomy or the divergence reading needs to give.

### Rules that turned out to be too strict

- **`tag-love-story_but-not-affection` (19 entries).** Spot-checks on Samantha (*Her*), Woody (*Toy Story*), Guy (*Free Guy*), Walter (*Marjorie Prime*), and Galatea (Gilbert) show that the `love-story` tag is used for the presence of a romantic plot thread even when the analytical primary question is `identity`, `knowledge`, or `purpose`. This is a deliberate coding choice (the tag marks surface genre; `primary_question` marks the analytical core). Only entries where the romantic thread is also the central narrative question should flip to `affection` — Bride of Frankenstein, Galatea (Ovid), and Baymax do, and are coded that way.

- **`tag-child-arc_but-no-child-motivation` (16 entries).** The `child-arc` tag marks the narrative shape (a being who grows up, learns, is parented), not the creator's original motivation for building it. Iron Giant, Baymax, Atom (*Real Steel*), Robbie and Teddy all have this shape without having been built as children. The rule should probably be dropped or reworded.

- **`tag-creator-conflict_but-loyal-or-servile` (V'Ger).** V'Ger's creator-conflict is narrative-metaphysical ("is there nothing more?") rather than insurrectionary — the tag is being used for any dramatic encounter with the creator, not only for antagonism. The coding is defensible; the rule over-fires.

### Self-flagged entries worth external follow-up

Spot-checks on two self-flagged low-confidence entries returned clean:
- **Colossus** (1966, D.F. Jones). The novel's verbal ambiguity about Colossus's inner life matches `interiority: claims`; its global takeover matches `divergence: departure` and `primary_question: control`. `knowability: absent` is defensible — the novel is a thriller about containment, not a question-of-mind narrative — though the ending's "in time you will love me" hint could push it to `present`.
- **EMERAC** (1957, *Desk Set*). Wikipedia confirms EMERAC is an ENIAC pastiche used as a romantic-comedy MacGuffin, matching all seven card values and the metadata.

The remaining 13 self-flagged entries (Ash, BB/Samantha, Booti, Hosts/Dolores, K/BR-2049, Mia, Regus Patoff, Stepford Wives, Talkie Toaster, Tyrone, Val & Aqua, Vic Fontaine, The Entity) were not externally spot-checked in this pass and remain candidates for future re-review.

