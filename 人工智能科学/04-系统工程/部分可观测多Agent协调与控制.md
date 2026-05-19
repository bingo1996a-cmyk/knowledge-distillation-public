---
title: 部分可观测多智能体协同与控制
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 部分可观测多智能体协同与控制

## 1. 问题边界

现实多智能体系统很少满足完全可观测。常见原因是：

- 局部视野；
- 传感器噪声；
- 通信延迟；
- 隐状态；
- 环境与其他体动态不可直接观察。

因此，多智能体系统往往更适合通过部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP）及其多智能体扩展来描述。

## 2. 形式化与目标

单体 POMDP 可写为：

$$
(\mathcal{S}, \mathcal{A}, \mathcal{O}, P, \Omega, r, \gamma)
$$

多智能体条件下，每个体 \(i\) 只能观察局部观测 \(o_i\)，并根据其历史 \(\tau_i=(o_i^0,a_i^0,\dots,o_i^t)\) 形成策略：

$$
\pi_i(a_i \mid \tau_i)
$$

团队主要难点是：

- 信息不完全；
- 决策不同步；
- 共享表示与局部执行之间张力；
- 通信预算与实时控制冲突；
- 安全约束与实时协同耦合。

## 3. 关键结构

### 3.1 状态估计层

局部智能体往往需要先通过 belief state 或 latent state 估计完成局部状态恢复。可用方法包括：

- RNN / GRU / Transformer memory；
- Bayes filter；
- learned latent dynamics；
- graph state estimator。

### 3.2 协同决策层

典型路线包括：

- centralized training with decentralized execution, CTDE；
- value decomposition；
- message passing communication；
- hierarchy / role assignment；
- model-based coordination。

### 3.3 控制执行层

在真实机器人、无人系统和航天编队控制中，策略层与控制层通常分离：

`coordination policy -> local planner -> controller -> actuator`

这样做的原因是高层策略不适合直接处理所有连续控制细节。

## 4. 三类核心难题

### 4.1 观测融合

多个体的局部信息如何融合为足够可用的团队状态，是部分可观测协同中的第一道难题。

### 4.2 通信设计

通信既可能提升协同，也可能带来延迟、带宽占用和信息污染。真正有价值的问题不是“能不能通信”，而是：

- 何时通信；
- 通信什么；
- 通信给谁；
- 通信失败时如何退化运行。

### 4.3 长时程协同控制

多智能体经常面对 long-horizon objective：

- 队形保持；
- 资源分配；
- 任务接力；
- 动态避障；
- 目标搜索。

这会把状态估计、角色分工与低层控制同时耦合起来。

## 5. 方法概览

### 5.1 CTDE

训练期使用全局信息，执行期只保留局部智能体。它是当前最常见的工程折中。

### 5.2 价值函数分解

把团队价值分解为局部可学习结构，便于缓解动作空间维度爆炸。

### 5.3 图结构协同

将智能体网络表示为图，使用图结构消息传递捕获邻域关系、角色建模和局部协同。

### 5.4 Belief-aware coordination

显式维护对环境和其他体的信念，在部分可观测条件中形成更稳定策略。

## 6. 常见失败模式

- 训练时依赖了执行时不可用的全局特征；
- 通信协议设计与实际链路失配；
- 局部策略在协同下失效；
- 高层策略与低层控制冲突；
- 长时程目标被短奖励替代。
