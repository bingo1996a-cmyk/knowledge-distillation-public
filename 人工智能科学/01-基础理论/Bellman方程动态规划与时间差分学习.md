---
title: Bellman 方程、动态规划与时序差分学习
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# Bellman 方程、动态规划与时序差分学习

## 1. 这页解决什么问题

强化学习（reinforcement learning, RL）的基本思想，不是“试错”四个字，而是：

- 用价值函数（value function）表达长期效用；
- 用 Bellman 方程把长期问题分解为局部递推；
- 用动态规划（dynamic programming, DP）在已知模型下求解；
- 用时序差分（temporal difference, TD）在未知模型下进行自举（bootstrapping）学习。

## 2. 马尔可夫决策过程

设 MDP 为五元组 `\langle \mathcal S, \mathcal A, P, R, \gamma \rangle`。

- `\mathcal S`：状态空间；
- `\mathcal A`：动作空间；
- `P(s'\mid s,a)`：状态转移；
- `R(s,a)` 或 `R(s,a,s')`：奖励；
- `\gamma \in [0,1)`：折扣因子。

策略 `\pi(a\mid s)` 决定在状态下如何选动作。

## 3. 价值函数与 Bellman 方程

### 3.1 状态价值函数

$$
V^\pi(s)=\mathbb E_\pi\left[\sum_{t=0}^\infty \gamma^t r_t \mid s_0=s\right].
$$

### 3.2 动作价值函数

$$
Q^\pi(s,a)=\mathbb E_\pi\left[\sum_{t=0}^\infty \gamma^t r_t \mid s_0=s,a_0=a\right].
$$

### 3.3 Bellman 期望方程

$$
V^\pi(s)=\sum_a \pi(a\mid s)\sum_{s',r} p(s',r\mid s,a)\left[r+\gamma V^\pi(s')\right].
$$

它表达的思想是：**长期回报 = 当前一步收益 + 折扣后的未来价值**。

### 3.4 Bellman 最优方程

$$
V^*(s)=\max_a \sum_{s',r} p(s',r\mid s,a)\left[r+\gamma V^*(s')\right].
$$

$$
Q^*(s,a)=\sum_{s',r} p(s',r\mid s,a)\left[r+\gamma \max_{a'}Q^*(s',a')\right].
$$

这是几乎所有 RL 算法的理论核心。

## 4. 动态规划：已知模型时如何求解

### 4.1 Policy Evaluation

给定策略 `\pi`，求解 `V^\pi`。方法是 Bellman 递推迭代。

### 4.2 Policy Improvement

利用贪心更新：

$$
\pi'(s)=\arg\max_a Q^\pi(s,a).
$$

### 4.3 Policy Iteration

在 evaluation 和 improvement 之间交替，直到收敛。

### 4.4 Value Iteration

把两步合并：

$$
V_{k+1}(s)=\max_a \sum_{s',r} p(s',r\mid s,a)\left[r+\gamma V_k(s')\right].
$$

优点是理论清楚；缺点是需要已知转移模型，且在大状态空间下难以直接使用。

## 5. Monte Carlo 与 TD 的差别

### 5.1 Monte Carlo

使用完整回合结束后的真实回报更新：

$$
G_t = \sum_{k=0}^{T-t-1} \gamma^k r_{t+k}.
$$

优点：无偏。  
缺点：方差大，必须等 episode 结束。

### 5.2 Temporal Difference

TD 使用一步自举目标：

$$
V(s_t) \leftarrow V(s_t) + \alpha \left[r_t + \gamma V(s_{t+1}) - V(s_t)\right].
$$

其中括号中的项称为 TD error：

$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t).
$$

TD 兼具：

- 无需等回合结束；
- 使用当前估计作为未来代理；
- 样本效率通常高于纯 Monte Carlo。

## 6. SARSA 与 Q-learning

### 6.1 SARSA：on-policy TD control

更新式：

$$
Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha\left[r_t + \gamma Q(s_{t+1},a_{t+1}) - Q(s_t,a_t)\right].
$$

它学习的是当前行为策略对应的价值，因此更保守，常更贴近真实执行策略。

### 6.2 Q-learning：off-policy TD control

更新式：

$$
Q(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha\left[r_t + \gamma \max_{a'} Q(s_{t+1},a') - Q(s_t,a_t)\right].
$$

它直接逼近最优动作价值函数 `Q^*`，因此更激进，但也更易受到过估计与不稳定性的影响。

## 7. 从 TD 到 DQN

当状态空间过大，表格型 `Q(s,a)` 不可行时，用神经网络近似：

$$
Q(s,a;\theta) \approx Q^*(s,a).
$$

DQN 的核心不只是“神经网络 + Q-learning”，而是三项工程化改动：

- experience replay；
- target network；
- mini-batch stochastic optimization。

这使 TD 控制首次在高维感知任务上稳定起来。

## 8. 进一步的算法家族关系

Bellman 递推是根；其后算法大致可按下面理解：

- DP：模型已知；
- MC：无模型，但依赖完整回报；
- TD：无模型，自举更新；
- SARSA / Q-learning：TD control；
- DQN / DDQN：函数逼近下的 value-based control；
- actor-critic：把 policy optimization 与 value estimation 结合；
- PPO / TRPO：对 actor 更新做更稳定的约束；
- SAC：把最大熵目标并入策略学习；
- MARL：在多智能体环境中处理非平稳与信用分配。

## 9. 强化学习的基本思想再解释一次

若用一句更深一点的话来概括 RL，其基本思想是：

> 在环境反馈不直接给出正确动作标签、且当前动作会改变未来数据分布的情况下，利用长期回报、价值递推与探索机制学习策略。

这使 RL 与监督学习的根本差别不在网络结构，而在：

- 数据不是静态给定；
- 标签不是直接提供；
- 优化对象是长期效用；
- 估计与决策相互耦合。

## 10. 仍需补入但常被忽略的栏目

用户在算法清单中已提到很多重要方法，但通常还容易漏掉：

- multi-armed bandit；
- eligibility traces / TD(\lambda)；
- expected SARSA；
- distributional RL；
- hierarchical RL；
- imitation learning / inverse RL；
- POMDP；
- model-based planning 与 tree search；
- reward shaping 与 constraint handling。

## 11. 建议联读

- [强化学习基础：探索、信用分配、离线强化学习与模型化方法](./reinforcement-learning-foundations-exploration-credit-assignment-and-offline-rl.md)
- [从 MDP 到深度强化学习：强化学习主线总论](../02-paradigms/reinforcement-learning-from-mdp-to-deep-rl.md)
- [策略梯度、actor-critic 与基于价值的深度强化学习](../03-model-families/policy-gradient-actor-critic-and-value-based-deep-rl.md)
- [强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO](../03-model-families/reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)
