---
title: 强化学习基础：探索、信用分配、离线强化学习与模型化方法
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 强化学习基础：探索、信用分配、离线强化学习与模型化方法

## 定位

这页不是强化学习的入门综述，而是回答四个真正决定 RL 是否可用的问题：探索（exploration）、信用分配（credit assignment）、离线强化学习（offline RL）以及模型化方法（model-based methods）。如果不抓住这四条线，很多 RL 方法会被误解成“只是在不同 benchmark 上换个算法名”。

## 一、强化学习的最小形式

标准 Markov Decision Process（MDP）可写为：

$$
(\mathcal{S}, \mathcal{A}, P, r, \gamma)
$$

目标是寻找策略 \(\pi(a\mid s)\)，最大化期望折扣回报：

$$
J(\pi)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty} \gamma^t r_t\right]
$$

## 二、探索为什么难

### 1. 稀疏奖励

真正困难的任务经常只有长链末端才给出奖励，局部试错很难发现有效路径。

### 2. 深层延迟后果

某些动作的收益要过很久才显现，这意味着“眼前奖励”并不能反映动作长期价值。

### 3. 探索代价

在机器人、控制、航天和多智能体场景中，探索往往伴随能耗、碰撞、越界或任务失败风险。

## 三、信用分配问题

长期回报到来时，必须反过来判断哪些状态、动作、通信或角色分配对结果真正负责。核心难点是：

- 时间跨度长；
- 多步行为相互依赖；
- 多智能体下责任耦合；
- 部分可观测导致证据不完整。

## 四、策略梯度直觉

策略梯度方法通过对期望回报求导，直接调整策略参数：

$$
\nabla_{\theta} J(\pi_{\theta})=\mathbb{E}_{\pi_{\theta}}\left[
\nabla_{\theta} \log \pi_{\theta}(a\mid s) \hat{A}(s,a)
\right]
$$

其中 \(\hat A(s,a)\) 是 advantage 估计。它的核心思想是：提高那些在实际采样中带来更高回报的动作概率，降低反之者。

## 五、离线强化学习为什么重要

现实系统中常拿不到无限在线交互。离线 RL 试图利用已有日志数据学习策略，但它面临：

- 行为策略未知；
- 分布外动作估值严重失真；
- 估值网络容易过乐观；
- 数据覆盖不足时，策略会被伪优势误导。

## 六、模型化方法为什么重新重要

model-based RL 通过学习动力学模型或世界模型，把真实环境交互成本转移到内部模拟。它的价值在于：

- 样本效率更高；
- 可进行反事实分析与安全筛选；
- 更易与规划、控制和 digital twin 结合。

## 七、与其他页面的关系

- [强化学习](../02-paradigms/reinforcement-learning.md)
- [从 MDP 到深度强化学习：强化学习主线总论](../02-paradigms/reinforcement-learning-from-mdp-to-deep-rl.md)
- [策略梯度、actor-critic 与基于价值的深度强化学习](../03-model-families/policy-gradient-actor-critic-and-value-based-deep-rl.md)
- [模型化强化学习、世界模型与规划](../03-model-families/model-based-rl-world-models-and-planning.md)
