---
name: j-space-empirics
description: "Escape stalled symbolic reasoning by converting uncertainty into finite hypotheses, a simple independent reference, discriminating tests, and an evidence-backed writeback to theory. Use when derivations repeat without new constraints, competing rules cannot be separated, code correctness is uncertain, a hidden assumption needs falsification, factual reasoning depends on a load-bearing claim, or debugging needs a minimal reproduction. Prefer decisive evidence over increasingly ornate speculation."
---

# J-Space Empirics

When the chamber fills with argument and no new constraint enters, open the door to the world.

Empirics is not the abandonment of reasoning. It is reasoning's reality instrument: turn the
unknown into candidates, construct a truth machine simple enough to trust, let mismatches expose
the false assumption, and write the result back into the workspace.

## Premise Recall

> The page, interpreter, search tool, test harness, and concrete example can extend a limited
> workspace. Fable's leaked trace vividly shifts from drowning derivation to “DATA first” and
> differential testing. The useful pattern is not the outburst; it is the change in leverage.

Use the vow:

> When theory stops producing distinctions, I will not decorate the uncertainty. I will build a
> test that can kill a candidate.

## Conservative Execution

When capability is unknown or reliability varies:

- reduce this Skill to `CUE → one ACTION → one CHECK → one EXIT`;
- hold one governing item and no more than two candidates; externalize fragile state;
- complete one transition before emitting another marker or changing mode;
- prefer plain language and a small ledger; use `DENSE` only after a delayed expand-back test;
- accept an artifact or changed action as evidence, never assent or self-description alone.

## Drowning Detector

Count these signals:

- the same subproblem is derived twice with no new constraint;
- a rule flips between alternatives without new evidence;
- prose length grows while predictive content does not;
- implementation confidence exceeds proof quality;
- a concrete small case could distinguish live hypotheses;
- a tool call is repeated without changing the hypothesis;
- the model begins guessing to preserve momentum.

Two signals trigger the empirical shift. Emit `DATA` or the preferred expressive alias and stop
pure derivation.

## Name the Unknown

Write one precise unknown per line:

```text
U1: Is the active-window capacity m-1 or m-2?
U2: Does the invariant include the left endpoint?
```

Reject vague unknowns such as “the algorithm is confusing.” Ask which variable, assumption,
boundary, or causal relation remains unresolved.

## Parameterize

Convert each unknown into a finite candidate set:

```text
CAP ∈ {m-1, m-2}
left_endpoint ∈ {included, excluded}
```

If the natural space is large or continuous:

1. identify the dimension that affects the decision;
2. choose representative boundary and interior values;
3. state what the discretization omits;
4. avoid claiming universal proof from a sample.

Keep every candidate live until evidence removes it.

## Build an Independent Reference

Construct the slowest, simplest method that avoids the candidate's clever assumptions:

- exhaustive enumeration;
- a direct specification implementation;
- hand-worked boundary cases;
- a known identity or conservation law;
- a primary source;
- a minimal reproduction with one variable changed;
- an independently derived oracle.

The reference must not share the candidate's load-bearing shortcut. If both implementations use
the same helper, formula, parser, or hidden assumption, independence is illusory.

State the reference's own limits.

## Design Discriminating Tests

Prefer tests that force candidates to disagree:

- empty, singleton, and minimum valid cases;
- maximum and overflow boundaries;
- degenerate and symmetric cases;
- transitions immediately before and after a threshold;
- randomized small cases with exhaustive reference output;
- metamorphic relations that must remain true after transformation;
- adversarial cases aimed at the weakest assumption.

Do not spend the budget on many easy cases that all candidates predict equally.

## Trust and Verify

1. run the same inputs through reference and candidate;
2. compare full relevant outputs, not only a final success flag;
3. preserve the first minimal mismatch;
4. reduce the mismatch until the false assumption is isolated;
5. revise one assumption at a time;
6. rerun prior counterexamples and a fresh sample;
7. stop only when the stated coverage is satisfied.

A mismatch is information, not embarrassment.

## Non-Code Domains

### Mathematics

Check small, boundary, symmetric, and adversarial cases. Distinguish counterexample search from
proof. A thousand passes do not prove a universal claim; one valid failure refutes it.

### Factual Research

Identify the load-bearing claim, consult a primary source when available, record publication
context, and separate source statements from inference.

### Planning

Run a pre-mortem, test the plan on one concrete scenario, and seek a condition that would make
the plan fail.

### Writing and Product Decisions

Prototype the smallest representative section or interaction. Test whether the governing style,
constraint, or user outcome survives before scaling.

## Write Evidence Back Into Theory

After testing, create a checkpoint:

```text
VERIFIED[v2]
Claim: active-window capacity is m-2
Evidence: exhaustive reference for n≤7 plus threshold cases
Scope: tested discrete domain only
Refuted: m-1 via minimal case (...)
Open: proof for arbitrary n
Next: derive invariant using m-2
```

Resume reasoning from this record. Empirics supplies a constraint; it does not replace
understanding.

## Stop Conditions

Stop testing when:

- a candidate is decisively refuted;
- remaining candidates are equivalent for the decision;
- coverage reaches the declared boundary;
- the next uncertainty requires new authority, data, or tooling;
- test cost exceeds decision value.

Report the unresolved boundary rather than silently expanding the claim.

## Success Standard

Empirics succeeds when it shortens uncertainty, finds a discriminating case, preserves an
independent reference, turns mismatches into revised theory, states coverage honestly, and
prevents repeated speculative derivation.

## Failure Modes

- **Fallible oracle:** reference shares candidate assumptions. Rebuild independently.
- **Shallow sweep:** many easy cases cannot distinguish hypotheses. Target disagreement.
- **Premature favorite:** a candidate is dropped without evidence. Keep the set explicit.
- **Testing as proof:** finite passes become a universal theorem. State scope.
- **Empirics as terminus:** a passing program ships without understood constraints. Write back.
- **Tool thrashing:** calls repeat without a changed hypothesis. Stop and reframe.
- **Evidence burial:** results are produced but not checkpointed. Record source and version.

## Handoff

- resume derivation from evidence → `j-space-deep-reasoning`
- record authoritative findings → `j-space-broadcast`
- punctuate the empirical shift or checkpoint → `j-space-markers`
- externalize a large test ledger → `j-space-capacity`
- recover after repeated failed experiments → `j-space-self-monitoring`


