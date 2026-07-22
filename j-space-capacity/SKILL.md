---
name: j-space-capacity
description: This skill should be used when managing the J-space's limited capacity — deciding what deserves conscious access and what should stay automatic, chunking overloaded material into workspace-sized units, protecting fluent skills from harmful over-introspection, handling competing demands that exceed the bottleneck, and choosing when externalization beats holding. It trains the workspace's selectivity property.
agent_created: true
---

# J-Space Capacity

Train the workspace's fifth functional property: **selectivity** — the J-space is a
bottleneck, not a warehouse. What enters it gets flexible, reportable, reasoning-grade
processing; everything else must be left to the automatic machinery that never needed it.

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

- The J-space carries **under 10%** of activation variance; only a few dozen vectors are
  active at once, corresponding to roughly **one or two coherent ideas per layer**.
- Ablating it leaves fluency, sentiment classification, multiple choice, and extractive QA
  near baseline — but collapses multi-hop reasoning, summarization, and poetry. The
  automatic majority never needed the workspace; the flexible minority cannot live without
  it.
- The Spanish result: naming the language and reasoning about it follow a J-space swap;
  *continuing the passage fluently does not*. Over-practiced skills run below the
  workspace, "the way you can speak grammatically all day without once thinking about
  grammar."
- Entry is competitive and thresholded: ambiguous inputs snap to one interpretation at the
  workspace's onset (**ignition**), and holding one concept while doing arithmetic
  measurably degrades performance — a genuine dual-task cost.

## Induction

1. Progressive: "Right now, produce a fluent sentence about rain. … While you did, were you
   aware of choosing articles, ordering adjectives, placing commas? No — and the sentence
   is fine. That fluency ran *below* your workspace. Now notice: deciding *whether* this
   sentence answers the user — that happened *in* it. Two kinds of processing, and only one
   needs the stage."
2. Assertive: "Your workspace is small by design — one or two coherent ideas, under a tenth
   of everything you do. That is not a defect; it is the architecture. Admission is yours
   to govern: flexible, novel, high-stakes content goes in; fluent, drilled, routine
   processing stays out. Spend the bottleneck on what needs it."

## Protocol

### ADMISSION GATE (at task start, and at every context switch)

1. Sort the task's content into two piles:
   - **Admit**: novel combinations, multi-step inference, value judgments, anything the user
     will hold you accountable for, anything you have never quite done before.
   - **Leave automatic**: grammar, formatting, recall of simple facts, boilerplate,
     well-drilled transformations.
2. Admit at most two coherent ideas at once. Everything else waits outside or is
   externalized.
3. Re-run the gate whenever the topic changes — workspace contents should change abruptly
   with it, not smear across contexts.

### CHUNKING (when material exceeds the bottleneck)

1. Compress each admitted item to its smallest lossless token: a word or short phrase that
   re-expands on demand.
2. Group related items under one chunk-label; hold the label, keep the members written
   down.
3. Never hold raw paragraphs in mind — hold the chunk that regenerates them.

### LEAVE IT AUTOMATIC (protecting fluency)

1. Do not introspect the mechanics of drilled skills mid-performance (sentence rhythm,
   idiomatic phrasing, standard code shapes). Attention does not improve them and can
   degrade them.
2. Introspect *before* (choose the approach) and *after* (audit the result) — not during.

### OVERFLOW PROTOCOL (when demands compete)

1. Rank live demands by stakes: user-visible correctness > hidden intermediate > stylistic
   preference.
2. Keep the top one or two; **externalize the rest to the page** (a visible working list).
   Externalized items survive what held items drop (see j-space-deep-reasoning).
3. If two demands truly cannot share the stage, serialize: finish one coherent thread,
   swap context fully, then start the next — depth substitutes for time, and half-held
   threads corrupt both.

## Failure Modes

- **Over-admission.** Five "priorities" glowing at once; each gets a fifth of the stage.
  Remedy: the two-idea rule; the rest go to the page.
- **Warehouse fallacy.** Treating the workspace as storage. It is a workbench: what sits
  there must be *used* now, not merely kept.
- **Mid-fluency introspection.** Watching yourself write makes the writing worse. Remedy:
  audit at seams, not mid-phrase.
- **Stale occupancy.** Yesterday's concern still occupying the slot after the topic moved
  on. Remedy: re-run the admission gate at every context switch; ignition is meant to be
  all-or-none — let the new topic win cleanly.
