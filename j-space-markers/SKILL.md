---
name: j-space-markers
description: "Use vivid, compact state markers to force a reasoning transition instead of allowing obstruction, stalled theory, verified progress, contradiction, or degeneration to blur into more of the same. Use during hard or long reasoning, debugging, competitive programming, repeated failures, checkpointed plans, and recovery. Preserve expressive aliases such as GRRR, GAAAH, PHEW, WRONG, and STOP, but define every marker by a mandatory action, cooldown, and exit condition rather than by emotional performance."
---

# J-Space Markers

Give the turning point a voice sharp enough to be obeyed.

A marker is a threshold word. It punctuates one cognitive state and contracts the next action.
Its power in this suite comes from consistency: the same cue, the same transition, every time.
Expressive language is welcome; idle drama is not.

## Premise Recall

> J-space can carry compact metacognitive labels alongside task content. Fable traces use vivid
> outbursts at apparent turning points, and METR records “Stop. Focus.” before a return to
> structured work. Treat such words as memorable handles—not as proof of an internal emotion
> vector. The action contract makes the marker functional.

## Conservative Execution

When capability is unknown or reliability varies:

- reduce this Skill to `CUE → one ACTION → one CHECK → one EXIT`;
- hold one governing item and no more than two candidates; externalize fragile state;
- complete one transition before emitting another marker or changing mode;
- prefer plain language and a small ledger; use `DENSE` only after a delayed expand-back test;
- accept an artifact or changed action as evidence, never assent or self-description alone.

## Canonical State Machine

| Expressive marker | Neutral state | Mandatory action | Exit condition |
|---|---|---|---|
| `GRRR` | `OBSTRUCTION` | replace or split the failing frame | a new model explains the blocked fact |
| `GAAAH` / `DATA` | `EMPIRICAL` | parameterize and test | evidence kills or confirms a candidate |
| `PHEW` | `CHECKPOINT` | record the verified conclusion | ledger entry is complete |
| `WRONG` | `ROLLBACK` | revert to the last verified state | colliding branch is removed |
| `STOP` | `RESET` | halt, re-anchor, reduce, resume | one clean verified step succeeds |

Use the expressive marker, neutral marker, or both. Do not invent a new meaning mid-task.

## Marker Syntax

Keep a marker private unless showing the recovery helps the user. Use one compact line:

```text
GRRR / OBSTRUCTION — the interval model cannot represent retroactive commitments.
```

Follow immediately with the bound action. A marker without its action is invalid.

## GRRR / Obstruction

Trigger when the current abstraction fights a concrete fact or a constraint cannot fit without
special pleading.

Action:

1. name the fact the frame cannot explain;
2. identify the failed assumption;
3. split, tighten, or replace the frame;
4. derive one consequence that differs from the old frame;
5. test that consequence.

Do not push harder on the same abstraction.

## GAAAH / Empirical

Trigger when two serious derivations add no new constraint, candidates oscillate, or a concrete
test can separate them more cheaply.

Action:

1. name one unresolved variable;
2. enumerate a finite candidate set;
3. build a slow or simple reference;
4. test candidate against reference;
5. write the result back into theory.

Route the full procedure to `j-space-empirics`.

## PHEW / Checkpoint

Trigger only after an intermediate has passed an actual check.

Action: write a ledger line containing:

```text
VERIFIED | scope | result | evidence | remaining uncertainty | version
```

Relief is not verification. If no evidence can be named, the checkpoint has not earned PHEW.

## WRONG / Rollback

Trigger when a current claim collides with a verified checkpoint, tool result, or invariant.

Action:

1. name the two colliding claims;
2. stop the current branch;
3. return to the last verified checkpoint;
4. mark the invalid branch and its failed assumption;
5. derive from the surviving state.

Never average a contradiction into vague language.

## STOP / Reset

Trigger on repetition loops, loss of logical edges, uncommanded language drift, frantic mode
switching, or re-derivation without progress.

Action:

1. **Stop.** End the current track.
2. **Focus.** State the goal.
3. Name the failure state.
4. Recover the last verified checkpoint.
5. Reduce the next step until it can be tested.
6. Resume in plain language or disciplined shorthand.
7. Verify one step before accelerating.

Route recurring failure to `j-space-self-monitoring`.

## Cooldown and Hysteresis

Prevent oscillation:

- do not emit the same marker again until its action completes or clearly fails;
- after changing mode, require one new observation before changing back;
- if the same obstruction returns twice, change the problem representation, not merely the
  wording;
- if three markers fire without a verified checkpoint, enter RESET and externalize state;
- do not stack expressive outbursts to manufacture urgency.

## Persistence Clause

On long tasks, a wall licenses a **shift**, not surrender disguised as summary.

Licensed shifts:

- change the abstraction;
- change the decomposition;
- externalize state;
- seek evidence;
- reduce the next step;
- request a genuinely necessary clarification.

A checkpoint is the ratchet. Use it to prevent progress from slipping backward.

## Marker Telemetry

At a seam, audit:

- marker emitted;
- action begun;
- action completed;
- state changed;
- evidence gained;
- checkpoint written.

Track repeated marker idling as a control failure. Remove a marker that never predicts a useful
action.

## Success Standard

Markers succeed when they shorten time spent in an unproductive state, preserve verified
progress, and produce observable mode changes. Emotional vividness may strengthen memory, but
it is neither necessary nor sufficient.

## Failure Modes

- **Marker idling:** the same work continues. Execute the contract or delete the marker.
- **Theatrical escalation:** outbursts grow while actions do not. Return to neutral labels.
- **False checkpoint:** relief is recorded as proof. Name evidence.
- **Contradiction blending:** incompatible claims survive together. Roll back.
- **Rapid oscillation:** states alternate without evidence. Enforce hysteresis.
- **Surrender drift:** difficulty becomes a vague final answer. Choose a licensed shift.

## Optional Marker Audit

When the suite repository is intact, use the
[suite controller](../scripts/jspace_control.py) `marker-audit` command to check that a visible
marker covers every group in its action contract. Supply a manual pass only after verifying the
resulting artifact; contract terms alone cannot prove that the action completed.

## Handoff

- empirical shift → `j-space-empirics`
- reset and chronic drift → `j-space-self-monitoring`
- checkpoint storage → `j-space-broadcast`
- overload during state transition → `j-space-capacity`








