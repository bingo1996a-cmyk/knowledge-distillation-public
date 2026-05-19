---
title: 策略梯度、Actor-Critic、TRPO、PPO 与优势估计
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 策略梯度、Actor-Critic、TRPO、PPO 与优势估计

> **阅读顺序**：本页是策略梯度与信任域方法的专门深挖页。完整算法谱系总览请先阅读 [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)；进阶公式推导还可参考 [深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C、MARL 与 MRL](./advanced-reinforcement-learning-algorithms-trpo-ppo-ddpg-td3-sac-a2c-a3c-and-marl.md)。

## 1. 基本问题

值函数方法适合离散动作和显式最大化，但面对高维连续动作时，直接学策略往往更自然。策略梯度方法的基本思想是：

$$
\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta),
$$

其中 $J(\theta)$ 表示策略的期望回报。

## 2. 策略梯度定理

策略梯度定理给出

$$
\nabla_\theta J(\theta)
= \mathbb E_{\pi_\theta}\big[\nabla_\theta \log \pi_\theta(a\mid s) Q^{\pi}(s,a)\big].
$$

它的重要性在于：不需要对环境动力学求导，也能估计策略更新方向。

## 3. REINFORCE

REINFORCE 用整段回报 $G_t$ 作为无偏估计：

$$
\nabla_\theta J(\theta)
\approx \sum_t \nabla_\theta \log \pi_\theta(a_t\mid s_t) G_t.
$$

优点是无偏；缺点是方差大。

## 4. baseline 与 advantage

为降方差，引入 baseline $b(s)$：

$$
\nabla_\theta J(\theta)
= \mathbb E\big[\nabla_\theta \log \pi_\theta(a\mid s) (Q(s,a)-b(s))\big].
$$

令 $b(s)=V(s)$，得到优势函数

$$
A(s,a)=Q(s,a)-V(s).
$$

这就引出 actor-critic。

## 5. Actor-Critic

- actor 更新策略；
- critic 估计价值或优势；
- 两者共同构成低方差、可在线更新的结构。

A2C 是同步版本，A3C 是异步并行版本。它们的差别主要在采样与更新并行方式。

## 6. GAE：优势估计的折中

广义优势估计（generalized advantage estimation, GAE）通过

$$
\hat A_t^{\text{GAE}(\gamma,\lambda)}
= \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}
$$

在偏差和方差之间做折中，其中

$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t).
$$

## 7. TRPO 与 PPO

TRPO 的核心是限制策略更新步长，避免新旧策略偏差过大。可写成带 KL 约束的优化：

$$
\max_\theta \; \mathbb E\left[\frac{\pi_\theta(a\mid s)}{\pi_{\theta_{old}}(a\mid s)} \hat A\right]
\quad
\text{s.t. } D_{KL}(\pi_{\theta_{old}}\|\pi_\theta) \le \delta.
$$

PPO 则用 clipping 把约束工程化：

$$
L^{\text{clip}}(\theta)
= \mathbb E\Big[\min(r_t(\theta)\hat A_t,
\text{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat A_t)\Big].
$$

PPO 的成功来自：

- 训练稳定；
- 实现简单；
- 对超参数相对鲁棒；
- 与并行采样和 GAE 配合良好。

## 8. 算法关系图

REINFORCE -> baseline -> actor-critic -> GAE -> TRPO/PPO。

也就是说，进化并不是一条“替换链”，而是一条围绕**方差控制、稳定更新和样本效率**逐步增强的改进链。

## 9. 建议联读

- [策略梯度、actor-critic 与基于价值的深度强化学习](./policy-gradient-actor-critic-and-value-based-deep-rl.md)
- [深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C 与 MARL](./advanced-reinforcement-learning-algorithms-trpo-ppo-ddpg-td3-sac-a2c-a3c-and-marl.md)
- [强化学习评估、离策略估计与安全部署](../04-systems-engineering/reinforcement-learning-evaluation-off-policy-estimation-and-safe-deployment.md)
