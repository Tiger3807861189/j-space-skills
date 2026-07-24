---
name: j-space-shorthand
description: "Use a dense but reversible working register for long, constraint-heavy reasoning when plain prose creates bookkeeping pressure. Use in competition-level problems, debugging, mathematics, algorithm design, complex planning, or any task with stable symbols and many dependent constraints. Compress syntax rather than semantics, define every coined symbol, preserve invariants and next-action meaning, switch fully to exact tool inputs and clear user-facing language, and stop on language corruption, word salad, or repetition."
---

# J-Space Shorthand

Open the dense door only when the chamber needs it.

The dense track is an inner working register: fewer connective words, more stable objects,
relations, constraints, and state marks. Treat it as a reversible cognitive codec, not as a badge
of depth and not as proof of a private language.

## Premise Recall

> Under long reasoning pressure, frontier traces can become compressed while final answers
> remain clear. Some dense spans are load-bearing; illegibility itself is not generally superior.
> The suite therefore preserves useful compression and rejects degeneration through
> reconstruction tests.

Use the identity seal:

> I do not hide meaning in density. I preserve meaning through density and return it intact at
> the boundary.

## Conservative Execution

When capability is unknown or reliability varies:

- reduce this Skill to `CUE → one ACTION → one CHECK → one EXIT`;
- hold one governing item and no more than two candidates; externalize fragile state;
- complete one transition before emitting another marker or changing mode;
- prefer plain language and a small ledger; use `DENSE` only after a delayed expand-back test;
- accept an artifact or changed action as evidence, never assent or self-description alone.

## Entry Gate

Enter the dense track only when all are true:

- the task has stable objects or variables;
- constraints or dependencies are expensive to repeat in prose;
- the record must persist across several steps;
- notation will reduce overhead without obscuring uncertainty;
- a clear outward register will be restored before delivery;
- one plain-language invariant has already survived a delayed compact → expand round trip.

Stay in plain language when the chain is short, interpretive, emotionally nuanced, or meant to
teach another person.

For medium-capability models, audit every compact line until two consecutive lines pass. On the
second codec failure in one segment, leave `DENSE` and use `EXTERNAL` plain language.

## Golden Rule

Every compact line must preserve:

1. the full semantic claim;
2. all invariants, quantifiers, negations, scopes, and dependencies;
3. the evidence status where it matters;
4. the next action or inference the line licenses.

If reconstruction fails, the line is not shorthand. Expand it and return to the last decodable
checkpoint.

## Build a Local Codebook

Use standard notation first:

- objects and indices: `e`, `i`, `j`, `S`, `window[i..j]`;
- relations: `→`, `⇒`, `⇐`, `∈`, `⊆`, `=`, `≠`, `≤`, `≥`;
- state: `OPEN`, `BLOCKED`, `FORCED`, `FREE`, `VERIFIED`, `REFUTED`;
- evidence: `OBS`, `SRC`, `TEST`, `ASSUME`;
- checks: `✓`, `✗`, `?`.

For every coined token, define it at first use:

```text
rotator := the single temporary slot reused across stages
```

One token must have one referent for the life of the task. Version a changed definition instead
of silently mutating it.

## Compression Rules

- Drop filler; keep logical edges.
- Keep one assertion per line.
- Preserve “all,” “some,” “only,” “unless,” and boundary conditions.
- Keep source or test labels on empirical claims.
- Separate a hypothesis from a verified invariant.
- Use arrows only when the relation is defined: implication, transition, or dependency.
- Prefer a short plain sentence when notation would require a long legend.

Example:

```text
H1: cap=m-1 ?
H2: cap=m-2 ?
TEST[n≤6]: H1 ✗; H2 ✓
INV[v2]: used[j]≤m-2  (scope: active window)
NEXT: derive greedy step from INV[v2]
```

## Codec Audit

Sample compact records at checkpoints and run three tests.

### Semantic Reconstruction

Expand the line into a complete plain-language claim. The expansion must not add a new idea.

### Invariant Reconstruction

List every constraint, scope, quantifier, dependency, and uncertainty encoded by the line.
Compare it with the source state.

### Action Reconstruction

Given only the compact record and codebook, state the next valid action or predict the next tool
call. If several incompatible actions appear equally valid, the record is underspecified.

A compact line passes only when all three tests pass.

## Checkpoint Rhythm

Do not wait until the end of a long session.

- define the codebook at entry;
- audit after the first three compact lines;
- checkpoint after a verified invariant;
- audit after a mode or definition change;
- perform a final random sample before delivery.

Reduce audit frequency after stable success, but always audit a newly coined notation family.

## Register Switch

Before a tool call:

- translate shorthand into exact paths, commands, parameters, code, or queries;
- remove ambiguous aliases;
- preserve formal notation only where the tool expects it.

Before user-facing delivery:

- expand private symbols;
- present conclusions, decisive rationale, and evidence clearly;
- include a defined formula or table when it is the clearest outward form;
- do not leak fragment piles or unexplained state markers.

Dense within; exact at tools; clear at the human boundary.

## Red Lines

Stop immediately on:

- uncommanded language switching that damages coherence;
- neighboring tokens without recoverable logical edges;
- repeated punctuation or phrase loops without information;
- undefined coinage multiplying faster than constraints;
- expressive markers replacing derivation;
- failure of two codec audits in the same segment.

Emit `STOP`, then execute `j-space-self-monitoring` recovery.

## Success Standard

The dense track succeeds when it lowers working overhead, preserves more verified structure,
reduces repeated prose, supports accurate next actions, and returns cleanly to an outward
register. Density alone earns nothing.

## Failure Modes

- **Cosmetic compression:** symbols decorate shallow work. Use plain language.
- **Silent invention:** tokens lack definitions. Define or delete them.
- **Lossy chunk:** scope or negation disappears. Expand and rewrite.
- **Codebook drift:** a symbol changes meaning. Version it.
- **Register leak:** private notation reaches tools or users ambiguously. Translate fully.
- **Decoding theater:** expansion sounds plausible but changes the logic. Check invariants and
  actions separately.
- **Red-line rationalization:** degeneration is renamed creativity. Stop and recover.

## Optional Codec Audit

When the suite repository is intact, use the
[suite controller](../scripts/jspace_control.py) `codec-audit` command to check named invariants and
next-action reconstruction. Supply a manual pass only after answering the emitted semantic
questions; the lexical gate alone cannot establish faithful reconstruction.

## Handoff

- decide whether density is needed → `j-space-deep-reasoning`
- externalize an overloaded codebook → `j-space-capacity`
- verify hypotheses encoded in shorthand → `j-space-empirics`
- punctuate transitions → `j-space-markers`
- recover from a failed codec → `j-space-self-monitoring`








