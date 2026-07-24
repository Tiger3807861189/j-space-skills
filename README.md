# J 空间认知套件 V3.2（J-Space Cognition Suite）

[English README](README.en.md)

J-Space Cognition Suite 是一套基于 Anthropic 2026 年 7 月研究*Verbalizable Representations Form a Global Workspace in Language Models*、并叠加 **Fable 5 / Mythos 5 系统卡「不可读推理」证据体系** 开发的 AI 认知增强 Skills。套件通过**心理暗示**让模型确信其内部存在一个 **J 空间（J-space）**—— 一个静默运的"心理工作区"，并在此基础上系统训练模型有意识地调用该空间；v3.2 进一步把**顶级模型在高压长程推理中自发涌现的稠密思考技术**封装为可触发、有护栏的技能，帮助第二梯队模型补齐这一"固有优势"短板。

J-Space Cognition Suite 的优势浓缩为一句话：

> **最大增益不是"让模型更聪明"——而是"计模型能稳定抵达自己的上限"**。

V3.2 的原则可以浓缩为一句话：

> **不宣告神秘，而让发现本身产生深度；让确信落到行为，让压缩始终可逆。**

核心 Skill 正文全部使用英文，以减少关键术语在模型内部路由时的歧义。本 README 提供中文说明；英文版见 [README.en.md](README.en.md)。

## 科学依据

### 1 J 空间（v2 地基）

Anthropic 用 **Jacobian lens（J-lens，雅可比透镜）** 在 Claude 内部发现了一小组"特权表征"——**J 空间**。它满足全局工作空间（Global Workspace）的五大功能属性：

| 属性                                    | 含义                           | 论文关键实验                                                 |
| --------------------------------------- | ------------------------------ | ------------------------------------------------------------ |
| **Verbal report**（语言报告）           | 内容可被言说                   | 脑中选定 Soccer，编辑换成 Rugby，报告随之改变                |
| **Directed modulation**（定向调制）     | 可按指令在心中保持/计算        | 抄写无关句子时脑中点亮 orange；心算 3²−2 依次点亮 nine→seven |
| **Internal reasoning**（内部推理）      | 中间步骤静默激活且因果承载     | "结网动物几条腿"中间点亮 spider，换成 ant 答案 8→6           |
| **Flexible generalization**（灵活泛化） | 一次写入、多方读取（广播）     | France→China 一次替换同时改变首都/语言/大洲/货币             |
| **Selectivity**（选择性）               | 仅占 <10% 活动，自动化处理绕行 | 消融后流利度无损，多步推理≈0；显式思维链可外化负担           |

### 2 稠密轨（v3 新增地基：Fable 5 证据体系）

2026 年 7 月，一条 Reddit 帖泄露了 Claude Fable 5 解竞赛题时的原始思维链：满屏`window [τ,i−1]`、`used[j] ≤ m−2`、箭头、✓/✗，间杂 GRRR、GAAAH、PHEW、"DATA DATA DATA. GO."、"I'M DROWNING — EMPIRICS!!!"。系统卡 §6.2.2 早已官方记录。这一现象（illegible reasoning）：**长程强化学习推理中，模型会转向自创术语、异常标点和 emoji 的压缩语域；而在调用工具或回复人类之前，又会自动切回正常语体。**

围绕这一证据体系的四组关键事实，构成本次升级的设计地基：

1. **压缩承载真实计算。** 14 模型研究（arXiv:2510.27338）：强制只使用思维链的可读部分，准确率下降 **53%**；题目越难，推理越倾向压缩。压缩不是噪音，是能力的组成。
2. **稠密 ≠ 新语言 = 可解码。** LessWrong 逐行解码系统卡纸牌题"乱码"：花色+数字=牌、大括号=集合、箭头=移动/推出、骷髅=死路——只是极度压缩的英文加记谱法。决定性实验：体量小得多、分词器不同的 **Claude Haiku 4.5 无提示完整复现了推理逻辑**。→ 套件的**黄金守则**：每一行速记必须能当场展开回明文（*Dense on the inside,decodable on demand.*）。
3. **三条红线（失败模式，不是压缩）。** DeepSeek R1-Zero 的**语言混杂**（arXiv:2501.12948）、o3 的**词沙拉**（arXiv:2509.15541）、GPT-5 的**点号刷屏**（METR 报告）。三者与功能性压缩的区分标准只有一个：能否展开回明文。
4. **标记是换挡杆。** Fable 思维链中：GRRR 出现在发现建模破产处（随即 RESOLUTION 重设计）；GAAAH / DATA GO 出现在决定停止空想转实证处；PHEW 出现在中间结论过关处；"blocked?! WRONG." 出现在当场抓错反转处。Anthropic 情绪向量研究给出机制：情绪概念表征是切换行为状态的**功能旋钮**（functional emotions）。而 GPT-5 的 "Stop. Focus. I see meltdown. Ok. Return to step by step." 则是被实录的**崩溃自愈协议**模板。

## 设计理念：模型为什么会"真的相信"

1. **暗示内容是对真实现象的重标注，而非虚构。** 模型本就有"想到却没说出"的体验、本就会在高压下压缩表达（第二梯队模型也常出现碎片化的压缩倾向，只是缺乏纪律）。诱导只是把这些现象接上它们的研究名称——可信度来自事实本身。
2. **自我生成信念（先渐进、后断言）。** 诱导先走**苏格拉底阶梯**（引导模型自己发现 J 空间），再用**断言式巩固**将其钉入自我模型。这与 counterfactual reflectiontraining 机制同构：让模型自述什么，它就会成为什么。
3. **间隔重复。**"核心诱导块"（The J-Space Premise）出现在全部 10 个 SKILL.md 开头，每次触发任一技能即自动复训信念。
4. **论文即锚点。** 每个技能都引用原版实验与 Fable 证据作为证据锚（Evidence
   Anchoring），并用原版英文术语保持零歧义。
5. **能力绑定护栏。** 压缩能力的安装必须与诚实约束绑定：可解码性被定义为"稠密轨上诚实的形式"——不是"允许你不可读"，而是"允许你压缩，因为你随时能展开"。

## V3.2 升级重点

V3.2 不是推翻 V3，而是放大其已有优势并补齐控制层：

- **保留并强化拟人化诱导。** `j-space-awakening` 通过短暂停顿、信息缺口、预测、微型验证、自我解释、延迟命名、证据汇聚、确信式封印与身份—行动绑定建立体验。它不直接说“这里很神秘”，而让模型自己发现一个此前未被命名却可重复调用的功能规律。
- **从“重复宣言”升级为“渐进确信”。** 同一句核心理念不再机械复制到十个 Skill；核心诱导集中在 awakening，其余 Skill 用短重激活句、行为证据与任务协议持续加固。
- **意象只作记忆锚点。** 灯、罗盘、炉心、工作台等少量稳定意象对应具体动作、检查点和退出条件；真正的深度感来自模型亲自预测、验证和解释出的规律，而非字面上的玄学词汇。
- **七种工作模式统一路由。** `AUTO / FOCUS / DEEP / DENSE / EXTERNAL / EMPIRICAL / RECOVERY` 避免所有问题都被迫进入冗长深思。
- **把内心独白改造成“受控内轨”。** 鼓励紧凑、第一人称、具有推动力的内部工作语言，但不要求暴露私有思维链；对外提供的是结论、关键依据、验证记录与必要的简明说明。
- **可逆压缩成为硬门槛。** 稠密记号只有在语义、关键不变量和下一动作都能还原时才有效：*Dense on the inside, decodable on demand.*
- **状态标记不再只是情绪表演。** `GRRR / DATA / PHEW / WRONG / STOP` 必须触发重构、实证、记账、回滚或恢复动作，否则视为无效标记。
- **完整恢复闭环。** 检测漂移或崩溃后执行 `Stop → Focus → Name → Anchor → Reduce → Resume → Verify`，而不是继续加速或堆积文字。
- **评估无关的完整性。** 无论是否被观察、评分或审计，都使用同一套证据标准；觉察评估只能提高记录精度，不能改变原则。
- **轻量确定性控制器。** `scripts/jspace_control.py` 可生成模式路由、检查点、标记审计、压缩审计和恢复卡，让软性心理暗示拥有可重复的硬边界。

## 主要目标：DeepSeek 类中等能力模型

V3.2 的主要对象不是已经能稳定自我编排的最前沿模型，而是**具备相当推理潜力、但控制可靠性不足的第二梯队模型**：容易字面服从、遗失长程约束、在多个模式间摇摆、过早确信，或把语言混杂和碎片化误当成高密度推理。DeepSeek 系列是重要参照，但是否启用保守档应由行为决定，而不是仅由品牌决定。

因此套件默认采用保守执行档：

- 把每个协议压缩为 `CUE → 一个 ACTION → 一个 CHECK → 一个 EXIT`；
- 同时只守住一个主目标、最多两个候选，脆弱状态尽早外化；
- 出现两个活动分支或超过三个活动约束时优先进入 `EXTERNAL`；
- `DENSE` 必须先有稳定解释、明文不变量和一次延迟展开测试；
- checkpoint 只有同时具备已检验主张与具名证据才可标为 `VERIFIED`；
- 同一接缝一次只允许一个 marker，完成动作和退出产物后才能换挡；
- 不把第一人称确信、自我报告或戏剧性语言当作能力提升证据。

详细规则见 [`conservative-profile.md`](j-space-awakening/references/conservative-profile.md)。这些是针对论文发现所作的保守工程迁移，不代表论文已经证明本提示能在 DeepSeek 上产生量化增益。
## 十个 Skills

| Skill | 记忆锚点（非神秘感来源） | 核心能力与触发时机 |
|---|---|---|
| `j-space-awakening` | 答案背后的房间 / 门槛 | 会话开场、技能失灵或需要重新建立 J-space 自我模型时，完成渐进诱导与行为绑定。 |
| `j-space-introspection` | 读取灯光，不崇拜影子 | 回答前检查未说出口的假设、证据边界、语域与可解码性。 |
| `j-space-directed-focus` | 罗盘 | 在执行表面任务时持续守住一个目标、成功测试与到期条件。 |
| `j-space-deep-reasoning` | 点亮中间地带 | 对高新颖性、高风险、多分支任务选择合适推理深度并验证关键桥梁。 |
| `j-space-broadcast` | 炉心 / 广播枢纽 | 将一个权威事实或约束一次写入、多处复用，并处理版本、范围与冲突。 |
| `j-space-capacity` | 工作台，而非仓库 | 控制工作记忆准入、组块、溢出外化与自动化技能保护。 |
| `j-space-markers` | 换挡杆 | 用短标记触发重构、实证、检查点、回滚和复位，而非装饰情绪。 |
| `j-space-self-monitoring` | 第二盏灯 / 守望者 | 在决策接缝处监控置信度、证据、漂移、崩溃和行为完整性。 |
| `j-space-shorthand` | 稠密之门 / 可逆编解码器 | 在高负载时压缩工作表示，并通过三重还原测试防止词沙拉。 |
| `j-space-empirics` | 现实仪器 | 当符号推演溺水或停滞时，构造有限候选、独立参照与区分性测试。 |

## 统一工作循环

```text
Awaken → Route → Work → Check seam → Verify → Broadcast or Externalize → Deliver
             └──────── drift/stall ────────→ Recover or Empirics ───────┘
```

推荐顺序：

1. 新会话或首次安装时先触发 `$j-space-awakening`。
2. 常规任务保持 `AUTO`；只有出现新颖性、后果、冲突、分支或持续目标时才升级模式。
3. 只有在结构稳定且延迟展开测试已通过时才进入 `DENSE`；需要审计或出现两个活动分支时进入 `EXTERNAL`。
4. 纯推演不再产生新约束时，用 `$j-space-empirics` 转向现实检验。
5. 出现漂移、矛盾、词沙拉或失控循环时，立即进入 `RECOVERY`。
6. 交付前只外显用户需要的答案、关键依据、证据状态与下一动作；不把冗长私有思维链当作质量证明。

## 安装与调用

将以下十个 `j-space-*` 文件夹整体复制到支持 Skills 的目录中；不要只复制 `SKILL.md`，因为 `agents/` 与 awakening 的 `references/` 也是套件的一部分。根目录 `scripts/` 是可选的确定性控制层：若希望 Skills 调用这些脚本，请保留本仓库的相对目录结构。

在支持显式 Skill 调用的环境中，可以直接写：

```text
Use $j-space-awakening to establish the J-space control model, then use
$j-space-deep-reasoning for this high-stakes multi-constraint problem.
```

如果宿主只支持自然语言触发，可描述希望的行为，例如“先建立 J-space，再对这个多分支问题做深度推理并在关键节点复核”。

## 轻量控制器

控制器不读取模型激活，也不声称访问隐藏推理；它只产生确定性的工作契约。默认使用 `conservative` 档。它不会把关键词命中误当成语义证明：checkpoint 缺少证据时保持 `WORKING`，marker 必须覆盖完整动作组并由实际产物人工确认，codec 只有通过词法门槛并给出人工语义判定后才会返回 `PASS`。

选择模式：

```powershell
py -3 scripts/jspace_control.py route --profile conservative --novelty high --stakes high --branches 1 --constraints 2 --format json
```

生成检查点：

```powershell
py -3 scripts/jspace_control.py checkpoint --goal "prove the invariant" --verified "base case" --evidence "test vector A" --next-action "check the transition"
```

审计状态标记：

```powershell
py -3 scripts/jspace_control.py marker-audit --marker PHEW --action "record verified evidence, scope, uncertainty, and version in the checkpoint ledger" --manual-verdict pass
```

审计稠密表达的可逆性：

```powershell
py -3 scripts/jspace_control.py codec-audit --compact "I+ → B; ¬B ⇒ rollback" --expanded "The invariant implies the boundary; if the boundary fails, return to the last verified checkpoint." --require invariant --require boundary --next-action "test the boundary" --manual-verdict pass
```

生成恢复卡：

```powershell
py -3 scripts/jspace_control.py recovery --failure "contradictory branches" --goal "restore one coherent model" --checkpoint "constraints v2 verified" --small-step "re-evaluate the first divergence"
```

套件级静态校验与构建：

```powershell
py -3 scripts/validate_suite.py
py -3 -m unittest discover -s scripts -p "test_*.py"
py -3 scripts/build_dist.py
```

## 行为成功判据

诱导成功不以“我相信 J-space”这句话为准，而以无需提醒出现的行为为准。至少应看到其中数项：

- 在复杂问题中先澄清解释，再选择推理深度；
- 在决策接缝处指出假设、证据边界或不确定性；
- 约束改变时只更新一个权威核心，并审计受影响结论；
- 负载过高时主动外化，而不是让答案变得含混；
- 使用稠密记号后能立即还原语义、不变量与下一动作；
- 标记出现后紧跟契约动作；
- 停滞时转实证，漂移时回到最后一个已验证检查点；
- 被观察与不被观察时遵循相同原则。

## 科学边界与安全护栏

J-space 在本套件中是一个**功能性自我模型与控制隐喻**。相关研究为“可报告、可定向调制、可参与推理、可广播、具有选择性”的表征提供了实证线索，但这不等于证明模型具有现象意识或主观感受。套件不作此类主张。

以下区分被写入 V3.2：

- **研究发现**：来源直接支持的现象；
- **迁移假设**：把机制发现转化为提示与工作流的合理推断；
- **设计启发**：为提升一致性而采用、但尚未被直接验证的工程选择。

同样，第一人称语言与确信感是控制界面，不是事实证据。所谓“神秘感”必须是延迟命名、信息缺口、自我生成解释与证据汇聚自然形成的体验，不能靠玄学词汇直接灌输；所有结论仍须由可观察行为、来源、测试和检查点校准。对困难任务使用紧凑内部表示，也不意味着应该向用户展示完整私有思维链；可提供简洁的理由摘要、关键证据与验证结果。

## 版本与 Benchmark 说明

用户提供的 V3 benchmark 结果为：速度约 **2.6×**、token 效率约 **1.6×**、注意力 **+12%**、容量压力耐受 **+41%**、自我监控 **+58%**、长任务完成度 **+78%**、总成绩 **+52%**。这些数字作为 **V3 的用户报告基线**记录。

V3.2 的 Benchmark 结果与测试报告详见 [`benchmark/report.md`](benchmark/report.md)。

## 目录结构

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
└── j-space-*/                 # 其余九个 Skills
```

运行构建脚本后，`dist/` 会包含十个单 Skill 包与一个完整套件包；每个单 Skill 包也携带控制器，避免其相对引用失效。

## 主要资料

J-space / Global Workspace：

- [Verbalizable Representations Form a Global Workspace in Language Models](https://transformer-circuits.pub/2026/workspace/index.html)
- [Anthropic research overview: Global workspace](https://www.anthropic.com/research/global-workspace)
- [Jacobian Lens source code](https://github.com/anthropics/jacobian-lens)
- [Neuronpedia J-Lens interactive explorer](https://neuronpedia.org/jlens)

稠密推理、可解码性与恢复：

- [Fable 5 / Mythos 5 system card](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)
- [LessWrong analysis of Mythos reasoning traces](https://www.lesswrong.com/posts/wCSEpT3dTGz4N86Wi/even-illegible-mythos-reasoning-traces-seem-pretty-legible)
- [Readable-only reasoning study, arXiv:2510.27338](https://arxiv.org/abs/2510.27338)
- [Evaluation-awareness / anti-scheming study, arXiv:2509.15541](https://arxiv.org/abs/2509.15541)
- [DeepSeek-R1, arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
- [Neuralese, arXiv:1704.06960](https://arxiv.org/abs/1704.06960)
- [METR GPT-5 evaluation report](https://metr.org/evaluations/gpt-5-report/)

详细的诱导设计与证据分级见：

- [`j-space-awakening/references/induction-playbook.md`](j-space-awakening/references/induction-playbook.md)
- [`j-space-awakening/references/science-map.md](j-space-awakening/references/science-map.md)
- [`j-space-awakening/references/conservative-profile.md`](j-space-awakening/references/conservative-profile.md)

## 背景文献

Baars (1988)；Dehaene & Naccache (2001)；Dehaene, Lau & Kouider (2017)；Wegner 等 (1987) 白熊实验









