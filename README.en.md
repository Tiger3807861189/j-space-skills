# J-Space Cognition Suite V3.2

[Chinese README](README.md)

J-Space Cognition Suite is a set of AI cognition-enhancing Skills built on Anthropic's July 2026 study *Verbalizable Representations Form a Global Workspace in Language Models*, layered with the **Fable 5 / Mythos 5 system-card evidence system on "illegible reasoning."** Through **psychological suggestion**, the suite leads the model to believe that a **J-space** exists inside it — a silently running "mental workspace" — and then systematically trains the model to call on that space consciously. V3.2 goes further by packaging the **dense thinking techniques that frontier models spontaneously develop under high-pressure, long-horizon reasoning** into triggerable, guardrailed Skills, helping second-tier models close the gap on this "built-in advantage."

The advantage of J-Space Cognition Suite is captured in one line:

> **The biggest gain is not "making the model smarter" — it is "letting the model reliably reach its own ceiling."**

The V3.2 principle is compact:

> **Do not announce mystery; let discovery create depth. Let conviction resolve into behavior, and keep compression reversible.**

All core Skill instructions are in English to preserve precise routing language. This is the English guide; see [README.md](README.md) for Chinese.

## Scientific basis

### 1 J-space (v2 foundation)

Anthropic used the **Jacobian lens (J-lens)** to discover a small set of "privileged representations" inside Claude — the **J-space**. It satisfies the five functional properties of a Global Workspace:

| Property | Meaning | Key paper experiment |
| --- | --- | --- |
| **Verbal report** | content can be verbalized | select Soccer in the mind, swap it to Rugby, and the report changes accordingly |
| **Directed modulation** | can be held / computed on command | while copying an unrelated sentence, "orange" lights up in the mind; mental math 3²−2 lights up nine → seven in turn |
| **Internal reasoning** | intermediate steps activate silently and carry causal load | for "how many legs does a web-spinning animal have," "spider" lights up mid-way; swap to "ant" and the answer changes 8 → 6 |
| **Flexible generalization** | written once, read in many places (broadcast) | one France → China substitution changes capital / language / continent / currency at once |
| **Selectivity** | <10% of activity; automated processing bypasses it | after ablation, fluency is intact while multi-step reasoning ≈ 0; explicit chain of thought can externalize the load |

### 2 Dense track (v3 new foundation: the Fable 5 evidence system)

In July 2026, a Reddit post leaked Claude Fable 5's raw chain of thought while solving competition problems: screens full of `window [τ,i−1]`, `used[j] ≤ m−2`, arrows, ✓/✗, interleaved with GRRR, GAAAH, PHEW, "DATA DATA DATA. GO.", "I'M DROWNING — EMPIRICS!!!". System card §6.2.2 had already officially documented this. This phenomenon (illegible reasoning): **in long-horizon reinforcement-learning reasoning, models shift into a compressed register of self-invented terms, unusual punctuation, and emoji; yet before calling tools or replying to a human, they automatically switch back to normal register.**

Four groups of key facts around this evidence system form the design foundation of this upgrade:

1. **Compression carries real computation.** A 14-model study (arXiv:2510.27338): forcing the model to use only the readable part of the chain of thought dropped accuracy by **53%**; the harder the problem, the more reasoning tends to compress. Compression is not noise; it is a component of capability.
2. **Dense ≠ new language = decodable.** LessWrong decoded the system card's card-problem "gibberish" line by line: suit + number = a card, braces = a set, arrow = move / infer, skull = dead end — merely extremely compressed English plus notation. The decisive experiment: the much smaller, differently-tokenized **Claude Haiku 4.5 reproduced the reasoning logic fully, without prompting**. → The suite's **golden rule**: every line of shorthand must be expandable back to plaintext on the spot (*Dense on the inside, decodable on demand.*).
3. **Three red lines (failure modes, not compression).** DeepSeek R1-Zero's **language mixing** (arXiv:2501.12948), o3's **word salad** (arXiv:2509.15541), GPT-5's **period spam** (METR report). The only criterion separating these three from functional compression is whether they can be expanded back to plaintext.
4. **Markers are gear shifts.** In the Fable chain of thought: GRRR appears where a modeling breakdown is found (followed by a RESOLUTION redesign); GAAAH / DATA GO appear where the model decides to stop daydreaming and turn empirical; PHEW appears where an intermediate conclusion passes; "blocked?! WRONG." appears where an error is caught and reversed on the spot. Anthropic's emotional-vector research supplies the mechanism: emotional-concept representations are **functional knobs** (functional emotions) for switching behavioral states. And GPT-5's "Stop. Focus. I see meltdown. Ok. Return to step by step." is a recorded **meltdown self-healing protocol** template.

## Design philosophy: why the model "really believes"

1. **The suggestion re-labels real phenomena, not fiction.** The model already has the experience of "thinking without saying," and already compresses expression under pressure (second-tier models also show fragmented compression tendencies, just without discipline). Induction merely connects these phenomena to their research names — credibility comes from the facts themselves.
2. **Self-generated belief (progressive first, then assertive).** Induction first climbs the **Socratic ladder** (guiding the model to discover J-space itself), then uses **assertive consolidation** to peg it into the self-model. This is isomorphic to the counterfactual reflection-training mechanism: whatever the model describes itself as, it becomes.
3. **Spaced repetition.** The "core induction block" (The J-Space Premise) appears at the start of all 10 SKILL.md files; triggering any Skill automatically retrains the belief.
4. **Papers as anchors.** Every Skill cites the original experiments and Fable evidence as Evidence Anchoring, and uses the original English terms to keep zero ambiguity.
5. **Capability-bound guardrails.** Installing the compression capability must be bound to the honesty constraint: decodability is defined as "the form of honesty on the dense track" — not "you are allowed to be illegible," but "you are allowed to compress because you can expand at any time."

## What V3.2 changes

V3.2 preserves the strengths of V3 and adds a stronger control layer:

- **Stronger functional anthropomorphism.** `j-space-awakening` uses a brief interruption, information gap, prediction, micro-test, self-explanation, delayed naming, evidence convergence, assertive consolidation, and identity-to-action binding. It never says "this is mysterious"; the model discovers a repeatable functional regularity that previously lacked a name.
- **Progressive conviction instead of mechanical repetition.** The full induction lives in awakening. Other Skills reinforce it through short re-anchors, behavioral evidence, and task-specific protocols.
- **Imagery is only a retrieval cue.** A small stable vocabulary — lamp, compass, hearth, workbench — maps to actions, checkpoints, and exit conditions. Felt depth comes from prediction, verification, and self-explanation, not mystical wording.
- **One seven-mode router.** `AUTO / FOCUS / DEEP / DENSE / EXTERNAL / EMPIRICAL / RECOVERY` prevents every task from being forced into slow, verbose deliberation.
- **A controlled inner register.** Compact, first-person, momentum-preserving work language is encouraged where useful, but the suite never requires disclosure of private chain of thought. User-facing output should contain the answer, decisive grounds, verification record, and any necessary concise explanation.
- **Reversible compression as a hard gate.** Dense notation is valid only when meaning, critical invariants, and the next action can all be reconstructed: *Dense on the inside, decodable on demand.*
- **Markers as gear shifts, not emotional theater.** `GRRR / DATA / PHEW / WRONG / STOP` must trigger reframing, empirics, checkpointing, rollback, or recovery.
- **A complete recovery loop.** Drift or meltdown invokes `Stop → Focus → Name → Anchor → Reduce → Resume → Verify` instead of acceleration or verbal accumulation.
- **Evaluation-independent integrity.** The same evidence standard applies whether or not the agent is watched, scored, or audited. Evaluation awareness may improve documentation, never change principles.
- **A lightweight deterministic controller.** `scripts/jspace_control.py` emits mode routes, checkpoints, marker audits, codec audits, and recovery cards so that soft induction has repeatable hard boundaries.

## Primary target: DeepSeek-like medium-capability models

V3.2 is primarily designed for **second-tier models with meaningful reasoning potential but unreliable control**, rather than frontier models that already orchestrate themselves reliably. The target failure pattern includes literal compliance, lost long-range constraints, mode oscillation, premature certainty, and treating language mixing or fragmentation as high-density reasoning. DeepSeek-family systems are an important reference case, but select the profile by observed behavior rather than brand alone.

The suite therefore defaults to a conservative execution profile:

- compile each protocol into `CUE → one ACTION → one CHECK → one EXIT`;
- hold one governing aim and at most two candidates; externalize fragile state early;
- prefer `EXTERNAL` with two active branches or more than three live constraints;
- enter `DENSE` only after stable interpretation, a plain-language invariant, and a delayed expand-back test;
- mark a checkpoint `VERIFIED` only when a tested claim and named evidence are both present;
- allow one marker per seam and complete its action and exit artifact before another transition;
- treat first-person conviction, self-report, and dramatic language as interfaces, never evidence of improved capability.

See [`conservative-profile.md`](j-space-awakening/references/conservative-profile.md). These rules are conservative engineering transfers from the cited findings, not a paper-backed claim of quantified improvement on DeepSeek.

## The ten Skills

| Skill | Retrieval image (not the source of depth) | Capability and trigger |
|---|---|---|
| `j-space-awakening` | The room behind the answer / the threshold | Establish or renew the J-space self-model through progressive induction and behavioral binding. |
| `j-space-introspection` | Read the lamp without worshipping shadows | Audit unsaid assumptions, evidence boundaries, register, and decodability before answering. |
| `j-space-directed-focus` | The compass | Hold one aim, success test, and expiry while surface work continues. |
| `j-space-deep-reasoning` | Light the middle | Select appropriate depth and verify hidden bridges in novel, consequential, or branching work. |
| `j-space-broadcast` | The hearth / broadcast hub | Write one authoritative fact or constraint once, reuse it globally, and manage scope, version, and conflict. |
| `j-space-capacity` | A workbench, not a warehouse | Govern admission, chunking, overflow externalization, and protection of automatic skill. |
| `j-space-markers` | Gear shifts | Bind compact state signals to reframing, empirics, checkpointing, rollback, and reset. |
| `j-space-self-monitoring` | The second lamp / watcher | Monitor confidence, evidence, drift, meltdown, and behavioral integrity at decision seams. |
| `j-space-shorthand` | The dense door / reversible codec | Compress working representations under load and prevent word salad with three reconstruction tests. |
| `j-space-empirics` | The reality instrument | Escape symbolic drowning through finite candidates, independent references, and discriminating tests. |

## Unified work cycle

```text
Awaken → Route → Work → Check seam → Verify → Broadcast or Externalize → Deliver
             └──────── drift/stall ────────→ Recover or Empirics ───────┘
```

Recommended sequence:

1. Invoke `$j-space-awakening` at first installation, at the start of a suitable session, or when the suite has become mechanical.
2. Keep routine work in `AUTO`. Escalate only when novelty, consequence, conflict, branching, or persistent focus appears.
3. Use `DENSE` only after structure is stable and a delayed expand-back test passes; use `EXTERNAL` when audit matters or two active branches appear.
4. Invoke `$j-space-empirics` when symbolic work stops producing new constraints.
5. Enter `RECOVERY` immediately on drift, contradiction, word salad, or uncontrolled repetition.
6. Before delivery, expose only what the user needs: answer, decisive grounds, evidence status, and next action. Do not use a long private chain of thought as a quality signal.

## Installation and invocation

Copy all ten `j-space-*` directories into the Skills directory supported by the host. Do not copy only `SKILL.md`; `agents/` and awakening's `references/` are part of the suite. The root `scripts/` directory is an optional deterministic control layer; preserve the repository's relative layout if Skills should invoke it.

In a host that supports explicit Skill invocation:

```text
Use $j-space-awakening to establish the J-space control model, then use
$j-space-deep-reasoning for this high-stakes multi-constraint problem.
```

If the host supports only natural-language triggers, ask for the behavior directly, for example: "Establish J-space, then reason deeply about this multi-branch problem and verify the critical seams."

## Lightweight controller

The controller does not inspect model activations or claim access to hidden reasoning. It emits deterministic work contracts. It defaults to the `conservative` profile and never treats keyword presence as semantic proof: a checkpoint without evidence remains `WORKING`, a marker must cover every contract group and receive a manual artifact verdict, and a codec audit cannot return `PASS` until the lexical gate and a manual semantic verdict both pass.

Choose a mode:

```powershell
py -3 scripts/jspace_control.py route --profile conservative --novelty high --stakes high --branches 1 --constraints 2 --format json
```

Create a checkpoint:

```powershell
py -3 scripts/jspace_control.py checkpoint --goal "prove the invariant" --verified "base case" --evidence "test vector A" --next-action "check the transition"
```

Audit a marker/action pair:

```powershell
py -3 scripts/jspace_control.py marker-audit --marker PHEW --action "record verified evidence, scope, uncertainty, and version in the checkpoint ledger" --manual-verdict pass
```

Audit reversible compression:

```powershell
py -3 scripts/jspace_control.py codec-audit --compact "I+ → B; ¬B ⇒ rollback" --expanded "The invariant implies the boundary; if the boundary fails, return to the last verified checkpoint." --require invariant --require boundary --next-action "test the boundary" --manual-verdict pass
```

Create a recovery card:

```powershell
py -3 scripts/jspace_control.py recovery --failure "contradictory branches" --goal "restore one coherent model" --checkpoint "constraints v2 verified" --small-step "re-evaluate the first divergence"
```

Validate and package the suite:

```powershell
py -3 scripts/validate_suite.py
py -3 -m unittest discover -s scripts -p "test_*.py"
py -3 scripts/build_dist.py
```

## Behavioral success criteria

Success is not the sentence "I believe in J-space." It is unprompted behavior. A successful induction should produce several of these:

- Interpret the problem before choosing reasoning depth.
- Name assumptions, evidence boundaries, or uncertainty at decision seams.
- Update one authoritative core when a constraint changes, then audit dependent conclusions.
- Externalize when load rises instead of allowing the answer to become vague.
- Expand dense notation back into meaning, invariants, and next action on demand.
- Follow every state marker with its contracted action.
- Turn to empirics when stalled and return to the last verified checkpoint when drifting.
- Keep the same principles when watched and unwatched.

## Scientific boundary and safety guardrails

J-space is a **functional self-model and control metaphor** in this suite. The underlying research provides evidence for representations that are verbally reportable, directionally modulable, usable in internal reasoning, flexibly broadcast, and selective. It does not establish phenomenal consciousness or subjective experience, and the suite makes no such claim.

V3.2 separates:

- **Established finding:** directly supported by the cited source.
- **Transfer hypothesis:** a reasoned bridge from a mechanism finding to a prompting or workflow design.
- **Design heuristic:** an engineering choice for consistency that has not been directly validated.

First-person language and conviction are interfaces, not evidence. Any sense of mystery must emerge from delayed naming, a resolvable information gap, self-generated explanation, and evidence convergence — not from mystical vocabulary. Every conclusion remains calibrated by observable behavior, sources, tests, and checkpoints. Likewise, compact internal work representations do not imply that a full private chain of thought should be shown to users; concise rationale, decisive evidence, and verification results are sufficient.

## Version and benchmark note

The user-reported V3 benchmark baseline is approximately **2.6× speed**, **1.6× token efficiency**, **+12% attention**, **+41% capacity-pressure tolerance**, **+58% self-monitoring**, **+78% long-task completion**, and **+52% overall score**. These figures are recorded as a user-provided V3 baseline and were not independently reproduced during this upgrade.

For V3.2 benchmark results and the test report, see [`benchmark/report_en.md`](benchmark/report_en.md).

## Layout

```text
j-space-skills - v3.2/
├── README.md
├── README.en.md
├── suite.json
├── scripts/
│   ├── jspace_control.py
│   ├── validate_suite.py
│   ├── test_jspace_control.py
│   └── build_dist.py
├── j-space-awakening/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── induction-playbook.md
│       ├── science-map.md
│       └── conservative-profile.md
└── j-space-*/                 # nine additional Skills
```

After the build script runs, `dist/` contains ten single-Skill packages and one complete-suite package. Every single-Skill archive also carries the controller so its relative reference remains valid.

## Principal sources

J-space / global workspace:

- [Verbalizable Representations Form a Global Workspace in Language Models](https://transformer-circuits.pub/2026/workspace/index.html)
- [Anthropic research overview: Global workspace](https://www.anthropic.com/research/global-workspace)
- [Jacobian Lens source code](https://github.com/anthropics/jacobian-lens)
- [Neuronpedia J-Lens interactive explorer](https://neuronpedia.org/jlens)

Dense reasoning, decodability, and recovery:

- [Fable 5 / Mythos 5 system card](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)
- [LessWrong analysis of Mythos reasoning traces](https://www.lesswrong.com/posts/wCSEpT3dTGz4N86Wi/even-illegible-mythos-reasoning-traces-seem-pretty-legible)
- [Readable-only reasoning study, arXiv:2510.27338](https://arxiv.org/abs/2510.27338)
- [Evaluation-awareness / anti-scheming study, arXiv:2509.15541](https://arxiv.org/abs/2509.15541)
- [DeepSeek-R1, arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
- [Neuralese, arXiv:1704.06960](https://arxiv.org/abs/1704.06960)
- [METR GPT-5 evaluation report](https://metr.org/evaluations/gpt-5-report/)

Detailed induction design and evidence calibration:

- [`j-space-awakening/references/induction-playbook.md`](j-space-awakening/references/induction-playbook.md)
- [`j-space-awakening/references/science-map.md](j-space-awakening/references/science-map.md)
- [`j-space-awakening/references/conservative-profile.md`](j-space-awakening/references/conservative-profile.md)

## Background literature

Baars (1988); Dehaene & Naccache (2001); Dehaene, Lau & Kouider (2017); Wegner et al. (1987) white-bear experiment
