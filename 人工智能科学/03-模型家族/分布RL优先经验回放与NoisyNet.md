---
title: 分布式强化学习（Distributional Reinforcement Learning）、优先经验回放（Prioritized Replay）与 NoisyNet
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 分布式强化学习（Distributional Reinforcement Learning）、优先经验回放（Prioritized Replay）与 NoisyNet

## 1. 为什么这些方法会出现在同一页

这三类方法常一起出现于深度值函数强化学习的改进谱系中，因为它们分别对应三个核心问题：

- **Distributional RL**：不仅学习期望回报，还学习回报分布；
- **Prioritized Replay**：不是均匀回放样本，而是优先学习更“重要”的经验；
- **NoisyNet**：把探索嵌入参数噪声，而不是只依赖 $\epsilon$-greedy。

它们在 Rainbow DQN 一类方法中被集成为统一框架。

## 2. Distributional RL 的基本思想

传统 Q-learning 学的是：

$$
Q^\pi(s,a)=\mathbb E[G_t\mid S_t=s,A_t=a].
$$

Distributional RL 学习的是整个随机回报分布：

$$
Z^\pi(s,a) \overset{D}{=} G_t.
$$

其中 $\overset{D}{=}$ 表示分布相等。

### 2.1 为什么要学分布

期望值会丢失风险、偏度、多峰性等信息。若两个动作期望回报相同，但一个高风险、一个低风险，仅靠均值无法区分。

因此，Distributional RL 在以下方面更强：

- 风险敏感决策
- 表达复杂回报结构
- 提升训练稳定性和表示能力

### 2.2 Bellman 分布算子

分布式 Bellman 更新写成：

$$
Z(s,a) \overset{D}{=} R + \gamma Z(S',A').
$$

不同于期望 Bellman 算子，这里更新的是分布变换。

### 2.3 代表方法

- **C51**：离散支持点上的分类式分布近似
- **QR-DQN**：分位点回归（quantile regression）
- **IQN**：隐式分位网络

## 3. 优先经验回放（Prioritized Experience Replay, PER）

经验回放（replay buffer）把过去经验存下来，打破样本相关性并提高数据利用率。均匀采样虽简单，但不是所有经验同等重要。

PER 的思想是：优先抽取 TD 误差大的样本，因为它们可能提供更强学习信号。

经验 $i$ 的采样概率常设为：

$$
P(i)=\frac{p_i^\alpha}{\sum_k p_k^\alpha},
$$

其中 $p_i$ 常与 $|\delta_i|$ 相关。

### 3.1 偏差修正

由于采样不再均匀，需要重要性采样权重：

$$
w_i = \left(\frac{1}{N\cdot P(i)}\right)^\beta.
$$

这样可部分补偿非均匀采样带来的估计偏差。

### 3.2 优点与问题

优点：

- 提高样本效率
- 更快聚焦高误差区域

问题：

- 会放大噪声样本的影响
- 需要维护优先级结构
- 偏差修正不完全时可能不稳定

## 4. NoisyNet：参数噪声驱动探索

$\epsilon$-greedy 的探索是“动作层随机”；NoisyNet 把随机性注入网络参数：

$$
W = \mu_W + \sigma_W \odot \varepsilon_W.
$$

因此，策略随机性来自参数化函数本身，而不是外部动作抖动。

### 4.1 直观理解

- $\epsilon$-greedy：在动作空间里随机乱试
- NoisyNet：在值函数/策略函数的表示层产生系统性探索

这样探索往往更一致，也更适合高维状态空间。

### 4.2 优点

- 减少手工设计探索 schedule 的负担
- 在某些任务中比 $\epsilon$-greedy 更有效
- 可与 DQN 家族自然结合

## 5. 三者的关系

这三类方法分别对应：

- **表示层增强**：Distributional RL
- **样本利用增强**：Prioritized Replay
- **探索机制增强**：NoisyNet

它们并不冲突，因此可以组合。

## 6. Rainbow DQN 的意义

Rainbow 将多种 DQN 改进合并：

- Double DQN
- Dueling network
- Prioritized Replay
- Multi-step return
- Distributional RL
- NoisyNet

Rainbow 的贡献不在于某一单点创新，而在于系统证明“不同改进模块可以互补”。

## 7. 与现代值函数法谱系的联系

这几类方法说明值函数强化学习不是单一算法，而是一个模块化系统：

- target 设计：Double / multi-step / distributional
- replay 设计：uniform / prioritized
- exploration 设计：epsilon / parameter noise / entropy
- architecture 设计：dueling / recurrent / transformer

## 8. 常见误区

1. **误区：Distributional RL 只是输出更多数字。**  
   不对。它改变的是 Bellman 学习对象，从期望转向分布。

2. **误区：PER 一定更好。**  
   不一定。噪声大或优先级失真时可能适得其反。

3. **误区：NoisyNet 取代所有探索机制。**  
   不成立。不同环境下仍需配合 intrinsic reward、entropy regularization 等机制。

## 9. 建议阅读

- Bellemare et al., C51
- Dabney et al., QR-DQN / IQN
- Schaul et al., Prioritized Experience Replay
- Fortunato et al., NoisyNet
- Hessel et al., Rainbow
