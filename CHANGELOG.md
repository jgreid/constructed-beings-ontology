# Changelog

All notable changes to the Constructed Beings Ontology are documented here.

---

## [2.5] — 2026-04

**Canonical-gap repair + self-audit + ancillary alignment release.** 332 → 405 entries net across the v2.4.4 scholar-audit (+77), v2.4.5 self-audit (−4, +6 coding corrections), and a doc catch-up sprint that brought the influence graph, classification summary, bibliography, and boundary-case documentation in line with the post-audit corpus. No schema changes — field and enum structure unchanged since v2.4.

### Summary

- **Corpus at 405 entries.** v2.4.4 added 77 canonical-gap entries spanning classical automata (Celedones, Daedalus's walking statues, Albertus Magnus's android), Romantic/pulp (Hawthorne's butterfly, Ellis's Steam Man, Baum's Scarecrow and Jack Pumpkinhead), Golden-Age SF shorts (Asimov's Cutie/Speedy/Herbie, Russell's Jay Score, Bradbury's Mechanical Hound and Electric Grandmother, Vonnegut's Salo, Dick's Buster Friendly / Lincoln Simulacrum / Claws / Olham, Sladek's Roderick), contemporary prose SF (Neuromancer-the-AI, ART), the Star Trek expansion (Rayna Kapec, Mudd androids, Moriarty, Control), the Toy Story and Pinocchio chains, Transformers splits, anime canon (FMA, Big O, Ergo Proxy, Mahoromatic, Negima, Haruhi, Saber Marionette, Sora no Otoshimono, Fate), and a video-game cluster (NieR splits, Overwatch, Deus Ex, Persona 3, SOMA, Mass Effect's Harbinger, Mega Man, Halo Infinite's Weapon). v2.4.5 retracted four entries on rule grounds (Alphonse Elric, Hayt, Khalkotauroi, Doraemon) and corrected six codings.
- **Doc catch-up.** 40 new influence-graph edges connecting the v2.4.4 additions into the existing lineage (6 adapts/sequel, 12 ensemble-splits, 21 inherits, 1 inverts). Classification summary refreshed with the 405 / 52% divergence numbers and two new methodology bullets documenting the v2.4.4/v2.4.5 releases. Bibliography expanded with 66 new source-line additions across Poetry, Folklore, Novels, Manga, Short Stories, Comics, Film, Television, and Video Games. Boundary-case doc now carries a worked-example section on the v2.4.5 retractions.
- **Knowability/knowing divergence rate: 210 of 405 (52%)** — stabilizing as the corpus broadens (v2.0: 21%; v2.1: 36%; v2.2: 47%; v2.4: 51%; v2.4.3: 53%; v2.5: 52%).

### Analytical notes

- **Substrate convention now explicitly documented.** The v2.4.5 self-audit surfaced and formalized the corpus's `biological`-substrate convention (reserved for synth-flesh and bioengineered tissue; natural-but-inert materials code to their animating principle). Five entries were corrected to align.
- **Boundary-case discipline codified.** v2.4.5's selective retention/retraction of the three v2.4.4 boundary-flagged entries (keep Jenny, retract Alphonse and Hayt) establishes that boundary flags in notes are not substitutes for clean rule application.
- **Toy Story ontology.** The four Toy Story entries articulate the franchise's "love-creates-personhood" thesis; Forky's post-v2.4.5 substrate coding is the corpus's cleanest staging of an inert-material-plus-animating-principle constructed being.
- **Neuromancer split.** Wintermute and Neuromancer are now individuated, aligning Gibson's two-AI structure with how the corpus already handles the GITS Kusanagi/Puppet Master, NieR 2B/A2/Pascal, and DADOES replicants/Buster Friendly splits.

### Files

- `schema/cb-schema.yaml`, `CLAUDE.md`, `README.md`, `analysis/influence_graph.yaml`: schema_version bumped from 2.4 to 2.5.
- `analysis/influence_graph.yaml`: +40 edges under a new "v2.4.4 canonical-gap repair" section; HTML regenerated.
- `output/classification_summary.md`: corpus count, divergence rate, and methodology notes refreshed.
- `docs/bibliography.md`: +66 source-line additions, existing lines expanded where the same source gained new beings.
- `docs/boundary_cases.md`: "v2.4.5 retractions as worked examples" section added.
- `output/*`: all generated analyses regenerated against the 405-entry corpus.

---

## [2.4.5] — 2026-04

**v2.4.4 self-audit corrections.** 409 → 405 entries (−4). No schema changes. A critical self-review of the v2.4.4 expansion identified four entries that fail the corpus's existing inclusion rules and six coding errors that contradicted established conventions. v2.4.5 retracts the four entries to `exclusions.yaml` and regularizes the coding.

### Retractions (4)

- **Alphonse Elric** (FMA) — fails `born-then-modified`. Al is a born human child whose consciousness is relocated to a constructed armor body. The corpus excludes Cybermen, RoboCop, the Altered Carbon sleeves, and Severance innies under this rule; Alphonse is the same case. Retracted to exclusions.yaml.
- **Hayt / Duncan Idaho ghola** (Dune Messiah) — deferred for consistency with the Altered Carbon sleeves. Tleilaxu axlotl-tank growth is, on closer reading, a biological gestation process rather than pure manufacture (particularly after the *Heretics* reveal). Retracted to exclusions.yaml as boundary-deferred.
- **Khalkotauroi** (Argonautica bronze bulls) — fails the individuated-character test. Unnamed, unspoken, two-as-yoke with no individual action. Closer to Groot / the Newts' `collective-no-individual` exclusion than to the individuated entries it was drafted alongside. Retracted to exclusions.yaml; the within-source reference is noted via talos.yaml.
- **Doraemon** — scope-boundary violation. The v2.4.2 anime expansion set "widely available in Western markets" as the scope test, and Doraemon's Western distribution is genuinely thin (despite his East Asian foundational stature). Retracted to exclusions.yaml as `out-of-scope`; a future East Asian scope revision may revisit.

### Coding corrections (6)

- **Substrate regularization.** v2.4.4 over-applied `biological` to natural-but-inert materials (straw, wood, pumpkin, craft assembly). The corpus's existing convention (pinocchio.yaml, golem-prague.yaml) reserves `biological` for synth-flesh and bioengineered tissue and codes inert-material-plus-magical-animation as `magical`. Corrected entries: scarecrow-oz, jack-pumpkinhead-oz, pinocchio-disney-1940, pinocchio-del-toro (all drop `biological`; codings align with Collodi). forky-toy-story-4 drops `biological` in favor of `mechanical + magical` for the craft-assembly substrate.
- **Medium correction for Daedalus's walking statues.** v2.4.4 coded `medium: poem` for the *Meno* reference; v2.4.5 corrects to `medium: folklore`, reflecting that the statue legend is an oral tradition Plato cites rather than original prose. Aligns with brazen-head's treatment of the medieval Bacon legend.
- **Moriarty prominence downgrade.** `major → supporting`. Two-episode appearance; the cultural-influence case supports but does not justify the `major` coding under the corpus's screen-time convention.
- **Neuromancer primary_question correction.** `identity → knowledge`. Gibson's Neuromancer-the-AI is the epistemic pole of the two-AI-merger plot; the Linda-beach material is part of his knowing rather than an identity crisis.
- **Salo substrate correction.** `mechanical → mechanical + biological`. Vonnegut describes Salo with explicit organic features (feathers, oil-gland communication, orange eyes) alongside his machine status; pure `mechanical` truncated the Tralfamadorian physiology the novel stages.

### Analytical notes

- **Substrate convention now explicitly documented.** The corpus treats `biological` as a coding for synth-flesh / bioengineered tissue / DNA-based construction. Natural-but-inert materials (clay, wood, straw, stuffed fabric, cardboard, plastic craft supplies) are coded to their animating principle (typically `magical` in pre-20th-century and children's-literature entries; `mechanical` or `mechanical + electrical` in industrial entries). The v2.4.4 self-audit surfaced this convention because five entries had drifted from it.
- **Boundary-case discipline.** v2.4.4 admitted three entries with in-notes boundary flags (Alphonse, Hayt, Jenny). v2.4.5 retracts two (Alphonse, Hayt) on strict-rule grounds and retains Jenny. The retention/retraction logic: Jenny's progenation-machine origin is manufacturing without prior continuous biological birth; Alphonse and Hayt both have continuous identity with prior-born persons and so fail the `born-then-modified` rule. The discipline is that boundary flags in notes are not substitutes for clean rule application.

---

## [2.4.4] — 2026-04

**Canonical-gap repair: classical, Golden-Age-SF, Star-Trek, anime, games, Toy Story, Pinocchios.** 332 → 409 entries (+77). No schema changes. The largest single expansion since v2.4.2, repairing gaps identified in a systematic scholar-audit of the corpus against Western literature and pop-culture canon. The primary target was foundational / canonical entries the corpus had not yet acknowledged rather than new cultural moments.

### Summary

- **Corpus expanded from 332 → 409 entries (+77, +23%).** Schema unchanged.
- **Classical / medieval gaps.** Khalkotauroi (Argonautica bronze bulls), Celedones (Pindar singing-maidens), Daedalus's walking statues (Plato's Meno), Albertus Magnus's android (medieval legend). The classical-automaton tradition is now substantially more complete.
- **Romantic / pulp lineage.** Hawthorne's mechanical butterfly ("The Artist of the Beautiful", 1844), Ellis's Steam Man of the Prairies (1868), Baum's Scarecrow (1900) and Jack Pumpkinhead (1904).
- **Golden-Age SF.** Asimov's Cutie / Speedy / Liar!-Herbie. Eric Frank Russell's Jay Score. Bradbury's Mechanical Hound and Electric Grandmother. Vonnegut's Salo (*Sirens of Titan*). Philip K. Dick's Simulacrum Lincoln, Buster Friendly, the "Second Variety" Claws, "Impostor" Olham. John Sladek's Roderick.
- **Contemporary prose SF.** Neuromancer-the-AI (distinct from Wintermute), Hayt (Duncan Idaho ghola, *Dune Messiah*), ART (Murderbot Diaries' *Artificial Condition* onwards).
- **Star Trek.** Rayna Kapec (TOS "Requiem for Methuselah"), Norman and the Mudd Androids (TOS "I, Mudd"), Professor Moriarty (TNG "Elementary, Dear Data" / "Ship in a Bottle"), Control (Discovery S2). Four canonical Star Trek entries the corpus had been missing.
- **Doctor Who.** D84 and the Voc Robots ("The Robots of Death", 1977), the Handbots ("The Girl Who Waited", 2011), Jenny ("The Doctor's Daughter", 2008; boundary-deferred flag).
- **Star Wars.** Chopper (*Rebels*/*Ahsoka*), Triple-Zero (*Darth Vader* comics 2015), D-O (*Rise of Skywalker*).
- **Toy Story / Disney.** Woody, Buzz Lightyear, Forky, Olaf (*Frozen*), plus source-text splits for the Disney 1940 *Pinocchio* and Guillermo del Toro's 2022 *Pinocchio*. The Pinocchio lineage chain is now Collodi → Disney 1940 → del Toro 2022.
- **Transformers.** Bumblebee, Starscream, Dinobot (*Beast Wars* "Code of Hero").
- **Anime / manga canonical additions.** Alphonse Elric (boundary-flagged), Father, and Envy (*Fullmetal Alchemist*); Illyasviel von Einzbern (*Fate/Stay Night*); Dorothy R. Wayneright (*The Big O*); Pino (*Ergo Proxy*); the Puppet Master / Project 2501 (within-source split from kusanagi-gits-1995); Mahoro (*Mahoromatic*); Chachamaru (*Negima*); Yuki Nagato (*Haruhi Suzumiya*); Lime and sisters (*Saber Marionette J*); Ikaros (*Heaven's Lost Property*); Doraemon (scope-boundary flagged).
- **Video games.** A2, Pascal, Adam and Eve (*NieR: Automata*, within-source splits); Bastion, Zenyatta (*Overwatch*); Helios (*Deus Ex*); Mega Man; WAU (*SOMA*); Harbinger (*Mass Effect*); Aigis (*Persona 3*); The Weapon (*Halo Infinite*).
- **Misc film/TV.** Colossus: The Forbin Project (1970 film, distinct from 1966 novel); The Questor (*Questor Tapes*); Mechagodzilla; ED-209 (*RoboCop*); Orac and Zen (*Blake's 7*); Quorra (*Tron: Legacy*); Tik-Tok (*Return to Oz* 1985 film, distinct from 1907 novel).
- **MCU AI cluster.** FRIDAY, KAREN ("Suit Lady"), Ragnarok / Clor (*Civil War* 2006).

### Analytical notes

- **Boundary-case additions.** Three entries admitted with explicit boundary-flag in notes: Alphonse Elric (FMA; born-then-modified vs. constructed ambiguity), Jenny (Doctor Who; progenation-machine ambiguity), Hayt (Dune ghola; cloned-plus-conditioning frame). All flagged for possible exclusion in future revisions if the born-then-modified rule is tightened.
- **Doraemon scope flag.** Included on foundational-prominence grounds with an explicit note that pre-2020s Western consumption was limited. Future scope revisions may reclassify.
- **Toy Story ontology.** The four *Toy Story* entries (Woody, Buzz, Forky) articulate the franchise's "love-creates-personhood" thesis; Forky's triple-substrate coding (`biological` + `mechanical` + `magical`) is the corpus's most explicit staging of this ontology.
- **Sequel-chain repairs.** Pinocchio: Collodi → Disney 1940 → del Toro 2022. Tik-Tok: 1907 novel → 1985 film. Cortana (Halo 4) → The Weapon (Halo Infinite). Claws ("Second Variety") → Screamers (1995).
- **Within-source splits.** A2, Pascal, Adam-and-Eve are within-source splits from the 2B/9S entries in *NieR: Automata*. Buster Friendly is within-source from the *DADOES* replicants. The Puppet Master is within-source from Kusanagi (1995). Khalkotauroi is within-source from Talos (Argonautica). Neuromancer-the-AI is within-source from Wintermute and Dixie Flatline. These splits follow the corpus's existing ensemble-split convention.

---

## [2.4.3] — 2026-04

**Bad-TV sidekicks and post-ChatGPT streaming/cinema expansion.** 313 → 332 entries (+19). No schema changes. Two scope repairs: (1) pre-80s and 80s TV sidekick/edge-case androids the earlier expansions missed, and (2) the emerging post-ChatGPT era of mass-culture AI depictions (2023–2025), where AI has visibly moved from SF speculation to daily cultural reference and the character-roles are shifting accordingly.

### Summary

- **Corpus expanded from 313 → 332 entries (+19, +6%).** Schema unchanged.
- **Bad-TV sidekick/edge-case coverage.** Ten entries repairing the pre-1990 American-network-TV android slot: Hymie (*Get Smart*, 1965), Rhoda Miller (*My Living Doll*, 1964), the Fembots (*Six Million Dollar Man*, 1976), Maximillion (*The Bionic Woman*, 1977), Yoyo (*Holmes & Yoyo*, 1976), Muffit II (*BSG* 1978), Andy (*Quark*, 1977), Dr. Theopolis (*Buck Rogers*, 1979), Automan & Cursor (*Automan*, 1983), Eve Edison (*Mann & Machine*, 1992).
- **Post-ChatGPT cultural-moment coverage.** Nine entries across 2020–2025 where the AI depiction has clearly shifted in register to reflect mass-public LLM availability: the Entity (*Mission: Impossible*, 2023/25), AIA (*Afraid*, 2024), Sunny (*Sunny*, 2024), Cosmo (*The Electric State*, 2025), Mickey Barnes (*Mickey 17*, 2025), Rouge Redstar (*Metallic Rouge*, 2024), Ares (*Tron: Ares*, 2025), Regus Patoff (*The Consultant*, 2023), and the earlier Devs Machine (*Devs*, 2020), which belongs analytically with this cluster.

### Analytical notes

- **Post-ChatGPT register shift.** The 2023–2025 entries share structural features that distinguish them from pre-2020 AI depictions: (1) disembodied/distributed operation over networks rather than anthropomorphic embodiment (Entity, AIA), (2) explicit reference to LLMs/language as the substrate (nearly all carry `linguistic` substrate), (3) `interiority: undecidable` appearing more frequently as the schema-level response to "can we tell the difference between simulation and experience" becoming a live cultural question (Entity, Patoff). This is the first release where `undecidable` is meaningfully clustered rather than a rare exception.
- **Hidden-programming-underneath structure.** *Sunny* introduces a distinctive 2020s coding pattern: the household AI that is not malfunctioning and not possessed but is carrying hidden specification from a party other than the nominal owner. This register will likely recur.
- **Print-with-memory-transfer entry.** *Mickey 17* is the corpus's first film-era canonical entry where bioprinting plus memory transfer produces a being coded as constructed rather than continuous. The coding follows the Black Mirror cookies precedent (the simultaneous-duplicates scene being the argument) rather than the *Pantheon*/*Upload* exclusion.

---

## [2.4.2] — 2026-04

**Schlock-cinema, horror-doll, and anime scope expansion.** 260 → 313 entries (+53). No schema changes. The largest single expansion since v2.4.0, repairing three of the corpus's previously-acknowledged thin spots: (1) low-budget and direct-to-video SF cinema across seven decades, (2) the magical-animation horror-doll lineage as legitimate constructed beings rather than an elided genre, and (3) anime/manga commonly consumed in Western markets.

### Summary

- **Corpus expanded from 260 → 313 entries (+53, +20%).** Schema unchanged. All entries conform to v2.4.
- **B-movie / schlock SF cinema coverage across seven decades.** 50s (Robot Monster, Gog, Tobor), 60s (Creation of the Humanoids), 70s (Silent Running, Westworld, Dark Star, Logan's Run), 80s (Saturn 3, Heartbeeps, Clash of the Titans, Android, Electric Dreams, Making Mr. Right, Cherry 2000, Chopping Mall, Deadly Friend), 90s (Hardware, Eve of Destruction, Lawnmower Man, Virtuosity, Screamers, Solo, Class of 1999), 2000s–2020s (Stealth, 9, The Machine, Autómata, Upgrade, Tau, A.X.L., Archive, Mother/Android, Jung_E, Atlas, Subservience).
- **Horror-doll lineage formally admitted.** Seven entries covering the animated-artifact horror tradition: Chucky (Child's Play), Toulon's Puppets (Puppet Master), the Obelisk Dolls (Dolls 1987), Demonic Toys, Billy (Dead Silence), Annabelle, Slappy (Goosebumps). All coded as `[magical, mechanical]` substrate following Tyrone and the Prague Golem.
- **Anime/manga scope opened.** Ten anime entries (Sharon Apple, Armitage, Lain, Chi/Chobits, Sammy, Isla, Lacia, Vivy) plus manga (Alpha Hatsuseno, Urasawa's Atom/Pluto). The `out-of-scope` exclusion reason in `data/exclusions.yaml` revised to reflect the scope opening.
- **Knowability/knowing divergence: ~52% of entries** (holding steady as the corpus grows). The schlock corpus clusters at `knowability: absent, knowing: absent` (B-movie register); the anime additions cluster at `knowability: primary, knowing: present` (characteristic of the SF-anime philosophical register).

### New entries (53)

**Film — 50s schlock (3):** Ro-Man (*Robot Monster*, 1953), Gog/Magog (*Gog*, 1954), Tobor (*Tobor the Great*, 1954).

**Film — 60s (1):** The Clickers (*Creation of the Humanoids*, 1962).

**Film — 70s (4):** Huey/Dewey/Louie (*Silent Running*, 1972), The Gunslinger (*Westworld*, 1973), Bomb #20 (*Dark Star*, 1974), Box (*Logan's Run*, 1976).

**Film — 80s (9):** Hector (*Saturn 3*, 1980), Val and Aqua (*Heartbeeps*, 1981), Bubo (*Clash of the Titans*, 1981), Max 404 (*Android*, 1982), Edgar (*Electric Dreams*, 1984), The Protectors (*Chopping Mall*, 1986), BB/Samantha (*Deadly Friend*, 1986), Cherry 2000 (1987), Ulysses (*Making Mr. Right*, 1987).

**Film — horror dolls (6):** The Obelisk Dolls (*Dolls*, 1987), Chucky (*Child's Play*, 1988), Toulon's Puppets (*Puppet Master*, 1989), Demonic Toys (1992), Billy (*Dead Silence*, 2007), Annabelle (*The Conjuring*, 2013).

**Novel — horror dolls (1):** Slappy (*Goosebumps*, 1993).

**Film — 90s (8):** The Educators (*Class of 1999*, 1990), M.A.R.K. 13 (*Hardware*, 1990), Eve VIII (*Eve of Destruction*, 1991), Jobe Smith (*The Lawnmower Man*, 1992), SID 6.7 (*Virtuosity*, 1995), Screamers (1995, after PKD's "Second Variety"), Solo (1996).

**Film — 2000s–2020s (12):** EDI (*Stealth*, 2005), The Stitchpunks (*9*, 2009), Ava (*The Machine*, 2013), The Pilgrims (*Autómata*, 2014), STEM (*Upgrade*, 2018), Tau (2018), A.X.L. (2018), J1/J2/J3 (*Archive*, 2020), The Androids (*Mother/Android*, 2021), Jung_E (2023), Smith/ARC-9 (*Atlas*, 2024), Alice (*Subservience*, 2024).

**Anime — television (8):** Sharon Apple (*Macross Plus*, 1994), Naomi Armitage (*Armitage III*, 1995), Lain Iwakura (*Serial Experiments Lain*, 1998), Chi/Elda/Freya (*Chobits*, 2001), Sammy (*Time of Eve*, 2008), Isla (*Plastic Memories*, 2015), Lacia (*Beatless*, 2018), Vivy/Diva (*Vivy: Fluorite Eye's Song*, 2021).

**Manga (2):** Alpha Hatsuseno (*Yokohama Kaidashi Kikō*, 1994), Atom (*Pluto*, Urasawa 2003 / 2023 anime).

### Analytical notes

- **Horror-doll coding convention established.** Magically animated constructed beings are coded with substrate `[magical, mechanical]` (or `[magical]` when the artifact body is itself enchanted rather than mechanically constructed), consistent with Tyrone (*Hand to God*) and the Prague Golem. The horror-doll entries are the first large-scale application of this convention.
- **Schlock-register clustering.** The B-movie entries cluster in the `interiority: none / claims` range and at `knowability: absent`, reflecting the schlock SF register's general disinterest in the consciousness question. Exceptions (SID 6.7, Max 404, Jobe) are noted as anomalies within their category.
- **Anime rights-arc lineage.** The anime entries disproportionately carry `primary_question: rights` or `identity` with high `knowability` — a distinct-from-Western-cinema analytical profile that the expanded corpus now surfaces. Particularly visible in Armitage, Time of Eve, Jung_E, Chobits, Plastic Memories.
- **`out-of-scope` exclusion reason revised** in `data/exclusions.yaml` to reflect that anime/manga widely available in Western markets is now in scope. Purely-Japanese texts without substantial Western distribution remain out-of-scope pending consultation.

---

## [2.4.1] — 2026-04

**Cheesy-cinematic and meta-constructed TV addenda.** 254 → 260 entries (+6). No schema changes. Adds six long-standing gaps in the TV sub-corpus, all in the built-for-company lineage: Twiki and Booti from *Buck Rogers in the 25th Century* (1979–81), and the four Satellite of Love bots from *Mystery Science Theater 3000* (1988–).

### New entries (6)

**Television — Buck Rogers (2):** Twiki (the TWKE-4 ambuquad, voiced by Mel Blanc), Booti (Twiki's love interest, voiced by Joan Rivers; included for the feminine-presentation-on-shared-substrate coding it enables, which rhymes with Gypsy below).

**Television — Mystery Science Theater 3000 (4):** Crow T. Robot, Tom Servo, Gypsy, Cambot. All four are diegetically constructed by Joel Robinson from scrap aboard the Satellite of Love; the ensemble-split tag is used across the four to record that card values diverge meaningfully (Cambot: primary_question `none`, epistemic_reach `behavioral`; the rest: `affection` + `conversational`; Gypsy: `designed` autonomy vs. Crow/Servo's `seized`).

### Analytical notes

- **Feminine-on-shared-substrate pairing.** Booti (Buck Rogers) and Gypsy (MST3K) both code feminine presentation layered onto a body-design otherwise indistinguishable from their masculine-coded counterparts (Twiki; Crow and Servo). The schema's `presentation` field records this vocabulary; the notes flag the structural echo between the two.
- **Meta-constructed beings.** The MST3K bots are the first corpus entries where the diegetic creator (Joel Robinson, a captive) is themselves a character, the building is an act of desperation-companionship, and the resulting bots regularly riff on other constructed beings in the SF movies they're forced to watch. Feeds a potential future analytical thread on recursive constructed-being coding.

---

## [2.4.0] — 2026-04

**Performing-arts and post-Siri/Alexa television expansion.** 224 → 254 entries (+30). First schema enum addition since v2.2 (`comics`): `opera`, `ballet`, and `musical` added to the medium enum. Repairs the corpus's two thinnest coverage areas — major TV sci-fi after the Siri/Alexa launches (2011, 2014) and stage works of any kind.

### Summary

- **Corpus expanded from 224 → 254 entries (+30, +13%).** All entries conform to the v2.4 schema.
- **Stage-works coverage tripled.** Pre-v2.4 the corpus had 5 stage entries, all pre-1925 (Brazen Head, Faust II Homunculus, Coppélia, Hoffmann/Olimpia, R.U.R.). v2.4 adds 13 stage entries spanning 1871–2017, including ballet (Petrushka), opera (d'Albert *Der Golem*), musicals (*Be More Chill*, *Maybe Happy Ending*), and major modern plays (*A Number*, *Marjorie Prime*, *The Nether*, *After the Blast*, *Hand to God*, the Nick Dear *Frankenstein*). Total stage entries: 17.
- **Post-2011 TV coverage expanded.** Pre-v2.4 had 21 post-2011 TV entries with major franchise gaps (Rick and Morty entirely absent; only Bender from Futurama; no Lower Decks; no Mrs. Davis). v2.4 adds 17 TV entries closing the most visible gaps.
- **Knowability/knowing divergence: 129 of 254 entries (51%).** Up from 47% in v2.3. The split continues to capture genuine analytical structure as the corpus grows.
- **Primary/primary cluster grew from 15 to 19 entries.** New primary/primary entries: Mrs. Davis, Marjorie Prime (play and film), Walter Prime, the Cleon Dynasty, Dolores Westworld, Niska, the SQUIP. The cluster's center of gravity is now firmly post-2011.
- **Observer-divergence cluster grew from 23 to 28 entries.** New observer-divergence entries: the Cleon Dynasty, Mrs. Davis, the Sons of A Number, Walter Prime, Marjorie Prime film. The Coppélia → Petrushka inversion expands the cluster's pre-1920 footprint.

### Schema changes

- **`opera`, `ballet`, and `musical` added to `metadata.medium` enum.** Non-breaking addition; existing `play` entries remain valid. Six entries reclassified to the new values: Coppélia and Petrushka (→ `ballet`), Olimpia and Der Golem (→ `opera`), Be More Chill and Maybe Happy Ending (→ `musical`). The bibliography's "Drama, Opera, Ballet, and Musicals" section was renamed to reflect the corpus's stage-medium diversity. `validate.py` and `analyze.py` updated accordingly.
- **No other schema changes.** Card axes, substrate, motivation, presentation, embodiment, prominence, creator_relationship, and tags are all unchanged.
- **Schema version bumped** from `"2.3"` to `"2.4"` in `schema/cb-schema.yaml`.

### New entries (30)

**Television — Rick and Morty (3):** Butter Robot ("Something Ricked This Way Comes," 2014), Mr. Meeseeks ("Meeseeks and Destroy," 2014), Space Cruiser AI ("The Ricks Must Be Crazy," 2015).

**Television — Star Trek: Lower Decks (3):** AGIMUS ("Where Pleasant Fountains Lie," 2021), Badgey ("Terminal Provocations," 2020 + S4 arc), Peanut Hamper ("No Small Parts," 2020 + "A Mathematically Perfect Redemption," 2022).

**Television — ensemble splits (4):** Calculon (Futurama), Robot Santa (Futurama), Dolores (Westworld), Niska (Humans).

**Television — standalones (7):** Mrs. Davis (Lindelof/Hernandez, 2023), AIDA / Madame Hydra (Agents of S.H.I.E.L.D., 2016–17), Miss Minutes (Loki, 2021–23), Ashley Too (Black Mirror, 2019), Zora (Star Trek: Discovery, 2019–22), the Cleon Dynasty (Foundation, 2021–), Professor Huyang (Ahsoka, 2023; Clone Wars 2012).

**Stage — plays (7):** Marjorie Prime (Harrison, 2014), Sons of A Number (Churchill, 2002), the Nick Dear *Frankenstein* (NT/Boyle, 2011), Iris (Haley's *The Nether*, 2013), Watson Intelligence (George, 2013), Tyrone (Askins's *Hand to God*, 2011), Arthur (Kazan's *After the Blast*, 2017).

**Stage — opera (1):** d'Albert *Der Golem* (1926).

**Stage — ballet (1):** Petrushka (Stravinsky/Fokine/Benois, 1911).

**Stage — musical (2):** the SQUIP (*Be More Chill*, Iconis/Tracz, 2015), Oliver and Claire (*Maybe Happy Ending*, Aronson/Park, 2016/Broadway 2024).

**Stage — adaptation (1):** Galatea-Gilbert (W.S. Gilbert's *Pygmalion and Galatea*, 1871).

**Film (1):** Marjorie Prime film (Almereyda, 2017) — adaptation of Harrison's play.

### Reclassifications

Six entries had their `medium` value reclassified following the enum addition:

- `coppelia-delibes` (1870): `play` → `ballet`
- `petrushka-stravinsky` (1911): `play` → `ballet`
- `olimpia-offenbach` (1881): `play` → `opera`
- `golem-d-albert-opera` (1926): `play` → `opera`
- `squip-be-more-chill` (2015): `play` → `musical`
- `oliver-claire-maybe-happy-ending` (2016): `play` → `musical`

No card properties (interiority, autonomy, divergence, primary_question, epistemic_reach, knowability, knowing) were changed for these entries. Notes were updated to reference the v2.4 reclassification.

### Exclusions register

Eleven new entries added to `data/exclusions.yaml`, repairing the v2.3 boundary-case coverage gap:

**Television exclusions (8):** Cybermen (Doctor Who, born-then-modified), the Borg (Star Trek, born-then-modified), the Innies (*Severance*, born-then-modified surgical partition), Uploaded Intelligences (*Pantheon*, born-then-modified upload), Nathan Brown and the Upload uploads (*Upload*, born-then-modified), the Sleeves (*Altered Carbon*, born-then-modified), the Peripherals (*The Peripheral*, boundary-deferred biomechanical), the Cyberpunks (*Edgerunners*, born-then-modified).

**Theater exclusions (3 + 1 cluster):** Eliza Doolittle (Shaw's *Pygmalion*, metaphorical-construct), Audrey II (*Little Shop of Horrors*, alien species), Mr. Zero (Rice's *The Adding Machine*, born-then-modified), and a cluster entry for theatrical puppets representing born characters (War Horse / Lion King / Life of Pi stage adaptations).

### Influence graph

- **32 new edges** added across the v2.4 expansion. Highlights:
  - The **Coppélia (1870) → Petrushka (1911) → R.U.R. (1920)** lineage now traces the puppet-with-soul tradition end to end. Petrushka is the load-bearing pre-RUR stage entry.
  - The **422-year Brazen Head → Tyrone** edge is the corpus's longest stage-to-stage influence edge, both coding interiority in the `claims`/`undecidable` cluster.
  - **A Number (Churchill, 2002) → Foundation Cleons (2021)** connects the two major clone-identity entries across stage and TV.
  - **Cookie ↔ Marjorie Prime (both 2014)** as same-year tonal inversion: same digital-recreation-of-the-dead mechanism, opposite tonal valence.
  - **Mrs. Davis** added to the benevolent-surveillance lineage from Person of Interest's Machine and Samaritan.
  - **Maybe Happy Ending** added to the WALL-E / Klara of the Sun discarded-companion-bot lineage.
  - **TOS evil-computer (M-5, Nomad) → AGIMUS** explicitly canonizes a 53-year lineage that *Lower Decks* makes diegetic.

### Documentation

- **`SCHEMA.md`** updated: medium-enum table expanded with notes column and v2.4 expansion callout; conversational-reach distribution note updated to 61% (156/254).
- **`docs/bibliography.md`** drama section renamed to **"Drama, Opera, Ballet, and Musicals"** and expanded from 5 to 18 entries; new TV entries added across Black Mirror, Rick and Morty, Lower Decks, Star Trek: Discovery, Loki, Foundation, Mrs. Davis, Ahsoka, Agents of S.H.I.E.L.D., and Maybe Happy Ending.
- **`README.md`** corpus statistics updated (224 → 254, 47% → 51% knowability/knowing divergence); BibTeX citation version bumped to 2.4.
- **`CLAUDE.md`** entry count and version reference updated.
- **`data/exclusions.yaml`** expanded with 11 new exclusion entries (see above).

### Source verification

The 30 v2.4 entries underwent a source-and-classification audit before release. Specific verifications:

- Premiere dates and venues confirmed for all 13 stage entries.
- Episode citations confirmed for all 6 *Rick and Morty* and *Lower Decks* episodes.
- Pulitzer-finalist claims for *Marjorie Prime* (2015) and *Watson Intelligence* (2014) confirmed against publicly listed records.
- Tony-related claims for *Maybe Happy Ending* softened to "major awards-season presence" pending verification of June 2025 ceremony outcomes.

### Migration notes

- **No breaking changes.** v2.3 tooling, validators, and analysis scripts work against v2.4 unchanged except for the medium enum addition. Anything that hardcodes the medium values (custom downstream code) needs to add `opera`, `ballet`, and `musical` to its allow-list.
- **Entry count in hardcoded headers updated.** `README.md` and `CLAUDE.md` are now updated.
- **Git recoverability.** The v2.3 224-entry corpus is the state at commit `a935c8f` (the v2.3 merge); the v2.4 expansion runs in three commits on the `claude/add-tv-show-references-TWtpm` branch.

### Known issues

- **Performing-arts coverage is now adequate for the post-1900 era but remains thin for pre-1900 opera and ballet.** A future expansion could add the Wegener / Wedekind / Rachilde turn-of-century constructed-being plays, opera adaptations of Frankenstein, and the Coppélia / Petrushka / R.U.R. cluster's intermediate Romantic ballets.
- **2024–2025 entries flagged as lower-confidence.** The Maybe Happy Ending Broadway claims and the Skeleton Crew / Mrs. Davis recency may benefit from re-review after wider critical discussion. No 2025 TV entries added in v2.4 pending broader critical landing.
- **Watson Intelligence and Marjorie Prime entries flag the post-Siri/Alexa cluster as 2013-onset rather than later.** This is consistent with the README's central finding but worth noting as the corpus continues to backfill.

---

## [2.3.0] — 2026-04

**Formal release.** Polish and consistency pass preparing v2.2 for Zenodo publication. No new entries; no schema changes.

### Changed

- **Citation version bumped** from 2.2 to 2.3 in README BibTeX block.
- **Companion piece** described as "blog" (Substack publication) rather than "essay" throughout.
- **Influence graph description** updated to remove stale "v2.0" and "Western fiction" references.
- **Classification summary methodology notes** updated: non-Western scope note reflects v2.2 Japanese entries; analytically significant entries list updated to include Harey (1961) and Golem XIV (1981); Companion and M3GAN 2.0 added to flagged-entries list.
- **M3GAN 2.0 autonomy** corrected from `seized` to `emergent` (matching first film and notes' claim of card stability).
- **Five missing influence graph edges** added: kusanagi→ava (observer-knowability), wall-e→roz (robot-learns-to-love), iron-giant→roz (animated departure), olympia→rei (observer lineage), data→demerzel (institutional humaniform).
- **CONTRIBUTING.md** medium note simplified, version pinning removed.
- **All analysis outputs regenerated** against final 224-entry corpus.

### Corpus

Unchanged at **224 entries**. 107 of 224 (47%) have divergent knowability/knowing values. 23 observer-divergence entries. 15 primary/primary entries. Influence graph: ~85 edges across 6 edge types.

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
