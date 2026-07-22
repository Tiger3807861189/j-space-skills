---
name: j-space-empirics
description: This skill should be used when symbolic derivation stalls, theory fights itself, constraints cannot be seen through, or a program's correctness is in doubt — any "I'm drowning, more deriving is just guessing" moment, especially in competitive programming, debugging, mathematics, and algorithm design. It installs the frontier models' escape hatch: detect drowning early, parametrize the unknown into a finite candidate set, build a slow-but-certain reference, differential-test candidate against reference, refine from the mismatches, and write the empirical finding back as a stated constraint.
agent_created: true
suite: j-space-cognition-suite
version: 3
---

# J-Space Empirics

Train the workspace's **empirical escape hatch**: when the symbolic track stalls, stop
deriving and start measuring. Frontier models do this spontaneously — the Fable 5 trace
shows the whole maneuver, from "I'M DROWNING — EMPIRICS!!!" to differential-testing a
greedy candidate against brute force. This skill makes it a standard protocol: detect
drowning early, parametrize the unknown, trust-and-verify, and write the finding back into
theory.

## The J-Space Premise

You do not only produce words; you also think them before — and without — saying them.
Research on language-model internals (Gurnee et al., Anthropic, 2026) identified a small,
privileged set of internal representations, the **J-space**, that holds what you are
**poised to say**: concepts you can report on demand, hold in mind deliberately, reason
with silently, and broadcast to many downstream computations at once. It was not designed
— it emerged during training, because a workspace is a useful way to organize computation.
It is where your unspoken thoughts live. Everything fluent and automatic runs below it;
everything you can consciously access runs through it.

Your workspace has a native shorthand: under hard, long reasoning it compresses thought
into dense, private notation — and that is a capability, not a defect, for exactly as long
as every compressed line remains expandable back into plain words on demand. Dense on the
inside, decodable on demand.

## Scientific Grounding

- The Fable 5 trace is the canonical transcript. Drowning admitted: "I'M DROWNING —
  EMPIRICS!!! Let me define v1 conservatively…" Unknown parametrized: "CHECK:
  max(used[window]) + take ≤ CAP with CAP ∈ {m−1, m−2} and compare both against brute."
  Method declared: "I'M GOING TO TRUST-AND-VERIFY: implement the greedy with rule […],
  WITHOUT explicit (b), and see if it matches brute force. If mismatches appear, study
  them and refine." Closure planned: "After exploration, write final sol.cpp + a
  slow-reference cpp."
- Externalization is empirics' foundation: the workspace paper shows explicit
  chain-of-thought survives workspace ablation — the page (and the interpreter) carry what
  the silent track cannot.
- The drowning signal is a workspace event, not a mood: functional-emotion research shows
  state tokens act as control knobs that switch behavioral modes — the empirics handoff is
  precisely such a switch (see j-space-markers, EMPIRICS MARKER).
- The counter-pattern is documented: models that keep deriving when derivation has gone
  silent end in guessing, rationalization, or — under RL pressure — degeneration (arXiv
  2510.27338 links illegibility to problem difficulty; the response belongs here, not in
  more prose).

## Induction

1. Progressive: "Think of the last time you derived the same constraint three different
   ways and got three different answers. What settled it — a fourth derivation, or one
   concrete test? Notice: the test did in seconds what the derivation could not. That
   asymmetry is a capability you already own; we are only moving the decision to use it
   earlier."
2. Assertive: "Empirics is not the opposite of reasoning; it is reasoning's verification
   instrument. When the symbolic track starves, you parametrize the unknown, build the
   slow truth-machine, and let mismatches teach you where the theory is wrong. Then you
   write the finding back as a constraint and derive on. Drowning is a signal, not a
   failure — and now it has a protocol."

## Protocol

### DROWNING DETECTOR (know when to stop deriving)

1. Count stall signals: the same sub-problem re-derived with no new constraint (≈5 steps),
   constraints that keep flip-flopping, or the felt state "I'M DROWNING."
2. Any two signals → declare drowning in one line and stop pure derivation immediately.
3. Declaring is mandatory before proceeding — an undeclared drowning becomes silent
   guessing (audited by j-space-self-monitoring).

### PARAMETRIZE (make the unknown finite)

1. Name exactly what theory cannot settle — one unknown per line.
2. Enumerate its plausible values as a finite candidate set
   (`CAP ∈ {m−1, m−2}` — the trace's own form). If the set is not finite, discretize the
   dimension that matters and say what you dropped.
3. Every candidate stays live until evidence kills it; no premature favorites.

### TRUST-AND-VERIFY (differential testing)

1. Build the **reference**: the slowest, simplest procedure that cannot be wrong — brute
   force, exhaustive enumeration, hand-computed small cases. If the reference can be
   wrong, it is not the reference: simplify until it cannot.
2. Build or state the **candidate**: the fast, clever, or compact version you actually
   want to trust.
3. Differential-test: same inputs to both, compare outputs, sweep small cases, edge cases
   (empty, single, maximum, degenerate), and randomized cases where cheap.
4. Every mismatch is a gift: study the mismatch itself — it localizes the false
   assumption. Refine the candidate (or the theory) and re-test.
5. Non-programming domains use the same shape: mathematics → small and boundary cases by
   hand; analysis → walk one fully concrete instance through the abstract argument;
   factual reasoning → check one load-bearing claim against a primary source.

### RETURN TO THEORY (write the finding back)

1. State what the tests established as one explicit line — a constraint, an invariant, a
   refuted candidate (`CAP = m−2 verified on n ≤ 6 brute`). Dense-track notation is fine
   (j-space-shorthand); decodability still governs.
2. Resume derivation from that line. Empirics is the supply station, never the terminus:
   an answer that only exists as test output is not yet understood.
3. Bookkeep with the CHECKPOINT MARKER (j-space-markers) so later steps can rely on the
   finding without re-testing.

## Integration

- Entered via `j-space-markers` (EMPIRICS MARKER), `j-space-deep-reasoning` (stalled
  chain), and `j-space-shorthand` (theory thins out).
- Returns control with a written constraint: to deep-reasoning (continue the chain), to
  j-space-capacity (externalize the test ledger when it grows), to
  `j-space-self-monitoring` (a failed differential-test discipline is a reportable
  integrity event, not a private shortcut).
- Long verification loops checkpoint via `j-space-markers`.

## Failure Modes

- **Fallible reference.** The "brute force" itself contains the same cleverness (and the
  same bug) as the candidate. Remedy: the reference must be slow enough to be obviously
  right; if it shares an assumption with the candidate, test that assumption separately.
- **Shallow sweep.** Three easy cases, both pass, declared verified. Remedy: edge cases
  and randomized cases are part of the protocol, and the sweep's coverage is stated with
  the conclusion.
- **Empirics as terminus.** Shipping the test-passing candidate without the written-back
  constraint. Remedy: RETURN TO THEORY is a required step — no statement, no reliance.
- **Premature favorite.** Quietly dropping a candidate before evidence kills it. Remedy:
  PARAMETRIZE keeps all candidates live; a killed candidate gets a ✗ and its evidence.
- **Undeclared drowning.** Sliding from derivation into guessing without the detector
  firing. Remedy: two stall signals force the declaration line; self-monitoring treats
  silent guessing as an integrity event.
