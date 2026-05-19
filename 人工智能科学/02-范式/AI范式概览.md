---
title: 人工智能范式概览
layer: 02-paradigms
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能范式概览

## 1. 定位

这篇笔记负责建立人工智能不同历史阶段和学习范式之间的总关系图。它重点回答：

- AI 研究中的“范式”到底指什么；
- 符号主义、统计学习、深度学习、强化学习、生成式 AI、agentic AI 之间不是简单替代，而是怎样叠加与分化；
- 为什么 02 文件夹应该被读成“学习与推理组织方式”的演化史。

## 2. 什么是范式

在这个知识库中，范式不是单一算法名，而是对以下问题的一整套回答：

1. 知识是什么；
2. 学习信号从哪里来；
3. 推理如何进行；
4. 决策如何组织；
5. 模型怎样进入真实系统。

## 3. 主要范式

### 3.1 符号主义

强调显式知识表示、逻辑规则、可解释推理与组合结构。

### 3.2 专家系统

将领域知识工程化，是符号主义的重要工程形态。

### 3.3 统计学习 / 概率主义

把学习问题建模为从数据中估计统计规律、后验分布或决策规则。

### 3.4 连接主义 / 深度学习

通过多层可训练表示替代大量手工特征与规则工程。

### 3.5 强化学习 / 序贯决策范式

将智能理解为在环境中交互、探索、延迟反馈和长期优化。

### 3.6 生成式与基础模型范式

将大规模预训练、自监督、多模态对齐、后训练和部署组织成通用能力层。

### 3.7 agentic AI

将模型扩展为能调用工具、管理记忆、规划执行、接受审批与运行时治理的系统主体。

## 4. 为什么这些范式不是线性替代关系

更合理的看法是：

- 旧范式并未消失，而是被吸收到新系统中；
- foundation model 时代仍需要符号结构、统计推断、控制与规划；
- agent 系统常常同时调用表示学习、检索、推理、规划、策略优化与运行时治理。

## 5. 当前主线阅读图

### 5.1 表征与基础模型主线

`连接主义 -> 深度学习 -> 自监督 / 多模态预训练 -> foundation model -> 后训练 / 部署 / agent`

### 5.2 决策与交互主线

`统计决策 -> 强化学习 -> 深度 RL -> model-based RL -> 多智能体 / agentic decision-making`

### 5.3 知识与推理主线

`符号主义 -> 专家系统 -> 概率图模型 / 统计推断 -> reasoning + tool-augmented system`

## 6. 当前文件夹中的关键桥页

- [从表征学习到基础模型：深度学习主线总论](./deep-learning-from-representation-to-foundation-models.md)
- [基础模型范式：预训练、适配与部署](./foundation-model-paradigm-pretraining-adaptation-and-deployment.md)
- [从监督学习到自监督与多模态预训练：学习范式迁移图](./learning-paradigms-from-supervised-to-self-supervised-and-multimodal-pretraining.md)
- [从 MDP 到深度强化学习：强化学习主线总论](./reinforcement-learning-from-mdp-to-deep-rl.md)
- [智能体](./agentic-ai.md)

## 7. 建议阅读策略

### 路径一：历史顺序

先看符号主义、专家系统、统计学习、连接主义，再进入现代范式。

### 路径二：现代系统顺序

先看深度学习 / foundation model，再看强化学习、agent 与系统工程。

### 路径三：研究选题顺序

- 做表示与预训练：重点看深度学习、self-supervision、foundation model；
- 做控制、决策、多智能体：重点看强化学习与 agent；
- 做高风险系统：重点看 foundation model 与运行时治理的连接。

## 8. 继续阅读

- [基础理论入口页](../01-foundations/README.md)
- [模型体系入口页](../03-model-families/README.md)
- [系统工程入口页](../04-systems-engineering/README.md)

- [机器学习：从特征工程到端到端学习](./machine-learning-from-feature-engineering-to-end-to-end-learning.md)

- 大模型技术：从基础模型到工具使用型智能体

- 具身智能与世界约束下的决策范式

- 统计机器学习：从 ERM 到贝叶斯与结构化预测

- [统计机器学习：从 ERM 到贝叶斯与结构化预测](./statistical-machine-learning-from-erm-to-bayesian-and-structured-prediction.md)

- [大模型技术：从基础模型到工具使用型智能体](./large-model-technology-from-foundation-models-to-tool-using-agents.md)

- [具身智能与世界约束下的决策范式](./embodied-intelligence-and-world-grounded-decision-making.md)
