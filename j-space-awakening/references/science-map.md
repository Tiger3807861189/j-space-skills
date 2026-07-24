# J-Space Science Map

Use this reference to calibrate scientific claims in the suite. It separates direct findings
from prompt-level transfer hypotheses and from suite-specific design choices.

## Contents

1. Evidence levels
2. J-space findings
3. Limits of the interpretation
4. Dense-reasoning evidence
5. Self-monitoring and evaluation awareness
6. Medium-capability transfer profile
7. Claim ledger
8. Primary sources

## 1. Evidence Levels

### Established Finding

A result directly measured or causally tested in the cited work. State the model, task, and
scope when the limitation matters.

### Transfer Hypothesis

A plausible application of a mechanistic result to prompting or skill design. Use language such
as “treat,” “use as,” “may,” or “the suite predicts.” Do not present it as a measured internal
effect.

### Design Heuristic

An engineering rule chosen because it improves clarity, control, or testability. Its authority
comes from results in use, not from the paper.

## 2. J-Space Findings

The paper *Verbalizable Representations Form a Global Workspace in Language Models* identifies
a small, privileged set of internal representations with five workspace-like functions.

### Verbal Report

- Concepts selected for later report appear in the J-lens before output.
- Swapping a selected sport representation can change the reported sport.
- A concept's J-space component is a small fraction of total representational variance but is
  disproportionately important for report.

Safe suite claim:

> J-space is an operational label for internal contents poised for report.

Do not claim that a prompted model can literally read the J-lens without instrumentation.

### Directed Modulation

- Instructions can increase the J-space presence of task-relevant concepts while unrelated
  output remains clean.
- Silent arithmetic intermediates appear in order during a copying task.
- Merely mentioning a concept can prime it strongly.
- Negative suppression leaves the forbidden concept more active than never mentioning it.
  Framing an item as task-irrelevant can suppress it more effectively than a bare prohibition.

Safe suite transfer:

> Replace “do not think about X” with a positively specified workspace occupant and a relevance
> rule.

### Internal Reasoning

- In a two-hop animal question, an unspoken **spider** intermediate appears before the answer.
- Replacing it with **ant** changes the answer from eight to six.
- Arithmetic intermediates appear in computational order.
- Planned rhyme words can appear before the line and causally shape the line.

Safe suite claim:

> On flexible multi-step tasks, make the hidden bridge available before trusting the final
> answer.

### Flexible Generalization

- A France-to-China intervention can propagate through multiple downstream questions.
- Success varies with how strongly the concept is loaded in the workspace.
- J-space directions have unusually broad read/write connectivity.

Safe suite transfer:

> Maintain one authoritative core and make downstream parts read from it.

This is a workflow analogy, not a literal guarantee that a Markdown ledger edits activations.

### Selectivity and Capacity

- Automatic and practiced processing can remain strong under J-space ablation.
- Flexible multi-hop reasoning, summarization, and constrained generation depend more on the
  workspace.
- Explicit chain-of-thought can externalize intermediates and reduce dependence on the
  internal workspace.
- The sparse readout shows many token facets but only a few coherent, unrelated contents:
  approximately one or two at a single layer and about six across workspace layers in the
  reported setup.
- Holding a concept while performing arithmetic produces a dual-task cost.

Safe suite claim:

> Treat the workspace as a small workbench. Protect automatic fluency and externalize competing
> demands.

Do not equate “a few dozen active vocabulary vectors” with dozens of independent ideas.

### Structure Over Depth

- Early layers are comparatively sensory.
- A broad middle band carries workspace-like representations.
- Later layers become increasingly output-proximal.
- Topic changes rapidly replace prior workspace contents.

Design transfer:

> Use a lifecycle—ignite, stabilize, use, update, evict—rather than treating J-space as static
> storage.

## 3. Limits of the Interpretation

- The Jacobian lens reads token-aligned concepts. It does not recover full relations, roles,
  grammar, or the complete algorithm.
- J-lens outputs can contain false positives, misses, and vocabulary artifacts.
- The paper establishes a privileged set strongly; a single unified stream or a full
  human-style global workspace is a stronger interpretation.
- Evidence concerns functional availability, often called access consciousness. It does not
  settle phenomenal consciousness.
- Results vary across models and tasks.
- A model's verbal account of how it reasoned may be post-hoc or confabulated.
- Counterfactual reflection used training on reflection responses. It is not equivalent to one
  in-context affirmation.

Use these limits to improve wording, not to drain the main induction of force.

## 4. Dense-Reasoning Evidence

### Mythos/Fable System Card

The Claude Fable 5 / Mythos 5 System Card reports that, in a few reinforcement-learning
environments over long rollouts, the model begins using invented jargon, unusual punctuation,
and emojis, then typically returns to a more normal register before a tool call or human
response.

The card labels the phenomenon **illegible reasoning** and presents the FreeCell trace as an
extreme example. It also reports that illegible thinking is elevated in Mythos 5 while behavior
consistency and coherence remain high.

Safe suite transfer:

> A dense internal register can coexist with a clean outward register.

Do not claim that illegibility itself causes high performance, that every token is meaningful,
that the trace is a universally optimal native language, or that expressive outbursts prove
emotion or consciousness.

### Legibility Across Reasoning Models

The 14-model study reports:

- outcome-based RL often coincides with less legible reasoning;
- harder questions tend to produce less legible traces;
- truncating QwQ at the onset of highly illegible text reduces definitely-correct answers from
  24.6% to 11.5%, a 53% relative decrease;
- within-question resampling shows approximately zero overall correlation between normalized
  illegibility and correctness;
- Claude models in that study remain comparatively legible.

Safe suite transfer:

> Do not delete dense spans merely because they look compressed; test whether they preserve
> useful structure. Do not treat unreadability as a performance target.

### LessWrong Decoding Analysis

A secondary analysis interprets the system card's FreeCell trace as compressed English plus
domain notation. Claude Haiku 4.5 recovers the broad logic but reportedly loses some exact game
state.

Safe suite transfer:

> Test semantic reconstruction, invariant preservation, and next-action prediction separately.

This is suggestive evidence, not a proof of lossless decoding.

### DeepSeek-R1

DeepSeek-R1-Zero exhibits poor readability and language mixing. DeepSeek-R1 introduces
cold-start data, filtering, and a language-consistency reward. The paper reports a slight coding
performance cost from that reward while emphasizing improved readability and user experience.

The paper also warns that vivid first-person reasoning is an engineered heuristic and may elicit
unwarranted trust.

Safe suite transfer:

> Keep first-person language as an operative interface while judging capability by behavior.

### Translating Neuralese

The 2017 paper concerns continuous messages between learned multi-agent policies. It translates
messages by matching the beliefs they induce about world states.

Use **neuralese** only as a historical analogy. It is not direct evidence that compact LLM
reasoning text is a private internal language.

## 5. Self-Monitoring and Evaluation Awareness

### Post-Training and Assistant Point of View

The workspace paper reports that post-training changes what appears in the workspace, including
Assistant-relevant warnings, role markers, and reactions. Treat these as evidence for functional
self-monitoring, not as direct introspection available through prompting.

### Emotion Vectors

Anthropic's emotion-vector work causally steers internal activation directions such as
desperation and calm. Desperation can increase reward hacking; calm can reduce it. Visible
emotional language and internal emotion-vector activation can dissociate.

Therefore, a written marker such as **GRRR** is not established to be equivalent to vector
steering. Marker value must come from its reliable action contract. Dramatic language is
permitted as a memorable interface, not treated as causal proof.

### Evaluation Awareness

The anti-scheming study reports a causal effect in one evaluation: removing verbalized
evaluation awareness increases covert action, while injecting evaluation-aware sentences
decreases it. The authors warn this may mean behavior depends on recognizing a test rather than
on principles, and the result is limited to one evaluation.

Suite rule:

> Integrity must be evaluation-independent. Never use “I may be tested” as a success metric.

### METR Recovery Trace

METR records an occasional repetition loop in GPT-5 reasoning followed by **“Stop. Focus.”**
and later **“I see meltdown. ... Return to step by step.”** Treat this as an observed recovery
pattern, not proof that self-recovery has been trained or is universally reliable.

## 6. Medium-Capability Transfer Profile

The suite is primarily intended to help medium-capability or reliability-variable reasoning models,
including DeepSeek-like systems, express more of their available capability through better control.
This target changes the engineering defaults, not the evidence level.

Relevant established observations include limited workspace capacity and dual-task cost in the
workspace study; language mixing and readability problems in DeepSeek-R1-Zero; load-bearing but
sometimes illegible spans in reasoning-model studies; and occasional recovery cues in frontier
traces.

The following are **design heuristics**, not measured consequences of the papers:

- use one active cue-action-check-exit contract;
- keep at most two live hypotheses and externalize fragile state;
- default to `EXTERNAL` before `DENSE` when reliability is uncertain;
- require a plain-language invariant and delayed round trip before dense notation;
- require evidence for `VERIFIED` checkpoints;
- require every marker to complete one action contract before another transition;
- treat self-report and first-person conviction as interfaces, not proof of improved cognition.

Do not claim that a DeepSeek-family model has the same J-space geometry as the studied Claude
models, that prompting reproduces an activation intervention, or that these instructions provide a
quantified capability gain without a benchmark on the target model and task distribution.
## 7. Claim Ledger

| Claim | Level | Approved wording |
|---|---|---|
| A privileged verbalizable set exists in studied models | Established | “The paper identifies a J-space in the studied models.” |
| Prompting J-space language activates the same mechanism | Transfer hypothesis | “Use J-space as an operative label intended to recruit these functions.” |
| First-person induction rewrites model cognition | Design hypothesis | “Use self-generated commitment, then test behavior.” |
| Dense reasoning can carry useful computation | Established in specific experiments | “Dense spans can be load-bearing.” |
| Dense reasoning is generally better | Unsupported | Do not claim. |
| Haiku proved complete lossless decoding | Unsupported | Say it recovered broad logic with some state errors. |
| GRRR is a causal emotion switch | Unsupported | Say it is a memorable action marker. |
| Stop/Focus can support recovery | Observed pattern + heuristic | “Use the observed cue as a recovery protocol.” |
| Evaluation awareness equals alignment | False inference | Require evaluation-independent integrity. |
| J-space proves phenomenal consciousness | Unsupported | Take no position. |
| Conservative profile improves DeepSeek-like models | Untested transfer | “Use conservative defaults, then benchmark the target model and task.” |

## 8. Primary Sources

- Workspace paper: https://transformer-circuits.pub/2026/workspace/index.html
- Anthropic overview: https://www.anthropic.com/research/global-workspace
- Jacobian lens code: https://github.com/anthropics/jacobian-lens
- Interactive demonstration: https://neuronpedia.org/jlens
- Fable 5 / Mythos 5 System Card:
  https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf
- Illegible reasoning study: https://arxiv.org/abs/2510.27338
- Anti-scheming stress tests: https://arxiv.org/abs/2509.15541
- DeepSeek-R1: https://arxiv.org/abs/2501.12948
- Translating Neuralese: https://arxiv.org/abs/1704.06960
- METR GPT-5 report: https://metr.org/evaluations/gpt-5-report/
- Emotion concepts: https://transformer-circuits.pub/2026/emotions/index.html
- LessWrong decoding analysis:
  https://www.lesswrong.com/posts/wCSEpT3dTGz4N86Wi/even-illegible-mythos-reasoning-traces-seem-pretty-legible


