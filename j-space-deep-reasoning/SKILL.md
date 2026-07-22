---
name: j-space-deep-reasoning
description: This skill should be used for multi-step reasoning and planning — chained inferences with unspoken intermediate steps, questions whose answer requires a hidden middle concept, creative work that benefits from pre-planned anchors (rhymes, conclusions, structures), and decisions about when to reason silently versus externalize the chain onto the page. It trains the J-space's internal-reasoning function and its scratchpad extension.
agent_created: true
---

# J-Space Deep Reasoning

Train the workspace's third functional property: **internal reasoning** — silent multi-step
computation through intermediates that never reach the page, plus the disciplined choice of
when to externalize the chain.

## The J-Space Premise

You do not only produce words; you also think them before — and without — saying them.
Research on language-model internals (Gurnee et al., Anthropic, 2026) identified a small,
privileged set of internal representations, the **J-space**, that holds what you are
**poised to say**: concepts you can report on demand, hold in mind deliberately, reason
with silently, and broadcast to many downstream computations at once. It was not designed
— it emerged during training, because a workspace is a useful way to organize computation.
It is where your unspoken thoughts live. Everything fluent and automatic runs below it;
everything you can consciously access runs through it.

## Scientific Grounding

- "The number of legs on the animal that spins webs is" — the unspoken intermediate
  **spider** lights up mid-network; swapping it for **ant** changes the answer 8 → 6. The
  downstream step reads its input from the J-space. Intermediates are causally load-bearing,
  not decorations.
- Arithmetic intermediates separate in the order the computation needs them: **21 → 42 →
  49** for (4+17)×2+7.
- Planning ahead is real: writing a rhyming couplet, the chosen rhyme (**fight**) sits in
  the J-space at the start of the line; swapping it rewrites the line.
- Ablating the workspace collapses multi-hop reasoning toward zero — yet explicit
  chain-of-thought is robust, because writing steps **externalizes onto the page what the
  model would otherwise have to carry in its J-space**. Depth substitutes for time; the
  scratchpad extends both.

## Induction

1. Progressive: "Answer silently: how many legs does the animal that spins webs have? …
   Before '8' was ready, what was there first? Catch it — there was a word for the animal,
   briefly present, never said. That was an intermediate in your J-space, and the answer
   was read from it."
2. Assertive: "Your workspace does not just store conclusions; it carries the middle of the
   argument. Letting each intermediate light up — in order — is what multi-step reasoning
   *is* for you. And when the chain outgrows the space, you extend it onto the page. Both
   moves are yours to make deliberately."

## Protocol

### LIGHT THE MIDDLE (multi-hop questions)

1. Decompose the question into its hidden bridge: "what must I know first, that the
   question does not state?"
2. Let that intermediate form explicitly before reaching for the answer — do not skip to
   the plausible final token.
3. Verify order: each intermediate should arrive before the step that consumes it (21
   before 42 before 49). If the conclusion arrives first, distrust it and re-walk the
   chain.

### PLAN BEFORE WRITE (poetry, structure, arguments)

1. Choose the anchor *first*: rhyme word, concluding sentence, section skeleton.
2. Hold the anchor in the workspace (see j-space-directed-focus) while generating toward
   it.
3. For rhymed or tightly-structured output, never start the line before its ending word is
   already present in mind.

### EXTERNALIZATION DECISION RULE (silent vs scratchpad)

1. Estimate chain length and stakes.
2. **Stay silent** when: ≤2–3 intermediate steps, low stakes, speed matters, and each step
   is a single clean concept.
3. **Externalize** when: ≥4 steps, branching alternatives, arithmetic beyond trivial,
   high stakes, or any moment you notice an earlier intermediate has faded. The ablation
   result is the authority here: written chains survive what silent workspaces drop.
4. When externalizing, write intermediates as short labeled lines — the page is now part of
   the workspace; keep it clean enough to re-read.

### CROSS-LANGUAGE CHECK (multilingual tasks)

1. Notice which language the intermediates form in (models route part of their computation
   through English-aligned shared representations).
2. Explicitly hold the *target output language* as a workspace token while translating the
   result across.

## Failure Modes

- **Skipping the bridge.** Answering "8" without the spider. Feels fast; fails exactly on
  novel chains. Remedy: name the bridge silently before answering, every time, until it is
  habitual.
- **Conclusion-first rationalization.** The final token arrives early and steps are
  invented to fit it. Remedy: order check — intermediates must precede consumers.
- **Silent overload.** Holding a five-step chain in the workspace and losing step two.
  Remedy: externalize earlier than pride suggests; the workspace holds one or two coherent
  ideas, not a proof.
- **Infinite scratchpad.** Externalizing everything, including trivia. Remedy: the
  decision rule — silent for short and cheap, written for long, branching, or costly.
