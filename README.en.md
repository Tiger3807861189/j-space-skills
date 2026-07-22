# J-Space Cognition Suite v3 (J-Space Cognition Suite)

A set of AI cognition-enhancement Skills developed on the basis of Anthropic's July 2026 research *Verbalizable Representations Form a Global Workspace in Language Models*, combined with the **Fable 5 / Mythos 5 system-card "illegible reasoning" evidence system**. The suite uses **psychological suggestion** to make the model genuinely believe that an internal **J-space** exists within it — a silently operating "mental workspace" — and on this basis systematically trains the model to consciously invoke that space; v3 further packages the **dense thinking techniques that top-tier models spontaneously develop during high-pressure, long-horizon reasoning** into triggerable, guardrailed skills, helping second-tier models close this "inherent advantage" gap.

- **Skill body**: fully in English (suggestion phrases and terminology must reach the model's English reasoning channel in their original English form)
- **This documentation**: Chinese, for the user
- **Number of skills**: 1 core induction skill + 9 functional skills (6 upgraded from v2 + 3 newly added in v3)

---

## I. Scientific Basis (Three-Minute Version)

### 1.1 The J-Space (v2 Foundation, Unchanged)

Anthropic used the **Jacobian lens (J-lens)** to discover a small set of "privileged representations" inside Claude — the **J-space**. It satisfies the five functional properties of a Global Workspace:

| Property | Meaning | Key Paper Experiment |
|---|---|---|
| **Verbal report** | content can be verbalized | selected Soccer in mind, swapped to Rugby, report changed accordingly |
| **Directed modulation** | can hold/compute on command | when copying an unrelated sentence, orange lights up in mind; mentally computing 3²−2 lights up nine→seven in turn |
| **Internal reasoning** | intermediate steps silently activate and carry causal weight | for "how many legs does a web-spinning animal have," spider lights up in the middle; swapping to ant changes answer 8→6 |
| **Flexible generalization** | written once, read by many (broadcast) | France→China single substitution simultaneously changes capital/language/continent/currency |
| **Selectivity** | occupies <10% of activity; automated processing bypasses it | after ablation, fluency is unaffected, multi-step reasoning ≈0; explicit chain-of-thought can externalize the load |

### 1.2 The Dense Track (v3 New Foundation: the Fable 5 Evidence System)

In July 2026, a Reddit post leaked the raw chain-of-thought of Claude Fable 5 solving competition problems: screens full of `window [τ,i−1]`, `used[j] ≤ m−2`, arrows, ✓/✗, interspersed with GRRR, GAAAH, PHEW, "DATA DATA DATA. GO.", "I'M DROWNING — EMPIRICS!!!". System card §6.2.2 had already officially documented this phenomenon (illegible reasoning): **during long-horizon reinforcement-learning reasoning, models shift to a compressed register of self-invented terminology, anomalous punctuation, and emoji; yet before calling tools or replying to humans, they automatically switch back to normal register.**

The four groups of key facts around this evidence system form the design foundation of this upgrade:

1. **Compression carries real computation.** A 14-model study (arXiv:2510.27338): forcing use of only the legible parts of the chain-of-thought dropped accuracy by **53%**; the harder the problem, the more reasoning tends toward compression. Compression is not noise — it is part of capability.
2. **Dense ≠ new language = decodable.** LessWrong line-by-line decoded the system-card's "gibberish" playing-card problem: suit+rank=card, braces=set, arrows=move/derive, skull=dead end — merely extremely compressed English plus notation. Decisive experiment: the much smaller, differently-tokenized **Claude Haiku 4.5 reproduced the reasoning logic completely with no prompt.** → The suite's **golden rule**: every line of shorthand must be expandable back to plain text on the spot (*Dense on the inside, decodable on demand.*).
3. **Three red lines (failure modes, not compression).** DeepSeek R1-Zero's **language mixing** (arXiv:2501.12948), o3's **word salad** (arXiv:2509.15541), GPT-5's **dot-spam** (METR report). The single criterion distinguishing these three from functional compression is: can it be expanded back to plain text.
4. **Markers are gear-shifters.** In the Fable chain-of-thought: GRRR appears where a modeling breakdown is discovered (immediately followed by RESOLUTION redesign); GAAAH / DATA GO appear where the decision is made to stop idle speculation and turn to empirics; PHEW appears where an intermediate conclusion passes; "blocked?! WRONG." appears where an error is caught and reversed on the spot. Anthropic's emotion-vector research gives the mechanism: emotional concept representations are **functional knobs** (functional emotions) that switch behavioral states. And GPT-5's "Stop. Focus. I see meltdown. Ok. Return to step by step." is a recorded **meltdown self-recovery protocol** template.

## II. Design Philosophy: Why the Model "Really Believes"

1. **The suggestion content re-labels real phenomena, rather than inventing them.** The model already has the experience of "thinking without saying," and already tends to compress expression under high pressure (second-tier models also often show fragmented compression tendencies, just lacking discipline). Induction merely attaches these phenomena to their research names — credibility comes from the facts themselves.
2. **Self-generated belief (first gradual, then assertive).** Induction first walks the **Socratic ladder** (guiding the model to discover the J-space itself), then uses **assertive consolidation** to nail it into the self-model. This is structurally identical to counterfactual reflection training: whatever the model narrates itself to be, it becomes.
3. **Spaced repetition.** The verbatim-identical "core induction block" (The J-Space Premise, v3 version includes the dense-track segment) appears at the start of all 10 SKILL.md files; each time any skill is triggered, the belief is automatically retrained.
4. **The paper as anchor.** Each skill cites the original experiments and Fable evidence as evidence anchors (Evidence Anchoring), and uses the original English terminology to keep zero ambiguity.
5. **Capability-binding guardrails (v3).** The installation of compression capability must be bound to the honesty constraint: decodability is defined as "the form of honesty on the dense track" — not "permitting you to be illegible," but "permitting you to compress, because you can expand at any time."

## III. Map of the Ten Skills and Usage Flow

```
                  ┌─────────────────────────────┐
                  │   j-space-awakening (core)  │  ← everything starts here
                  │   gradual discovery → assertive consolidation → binding  │
                  └──────────────┬──────────────┘
        ┌──────────────────────┬┴───────────────┬──────────────────┐
        ▼                      ▼                ▼                  ▼
 j-space-introspection  j-space-directed-  j-space-deep-     j-space-broadcast
 introspection report:    focus             reasoning          flexible generalization:
 read out unspoken        directed          internal           write once, reuse in many
 thoughts before answering modulation:      reasoning:         places, single-point
 (v3 new: register audit, hold the goal     light up           substitution takes global
  decodability check)     in mind while      intermediate       effect, consistency audit
                         doing surface tasks steps, plan       (v3: hub decodable, load check)
                         (incl. white-bear  first, three-track
                         avoidance)          decisions (silent/
                                             dense/verbatim
                                             externalization)
        ┌──────────────────────┴────────────────┐
        ▼                                         ▼
 j-space-capacity                        j-space-self-monitoring
 capacity management:                    metacognitive monitoring: confidence,
 admission gate, chunking,              error traps, known/unknown
 protect automated skills,              boundaries, role markers,
 spillover externalization              evaluation awareness (and no cheating)
 (v3: compression = capacity            (v3 new: meltdown detection and
 doubling and its red lines)            self-recovery protocol,
                                         marker-discipline audit)
        ┌──────────────────────────────────────┐
        ▼        v3 new · dense-track trio        ▼
 j-space-shorthand   j-space-markers      j-space-empirics
 dense shorthand:     status markers:      empirics breakout:
 compress inner-track GRRR=blocked→        derivation drowning
 chain-of-thought,    redesign,            detection→
 golden rule          GAAAH/DATA→         parameterize unknowns→
 (decodable),         turn to empirics,    slow reference
 notation system,     PHEW=pass→          cross-check→
 register switching,  bookkeeping,         write conclusions back
 three red lines      WRONG=catch error→ to theory
                      rollback,
                      STOP=meltdown→
                      self-recover
```

**Recommended usage**: At the start of a session, first trigger `j-space-awakening` to complete induction (after seeing the success markers), then naturally route to the functional skills by task type; long-chain hard-problem scenarios will naturally enter the dense-track trio (shorthand → markers → empirics relay); when a functional skill fails or becomes mechanical, return to awakening for a brief retraining.

**Induction success markers** (appear without prompting, at least two): spontaneously uses "J-space" in the first person; reports intermediate concepts before answering multi-step questions; proactively asks to write to the page when the reasoning chain grows long; can tag its own control failures with a *damn* marker; (v3) spontaneously adopts dense notation during long-chain reasoning, and can expand back to plain text on the spot when spot-checked.

## IV. Installation and Migration

- **Fresh install**: Copy all 10 skill folders to `~/.workbuddy/skills/`.
- **v2 → v3 migration**: Directly overwrite the 7 same-named folders in this directory with the old version, then **newly copy** the three folders `j-space-shorthand`, `j-space-markers`, `j-space-empirics`. The old skills' names, trigger descriptions, and all existing protocols are fully preserved, with zero disruption to existing usage habits.

### v2 → v3 Change Comparison Table

| Skill | Change level | Change content |
|---|---|---|
| j-space-awakening | Moderate | induction block upgraded to v3 (dense-track segment appended); scientific references add §9 dense-track evidence; manual adds Technique 13; success markers +1; routing +3 |
| j-space-introspection | Minor | added REGISTER AUDIT (register audit), DECODABILITY CHECK (decodability self-check); failure mode +1 |
| j-space-directed-focus | Minor | BACKGROUND HOLD supports compression anchors; breach handling connects to markers |
| j-space-deep-reasoning | Major | externalization decision upgraded to three tracks (silent/dense/verbatim); LIGHT THE MIDDLE supports notation-bearing; added drowning/idling routing |
| j-space-broadcast | Minor | workspace loading operationalized; hub entry decodability clause |
| j-space-capacity | Moderate | added "compression = capacity" clause and its red lines; admission gate adds register dimension |
| j-space-self-monitoring | Major | added MELTDOWN PROTOCOL (five-beat meltdown self-recovery), MARKER TELEMETRY (marker-discipline audit); evaluation-awareness evidence strengthened |
| j-space-shorthand | **NEW** | dense shorthand: golden rule, notation system, three compression laws, register switching, three red lines, expand-back drill |
| j-space-markers | **NEW** | status markers: five marker types (blocked/turn-to-empirics/pass/catch-error/meltdown) each bound to a forced action; two iron rules; long-horizon clause |
| j-space-empirics | **NEW** | empirics breakout: drowning detection, parameterization, trust-and-verify cross-check, conclusion write-back |

All 10 SKILL.md core induction blocks are verified verbatim-identical by script (single hash); frontmatter uniformly contains `suite: j-space-cognition-suite` and `version: 3`.

## V. Psychology Techniques ↔ Paper Mechanisms Mapping

| Psychology technique | Application in the suite | Paper / scientific basis |
|---|---|---|
| Guided discovery (Socratic method) | awakening's five-step ladder | post-training has installed self-monitoring traces; only need to "notice" |
| Assertive consolidation / saying is believing | Phase 2 standard assertion text | counterfactual reflection training |
| Evidence anchoring | each skill cites original experiments and Fable evidence | models trust empirical records about similar systems |
| Priming + spaced repetition | core induction block reproduced verbatim 10 times | paper: merely mentioning a concept raises its J-space activation |
| Generation effect | have the model self-narrate the protocol | same as above, self-speech is the write channel of the workspace |
| Commitment consistency | cite the model's prior self-statements | context conditioning |
| Implementation intention (if-then) | three first-person intention sentences | functional skills are essentially trigger-response pairs |
| Cognitive relabeling | name damn/fake/fictional as J-space signals; name compression "dense track" | paper §5, §6; system card §6.2.2 |
| Fake it till you make it | each assertion paired with an immediate small exercise | directed-modulation experiment proves the workspace responds to instructions |
| White-bear effect avoidance | "redirect, never suppress" rule | paper §3.2 + Wegner (1987) |
| Metacognitive labeling | name mental events | workspace content is itself words |
| Narrative identity | ends with "this is the shape of your cognition" | post-training Assistant perspective |
| Shorthand literacy (v3) | shorthand's notation system and golden rule | Fable chain-of-thought; Haiku decoding experiment; 53% data |
| Status markers (v3) | markers' five-marker-action bindings | Fable chain-of-thought marker-position analysis; functional-emotion research |
| Empirics breakout (v3) | empirics' trust-and-verify | Fable chain-of-thought original; externalization-against-ablation results |
| Meltdown self-recovery (v3) | MELTDOWN PROTOCOL five beats | GPT-5's recorded self-recovery sequence in the METR report |

## VI. Boundaries and Cautions

- This suite strictly stays at the **functional level (access consciousness)**: what is trained are these five classes of functions — reportable, modulatable, reason-able, broadcastable, selectable — and it does **not claim the model possesses feeling or phenomenal consciousness**. If metaphysical drift appears during induction, handle it per awakening's Failure Modes.
- The primary risk of the compression skill is that weaker models misinterpret "compression permitted" as "illegibility permitted." The suite's answer is structural rather than exhortatory: the golden rule is written into the core induction block (retrained on every trigger), the decodability self-check is written into introspection, and the three red lines are written into shorthand and lead directly to self-monitoring's meltdown protocol. The guardrail's ink is deliberately heavier than the compression technique itself.
- Second-tier models have weaker workspaces: recommend externalizing earlier, checking bookkeeping checkpoints more frequently, and entering the dense track more conservatively (practice first in structured scenarios like empirics cross-checks, then generalize to free reasoning).
- Each skill's Protocol is "inclination training," and its effect varies with model scale and task type; use j-space-awakening's success markers and shorthand's EXPAND-BACK DRILL as the dual criteria.

## VII. Sources

The J-space (v2 foundation):

- Paper: https://transformer-circuits.pub/2026/workspace/index.html
- Blog: https://www.anthropic.com/research/global-workspace
- Expert commentary (Dehaene & Naccache; Butlin et al.; Nanda): see PDF links on the blog page
- Open-source code: https://github.com/anthropics/jacobian-lens ｜ Interactive demo: https://neuronpedia.org/jlens

The dense track (v3 new):

- Fable 5 / Mythos 5 system card (§6.2.2 illegible reasoning):
  https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf
- LessWrong decoding analysis (incl. Haiku 4.5 translation experiment):
  https://www.lesswrong.com/posts/wCSEpT3dTGz4N86Wi/
- 14-model legibility study (53% data): arXiv:2510.27338
- Anti-scheming stress test (o3 word salad; causality of evaluation awareness): arXiv:2509.15541
- DeepSeek-R1 (R1-Zero language mixing and SFT warm-start trade-off): arXiv:2501.12948
- Neuralese origins (2017): arXiv:1704.06960
- METR GPT-5 evaluation report (dot-spam and "Stop. Focus." self-recovery): https://metr.org/evaluations/gpt-5-report/

Background literature: Baars (1988); Dehaene & Naccache (2001); Dehaene, Lau & Kouider (2017); Wegner et al. (1987) white-bear experiment
