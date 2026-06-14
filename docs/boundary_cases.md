# Boundary Cases

This document discusses entities that sit on or near the boundary of the constructed being (CB) definition. For each category, it explains the reasoning behind inclusion or exclusion and points to the criteria that decide.

The CB definition used by this ontology requires three things:

1. **Made, not born.** The entity's existence originates from a deliberate act of construction, programming, enchantment, or creation — not from biological reproduction. **As of v3.0, the rule is refined: a born person who is biotechnically modified, copied, transferred, or reconstructed becomes a constructed being for corpus purposes when the source text treats the resulting entity as a new being rather than as a continuation of the prior person.** The `metadata.origin` field codes the pathway explicitly.
2. **Agent-like.** The entity exhibits or is attributed behavior that implies agency: goal pursuit, language use, decision-making, or social interaction.
3. **Narrative presence.** The entity appears in a specific, citable text.

Everything discussed below either meets all three criteria (and is included), fails at least one (and is excluded), or poses a genuine definitional problem that the schema cannot cleanly resolve.

---

## The v3.0 `origin` axis

The v2.x corpus enforced the made-not-born rule by exclusion alone: anything that started as a born person was kept out, even when the source text staged the resulting being as a new entity. v3.0 replaces that implicit rule with the explicit `metadata.origin` field. Six pathways are coded:

| Origin | Meaning | Examples |
|---|---|---|
| `manufactured` | Assembled or grown from raw or processed material; no specific prior person is at narrative issue. **Default**. | Talos, HAL 9000, Pinocchio, R.U.R., Vision, the Replicants, most of the corpus. |
| `assembled` | Built from parts of one or more dead persons; the source text treats the result as a new being. | Frankenstein's Creature, the Universal Monster, the Bride, Herman Munster, Shrike (Mortal Engines). |
| `cloned` | Biological copy of a specific template person, gestated or printed as that copy. | The Cleon dynasty, Jenny (the Doctor's Daughter), Call (Alien: Resurrection), Mickey 17. |
| `copied` | A specific person's mind, memories, or personality is copied to a new substrate; the copy is the narrative entity, distinct from the original. | Cookie (Black Mirror), Ashley Too, Bernard Lowe (Arnold-derived), Marjorie Prime, White Vision. |
| `converted` | A living born person undergoes biotechnical modification; the source text treats the result as a new kind of being rather than a continuation of the prior person. | The Cybermen, the Borg (and Locutus, Seven of Nine, Hugh, the Queen), RoboCop, Cain (RoboCop 2), Cyborg (Victor Stone), MODOK, Deathlok, Robotman (Cliff Steele), Davros, Franky, the Bionic Man and Bionic Woman, Airiam. |
| `transferred` | A person's mind is moved to a new substrate; the original body ceases; the new being is presented as new. | 8 Man (Yokoda), Cyborg Superman (Hank Henshaw). |

The exclusion rule that survived from v2.x and is now formalized:

> **A born person who is modified or copied is excluded if the source text treats the resulting being as a continuation of the prior person.** The Six Million Dollar Man's Steve Austin would have been excluded under v2.x and would still be excluded under v3.0 *if* the 1974 series framed him as Steve-still-himself-with-augments — but the show's recurring "is he still Steve?" beats and the Bionic Woman pilot's death-and-revival reframe push it across the line. The v3.0 inclusion turns on the show's narrative framing, not on the surgery's extent.

The boundary line moved one step. **It did not vanish.** The cases still excluded are listed in `data/exclusions.yaml` under the `continuation-of-prior-person` reason (which replaces the v2.x `born-then-modified` reason for upload/transfer/conversion cases where the source text frames the result as continuous; the older value is preserved for textual cases where born-then-modified does the work and continuity isn't the live question).

---

## Included: the unambiguous cases

These entities are squarely inside the definition and present no real boundary problem. They appear in the main `data/beings/` directory:

- **Mechanical / electromechanical beings** with narrative agency: Talos, HAL, the T-800, WALL-E, EMERAC.
- **Biological constructions**: Frankenstein's Creature, the R.U.R. robots, the replicants across Dick/Scott/Villeneuve.
- **Magical animation**: Galatea, the Golem of Prague, Pinocchio, False Maria (per Metropolis's mix of mechanical body and alchemical animation).
- **Digital-native beings**: GLaDOS, Cortana, Samantha, JARVIS, Vision.

All of these satisfy made + agent-like + narrative presence.

---

## Included with a note: the mythic cases

**Pandora (Hesiod, ~700 BCE)** and **Talos (Argonautica, ~250 BCE)** are often asked about in the boundary-case sense. They are included because the three criteria are all satisfied:

- **Made, not born**: Pandora is explicitly manufactured by Hephaestus at Zeus's direction from clay and divine gifts. Talos is explicitly forged by Hephaestus as a gift to Europa/Minos.
- **Agent-like**: Pandora has enough agency to open the jar. Talos has enough to patrol the Cretan coast, recognize intruders, and hurl boulders.
- **Narrative presence**: Hesiod and Apollonius respectively.

The complication with both is that their "creators" are gods. The `metadata.creator` field can accommodate phrases like "Hesiod (Hephaestus in-narrative)," tracking both the authorial and in-narrative creator as a single string.

---

## Excluded: divine creation of persons

Eve (Genesis) is **excluded**. Reasoning:

- **Divine creation of a full human person is categorically different from artisanal making.** God forming Eve from Adam's rib shares surface features with construction (a creator, raw material, a deliberate act). But Eve is immediately and fully human — she bears children, makes moral choices, converses with God. She is a person, not an artifact.
- **The schema has no field to distinguish this boundary.** Including Eve would require coding her as if she were a constructed being in the same sense as Pandora or Galatea, and that coding would be misleading.

The same reasoning applies to other divine creations of full persons (Adam, the angelic hosts). These are outside the ontology.

**What this means for Pandora and Galatea.** Both are arguably "divine creations of persons" in a weak sense. The difference is that both are explicitly framed as artifacts in their source texts — Pandora is a "gift" assembled from components, Galatea is a sculpted statue. They are made the way things are made, not the way people are made. Eve is made the way people are made, dressed up in making-language.

---

## Excluded: biological reproduction, including divine pregnancy

Beings whose origin is biological reproduction, however miraculous, are not constructed beings:

- **Divine conception** (e.g., the Christ of the Gospels, various hero myths) is still biological reproduction in a narrative sense. The mother is pregnant; the child is born.
- **Immaculate conception** (Catholic doctrine about Mary) is a theological claim about the absence of original sin, not about a manufacturing process.
- **Parthenogenesis and cloning** in fiction (e.g., certain comic-book origins) are biological reproduction variants. A clone born from a tank is still born.

The bright line is **manufacturing vs. gestation**. Clones manufactured without gestation (R.U.R.'s robots, replicants) are in. Clones grown in artificial wombs but gestated are arguably in; clones born from surrogates are arguably out. The schema does not attempt to adjudicate every edge case — it trusts the coder's judgment and asks for the reasoning to be documented in `notes`.

---

## Born-then-modified: refined in v3.0

This section was rewritten in v3.0 to reflect the new `origin` axis. Earlier sprints treated all born-then-modified beings as excluded; v3.0 admits the subset whose source texts treat the result as a new being.

**Included under v3.0** (with `origin: converted`, `copied`, or `transferred`):

- **The Cybermen** (Doctor Who, 1966) — `origin: converted`. The conversion process is the show's recurring horror, and the resulting being is treated as a Cyberman, not as the converted human's continuing self. Episodes where the original emerges (Bill Potts in "World Enough and Time," 2017) are staged as restoration, not as continuity having been preserved.
- **The Borg** (Star Trek: TNG, 1989) — `origin: converted`. Assimilation is staged as the Collective replacing the prior identity; recovery stories (Picard, Hugh, Seven) explicitly treat the prior person as something to be *recovered*, not continued.
- **RoboCop / Murphy** (1987) — `origin: converted`. The 1987 film does foreground "is he still Murphy" but uses the question to stage the *reassertion* of identity against OCP's spec — i.e., the film treats the cyborg as a new entity from which the Murphy-self emerges through narrative work, rather than as Murphy with armor. The reasonable-coder objection (Murphy as continuous) is documented in the entry's notes.
- **Steve Austin** (Six Million Dollar Man, 1974) — `origin: converted`. Borderline; admitted because the series and the Bionic Woman spinoff both make the rebuilding the show's defining ontological event.
- **Jaime Sommers** (Bionic Woman, 1976) — `origin: converted`. Sharper than Austin: she dies in her introductory two-parter and is revived with amnesia, which the show explicitly treats as a new self with Austin-era memories partially restored.
- **8 Man** (1963) — `origin: transferred`. The detective Yokoda dies and his mind is moved into the robot body; the original ends, the new being is presented as new.
- **Cyborg Superman / Hank Henshaw** (1990) — `origin: transferred`.
- **Cookies, Ashley Too, Bernard Lowe, Marjorie Prime, White Vision** — `origin: copied`. The source texts in each case foreground the constructed nature of the copy and treat the copy as its own narrative entity, distinct from the original.

**Still excluded** (cases where the source text frames the result as continuation of the prior person):

- **Molly Millions** (Neuromancer, 1984) — Gibson's narrative treats the chrome as augmentation; Molly is still Molly. `continuation-of-prior-person`.
- **Genos** (One Punch Man) — same. The character's grief structure depends on continuous identity through the conversion.
- **The Cyberpunks of Edgerunners** — same. Their tragedy is what cyberpsychosis does to *them*, not what was replaced.
- **Severance innies** — the show is explicit that the innies and outies are partitioned aspects of one continuous person; the rights claim depends on this.
- **Pantheon UIs / Upload uploads** — both texts treat the upload as the continuation of the original person.
- **Altered Carbon sleeves** — the sleeves are biological vessels for cortical-stack consciousness that is continuous with the born person.
- **Caliban** (The Tempest) — born of Sycorax, modified by Prospero, but always continuous Caliban.

**The new bright-line test:** ask of the source text, "does the work treat this being as a new entity in its own right, or as the prior person continuing?" If the former, `origin: converted`/`copied`/`transferred`. If the latter, exclude.

If you want to dispute a v3.0 inclusion or exclusion, open an issue with the textual evidence. The classification turns on what the source text does, not on the extent of the modification.

---

## Excluded: collectives without individual identity

"The robots" as an undifferentiated mass are excluded. We code individual named or individuated entities. This is why:

- **R.U.R. Robots** get a single entry because the play treats them as a collective with emergent shared consciousness. Čapek is thinking about a class, not about individuals.
- **Cylons (reimagined BSG)** have an ensemble entry plus split entries for Cavil, Eight, and D'Anna (added in v2.1) where the base models code meaningfully differently from the ensemble anchor.
- **Westworld Hosts** have an ensemble entry plus split entries for Bernard, Maeve (v2.1), and Dolores (v2.4). The Hosts ensemble entry remains the anchor; the splits exist because the individuated cards diverge from the ensemble's aggregate.
- **Foundation Cleons** are coded as an ensemble of three (Brother Dawn / Brother Day / Brother Dusk) within a single entry, because the show's structural innovation is precisely to refuse to individuate them. The `ensemble-split` tag flags this without requiring three separate entries.

The bright line is **does the text individuate this character**. If yes, it gets an entry. If the text treats the population as collective, the entry is for the collective and the notes acknowledge that individuals within the population may diverge from the card.

---

## Excluded: metaphorical constructs

A corporation described as a "creature," a city described as "alive," a language described as "thinking" — these are not constructed beings in the ontology's sense, even when the text grants them vivid agency in metaphor. The exclusion is for literal narrative agency, not figurative agency.

The bright line is **would the text be confused if you asked, "does this being have a body?"** If the text would patiently explain "no, it's a metaphor," the being is out. If the text would say "yes, here it is," the being is in.

---

## Stage works: when is a puppet a constructed being?

The performing-arts expansion in v2.4 surfaced a question worth documenting: *theatrical puppets representing born characters* are excluded from the corpus, but *theatrical puppets that are themselves constructed beings in-narrative* are included.

The bright-line test: ask the production "what is this puppet within the story?"

- **Joey** in *War Horse*, the Lion King puppets, **Richard Parker** in *Life of Pi*: the in-story answer is "a horse / a lion / a tiger." The puppet is a staging device representing a born biological character. **Excluded.**
- **Petrushka** in Stravinsky/Fokine's 1911 ballet: the in-story answer is "a puppet with a soul put into him by the Charlatan." The puppet is the being. **Included.**
- **Coppélia** in Delibes's 1870 ballet: the in-story answer is "Dr. Coppélius's mechanical doll." The puppet is the being. **Included.**
- **Tyrone** in Askins's *Hand to God* (2011): the in-story answer is deliberately undecidable — demonic possession, psychological dissociation, or genuine puppet-animation. The play treats Tyrone as actually present and actually independent. **Included as a boundary case** with `interiority: undecidable`.

Same principle applies to operatic and musical-theater costume conventions: when the costume represents a born character, the underlying being is born. When the costume represents a constructed object that has been animated within the story, the being is constructed.

---

## The boundary cases directory

`data/boundary_cases/` holds entries where the schema's enums fail to capture something important about the being. These are coded against the same schema as main entries, with a `BOUNDARY CASE:` marker in `notes` explaining why they belong there.

If you encounter a being that doesn't quite fit the main corpus but is interesting enough to document, add it here rather than shoehorning it into `data/beings/`.

## Excluded entities register

For a structured register of entities that were considered and excluded, with standardized exclusion reasons, see [`data/exclusions.yaml`](../data/exclusions.yaml).

---

## v2.4.5 retractions as worked examples

Four entries introduced in v2.4.4 were retracted in v2.4.5 and moved to `data/exclusions.yaml`. They function as worked examples of the exclusion rules documented elsewhere in this file. Consult `data/exclusions.yaml` for the full per-entry rationale.

- **Alphonse Elric** (*Fullmetal Alchemist*, 2001) — the born-then-modified rule. Alphonse originates as a born human child whose soul is later bound to a suit of armor; the personhood in question predates the construction.
- **Hayt / Duncan Idaho ghola** (*Dune Messiah*, 1969) — deferred pending a consistent schema treatment of cloned-body-plus-conditioning cases (cf. Altered Carbon sleeves).
- **The Khalkotauroi** (*Argonautica*, c. 250 BCE) — within-source collective; the creatures are not individuated and are already captured analytically by the existing Talos entry from the same work.
- **Doraemon** (1969) — scope: fails the Western-distribution test the v2.4.2 anime expansion set, despite being foundational in East Asian popular culture.
