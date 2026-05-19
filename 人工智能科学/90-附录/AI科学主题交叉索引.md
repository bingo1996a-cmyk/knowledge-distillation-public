---
title: 人工智能科学跨专题索引表
layer: 90-appendices
tags:
  - evaluation
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能科学跨专题索引表

## 用途

这份索引表用于解决一个常见问题：

同一个研究主题，往往同时散落在基础理论、模型族、系统工程、应用和治理多个分区里。若没有交叉索引，读者很容易只能看到局部页面，而看不到完整主线。

## 一、按研究问题组织的交叉索引

### 1. 多智能体协同与信用分配

- 理论：
  - [期望、估计、不确定性与推断](../01-foundations/uncertainty-estimation-and-inference.md)
  - [动态系统、估计与控制：人工智能的另一条理论主线](../01-foundations/dynamical-systems-estimation-and-control-for-ai.md)
- 范式：
  - [强化学习](../02-paradigms/reinforcement-learning.md)
  - [深度强化学习](../02-paradigms/deep-reinforcement-learning.md)
- 系统工程：
  - [多智能体系统](../04-systems-engineering/multi-agent-systems.md)
  - [多智能体系统中的博弈、通信、协调与信用分配](../04-systems-engineering/multi-agent-games-communication-coordination-and-credit-assignment.md)
  - [多智能体 CTDE、价值分解与反事实信用分配](../04-systems-engineering/multi-agent-ctde-value-decomposition-and-counterfactual-credit.md)
- 应用：
  - [控制科学与工程中的人工智能：总论](../06-applications/control-science-and-engineering-overview.md)
  - [智能控制](../06-applications/intelligent-control.md)

### 2. scientific agent 与科研自动化

- 理论：
  - [科学机器学习中的物理约束学习](../01-foundations/scientific-machine-learning-and-physics-constrained-learning.md)
  - [神经算子、物理引导学习与可微分仿真](../01-foundations/neural-operators-physics-informed-learning-and-differentiable-simulation.md)
- 模型：
  - [世界模型](../03-model-families/world-models.md)
  - [持续交互智能体与世界建模](../03-model-families/interactive-agents-and-continual-world-modeling.md)
- 系统工程：
  - [检索增强、工具调用与记忆系统](../04-systems-engineering/retrieval-augmentation-tool-use-and-memory.md)
  - [智能体记忆、任务图与 planner-critic 系统](../04-systems-engineering/agent-memory-task-graphs-and-planner-critic-systems.md)
  - [智能体审批流、权限控制与 guardrails](../04-systems-engineering/agent-approval-flows-permissioning-and-guardrails.md)
- 应用：
  - [人工智能在科学发现中的应用](../06-applications/ai-for-scientific-discovery.md)
  - [scientific agent 与实验自动化](../06-applications/scientific-agents-and-experiment-automation.md)
- 治理：
  - [AI TEVV：测试、评估、验证与确认](../07-evaluation-safety-governance/ai-testing-evaluation-verification-and-validation.md)

### 3. 高风险 AI 的治理与发布

- 系统工程：
  - [对齐审计、隐藏目标与目标漂移](../04-systems-engineering/alignment-audit-and-hidden-objectives.md)
  - [智能体评测、可观测性与审计](../04-systems-engineering/agent-evaluation-observability-and-auditing.md)
  - [智能体审批流、权限控制与 guardrails](../04-systems-engineering/agent-approval-flows-permissioning-and-guardrails.md)
- 治理：
  - [评测、红队测试与风险分级](../07-evaluation-safety-governance/evaluation-red-teaming-and-risk-tiering.md)
  - [AI TEVV：测试、评估、验证与确认](../07-evaluation-safety-governance/ai-testing-evaluation-verification-and-validation.md)
  - [模型卡、系统卡与发布门禁](../07-evaluation-safety-governance/model-cards-system-cards-and-release-gates.md)
- 附录：
  - [红队工单与审计日志模板](./red-team-ticket-and-audit-log-templates.md)

### 4. 复杂系统与协同决策支持

- 系统工程：
  - [多智能体系统中的博弈、通信、协调与信用分配](../04-systems-engineering/multi-agent-games-communication-coordination-and-credit-assignment.md)
  - [多智能体 CTDE、价值分解与反事实信用分配](../04-systems-engineering/multi-agent-ctde-value-decomposition-and-counterfactual-credit.md)
  - [智能体审批流、权限控制与 guardrails](../04-systems-engineering/agent-approval-flows-permissioning-and-guardrails.md)
- 治理：
  - [AI TEVV：测试、评估、验证与确认](../07-evaluation-safety-governance/ai-testing-evaluation-verification-and-validation.md)
  - [模型卡、系统卡与发布门禁](../07-evaluation-safety-governance/model-cards-system-cards-and-release-gates.md)

## 二、按方法组织的交叉索引

### 1. 世界模型 / 环境建模

- [世界模型](../03-model-families/world-models.md)
- [持续交互智能体与世界建模](../03-model-families/interactive-agents-and-continual-world-modeling.md)
- [scientific agent 与实验自动化](../06-applications/scientific-agents-and-experiment-automation.md)
- [具身智能与 Physical AI](../06-applications/embodied-intelligence-and-physical-ai.md)

### 2. 物理约束学习 / SciML

- [神经算子、物理引导学习与可微分仿真](../01-foundations/neural-operators-physics-informed-learning-and-differentiable-simulation.md)
- [科学机器学习中的物理约束学习](../01-foundations/scientific-machine-learning-and-physics-constrained-learning.md)
- [人工智能在天气、气候与物理建模中的应用](../06-applications/ai-for-weather-climate-and-physical-modeling.md)
- [人工智能在科学发现中的应用](../06-applications/ai-for-scientific-discovery.md)

### 3. 发布门禁 / 审计 / 风险分级

- [评测驱动开发](../04-systems-engineering/evaluation-driven-development.md)
- [智能体评测、可观测性与审计](../04-systems-engineering/agent-evaluation-observability-and-auditing.md)
- [对齐审计、隐藏目标与目标漂移](../04-systems-engineering/alignment-audit-and-hidden-objectives.md)
- [AI TEVV：测试、评估、验证与确认](../07-evaluation-safety-governance/ai-testing-evaluation-verification-and-validation.md)
- [模型卡、系统卡与发布门禁](../07-evaluation-safety-governance/model-cards-system-cards-and-release-gates.md)

## 三、使用建议

### 1. 先按问题走，再按方法补

如果你是从研究问题出发，优先使用“按研究问题组织”的索引；若你已经确定要研究某类方法，再用“按方法组织”的索引补足上下游。

### 2. 每读一个应用页，至少回看一页理论和一页治理

这样更容易避免只看到“能做什么”，却忽略“为什么成立”和“如何约束”。

### 3. 开题前先画自己的交叉索引

对博士研究而言，真正重要的是把自己的题目映射进这张交叉表，而不是只读某一条单线文献。
