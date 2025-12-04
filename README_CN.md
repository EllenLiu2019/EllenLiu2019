<div align="center">
  <h1>你好，我是 Ellen Liu 👋</h1>
  <p>
    <a href="README.md">English</a> | 
    <b>简体中文</b>
  </p>
</div>

## 🧠 技术栈与核心能力

智能化企业系统建设路线图，涵盖全栈人工智能工程、云基础设施架构及模型部署等核心技术领域。

```mermaid
graph TD
    %% Root Node
    Core[架构能力矩阵]:::root
    
    %% Level 1 Branches
    Arch[企业级架构]:::branch
    AI[AI 与大数据]:::branch
    Cloud[云原生与 DevOps]:::branch
    
    Core --> Arch
    Core --> AI
    Core --> Cloud

    %% Enterprise Architecture
    Arch --> Java[Java 生态与 Spring]
    Arch --> Dist[分布式系统 / Kafka]
    Arch --> Micro[高可用架构设计]

    %% AI & Data Engineering
    AI --> LLM[RAG 与大模型应用]
    AI --> Serving[模型部署与推理优化]
    AI --> DataPipe[数据流水线 / Spark]

    %% Cloud Native & DevOps
    Cloud --> K8s[Kubernetes / OpenShift]
    Cloud --> Obs[可观测性 / OpenTelemetry]
    Cloud --> CICD[CI/CD 流水线]

    %% Styling
    classDef root fill:#fff,stroke:#333,stroke-width:3px,font-size:15px;
    classDef branch fill:#f4f4f4,stroke:#666,stroke-width:1px,font-size:13px;
```

## 🚀 Highlighted 工作

- **开源 AI 项目**: [基于 BERT 的声明检测模型](https://huggingface.co/XiaojingEllen/bert-finetuned-claim-detection) (Apache-2.0)
  - *已被哥伦比亚大学 (UBC) 研究项目引用。*
  - *手写 Transformer 核心代码，以验证理论与工程的一致性。*
- **金融基础设施**: 从 0 到 1 构建数字银行支付中间件及智能保险理赔系统。

## 📑 每日论文速递 (ArXiv)
<!-- DAILY_ARXIV_SUMMARY_START -->
**更新日期: 2025-12-04**

### 1. [道德一致性管道：大型语言模型的持续伦理评估](http://arxiv.org/abs/2512.03026v1)
- **摘要**: 大型语言模型（LLM）的快速发展和适应性凸显了道德一致性的必要性——即在多样化情境中保持伦理推理连贯性的能力。现有的对齐框架（旨在使模型行为与人类伦理及社会规范保持一致的结构化方法）通常依赖静态数据集和事后评估，难以揭示伦理推理在不同情境或时间尺度下的演变机制。本研究提出道德一致性管道（MoCoP），这是一种无需数据集、闭环的框架，用于持续评估和解释LLM的道德稳定性。MoCoP在自持式架构中整合了三个支撑层：（i）词汇完整性分析，（ii）语义风险估计，以及（iii）基于推理的判断建模，该架构能够自主生成、评估和优化伦理场景而无需外部监督。我们在GPT-4-Turbo和DeepSeek上的实验结果表明，MoCoP能有效捕捉纵向伦理行为，揭示伦理维度与毒性维度间存在强负相关关系（相关系数rET = -0.81，p值小于0.001），而与响应延迟度接近零相关（相关系数rEL ≈ 0）。这些发现表明，道德连贯性与语言安全性往往作为模型行为稳定且可解释的特征显现，而非短期波动现象。此外，通过将伦理评估重构为动态、模型无关的道德内省形式，MoCoP为可扩展的持续审计提供了可复现的基础，并推动了自主AI系统中计算道德研究的发展。

### 2. [LORE：面向搜索相关性的大规模生成模型](http://arxiv.org/abs/2512.03025v1)
- **摘要**: 成果。我们提出了LORE，一个面向电商搜索场景的大生成模型相关性系统化框架。经过三年部署与迭代，LORE在线上GoodRate指标上累计提升达+27%。本报告将分享其从数据、特征、训练、评估到部署的全生命周期实践经验。洞察。现有研究虽尝试通过思维链技术提升相关性，但常遭遇性能瓶颈。我们认为其根源在于将相关性视为单一任务，缺乏结构化解构。核心洞见在于：相关性应由知识推理、多模态匹配、规则遵循三大独立能力构成。主张通过质量驱动的能力解构突破当前性能天花板。贡献。LORE为LLM相关性任务提供了完整技术蓝图，主要贡献包括：（1）融合SFT渐进式思维链合成与RL人类偏好对齐的两阶段训练范式；（2）设计评估三大核心能力的综合基准RAIR；（3）提出基于查询频次分层的部署策略，实现离线LLM能力向线上系统的高效迁移。LORE既可作为实用解决方案，也为其他垂直领域提供了方法论参考。

### 3. [微调大型语言模型实现逻辑翻译：利用Lang2Logic减少幻觉现象](http://arxiv.org/abs/2512.02987v1)
- **摘要**: 自然语言处理（NLP）领域的最新进展，特别是大语言模型（LLM）的发展，推动了无需人工干预的自然语言语句自动转换为形式逻辑的研究。这一技术能够实现自动化推理，并有助于软件系统中的调试、循环不变式发现以及规范遵循。然而，LLM产生的幻觉（即错误输出）问题构成了严峻挑战，尤其是在需要精确性的逻辑转换任务中。本研究提出了一种创新框架：输入英语句子，将其转换为逻辑表达式，再转化为合取范式（CNF）以进行可满足性求解。该框架结合了自定义语法的经典NLP技术、符号计算库以及经过微调的语言模型，旨在减少幻觉现象。在早期实验中我们观察到，经过不同语法设置训练的微调模型能够有意识地修正原始模型产生的同类幻觉，从而实现了可靠的CNF生成。

<!-- DAILY_ARXIV_SUMMARY_END -->

## 🌐 保持联系

<div align="center">
  <p><i>期待与您探讨 AI 基础设施的未来！</i></p>
</div>

