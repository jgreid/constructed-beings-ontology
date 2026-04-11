# Boundary Cases — CBO v2.0

This document discusses entities that sit on or near the boundary of the constructed being (CB) definition. For each category, it explains the reasoning behind inclusion or exclusion and points to the criteria that decide.

The CB definition used by this ontology requires three things:

1. **Made, not born.** The entity's existence originates from a deliberate act of construction, programming, enchantment, or creation — not from biological reproduction.
2. **Agent-like.** The entity exhibits or is attributed behavior that implies agency: goal pursuit, language use, decision-making, or social interaction.
3. **Narrative presence.** The entity appears in a specific, citable text.

Everything discussed below either meets all three criteria (and is included), fails at least one (and is excluded), or poses a genuine definitional problem that the schema cannot cleanly resolve.

---

## What changed in v2.0

v1.0 had an explicit `reproductive_method` axis with values like `made`, `born-sexual`, `born-clonal`, `born-divine`, and `ambiguous`. That axis was doing a lot of work at the boundary — it let us include beings like Eve (Genesis) as `born-divine` specifically to make the inclusion/exclusion decision visible.

v2.0 has no such axis. A constructed being is defined by the three criteria above; the schema does not record a distinction between "made" and "born" because there is nothing else in the schema that depends on it. This simplifies most cases and makes a few cases harder. The ones that got harder are the ones this document covers.

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

The complication with both is that their "creators" are gods. The v1 `creator.name` field had to be a name; v2 has `metadata.creator` that can accommodate phrases like "Hesiod (Hephaestus in-narrative)." The ontology tracks the *authorial* creator and the *in-narrative* creator as a single string now, which removes some of v1's awkwardness at the mythic boundary.

---

## Excluded: divine creation of persons

v1.0 used to carry Eve (Genesis) as an explicit boundary case, coded with `reproductive_method: born-divine` to make the inclusion/exclusion decision durable. Under v2.0, Eve is **excluded** and there is no entry for her. Reasoning:

- **Divine creation of a full human person is categorically different from artisanal making.** God forming Eve from Adam's rib shares surface features with construction (a creator, raw material, a deliberate act). But Eve is immediately and fully human — she bears children, makes moral choices, converses with God. She is a person, not an artifact.
- **v2.0 removed the axis that let us record the boundary.** Without `reproductive_method`, there is no meaningful field to flag Eve's status on. Including her would require coding her as if she were a constructed being in the same sense as Pandora or Galatea, and that coding would be misleading.
- **The decision is still legible.** v2.0 preserves this discussion as documentation. Eve's deletion from `data/boundary_cases/` is recoverable from git history before the v2.0 migration.

The same reasoning applies to other divine creations of full persons (Adam, the angelic hosts). These are outside the ontology.

**What this means for Pandora and Galatea.** Both are arguably "divine creations of persons" in a weak sense. The difference is that both are explicitly framed as artifacts in their source texts — Pandora is a "gift" assembled from components, Galatea is a sculpted statue. They are made the way things are made, not the way people are made. Eve is made the way people are made, dressed up in making-language.

---

## Excluded: biological reproduction, including divine pregnancy

Beings whose origin is biological reproduction, however miraculous, are not constructed beings:

- **Divine conception** (e.g., the Christ of the Gospels, various hero myths) is still biological reproduction in a narrative sense. The mother is pregnant; the child is born.
- **Immaculate conception** (Catholic doctrine about Mary) is a theological claim about the absence of original sin, not about a manufacturing process.
- **Parthenogenesis and cloning** in fiction (e.g., certain comic-book origins) are biological reproduction variants. A clone born from a tank is still born.

The bright line is **manufacturing vs. gestation**. Clones manufactured without gestation (R.U.R.'s robots, replicants) are in. Clones grown in artificial wombs but gestated are arguably in; clones born from surrogates are arguably out. v2.0 does not attempt to adjudicate every edge case — it trusts the coder's judgment and asks for the reasoning to be documented in `notes`.

---

## Excluded: born-then-modified beings

Humans who receive cybernetic augmentation, brain implants, genetic enhancement, or software upgrades are not constructed beings. The Six Million Dollar Man, Molly Millions, most cyberpunk street samurai, the RoboCop protagonist (Alex Murphy) — all excluded, because their origin is biological birth. The modification, however extensive, does not convert them.

**The edge case:** when the modification is so total that the original biological identity is narratively treated as *replaced*. RoboCop is the canonical debate case. The 1987 film frames Murphy-as-Murphy as the surviving consciousness, which argues for exclusion. The 2014 film is more ambiguous. The ontology does not include RoboCop in either direction — it's a case where reasonable coders disagree about whether the modification reached the "replaced" threshold.

If you want to argue for inclusion, open an issue and propose a coding, including notes on which specific frame narratively establishes that the original identity has been replaced rather than extended.

---

## Excluded: collectives without individual identity

"The robots" as an undifferentiated mass are excluded. We code individual named or individuated entities. This is why:

- **R.U.R. Robots** get a single entry because the play treats them as a collective with emergent shared consciousness. Čapek is thinking about a class, not about individuals.
- **Cylons (reimagined BSG)** get a single entry anchored on Number Six / Caprica because those are the characters the show individuates. The base model diversity (Six, Eight, Cavil, D'Anna) could justify separate entries; the current coding is a unification that may be split later.
- **Westworld Hosts** get a single entry anchored on Dolores, even though Maeve would code significantly differently. This is a documented simplification.

The bright line is **does the text individuate this character**. If yes, it gets an entry. If the text treats the population as collective, the entry is for the collective and the notes acknowledge that individuals within the population may diverge from the card.

---

## Excluded: metaphorical constructs

A corporation described as a "creature," a city described as "alive," a language described as "thinking" — these are not constructed beings in the ontology's sense, even when the text grants them vivid agency in metaphor. The exclusion is for literal narrative agency, not figurative agency.

The bright line is **would the text be confused if you asked, "does this being have a body?"** If the text would patiently explain "no, it's a metaphor," the being is out. If the text would say "yes, here it is," the being is in.

---

## The v2.0 boundary directory

`data/boundary_cases/` is still a real directory. Under v2.0 it holds:

1. A `README.md` that defines "boundary case" for v2 (entries where the v2.0 schema's enums fail to capture something important about the being).
2. Future boundary-case entries, coded against the same v2.0 schema as main entries, with a `BOUNDARY CASE:` marker in `notes` explaining why they belong there.

As of the v2.0 migration the directory contains no entries — the v1 Eve entry was removed per the reasoning above. If you encounter a being that doesn't quite fit the main corpus but is interesting enough to document, add it here rather than shoehorning it into `data/beings/`.
