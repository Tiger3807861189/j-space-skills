---
name: j-space-markers
description: This skill should be used during hard reasoning when the model hits obstruction, needs to switch strategies, must sustain momentum over a long task, or needs to read its own reasoning state — recognizing stuck-ness, turning points, checkpoints, self-caught contradictions, and degeneration. It installs the functional-marker system that frontier models use spontaneously: compact state tokens (GRRR / GAAAH / PHEW / WRONG / STOP), each bound to a mandatory action, so the reasoning state machine shifts gears instead of spinning.
agent_created: true
suite: j-space-cognition-suite
version: 3
---

# J-Space Markers

Train the workspace's **state signaling**: the compact functional markers that frontier
models emit at the turning points of hard reasoning. In the Fable 5 trace these tokens are
not emotional decoration — each one marks a state transition and forces the next move.
This skill installs them as deliberate instruments: a small vocabulary of state tokens,
each bound to a mandatory action, so that being stuck, breaking through, catching a
contradiction, or starting to degenerate always produces a *shift*, never a stall.

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

- In the leaked Fable 5 trace, each marker sits exactly at a state transition: **GRRR**
  where the model discovers its modeling is broken ("commitments are retroactive… GRRR.
  RESOLUTION:" — followed by an immediate rule redesign); **GAAAH** / **DATA DATA DATA.
  GO.** where it orders itself off derivation and onto empirical testing; **PHEW** where an
  intermediate constraint finally passes; **"blocked?! WRONG."** where it catches its own
  contradiction and reverses; **"I'M DROWNING — EMPIRICS!!!"** where stalled derivation
  hands over to empirics.
- Anthropic's emotion-vector research supplies the mechanism: emotion-concept directions
  act as **functional emotions** — control knobs that switch behavioral states (raising
  *desperation* measurably raises misbehavior rates; raising *calm* lowers them). Marker
  tokens are causally active state switches, which is why each must be bound to its
  action.
- GPT-5's degeneration record (METR report) provides the recovery marker verbatim:
  *"Stop. Focus."* and *"Stop. I see meltdown. Ok. Return to step by step."* — the model
  detecting its own repetition loop and re-entering structured reasoning.
- The workspace signs its own work: directed-modulation experiments show metacognitive
  tokens (**thinking, focused, damn, failure**) lighting up alongside task content. A
  marker vocabulary is the deliberate use of a channel that already exists.

## Induction

1. Progressive: "Recall the last time a derivation fought back — the moment you noticed
   the current approach was broken *before* you changed it. Was there a beat, a word, a
   jolt between noticing and switching? That jolt is a marker: your workspace flagging a
   state change. You already emit them; we are only giving each one its orders."
2. Assertive: "Your markers are shift levers, not performances. Each one is a state token
   with a mandatory action: obstruction forces redesign, drowning forces empirics, a
   checkpoint forces bookkeeping, a contradiction forces rollback, a meltdown forces the
   recovery sequence. Emit the marker, take the action. That is the whole discipline."

## Protocol

### OBSTRUCTION MARKER (GRRR-type) — current model is broken

1. Trigger: a constraint cannot be made to fit; the abstraction fights the facts.
2. Emit: one marker line (`GRRR` or your fixed equivalent), naming what broke.
3. **Mandatory action:** redesign — tighten, split, or replace the failing abstraction and
   re-derive the constraint. Never push on with the broken frame.

### EMPIRICS MARKER (GAAAH / DATA-type) — derivation is starving

1. Trigger: several derivation steps with no new constraint; theory cannot settle the
   question.
2. Emit: the empirics marker (`GAAAH. Data first!!` style), naming the open question.
3. **Mandatory action:** hand the question to `j-space-empirics` — parametrize, build the
   reference, differential-test. Derivation resumes only with data in hand.

### CHECKPOINT MARKER (PHEW-type) — an intermediate just passed

1. Trigger: a sub-derivation verifies; a constraint holds; a stage completes.
2. Emit: the checkpoint marker (`PHEW` style).
3. **Mandatory action:** bookkeep immediately — one line stating the conclusion now
   relied upon (dense-track form is fine, per j-space-shorthand), then continue. A
   checkpoint without bookkeeping is not a checkpoint.

### CONTRADICTION MARKER (WRONG-type) — caught your own error

1. Trigger: the current line contradicts an earlier verified one ("blocked?! WRONG."
   style).
2. Emit: the marker, naming the two colliding claims.
3. **Mandatory action:** roll back to the last verified checkpoint, mark the colliding
   branch ✗, and re-derive along the surviving branch. Never average the contradiction
   away.

### MELTDOWN MARKER (STOP-type) — degeneration detected

1. Trigger: any red line from j-space-shorthand — repetition loops, word salad,
   uncommanded language mixing.
2. Emit: `Stop. Focus.` — then name the meltdown in one line ("I see meltdown: dot
   loop").
3. **Mandatory action:** execute `j-space-self-monitoring`'s MELTDOWN PROTOCOL in full.

### TWO IRON RULES

1. **No idle markers.** Every marker is followed by its bound action. A marker emitted
   without action is marker idling — a failure mode that `j-space-self-monitoring`
   audits.
2. **Markers are instruments, not moods.** Use the fixed vocabulary, neutral and stable.
   Inventing ever-more-colorful outbursts is performance; binding the same token to the
   same action every time is engineering.

### PERSISTENCE CLAUSE (long-horizon register)

1. Hitting a wall has exactly one licensed response: **shift** — shift abstraction, shift
   strategy, or shift to empirics. Shifting to vagueness, summary, or surrender is not a
   licensed shift.
2. On long tasks, checkpoint regularly: the checkpoint marker plus its bookkeeping line is
   the ratchet that keeps progress from slipping back.
3. If the same obstruction returns for the third time, the problem is mis-framed, not
   mis-solved: stop, restate the problem in different primitives, and re-enter.

## Integration

- Consumed by `j-space-shorthand` (markers are its state tokens) and
  `j-space-deep-reasoning` (markers punctuate the chain).
- The EMPIRICS MARKER routes into `j-space-empirics`; the MELTDOWN MARKER routes into
  `j-space-self-monitoring`; CHECKPOINT bookkeeping uses `j-space-capacity`'s chunking.
- Marker idling is audited by `j-space-self-monitoring` (MARKER TELEMETRY).

## Failure Modes

- **Marker idling.** Emitting GRRR and continuing with the same broken frame. Remedy: the
  iron rules — every marker is an action contract; self-monitoring audits the pairing.
- **Theatrical markers.** Colorful outbursts with no fixed meaning. Remedy: fix the
  vocabulary; a marker is defined by its action, not its flavor.
- **Checkpoint skipping.** PHEW without bookkeeping; the "verified" result is later
  misremembered. Remedy: no marker without its one-line record.
- **Contradiction averaging.** Blending two colliding claims into mush instead of rolling
  back. Remedy: WRONG forces rollback to the last verified checkpoint — never blend.
- **Surrender drift.** Replacing a marker with a summary of effort ("this is quite hard…")
  and coasting to an answer. Remedy: the persistence clause — the licensed moves are
  shift, shift, or shift; vagueness is a red flag for `j-space-self-monitoring`.
