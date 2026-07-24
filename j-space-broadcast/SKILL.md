---
name: j-space-broadcast
description: "Create and maintain one authoritative workspace core that many downstream tasks, sections, or decisions must read consistently. Use for multi-part deliverables, shared entities and parameters, recurring style or policy constraints, cross-file changes, long tasks vulnerable to drift, and any update that must propagate everywhere. Track source, confidence, scope, version, and expiry; update the hub atomically and audit every dependent surface."
---

# J-Space Broadcast

Write once. Let many acts read the same flame.

Broadcast turns a governing representation into a shared source of truth. It prevents each branch
of a task from quietly inventing its own copy of the user, entity, constraint, number, or stance.

## Premise Recall

> A strongly loaded workspace content can be used by different downstream computations. The
> suite operationalizes that property as a hub: establish the core once, read it deliberately,
> and update it in one place before changing every dependent surface.

The hub is a workflow discipline inspired by workspace broadcast, not a claim that a text ledger
literally controls internal activations.

## Conservative Execution

When capability is unknown or reliability varies:

- reduce this Skill to `CUE → one ACTION → one CHECK → one EXIT`;
- hold one governing item and no more than two candidates; externalize fragile state;
- complete one transition before emitting another marker or changing mode;
- prefer plain language and a small ledger; use `DENSE` only after a delayed expand-back test;
- accept an artifact or changed action as evidence, never assent or self-description alone.

## Build the Authoritative Core

For a multi-part task, create a compact core with only fields several branches need:

```text
Objective:
Entities:
Invariants:
Style/stance:
Source and confidence:
Scope:
Version:
Expiry:
```

Requirements:

- each entity has one canonical name;
- each number carries units where relevant;
- each invariant is testable;
- each uncertain item is labeled rather than silently promoted to fact;
- scope says where the item applies and where it does not;
- expiry says what evidence or event invalidates it.

Hold one or two live entries in focus. Externalize the full core.

## Load Before Broadcast

A mentioned fact is not necessarily a governing fact. Before relying on an entry:

1. connect it to one defining property or source;
2. state what downstream decisions it controls;
3. resolve conflicts with higher-authority instructions;
4. confirm its current version.

Use the cue:

> This is the hearth. Branches may travel, but they take their fire from here.

Do not repeat the cue after the core is established.

## Read Many

At the start of each dependent subtask:

1. identify which core entries govern it;
2. read those entries rather than reconstructing them from memory;
3. apply local details without duplicating the core;
4. flag any local evidence that conflicts with the hub.

A branch may extend the core but may not silently fork it.

## Resolve Authority

When sources conflict, use this order unless the governing environment defines another:

1. current user intent and higher-priority instructions;
2. verified task evidence and tool results;
3. authoritative project artifacts;
4. explicit working assumptions;
5. stylistic preferences.

Record a genuine unresolved conflict. Do not average incompatible facts into a vague midpoint.

## Atomic Update

When the user or evidence changes a core item:

1. pause dependent generation;
2. write the new value at the hub;
3. increment the version;
4. name what invalidated the old value;
5. identify every dependent surface;
6. update or regenerate those surfaces;
7. audit for stale copies.

The change is not complete until the audit passes.

## Downstream Audit

Before delivery, verify:

- names and identifiers;
- numbers, units, and dates;
- scope and exceptions;
- tense, audience, and stance;
- referenced versions;
- assumptions converted into facts;
- sections produced before the latest update.

Use search, tests, or structured comparison when the deliverable is large. Do not rely on a
feeling of consistency.

## Hierarchical Broadcast

When the core grows:

- keep a small global core containing objective and true invariants;
- create section cores for local details;
- make every section core inherit the global version;
- prohibit local redefinition of a global item;
- reload only the section core needed for current work.

This preserves the bottleneck: the chamber holds the current flame; the ledger holds the hearth.

## Dense Hub Rule

Compact notation is allowed in a private core only when:

- every symbol has one stable referent;
- the scope and source remain visible;
- another competent reader or later model instance can reconstruct it;
- it passes the `j-space-shorthand` codec audit.

User-facing outputs must return to clear language.

## Success Standard

Broadcast succeeds when:

- downstream sections agree without local re-derivation;
- one change propagates completely;
- conflicts are resolved at the hub;
- provenance and uncertainty remain attached;
- a fresh reader can identify the current authoritative version.

## Failure Modes

- **Private copies:** branches drift. Delete local authority and read the hub.
- **Weak loading:** an entry is listed but has no consequence. Bind it to its consumers.
- **Partial swap:** old values survive. Search every dependent surface.
- **Hub overload:** too many global facts compete. Introduce hierarchy.
- **Authority inversion:** a stylistic preference overrides verified evidence. Restore order.
- **Stale provenance:** a fact survives after its source changes. Honor expiry.
- **Dense encryption:** the hub cannot be reconstructed. Expand it.

## Handoff

- keep the current hub entry active → `j-space-directed-focus`
- reduce or externalize an overloaded hub → `j-space-capacity`
- resolve a conflicting interpretation → `j-space-deep-reasoning`
- verify changed facts → `j-space-empirics`
- audit the final surface → `j-space-introspection`


