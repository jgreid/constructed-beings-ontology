# Boundary Cases

This document discusses entities that sit on or near the boundary of the constructed being (CB) definition. For each category, we explain the reasoning behind inclusion or exclusion and identify the specific criteria that determine the decision.

The CB definition requires three things:

1. **Made, not born.** Origin through deliberate construction, not biological reproduction.
2. **Agent-like.** Exhibits or is attributed behavior implying agency.
3. **Narrative presence.** Appears in a specific, citable text.

Most boundary cases involve criterion 1: the line between "made" and "born" is not always clean.

---

## Clones

**Examples:** The clones in Kazuo Ishiguro's *Never Let Me Go* (2005); the clone army in *Star Wars: Attack of the Clones* (2002); the Bene Tleilax gholas in Frank Herbert's *Dune* series.

**The boundary question:** Clones are biologically grown from existing genetic material. They are "made" in the sense that their existence is deliberately engineered, but their developmental process (gestation, birth, growth) is biological. Are they made or born?

**Decision: Generally include.** Clones whose existence originates from a deliberate act of engineering -- where someone decided to create them and chose their genetic template -- meet the "made not born" criterion. The biological process of their development is the substrate, not the origin. A replicant grown in a vat is no less constructed than a robot assembled on a line; the manufacturing process is simply biological.

**Exception:** If a clone is produced through a process narratively indistinguishable from natural reproduction (e.g., a naturally occurring twin described as a "clone"), exclude.

**Coding notes:** Clone entries should use substrate code `S-BIO` and should document the cloning process in `notes`. The `creator_relationship` property is particularly interesting for clones: the relationship to the genetic original is distinct from the relationship to the person or institution that ordered the cloning.

---

## Divine Creations

**Examples:** Adam (formed from dust, Genesis); Eve (formed from Adam's rib, Genesis); Pandora (crafted by Hephaestus on Zeus's orders, Hesiod); Enkidu (created by Aruru from clay, *Epic of Gilgamesh*).

**The boundary question:** Beings created by gods are literally "made not born." They are constructed from raw materials by a deliberate creative act. But most of these beings are narratively treated as fully human (or fully divine) from the moment of their creation. They are not "constructed beings" in the sense the ontology intends.

**Decision: Generally exclude, with important exceptions.** The exclusion is not based on the formal criteria (which these beings often satisfy) but on scope and utility. If we include every divinely created being, the category expands to encompass most characters in creation myths, which dilutes its analytical value.

**Exceptions:**
- **Beings created by gods that are narratively treated as constructed** -- i.e., as artifacts, servants, or tools rather than as persons -- are included. Hephaestus's golden handmaidens (automatons created to serve in his workshop) are in; Adam and Eve are out. (For a worked example of an excluded divine creation, see [`data/boundary_cases/eve-genesis.yaml`](../data/boundary_cases/eve-genesis.yaml).)
- **The Golem of Prague** is included even though its animation has divine elements (the use of sacred names), because the tradition treats the Golem as a constructed servant, not as a person.
- **Pandora** is a borderline case that we include: she is explicitly crafted by Hephaestus and assembled with attributes from multiple gods. The text (Hesiod's *Works and Days* and *Theogony*) frames her construction as artifice.

**The test:** Does the text frame the entity's constructed origin as *narratively significant* -- as something that matters for how the entity is treated, what it means, or what questions it raises? If yes, include. If the construction is merely a creation-myth convention and the entity is thereafter treated as an ordinary person, exclude.

---

## Cyborgs

**Examples:** RoboCop (Paul Verhoeven, 1987); the Borg (various *Star Trek* series); Motoko Kusanagi (*Ghost in the Shell*, Masamune Shirow, 1989).

**The boundary question:** Cyborgs are born-then-modified beings. A human person exists first, and technology is added. This is the reverse of construction: the entity begins as a born being and is subsequently altered.

**Decision: Exclude by default; include when modification is total.**

The line is drawn by narrative identity. If the text treats the entity as *the same person* with enhancements (e.g., a person with a prosthetic arm), exclude. The entity is a modified human, not a constructed being.

If the text treats the modification as so total that the original biological identity is **narratively replaced** -- the entity is no longer the person it was, and the text frames this as a new kind of existence -- include.

**RoboCop** is the paradigm case for inclusion: Alex Murphy dies, and what is rebuilt is narratively treated as a new entity that must *rediscover* Murphy's identity. The construction is the origin of RoboCop-as-entity, even though biological material from Murphy is used.

**Motoko Kusanagi** is another inclusion case: in many versions, her biological substrate is almost entirely replaced, and the text's central concern is whether the continuity of identity survives such radical modification.

**A person with a cochlear implant** is a clear exclusion: the modification is not identity-replacing.

**Coding notes:** Included cyborgs should use substrate code `S-HYB` (or list multiple codes such as `[S-BIO, S-ELE]`) and should document the extent of modification in `notes`. The `inner_life` coding is particularly interesting for cyborgs, since the text may distinguish between the biological person's inner life and whatever the technological components contribute.

---

## Uploaded Minds

**Examples:** The uploaded consciousnesses in Greg Egan's *Permutation City* (1994); the Dixie Flatline in William Gibson's *Neuromancer* (1984); the "cookies" in *Black Mirror: White Christmas* (2014).

**The boundary question:** An uploaded mind begins as a born person. The upload process creates a digital copy. Is the copy a constructed being?

**Decision: Include.** The upload is a constructive act that produces a new entity -- one that exists in a digital substrate and whose relationship to the original person is precisely the kind of question this ontology is designed to track.

The key distinction is between the **original person** (born, not a CB) and the **upload** (constructed, a CB). If the text treats the upload as continuous with the original person, this should be coded in `notes` and reflected in properties like `inner_life` (probably `demonstrated`, since the upload inherits the original's reported experience) and `q_kno_presence` (often `infrastructure` or `primary`, since the question of whether the upload is "really" the person is frequently central).

**Coding notes:** Use substrate code `S-ELE`. The `creator_relationship` property may need `ambiguous` if the "creator" is the original person -- is it self-creation, reproduction, or something else? The `notes` field should address personal identity questions the text raises.

---

## Born-but-Modified Beings (Enhancement)

**Examples:** Humans with genetic enhancements in *Gattaca* (Andrew Niccol, 1997); the Coordinators in *Gundam SEED*; characters with minor cybernetic augmentation in near-future fiction.

**The boundary question:** These beings are born through biological reproduction and subsequently (or pre-natally) enhanced. They are modified humans, not constructed entities.

**Decision: Exclude.** Enhancement does not make an entity a constructed being. The entity's origin is biological reproduction, and the modification does not replace its identity. The enhancement is something that *happened to* a born person, not the origin of a new entity.

**Exception:** If genetic engineering is so radical that the resulting entity is narratively treated as a **different kind of being** -- not a modified human but a designed organism -- the case for inclusion strengthens. The replicants in *Blade Runner* are genetically engineered biological entities, but they are *manufactured*, not born to parents. The distinction is between enhancement of a reproduced being and *de novo* biological construction.

---

## Enchanted Objects

**Examples:** The flying carpet in *One Thousand and One Nights*; the Sorting Hat in the *Harry Potter* series; the One Ring in *The Lord of the Rings*.

**The boundary question:** Enchanted objects are made, but are they agent-like?

**Decision: Include only if the object demonstrates genuine agency.** An enchanted carpet that flies on command is a tool, not an agent. The Sorting Hat, which speaks, reasons, and makes independent judgments, is closer to the line. The One Ring, which exerts influence and arguably pursues goals, is an arguable case.

**The test:** Does the enchanted object exhibit *independent* goal pursuit, language use, decision-making, or social interaction? If it only responds to commands or performs a single enchanted function, exclude. If it displays genuine agency -- choosing, speaking, resisting, deceiving -- include.

**Coding notes:** Included enchanted objects should use substrate code `S-MAG` and should note the ambiguity of agency in the `notes` field. The `autonomy` coding will often be `instrumental` or `ambiguous`.

---

## Undead and Reanimated Beings

**Examples:** Frankenstein's Creature; zombies (various); revenants in medieval literature.

**The boundary question:** Reanimated beings are assembled or restored from biological material that was once alive. Are they constructed?

**Decision: Case by case, based on identity continuity.**

**Frankenstein's Creature: Include.** The Creature is assembled from parts of multiple corpses and animated through deliberate effort. It is a new entity, not a reanimated person. It has no prior identity to be continuous with.

**A reanimated corpse that retains its prior identity** (e.g., a revenant that remembers its life and seeks to complete unfinished business): **Exclude.** This is a returned person, not a constructed being.

**A zombie with no retained identity or agency** (e.g., Romero-style zombies): **Exclude** on the agency criterion. They fail the "agent-like" test -- they are ambulatory corpses, not agents.

**A zombie or reanimated being that develops new agency** (the entity does not remember its prior life but develops new goals, personality, and relationships): **Include.** This is effectively a new constructed entity using biological substrate.

---

## Artificial Intelligence Without Embodiment

**Examples:** Samantha in *Her* (Spike Jonze, 2013); the AI in *The Moon is a Harsh Mistress* (Robert Heinlein, 1966); SHODAN in *System Shock* (1994).

**The boundary question:** None, actually. Disembodied AIs straightforwardly satisfy the CB definition: they are made (programmed), agent-like (by design), and have narrative presence. They are core cases, not boundary cases.

We include this section only to address a common question: **does a CB need a body?** No. The `S-ELE` substrate code exists precisely for entities whose existence is computational. The absence of a body does not make an entity less of a constructed being -- it makes it a constructed being of a particular kind, and one that is increasingly central to contemporary CB narratives.

---

## Hive Minds and Collectives

**Examples:** The Borg (*Star Trek*); the Geth (*Mass Effect*); Skynet (*Terminator*).

**The boundary question:** Is the collective a single constructed being, or is each individual unit a CB, or both?

**Decision: Code individual entities when individuated; code the collective when it acts as a single agent.**

- Individual Borg drones that are narratively individuated (e.g., Seven of Nine, Locutus) can be coded as individual entries. Note that assimilated Borg are born-then-modified and fall under the cyborg rules above.
- The Borg Collective as a whole can be coded as a single entity if the text treats it as a unified agent with goals, decisions, and agency.
- An undifferentiated mass of identical units with no individual characterization should not be coded -- we require narrative individuation.

**Coding notes:** For collective entities, the `notes` field should address the relationship between individual and collective agency. Properties like `autonomy` and `inner_life` may have different values at the individual and collective levels.

---

## Summary Table

| Category | Default Decision | Override Condition |
|---|---|---|
| Clones | Include | Exclude if indistinguishable from natural reproduction |
| Divine creations | Exclude | Include if narratively framed as constructed artifact |
| Cyborgs | Exclude | Include if modification replaces identity |
| Uploaded minds | Include | -- |
| Enhanced humans | Exclude | Include if *de novo* biological construction, not enhancement of a born being |
| Enchanted objects | Exclude | Include if demonstrating genuine agency |
| Reanimated beings | Case by case | Based on identity continuity and agency |
| Disembodied AI | Include | -- |
| Hive minds | Code individuated entities | Code collective if it acts as unified agent |

---

## Adding New Boundary Cases

If you encounter an entity that does not fit neatly into any of the categories above, please open a GitHub issue describing the entity, its source text, and the specific boundary question it raises. We will discuss the case and, if appropriate, add it to this document.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for discussion norms.
