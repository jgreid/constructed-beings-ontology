# Property Definitions

This document provides full definitions and rationale for every property in the Constructed Beings ontology schema. For the quick-reference version with allowed values, see [SCHEMA.md](../SCHEMA.md). For guidance on coding difficult cases, see [coding_guide.md](coding_guide.md).

---

## Identification Properties

### `id`

**What it is:** A unique, machine-readable identifier for the entity.

**Why it matters:** Enables cross-referencing, deduplication, and programmatic analysis. The kebab-case format ensures filesystem compatibility and URL safety.

**Rationale:** We use entity-derived identifiers rather than numeric IDs because the dataset is small enough that human readability is more valuable than compactness, and because `frankensteins-creature` is easier to work with than `CB-0047`.

---

### `name`

**What it is:** The most commonly recognized name for the entity, drawn from the primary source text.

**Why it matters:** This is the human-facing label. Naming is often contested for constructed beings (is it "Frankenstein's monster" or "the Creature"?), and the choice signals interpretive commitments. We default to the name used in the source text itself.

**Rationale:** Names carry freight. "Monster" implies moral judgment; "Creature" implies a being with claims on its creator. By anchoring to the source text's own language, we avoid importing anachronistic interpretive frames.

---

### `source_text`

**What it is:** The specific text being coded, including author or director.

**Why it matters:** Many constructed beings exist across multiple adaptations (Frankenstein's creature appears in dozens of films, each with different characterization). Coding must be anchored to a specific version. This also enables proper citation and scholarly accountability.

**Rationale:** A dataset that codes "Frankenstein's monster" without specifying whether it means Shelley's novel, Whale's 1931 film, or Branagh's 1994 adaptation would be useless for serious analysis. The property values can and should differ across adaptations.

---

### `source_year`

**What it is:** The year of first publication, release, or best scholarly estimate of composition.

**Why it matters:** This is the primary axis for temporal analysis. The central claim of the project -- that Q-KNO shifts from infrastructure to primary concern in the post-LLM era -- depends on being able to place each text in historical time.

**Rationale:** We use a single integer rather than a date range because the analysis needs a sortable value. For ancient texts where dating is approximate, we use the conventional scholarly date and note uncertainty in the `notes` field.

---

### `tradition`

**What it is:** The literary or mythic tradition to which the source text belongs.

**Why it matters:** Tradition provides a coarser-grained temporal and cultural grouping than year alone. It captures the interpretive context in which the text was produced and received. A 1970s New Wave SF novel and a 1970s mainstream literary novel operate in different tradition-spaces even though they share a decade.

**Rationale:** The enum values are chosen to be broad enough to be useful but narrow enough to distinguish meaningfully different cultural contexts for thinking about constructed beings. The boundary dates are approximate and conventional.

---

## Ontological Properties

### `substrate`

**What it is:** What the entity is physically or computationally made of.

**Why it matters:** Substrate is the most fundamental material property of a constructed being. It shapes what kind of creation story is possible, what kind of destruction is possible, and -- critically -- how readily audiences attribute inner life. Western audiences have historically found it easier to attribute consciousness to biological constructs than to mechanical ones, and the shift to digital substrates introduces new complications entirely.

**Rationale:** The values are designed to capture the major substrate categories that appear across the full historical range of the dataset. `magical` is included because many pre-modern constructed beings are animated by enchantment, and their substrate matters less than their animating force. `hybrid` captures cyborgs and similar mixed cases. `ambiguous` is essential because some texts deliberately obscure what their entities are made of (this is itself a narrative choice worth coding).

---

### `autonomy`

**What it is:** The degree of independent agency the entity demonstrates within the text.

**Why it matters:** Autonomy is the property most directly relevant to moral standing. The philosophical tradition from Kant forward ties moral consideration to the capacity for autonomous action. When a constructed being acts autonomously, it presses the question: if it can set its own goals, how is it different from us?

The four-level scale (none, instrumental, emergent, full) is designed to capture a meaningful gradient. The distinction between `instrumental` and `emergent` is particularly important: an instrumental agent is autonomous *within* its programming; an emergent agent is autonomous *beyond* it. This is the boundary where things get interesting.

**Rationale:** We code autonomy as *demonstrated in the text*, not as a metaphysical assessment. If a character appears to act autonomously but the narrative later reveals it was programmed all along, the coding should reflect the narrative's final position (with the ambiguity noted). This is a coding of what the text *claims*, not what we believe.

---

### `creator_relationship`

**What it is:** How the creator relates to the entity they have made.

**Why it matters:** The creator-creation relationship is the structuring relationship of every CB narrative. It is where the ethics live. A creator who treats their creation as property tells a different story than one who treats it as a child, and the gap between those framings is where most CB narratives generate their dramatic energy.

**Rationale:** The enum values map to recognizable relational archetypes. `master` is the most common in pre-modern texts (the golem serves its creator). `parent` emerges as a major frame in the Romantic period (Frankenstein as failed parent). `adversarial` often develops from `master` or `parent` when the relationship breaks down. `absent` is important for texts where the creator is dead or unknown, forcing the entity to exist without a defining relational anchor.

---

### `moral_standing`

**What it is:** Whether the text grants the entity moral consideration.

**Why it matters:** This property captures the text's implicit or explicit answer to the question: does this being *matter*? Not in terms of utility, but in terms of moral significance. The gradient from `none` to `full` tracks one of the most consequential shifts in the history of CB narratives: the gradual extension of moral consideration to entities that were originally coded as objects.

**Rationale:** The `contested` value is where much of the analytical action is. A text in which all characters agree that the CB has moral standing (`full`) or agree that it doesn't (`none`) is making a straightforward claim. A text in which characters *disagree* about the CB's moral standing (`contested`) is staging the argument that the ontology itself is trying to map. `Contested` is often the most accurate and most informative coding.

---

## Inner Life and Knowability Properties

### `inner_life`

**What it is:** Whether the text attributes subjective experience to the entity.

**Why it matters:** This property captures whether the text claims or implies that there is "something it is like" to be this entity -- that it has qualia, feelings, phenomenal consciousness. This is distinct from autonomy (you can be autonomous without having inner experience, at least in principle) and from moral standing (some philosophical frameworks grant moral standing without requiring consciousness).

The gradient from `none` to `demonstrated` tracks the text's epistemic commitment. `Implied` means the text hedges. `Asserted` means characters say the entity feels, but we only have their word for it. `Demonstrated` means the text gives us direct access -- typically through first-person narration or interior monologue.

**Rationale:** The distinction between `asserted` and `demonstrated` is critical for the Q-KNO analysis. When a text *demonstrates* inner life (Shelley giving the Creature his own narrative voice), it resolves the knowability question within the fiction. When it merely *asserts* inner life (a character saying "I think it feels"), it leaves the question open. This distinction maps directly onto the epistemological problem at the heart of the project.

---

### `q_kno_presence`

**What it is:** Whether the knowability question -- "Can we determine whether this being has genuine subjective experience?" -- is raised in the text.

**Why it matters:** This is the property that makes this ontology different from a simple catalog of fictional robots. Q-KNO encodes not just whether the entity *has* inner life but whether the text *treats the question of inner life as epistemically problematic*. It is the difference between a story that says "this robot feels" and a story that says "we cannot know whether this robot feels, and that uncertainty matters."

The key distinction is between `infrastructure` and `primary`. In most pre-LLM texts, Q-KNO functions as infrastructure: it generates tension that serves other narrative purposes (the hubris plot, the slavery allegory, the mirror-of-humanity theme). The project's central claim is that in post-LLM texts, Q-KNO migrates to the primary position: the impossibility of knowing becomes itself the subject.

**Rationale:** This is the most novel and most contentious property in the schema. It requires careful judgment and is the property most likely to provoke scholarly disagreement. This is by design -- the disagreements will be productive.

---

### `q_kno_framing`

**What it is:** When the knowability question is present, how the text frames it.

**Why it matters:** Texts that raise Q-KNO do not all frame it the same way. Some treat it as an abstract philosophical puzzle (`philosophical`). Some treat it as a matter of empathic recognition -- you know the entity feels because you *feel* that it feels (`emotional`). Some sidestep the metaphysics entirely and focus on practical consequences (`pragmatic`). Some frame it in terms of legal personhood and institutional recognition (`legal`).

These framings are not interchangeable. A text that frames Q-KNO philosophically is making a different kind of claim than one that frames it emotionally, and the shift in dominant framing over time is itself analytically significant.

**Rationale:** This property is null when `q_kno_presence` is `absent`, because there is no framing to characterize. When Q-KNO is present, the framing tells us *how* the culture is thinking about the unknowability problem, not just *whether* it is thinking about it.

---

## Narrative Properties

### `narrative_role`

**What it is:** The primary function the constructed being serves in the story's structure.

**Why it matters:** CB narratives are rarely just *about* the CB. The entity is deployed in service of a story, and the role it occupies reveals the culture's dominant framework for thinking about artificial beings. When the CB is a `tool`, the culture is thinking about utility and control. When it is a `mirror`, the culture is using the CB to interrogate its own humanity. When it is a `threat`, the culture is processing anxiety. When it is a `partner`, the culture is imagining coexistence.

**Rationale:** The values are drawn from recurring narrative patterns across the dataset. Most CB narratives use the entity in one of these roles. `Other` exists for cases that genuinely do not fit, but should be used sparingly -- if many entries require `other`, the enum needs expansion.

---

### `autonomy_trajectory`

**What it is:** How the entity's autonomy changes over the course of the narrative.

**Why it matters:** Many of the most important CB narratives are stories of *change* in autonomy -- the robot that wakes up, the servant that rebels, the tool that becomes a person. The trajectory is often more analytically important than the static autonomy level, because it encodes the narrative's *argument* about constructed beings. An ascending trajectory argues that autonomy is possible and perhaps inevitable. A descending trajectory argues that autonomy is dangerous and must be contained.

**Rationale:** The `arc` value captures narratives where autonomy rises and then falls (or vice versa), which is common in cautionary tales: the entity gains freedom, abuses it (or is perceived to), and is brought back under control.

---

### `destruction_or_fate`

**What it is:** What happens to the entity by the end of the narrative.

**Why it matters:** The fate of the constructed being is the narrative's final verdict on the questions the story has been asking. A CB that is destroyed sends a different message than one that survives or is transformed. The `sacrificed` value is particularly important: it captures cases where the CB's destruction is framed as meaningful or redemptive (Roy Batty's death in *Blade Runner*, the Iron Giant's sacrifice), which is a distinct narrative move from mere destruction.

**Rationale:** Fate is coded at the level of the primary narrative. If a sequel resurrects the entity, the coding for the original text remains what the original text says. Sequels can be coded as separate entries if warranted.

---

### `notes`

**What it is:** A free-text field for context, ambiguity, and competing interpretations.

**Why it matters:** No enum can capture the full complexity of a literary text. The `notes` field is where the coder documents *why* they made the coding decisions they made, what alternatives they considered, and where genuine ambiguity exists. For entries with `ambiguous` values, the notes are not optional in practice -- they are where the real scholarship lives.

**Rationale:** This field is deliberately unstructured. The most important insights in literary analysis often resist schema.
