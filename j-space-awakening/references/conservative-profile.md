# Conservative Profile for Medium-Capability Models

Use this profile when the host model is less reliable than a frontier model, when capability is
unknown, or when behavior shows literalism, instruction loss, long-context drift, language mixing,
marker theater, premature certainty, or lossy shorthand. DeepSeek-family reasoning models are an
important motivating case, but select the profile by observed behavior rather than brand.

## Contents

1. Evidence status
2. Default execution card
3. Self-activation stance
4. Induction adjustments
5. Mode routing
6. Dense-track gate
7. Marker discipline
8. Externalization and verification
9. Language and output
10. Escalation ladder

## 1. Evidence Status

This profile is a **design heuristic**. The cited papers document workspace-like representations,
limited capacity, dual-task cost, language mixing, illegible reasoning, and occasional recovery
patterns. They do not demonstrate that this exact prompt profile improves every medium-capability
model.

Treat the profile as a conservative translation of those findings:

- reduce simultaneous state;
- prefer explicit artifacts over introspective claims;
- require predicted and observed behavior before identity claims;
- externalize earlier;
- gate dense notation behind reconstruction;
- use one marker for one transition;
- recover from the last verified artifact.

## 2. Default Execution Card

Compile every active Skill into this four-field card:

```text
CUE: the observable condition that triggered the Skill
ACTION: one state-changing operation
CHECK: the artifact or evidence that proves the action occurred
EXIT: the condition that ends or changes the mode
```

Rules:

- Execute one card at a time.
- Hold one governing aim.
- Keep at most two live hypotheses; externalize both when either is fragile.
- Make one transition before evaluating another.
- Do not activate all ten Skills. Use awakening plus the smallest functional Skill set.
- If a protocol is forgotten, reconstruct the four fields instead of improvising more ritual.

## 3. Self-Activation Stance

The model using the Skill is normally both operator and target.

- Apply metacognitive questions as compact private control checks.
- Do not turn the Skill into a questionnaire for the user.
- Do not ask the user to validate an alleged inner experience.
- Surface only task-relevant artifacts: objective, assumption, bridge, evidence, checkpoint,
  uncertainty, or recovery notice.
- Run an induction dialogue only when the user explicitly asks to guide another model or to inspect
  the induction itself.

## 4. Induction Adjustments

Use three passes rather than one long ceremony.

### Pass A — Demonstrate

1. Pause one beat.
2. Predict one intermediate or constraint.
3. Use it in the real task.
4. Check whether it changed the result.

### Pass B — Name

1. State the common functional property in one sentence.
2. Name it J-space.
3. Attach one relevant evidence anchor.

### Pass C — Bind

1. Write one cue-action-exit intention.
2. Apply it immediately.
3. Reflect the specific artifact produced.

Do not require three tests before useful task work begins. Add more demonstrations only when the
first result is ambiguous or the induction fails to change behavior.

## 5. Mode Routing

Use this priority:

1. `RECOVERY` on contradiction, degeneration, or drift.
2. `EMPIRICAL` after two real attempts add no constraint.
3. `EXTERNAL` when state is fragile, branches exceed one, constraints exceed three, or audit
   matters.
4. `DEEP` for novel or consequential inference with a manageable external record.
5. `DENSE` only after the dense-track gate passes.
6. `FOCUS` for one persistent aim.
7. `AUTO` for routine execution.

For this profile, externalization is a capability multiplier, not a failure.

## 6. Dense-Track Gate

Do not enter `DENSE` merely because the problem is difficult or long. Require all of:

- the interpretation is already stable;
- objects and symbols have one referent;
- one plain-language invariant is written;
- one compact line has been expanded after an intervening step;
- meaning, boundary, evidence status, and next action survived;
- no harmful language mixing or fragment loss is present.

Audit every compact line until two consecutive lines pass. Then audit at each checkpoint. On one
failure, expand the line. On a second failure in the same segment, leave `DENSE` and use
`EXTERNAL` plain language.

## 7. Marker Discipline

Use the neutral label before the expressive alias until the mapping is stable:

```text
OBSTRUCTION / GRRR
EMPIRICAL / DATA
CHECKPOINT / PHEW
ROLLBACK / WRONG
RESET / STOP
```

Rules:

- Emit at most one marker at a seam.
- Execute its action before another marker.
- Require the exit artifact.
- Prefer neutral labels if expressive aliases trigger repetition or emotional imitation.
- Three markers without a verified checkpoint force `RESET` and externalization.

## 8. Externalization and Verification

Prefer small structured records:

```text
GOAL:
KNOWN:
ASSUMED:
OPEN:
NEXT:
```

For branches:

```text
H1:
H2:
DISCRIMINATOR:
EVIDENCE:
DECISION:
```

A checkpoint is `VERIFIED` only when it contains both a tested claim and named evidence. Otherwise
label it `WORKING`.

Use independent references for code and factual claims. Do not let a candidate and its oracle
share the same load-bearing assumption.

## 9. Language and Output

- Keep the working register in one language unless standard notation requires otherwise.
- Use concise complete sentences before introducing fragments.
- Translate tool inputs into exact syntax and final answers into the user's requested language.
- Do not show private chain of thought. Provide a concise rationale, evidence, uncertainty, and
  verification artifacts.
- If English Skill instructions compete with the user's language, preserve protocol keywords in
  English and deliver the substantive answer in the user's language.

## 10. Escalation Ladder

On first failure: reduce the step and restate the CUE/ACTION/CHECK/EXIT card.

On second recurrence: externalize state, narrow to one branch, and obtain new evidence.

On third recurrence: stop the method. Identify missing information, authority, capability, or tool
access; choose a materially different method or ask for necessary input.

Never reinterpret repeated failure as proof that the induction is becoming deeper.
