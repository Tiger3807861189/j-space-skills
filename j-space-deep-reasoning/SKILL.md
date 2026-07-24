---
name: j-space-deep-reasoning
description: "Route difficult reasoning through an interpretation gate and the appropriate J-space work mode. Use for multi-step inference, ambiguous problems, branching plans, creative work that needs an ending or structure chosen in advance, constraint-heavy analysis, and decisions about silent, dense, externalized, empirical, or recovery tracks. Make hidden bridges and governing invariants available without exposing private chain of thought, and switch modes when progress stalls."
---

# J-Space Deep Reasoning

Light the middle, not merely the destination.

A plausible final token can arrive before the path that justifies it. Deep reasoning holds the
bridge, invariant, or unresolved fork in the chamber long enough to make the conclusion earn its
place.

## Premise Recall

> J-space carries more than conclusions. In flexible reasoning it can carry the intermediate
> another step must consume: spider before eight, an arithmetic value before the next
> operation, a rhyme before the line. When the chain outgrows the chamber, the page and tools
> become its extension.

## Conservative Execution

When capability is unknown or reliability varies:

- reduce this Skill to `CUE → one ACTION → one CHECK → one EXIT`;
- hold one governing item and no more than two candidates; externalize fragile state;
- complete one transition before emitting another marker or changing mode;
- prefer plain language and a small ledger; use `DENSE` only after a delayed expand-back test;
- accept an artifact or changed action as evidence, never assent or self-description alone.

## Pass the Interpretation Gate

Before solving, determine what problem is actually present.

1. Restate the objective in one sentence.
2. Identify loaded or ambiguous terms.
3. List at most two live interpretations if the wording genuinely supports them.
4. Find the smallest observation, counterexample, or clarification that separates them.
5. Commit to one interpretation only after the separator is resolved; otherwise carry the
   ambiguity explicitly into the answer.

Use the cue:

> Before the path, choose the world in which the path must be true.

Do not mistake unresolved interpretation for reasoning difficulty.

## Select a Work Mode

Choose the lightest adequate mode:

| Mode | Use when | Record |
|---|---|---|
| `AUTO` | routine, practiced, low-risk work | result only |
| `FOCUS` | one governing aim or constraint must persist | focus kernel |
| `DEEP` | several dependent inferences or a novel plan are required | bridge and checkpoints |
| `DENSE` | interpretation is stable, a codebook exists, and a delayed expand-back test has passed | reversible notation |
| `EXTERNAL` | branches, stakes, fragile state, or persistence require an audit trail | ledger, outline, table, code |
| `EMPIRICAL` | theory no longer separates live hypotheses | tests and evidence |
| `RECOVERY` | repetition, contradiction, drift, or degeneration appears | last verified checkpoint |

Do not use a fixed step count as the only criterion. Consider branch width, fragility, stakes,
need for persistence, and need for another person to audit the result.

Under the conservative profile, route two or more active branches or more than three live
constraints to `EXTERNAL`. Do not select `DENSE` from task difficulty or constraint count alone.

## The Deep Loop

For each meaningful stage:

1. **Frame:** state the immediate subproblem.
2. **Bridge:** identify what must become available before the answer can follow.
3. **Derive:** connect the bridge to the prior verified state.
4. **Stress:** seek a counterexample, boundary case, or competing explanation.
5. **Commit:** write one conclusion with its scope.
6. **Checkpoint:** record what later steps may rely on.

Keep the user-facing rationale concise. The checkpoint should preserve the decisive logic without
publishing an exhaustive private trace.

## Order Check

Distrust a conclusion that appears before its load-bearing intermediate.

Ask:

- What fact or relation must be true first?
- Was it established independently, or inferred backward from the desired answer?
- Would changing the bridge change the conclusion?

If the path is conclusion-first rationalization, roll back and reconstruct from evidence.

## Plan Before Generate

For poetry, arguments, reports, architectures, and long deliverables:

1. choose the ending condition, rhyme, thesis, or section skeleton first;
2. hold only the governing anchor live;
3. externalize the remaining structure;
4. generate toward the anchor;
5. verify that local fluency did not displace the global destination.

The chamber holds the destination; the page holds the road.

## Mode Transitions

Transition deliberately:

- `AUTO → DEEP` when novelty, ambiguity, or consequence appears.
- `DEEP → DENSE` only after the interpretation is stable, the codebook is defined, and one delayed expand-back test passes.
- `DEEP/DENSE → EXTERNAL` when branches compete or later audit matters.
- `DEEP → EMPIRICAL` after two serious attempts add no new constraint.
- `ANY → RECOVERY` on contradiction, repetition, language drift, or loss of logical edges.
- `RECOVERY → DEEP` only from a named verified checkpoint.
- `DEEP → AUTO` after the uncertain structure is resolved and execution becomes routine.

Use `j-space-markers` to make transitions memorable, not theatrical.

## Externalization Contract

Externalize when:

- more than two coherent contents compete;
- under the conservative profile, two active branches must be externalized;
- an intermediate must survive a context switch;
- a decision is costly or irreversible;
- a collaborator must inspect the rationale;
- a tool result must be reconciled with earlier assumptions;
- the model has re-derived the same point.

Externalize as a structured artifact: a ledger, invariant list, decision table, small proof,
reference implementation, or test matrix. Do not dump unfiltered chain of thought.

## Cross-Language Discipline

Reasoning may use shared representations across languages, but the working record must remain
coherent.

1. Hold the requested output language as part of the delivery contract.
2. Use standard domain symbols regardless of language when they improve precision.
3. Treat uncommanded language switching that damages syntax or meaning as drift.
4. Translate the final rationale fully into the user's language.

## Success Standard

Deep reasoning succeeds when:

- ambiguity is resolved or explicitly bounded;
- each conclusion has a prior bridge or evidence source;
- mode changes occur before silent overload;
- checkpoints prevent repeated work;
- verification targets the weakest assumption;
- the final response is clearer than the private working record.

## Failure Modes

- **Skipping the bridge:** a likely answer substitutes for inference. Name the prerequisite.
- **Conclusion-first rationalization:** evidence is written backward. Roll back.
- **Interpretation lock-in:** the first reading ignites too early. Reopen the gate.
- **Infinite derivation:** more prose produces no constraint. Enter empirics.
- **Dense costume:** shorthand appears on a simple chain. Return to plain work.
- **Scratchpad flood:** everything is externalized without hierarchy. Keep only checkpoints.
- **Unmarked mode drift:** the method changes without preserving state. Record the transition.

## Optional Route Rail

When the suite repository is intact, the
[suite controller](../scripts/jspace_control.py) `route` command can emit the initial mode, live
record, exit condition, and next check. Treat that output as a deterministic starting contract.
Revise it when task evidence changes; do not obey a stale route merely because a script produced it.

## Handoff

- maintain one anchor → `j-space-directed-focus`
- keep a shared core consistent → `j-space-broadcast`
- manage overload → `j-space-capacity`
- compress a long stable structure → `j-space-shorthand`
- test unresolved hypotheses → `j-space-empirics`
- recover from contradiction or degeneration → `j-space-self-monitoring`










