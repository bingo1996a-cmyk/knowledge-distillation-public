---
title: 值函数强化学习：DP、TD、SARSA、Q-learning、DQN 与 Double DQN
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 值函数强化学习：DP、TD、SARSA、Q-learning、DQN 与 Double DQN

> **阅读顺序**：本页是值函数方法的专门深挖页。完整算法谱系总览请先阅读 [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)，然后回到本页获取值函数分支的细节推导。

## 1. 总体主线

值函数方法的核心思想是：**不直接学动作本身，而先学“这个状态或动作有多值钱”**。

这条线可按复杂度递进理解：

1. 动态规划（DP）：模型已知，直接求 Bellman 方程；
2. TD 与 SARSA：模型未知，但在线估计价值；
3. Q-learning：离策略地逼近最优动作价值；
4. DQN：用神经网络处理高维状态；
5. Double DQN：修正最大化偏差。

## 2. Bellman 递推是共同底座

所有这些方法都建立在同一递推上：

$$
Q^{\pi}(s,a) = \mathbb{E}[r + \gamma Q^{\pi}(s',a')].
$$

区别只在于：

- 模型已知还是未知；
- 是评估当前策略还是逼近最优策略；
- 使用表格还是函数逼近；
- 更新目标由谁给出。

## 3. DP：已知模型时的精确递推

值迭代（value iteration）写成：

$$
V_{k+1}(s)=\max_a \sum_{s'} P(s'\mid s,a) [r(s,a,s') + \gamma V_k(s')].
$$

策略迭代（policy iteration）则在“策略评估—策略改进”之间交替。

DP 的局限不是原理不对，而是现实中常没有精确模型，也难以枚举全状态空间。

## 4. TD 与 SARSA

TD(0) 的状态价值更新为

$$
V(s_t) \leftarrow V(s_t) + \alpha \big[r_t + \gamma V(s_{t+1}) - V(s_t)\big].
$$

SARSA 的动作价值更新为

$$
Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha \big[r_t + \gamma Q(s_{t+1},a_{t+1}) - Q(s_t,a_t)\big].
$$

SARSA 是**在行为策略上更新**，因此更贴近 on-policy 学习。

## 5. Q-learning

Q-learning 的核心更新为

$$
Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha \big[r_t + \gamma \max_{a'}Q(s_{t+1},a') - Q(s_t,a_t)\big].
$$

它的关键特征是：

- 行为策略可以是 $\epsilon$-greedy；
- 更新目标却朝“最大未来价值”逼近；
- 因而属于 off-policy 方法。

## 6. DQN 的三件关键工程技巧

DQN 本身不是“Q-learning + 深度网络”这么简单。真正让它工作的是三项稳定化技术：

1. **experience replay**：打散样本相关性；
2. **target network**：降低 bootstrap 目标震荡；
3. **reward / gradient clipping**：抑制数值不稳定。

损失函数一般写作

$$
L(\theta)=\mathbb{E}_{(s,a,r,s')\sim \mathcal D}
\Big[y - Q_\theta(s,a)\Big]^2,
$$

其中

$$
y = r + \gamma \max_{a'} Q_{\theta^-}(s',a').
$$

## 7. Double DQN 修正什么

DQN 在取最大值时容易高估：

$$
\max_a \hat Q(s,a)
$$

会把噪声也一并放大。Double DQN 的做法是：

- 用在线网络选动作；
- 用目标网络评动作。

即

$$
y = r + \gamma Q_{\theta^-}\Big(s', \arg\max_{a'} Q_\theta(s',a')\Big).
$$

这样能显著降低过估计偏差。

## 8. 各算法之间的联系与区别

| 算法 | 是否已知模型 | 是否 bootstrap | 是否 on-policy | 是否用神经网络 |
|---|---|---|---|---|
| DP | 是 | 是 | 视情形 | 否 |
| TD | 否 | 是 | 常为 on-policy | 否 |
| SARSA | 否 | 是 | 是 | 否/可扩展 |
| Q-learning | 否 | 是 | 否 | 否/可扩展 |
| DQN | 否 | 是 | 否 | 是 |
| Double DQN | 否 | 是 | 否 | 是 |

## 9. 常见失败模式

- 奖励稀疏导致估计滞后；
- 探索不足导致局部最优；
- replay buffer 分布偏置；
- target 震荡导致训练不稳定；
- 在连续动作空间中直接最大化 $Q$ 不可行。

## 10. 建议联读

- [Bellman 方程、动态规划与时序差分学习](../01-foundations/bellman-equations-dynamic-programming-and-temporal-difference-learning.md)
- [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)
- [深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C 与 MARL](./advanced-reinforcement-learning-algorithms-trpo-ppo-ddpg-td3-sac-a2c-a3c-and-marl.md)
