---
title: TD(λ)、Expected SARSA、资格迹（Eligibility Traces）与 n 步方法（n-step Methods）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# TD(λ)、Expected SARSA、资格迹（Eligibility Traces）与 n 步方法（n-step Methods）

## 1. 这一页解决什么问题

值函数学习的核心矛盾是：

- 单步 TD（Temporal Difference）更新方差低，但传播回报信息慢；
- Monte Carlo 更新传播信息快，但方差高且必须等回合结束。

TD($\lambda$)、资格迹（eligibility traces）与 n 步方法正是为了解决这一矛盾。它们提供了从“一步 bootstrap”到“整回合回报”的连续桥梁。

## 2. 从一步 TD 到 n 步回报

一步 TD 目标：

$$
G_t^{(1)} = R_{t+1}+\gamma V(S_{t+1}).
$$

二步目标：

$$
G_t^{(2)} = R_{t+1}+\gamma R_{t+2}+\gamma^2 V(S_{t+2}).
$$

一般 n 步目标：

$$
G_t^{(n)} = \sum_{k=0}^{n-1} \gamma^k R_{t+k+1}+\gamma^n V(S_{t+n}).
$$

当 $n=1$ 时退化为一步 TD；当 $n$ 足够长直到 episode 结束时，逼近 Monte Carlo 回报。

## 3. λ-return：把所有 n 步目标加权平均

TD($\lambda$) 的关键思想是对所有 n 步目标做指数加权：

$$
G_t^{\lambda}=(1-\lambda)\sum_{n=1}^{\infty}\lambda^{n-1}G_t^{(n)}.
$$

这里：

- $\lambda=0$ 时，完全退化为一步 TD；
- $\lambda\to 1$ 时，更接近 Monte Carlo。

因此，$\lambda$ 控制了偏差—方差权衡与 credit assignment 的传播深度。

## 4. 资格迹（Eligibility Trace）的基本思想

直接计算所有 n 步目标代价很高。资格迹提供了一个在线实现方法。

直观上，资格迹记录“过去状态/动作在当前时刻还应被追责多少”。若某状态最近刚访问过，资格迹大；若已久远，资格迹按 $\gamma\lambda$ 衰减。

最常见的累积迹（accumulating trace）形式：

$$
e_t(s)=\gamma\lambda e_{t-1}(s)+\mathbf{1}\{S_t=s\}.
$$

随后用 TD 误差对所有状态更新：

$$
V(s) \leftarrow V(s)+\alpha \delta_t e_t(s).
$$

这等于把当前 TD 误差“向后传播”到先前相关状态。

## 5. TD(λ) 的前向视图与后向视图

- **前向视图（forward view）**：从理论上定义 $\lambda$-return
- **后向视图（backward view）**：用资格迹在线实现

在线性函数逼近和特定条件下，两者是等价的。

## 6. SARSA、Expected SARSA 与 Q-learning 的关系

### 6.1 SARSA

SARSA 的更新目标：

$$
Q(S_t,A_t) \leftarrow Q(S_t,A_t)+\alpha\big[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)\big].
$$

它是**on-policy** 方法，因为目标使用了行为策略实际选出的下一个动作 $A_{t+1}$。

### 6.2 Expected SARSA

Expected SARSA 把随机动作替换为对策略的期望：

$$
Q(S_t,A_t) \leftarrow Q(S_t,A_t)+\alpha\left[R_{t+1}+\gamma\sum_a \pi(a\mid S_{t+1})Q(S_{t+1},a)-Q(S_t,A_t)\right].
$$

它比 SARSA 方差更低，因为把下一个动作的随机性积分掉了。

### 6.3 Q-learning

Q-learning 使用贪心 bootstrap：

$$
Q(S_t,A_t) \leftarrow Q(S_t,A_t)+\alpha\big[R_{t+1}+\gamma \max_a Q(S_{t+1},a)-Q(S_t,A_t)\big].
$$

它是 **off-policy**，目标策略与行为策略可以不同。

## 7. Expected SARSA 为什么重要

Expected SARSA 常被忽略，但它在值函数法谱系里很关键，因为它站在 SARSA 与 Q-learning 之间：

- 保留 on-policy / expectation 结构
- 降低了动作采样导致的方差
- 更适合与 soft policy、entropy regularization 等结构连接

从广义角度看，许多 actor-critic / soft Q 一类方法都可理解为对“期望化 bootstrap”的扩展。

## 8. n 步方法与深度强化学习

在深度强化学习里，n 步回报十分常见。原因是：

- 一步 bootstrap 太短，credit assignment 慢
- Monte Carlo 太高方差
- n 步回报折中较好

典型应用包括：

- A3C 中使用 n-step return
- Rainbow DQN 中纳入 multi-step target
- 分布式 RL 中常结合 replay 与 n-step return

## 9. TD(λ) 与函数逼近的复杂性

在表格型方法中，TD($\lambda$) 很自然。但在非线性函数逼近中，需要注意：

- trace 的定义不再简单是每个状态一个标量
- off-policy + bootstrapping + function approximation 容易不稳定
- 这与经典的“deadly triad”有关

因此，深度 RL 中往往更常见显式 n-step return，而不是完整的资格迹实现。

## 10. 三类方法的谱系关系

可以把它们放在一条链上理解：

- TD(0)：最短 credit horizon
- TD($\lambda$)：可调 horizon
- n-step TD：显式固定 horizon
- Monte Carlo：最大 horizon

另一条链是：

- SARSA：on-policy sampled bootstrap
- Expected SARSA：on-policy expected bootstrap
- Q-learning：off-policy greedy bootstrap

这两条链交叉后，构成了值函数法的核心骨架。

## 11. 常见失败模式

1. $\lambda$ 太大：方差过高，学习不稳定  
2. $\lambda$ 太小：长期 credit propagation 太慢  
3. off-policy + eligibility traces：实现复杂且易不稳定  
4. 函数逼近下，长 horizon bootstrap 可能放大误差

## 12. 建议阅读

- Sutton and Barto, *Reinforcement Learning: An Introduction*
- Watkins and Dayan, Q-learning
- SARSA / Expected SARSA 经典论文
- Rainbow DQN 与 multi-step return 相关工作
