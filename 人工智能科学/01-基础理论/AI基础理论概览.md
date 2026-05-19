---
title: 人工智能基础理论概览
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 人工智能基础理论概览

## 1. 定位

这篇笔记不是简单罗列数学先修课，而是为人工智能科学建立一张**稳定理论总图**，回答：

- AI 背后到底有哪些真正长期有效的理论支柱；
- 为什么现代系统工程、foundation model、scientific agent 和高风险治理仍然要回到基础理论；
- 01 文件夹内部应如何阅读。

## 2. 这条主线研究什么

人工智能的基础理论并不等于“只看数学公式”，它研究的是：

1. **如何表示问题**：状态、变量、图结构、函数、轨迹、知识；
2. **如何从数据中学习**：统计学习、泛化、优化、表征；
3. **如何处理不确定性**：概率、估计、校准、推断、漂移；
4. **如何进入动态系统**：控制、强化学习、world model、可微分仿真；
5. **如何把结构写进模型**：几何、对称性、归纳偏置、因果与机制不变性。

## 3. 当前板块结构

### 3.1 数学、统计与经典理论底座

- 搜索、优化与启发式方法；
- 图论与图结构基础；
- 概率、统计与统计学习；
- 信息论；
- 泛化与学习理论。

### 3.2 深度学习桥接理论

- 优化、尺度扩展与泛化；
- 表征学习、自监督学习与迁移；
- 几何、对称性、不变性与归纳偏置；
- 因果性、分布偏移与 OOD 泛化。

### 3.3 强化学习与动态系统桥接理论

- 强化学习中的探索、信用分配、离线学习与模型化方法；
- 动态系统、估计与控制；
- 不确定性量化、校准与可验证推断。

### 3.4 科学系统桥接理论

- 神经算子；
- 物理引导学习；
- 可微分仿真；
- 科学机器学习中的结构约束。

## 4. 为什么这一层越来越重要

在小模型、封闭任务时代，很多系统问题可以暂时被“工程调参”掩盖；在 foundation model、scientific agent、AI 航天和高风险部署时代，理论问题重新变成系统问题：

- calibration 失效会直接影响发布门禁；
- distribution shift 会影响部署可靠性；
- 几何结构与归纳偏置会决定样本效率；
- 动态系统视角会影响控制、规划和多智能体协同；
- 不确定性估计会影响审批流、runtime governance 与 safe degradation。

## 5. 建议阅读路径

### 路径一：先搭底座

- [概率、统计与统计学习](./probability-statistics-and-statistical-learning.md)
- [人工智能中的信息论](./information-theory-for-ai.md)
- [泛化与学习理论](./generalization-and-learning-theory.md)

### 路径二：深度学习桥页

- [深度学习中的优化、尺度扩展与泛化](./optimization-scaling-and-generalization-in-deep-learning.md)
- [表征学习、自监督学习与迁移](./representation-learning-self-supervision-and-transfer.md)
- [几何、对称性、不变性与归纳偏置](./geometry-symmetry-invariance-and-inductive-bias.md)
- [因果性、分布偏移与分布外泛化](./causality-distribution-shift-and-out-of-distribution-generalization.md)

### 路径三：动态系统与强化学习桥页

- [强化学习基础：探索、信用分配、离线强化学习与模型化方法](./reinforcement-learning-foundations-exploration-credit-assignment-and-offline-rl.md)
- [动态系统、估计与控制：人工智能的另一条理论主线](./dynamical-systems-estimation-and-control-for-ai.md)
- [不确定性量化、校准与可验证推断](./uncertainty-quantification-calibration-and-verifiable-inference.md)

### 路径四：科学系统桥页

- [神经算子、物理引导学习与可微分仿真](./neural-operators-physics-informed-learning-and-differentiable-simulation.md)
- [科学机器学习中的物理约束学习](./scientific-machine-learning-and-physics-constrained-learning.md)

## 6. 与其他层的关系

- 向上连接 [02 范式层](../02-paradigms/overview-of-ai-paradigms.md)：回答“这些理论服务于哪类学习范式”；
- 向右连接 [03 模型层](../03-model-families/overview-of-ai-model-families.md)：回答“这些理论如何进入具体模型”；
- 向下连接 [04 系统工程](../04-systems-engineering/overview-of-ai-systems-engineering.md)：回答“理论如何转化为训练、部署、监测与治理流程”。

- [目标函数、风险最小化与正则化](./objective-functions-risk-minimization-and-regularization.md)

- 统计决策理论、贝叶斯方法与学习原理

- 反向传播、损失函数、激活函数与梯度下降

- Bellman 方程、动态规划与时序差分学习

- [统计决策理论、贝叶斯方法与学习原理](./statistical-decision-theory-bayes-and-learning-principles.md)

- [反向传播、损失函数、激活函数与梯度下降](./backpropagation-loss-functions-activation-functions-and-gradient-descent.md)

- [Bellman 方程、动态规划与时序差分学习](./bellman-equations-dynamic-programming-and-temporal-difference-learning.md)

- [优化理论（Optimization Theory）：凸性、一阶方法、对偶与机器学习中的训练原理](./optimization-theory-convexity-first-order-methods-and-duality.md)
