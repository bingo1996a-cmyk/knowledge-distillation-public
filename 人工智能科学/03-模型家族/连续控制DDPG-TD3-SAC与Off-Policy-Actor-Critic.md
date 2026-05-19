---
title: 连续控制：DDPG、TD3、SAC 与离策略 Actor-Critic
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 连续控制：DDPG、TD3、SAC 与离策略 Actor-Critic

> **阅读顺序**：本页是连续控制方法的专门深挖页。完整算法谱系总览请先阅读 [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)；进阶推导还可参考 [深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C、MARL 与 MRL](./advanced-reinforcement-learning-algorithms-trpo-ppo-ddpg-td3-sac-a2c-a3c-and-marl.md)。

## 1. 为什么连续控制需要另一套方法

在连续动作空间中，$\arg\max_a Q(s,a)$ 往往无法显式求解，因此不能直接把 DQN 套过去。解决思路是：

- 用 actor 近似最优动作；
- 用 critic 评估动作质量；
- 采用 off-policy 学习提高样本复用率。

## 2. DDPG

DDPG 可看作“DQN + deterministic policy gradient + target network + replay buffer”。

deterministic policy gradient 形式为

$$
\nabla_\theta J(\theta)
= \mathbb E_s\big[\nabla_a Q(s,a)\vert_{a=\mu_\theta(s)} \nabla_\theta \mu_\theta(s)\big].
$$

优点：

- 连续动作可处理；
- 样本效率高于纯 on-policy 方法。

缺点：

- 对超参数敏感；
- 容易过估计和崩溃；
- 探索依赖外加噪声，较脆弱。

## 3. TD3

TD3 主要修复 DDPG 的三类问题：

1. **双 critic**：减少 overestimation；
2. **延迟 actor 更新**：让 critic 先稳定；
3. **target policy smoothing**：降低 target exploitation。

其思想与 Double DQN 一脉相承：不要轻易相信单一 critic 给出的乐观估计。

## 4. SAC

SAC 的关键创新是最大熵目标：

$$
J(\pi)=\sum_t \mathbb E\big[r(s_t,a_t)+\alpha \mathcal H(\pi(\cdot\mid s_t))\big].
$$

这意味着策略不仅追求高回报，还追求足够随机性，从而：

- 改善探索；
- 提升训练稳定性；
- 使策略在局部扰动下更鲁棒。

## 5. DDPG、TD3、SAC 的比较

| 算法 | 策略类型 | critic 个数 | 目标特点 |
|---|---|---|---|
| DDPG | 确定性 | 单 critic | 直接最大化 Q |
| TD3 | 确定性 | 双 critic | 降低过估计 |
| SAC | 随机性策略 | 双 critic 常见 | 最大熵目标 |

## 6. 常见失败模式

- 连续动作边界处理不当；
- 奖励尺度不稳定；
- critic 过拟合 replay buffer；
- 真实机器人系统中 sim2real gap 过大。

## 7. 建议联读

- [策略梯度、Actor-Critic、TRPO、PPO 与优势估计](./policy-gradient-actor-critic-trpo-ppo-and-advantage-estimation.md)
- [offline RL、安全 RL 与 sim2real 流水线](../04-systems-engineering/offline-rl-safe-rl-and-sim2real-pipelines.md)
- [constrained RL、MPC bridge 与 shielded control](../04-systems-engineering/constrained-rl-mpc-bridges-and-shielded-control.md)
