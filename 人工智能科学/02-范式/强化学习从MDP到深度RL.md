---
title: 从 MDP 到深度强化学习：强化学习主线总论
layer: 02-paradigms
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 从 MDP 到深度强化学习：强化学习主线总论

## 定位

这一页把强化学习（Reinforcement Learning, RL）组织成一条课程级主线：

`MDP -> value / policy -> actor-critic -> deep RL -> offline RL -> model-based RL -> MARL`

它的目标不是罗列算法，而是把强化学习中最经常被拆散讨论的问题重新连起来：

- 序贯决策的数学结构；
- 探索与信用分配；
- 样本效率与分布偏移；
- 安全约束与现实部署；
- 单智能体到多智能体、再到控制与具身系统的过渡。

## 一、概念边界

强化学习处理的是：  
**智能体如何在环境中通过交互学习策略，以最大化长期累积回报。**

与监督学习相比，它的难点不是标签缺失，而是：

- 回报延迟；
- 观测部分可见；
- 动作会改变未来数据分布；
- 探索具有成本；
- 在线试错可能危险。

## 二、形式化起点：MDP

标准马尔可夫决策过程（Markov Decision Process, MDP）可写为：

\[
\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, P, R, \gamma \rangle
\]

其中：

- \(\mathcal{S}\)：状态空间；
- \(\mathcal{A}\)：动作空间；
- \(P\)：状态转移；
- \(R\)：奖励函数；
- \(\gamma\)：折扣因子。

目标通常写为：

\[
J(\pi)=\mathbb{E}_{\tau\sim\pi}\left[\sum_{t=0}^{T}\gamma^t r_t\right]
\]

其中 \(\pi(a|s)\) 为策略。

## 三、value / policy 两条主线

### 1. value-based 视角

核心是价值函数：

\[
V^\pi(s)=\mathbb{E}_\pi\left[\sum_{t=0}^{T}\gamma^t r_t \mid s_0=s\right]
\]

以及动作价值函数：

\[
Q^\pi(s,a)=\mathbb{E}_\pi\left[\sum_{t=0}^{T}\gamma^t r_t \mid s_0=s,a_0=a\right]
\]

这条线更强调：

- Bellman 方程；
- bootstrapping；
- 价值估计误差；
- 离散动作场景的可解性。

### 2. policy-based 视角

策略梯度直接优化策略参数：

\[
\nabla_\theta J(\pi_\theta)
\]

这条线更适合：

- 连续控制；
- 高维动作空间；
- 随机策略；
- 加入约束、熵项和分布控制。

## 四、actor-critic 主线

actor-critic 把两条线结合：

- actor 负责产生动作；
- critic 负责提供价值估计或优势估计。

它之所以重要，是因为现代深度 RL、连续控制、多智能体和安全 RL 都大量使用这一结构。

## 五、deep RL 主线

深度强化学习的关键变化不是“把神经网络换进去”这么简单，而是：

- 高维状态可以被表征学习处理；
- 离散/连续动作都可进入统一训练框架；
- replay、target network、normalization 等系统机制变得关键；
- 训练稳定性和样本效率成为中心难题。

## 六、offline RL 主线

offline RL 处理的是：  
只给定静态数据集，不允许或很少允许在线探索。

这时核心问题变成：

- 分布外动作（out-of-distribution action）估计不稳定；
- value overestimation；
- 数据质量与覆盖度决定上限；
- 保守策略和性能提升之间如何权衡。

## 七、model-based RL 主线

model-based RL 试图学习环境模型，或利用已知动力学模型进行规划。  
它之所以重要，在于可以：

- 提高样本效率；
- 提供可解释中间对象；
- 更容易与 world model、控制、MPC、scientific simulator 对接。

## 八、MARL 主线

多智能体强化学习（Multi-Agent Reinforcement Learning, MARL）把单体 RL 的难点进一步扩大：

- 环境非平稳；
- 局部观测；
- 联合动作爆炸；
- 信用分配更困难；
- 通信、协同和对抗并存。

## 九、常见失败模式

- exploration 不足导致局部最优；
- 奖励设计错误，学到 reward hacking；
- offline RL 中分布偏移严重；
- model-based RL 中模型误差被规划放大；
- sim2real 失败；
- MARL 中信用分配模糊，学不出协同行为。

## 十、评测指标

- episodic return；
- sample efficiency；
- regret；
- success rate；
- safety constraint violation；
- calibration / uncertainty；
- robustness under distribution shift；
- sim2real transfer quality。

## 十一、研究切口

- exploration 与 uncertainty 是否可以统一；
- offline RL 中数据质量与最优性能界限如何刻画；
- world model 与 planning 到底何时胜过 model-free；
- safe RL 如何和真实审批流、人机协作结合；
- MARL 的 credit assignment 如何进入可审计系统工程。

## 十二、与知识库其他页面的关系

- 与 [强化学习基础：探索、信用分配、离线强化学习与模型化方法](../01-foundations/reinforcement-learning-foundations-exploration-credit-assignment-and-offline-rl.md) 相接；
- 与 [策略梯度、actor-critic 与基于价值的深度强化学习](../03-model-families/policy-gradient-actor-critic-and-value-based-deep-rl.md) 相接；
- 与 [模型化强化学习、世界模型与规划](../03-model-families/model-based-rl-world-models-and-planning.md) 相接；
- 与 [offline RL、安全 RL 与 sim2real 流水线](../04-systems-engineering/offline-rl-safe-rl-and-sim2real-pipelines.md) 相接；
- 与 [多智能体强化学习与信用分配](../04-systems-engineering/multi-agent-reinforcement-learning-and-credit-assignment.md) 相接。
