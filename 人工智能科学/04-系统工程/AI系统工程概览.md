---
title: 人工智能系统工程概览
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能系统工程概览

## 定位

这篇笔记回答的问题是：模型之外，人工智能系统如何被构造、训练、评估、部署、监测、治理和持续迭代。对博士研究与工程实践而言，单个模型页只解释“能力来源”，系统工程页解释“能力如何真正进入现实系统”。

## 一、系统工程的最小闭环

一个完整的 AI 系统至少包含：

1. 数据与数据治理；
2. 目标函数与训练链；
3. 评测与验收；
4. 推理、部署与服务化；
5. 监测、事故处置与再验证；
6. 权限、审计、发布门禁与责任链。

## 二、当前主干页面

- [数据](./data-for-ai-systems.md)
- [预训练、微调与后训练](./pretraining-and-post-training.md)
- [后训练、对齐与偏好优化](./post-training-alignment-and-preference-optimization.md)
- [优化、正则化、课程学习与数据混合设计](./optimization-regularization-curriculum-and-data-mixture-design.md)
- [推理与部署](./inference-serving-and-deployment.md)
- [评测驱动开发](./evaluation-driven-development.md)
- [智能体系统](./agent-memory-task-graphs-and-planner-critic-systems.md)
- [多智能体系统](./multi-agent-systems.md)
- [机器学习系统生命周期、可复现性与闭环迭代](./machine-learning-systems-lifecycle-reproducibility-and-closed-loop-iteration.md)

## 三、为什么系统工程是研究主干而不是附属章节

很多论文只解释模型如何工作，却不解释系统为什么失效。现实中更常见的问题是：

- 数据脏；
- 训练不可复现；
- 指标与目标错配；
- 线上分布漂移；
- 权限和审批流薄弱；
- 事故无法复盘。

因此，系统工程不是“部署人员的事”，而是 AI 研究闭环的一部分。

- 反向传播、优化器、归一化与训练栈

- 强化学习训练循环、基准、评估指标与失败模式

- 大模型训练、推理、对齐与评测栈

- [反向传播、优化器、归一化与训练栈](./backpropagation-optimizers-normalization-and-training-stacks.md)

- [强化学习训练循环、基准、评估指标与失败模式](./reinforcement-learning-training-loops-benchmarks-and-failure-modes.md)

- [大模型训练、推理、对齐与评测栈](./large-model-training-inference-alignment-and-evaluation-stack.md)

## 联读

- [预训练、微调与后训练](./pretraining-and-post-training.md)
- [推理、服务与部署](./inference-serving-and-deployment.md)
- [机器学习系统生命周期、可复现性与闭环迭代](./machine-learning-systems-lifecycle-reproducibility-and-closed-loop-iteration.md)
- [运行时治理、策略执行与安全降级](./runtime-governance-policy-enforcement-and-safe-degradation.md)

## 参考文献

[1] Sculley, D. et al. *Hidden Technical Debt in Machine Learning Systems*. NeurIPS, 2015.
[2] Hazelwood, K. et al. *Applied Machine Learning at Facebook: A Datacenter Infrastructure Perspective*. HPCA, 2018.
[3] 周志华. *机器学习*. 清华大学出版社, 2016.
