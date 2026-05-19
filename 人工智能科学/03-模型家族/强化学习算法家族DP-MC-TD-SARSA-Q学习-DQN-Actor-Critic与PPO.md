---
title: 强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 强化学习算法谱系：DP、MC、TD、SARSA、Q-learning、DQN、actor-critic 与 PPO

> **阅读顺序**：本页是强化学习算法谱系的总览入口页，提供从 DP 到现代深度 RL 的六层算法谱系。详细的公式推导与进阶变体说明参见 [深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C、MARL 与 MRL](./advanced-reinforcement-learning-algorithms-trpo-ppo-ddpg-td3-sac-a2c-a3c-and-marl.md)。各算法类别的深层展开见各自的独立专题页（值函数深挖 / 策略梯度深挖 / 连续控制深挖 / TD(λ) / 分布式 RL 等）。

## 1. 为什么需要算法谱系页

用户在清单中列出了 DP、Q-learning、TD、SARSA、AC、A2C、A3C、DQN、DDQN、DDPG、SAC、PPO、TRPO、MARL、MRL 等方法。单列清单会碎片化；更合理的方式是用“算法谱系”理解它们之间的继承关系。

## 2. 第一层：DP、MC、TD

### 2.1 Dynamic Programming

已知环境模型时，使用 Bellman 递推求解。

### 2.2 Monte Carlo

基于完整回合回报，更新无偏但方差大。

### 2.3 Temporal Difference

用 bootstrap 估计长期价值，是表格型强化学习到深度强化学习的桥。

## 3. 第二层：SARSA 与 Q-learning

### 3.1 SARSA

on-policy。学习当前行为策略下的动作价值。

### 3.2 Q-learning

off-policy。直接逼近最优动作价值。

## 4. 第三层：DQN 与 DDQN

### 4.1 DQN

关键组件：

- replay buffer；
- target network；
- CNN / MLP approximation。

### 4.2 DDQN

通过解耦动作选择与动作评估缓解 Q 值过估计。

## 5. 第四层：Policy Gradient 与 Actor-Critic

### 5.1 Policy Gradient

直接优化策略参数，而不是间接通过 Q 表。

### 5.2 Actor-Critic

- Actor：输出策略；
- Critic：估计价值或优势。

这比纯 value-based 方法更自然地处理连续动作和大动作空间。

### 5.3 A2C / A3C

- A2C：同步优势 actor-critic；
- A3C：异步并行 actor-critic。

## 6. 第五层：连续控制与现代 policy optimization

### 6.1 DDPG

把 DQN 的思路扩展到连续动作，通过 deterministic policy gradient 工作。

### 6.2 TRPO

通过 trust region 约束更新幅度，提高稳定性。

### 6.3 PPO

PPO 用 clipping 近似 trust-region，工程上更简单，成为现代 RL 主力方法之一。

### 6.4 SAC

Soft Actor-Critic 把最大熵思想并入目标，兼顾探索与稳定性，连续控制中非常重要。

## 7. 第六层：MARL 与 MRL

### 7.1 MARL

多智能体强化学习研究：

- 非平稳；
- 信用分配；
- 通信；
- 集中训练、分散执行（CTDE）。

### 7.2 MRL 缩写的歧义

MRL 在不同文献中可能指：

- multi-agent reinforcement learning 的简写变体；
- meta reinforcement learning；
- modular reinforcement learning。

因此在知识库中不宜只写缩写，必须指明语境。

## 8. 强化学习关键技术与常见改进

你点到“强化学习的关键技术及改进”，应至少包含：

- exploration strategy；
- experience replay；
- target network；
- double / dueling / distributional trick；
- prioritized replay；
- entropy regularization；
- generalized advantage estimation；
- trust region / clipping；
- model-based rollout；
- offline RL conservatism；
- safe RL constraints；
- reward shaping；
- curriculum；
- hierarchical RL；
- imitation / inverse RL。

## 9. 训练过程如何理解

典型 RL 训练循环包含：

1. 与环境交互收集轨迹；
2. 计算 return / advantage / TD target；
3. 更新 value / policy / model；
4. 周期性评估与 checkpoint；
5. 调整探索、学习率、熵系数或约束权重。

## 10. 最新研究趋势

近一阶段研究更关注：

- RL 与 LLM / agent 结合；
- 分层 RL；
- world model + planning；
- 离线与安全约束；
- 大规模多智能体；
- 推理时 search 与 verifier loop。

## 11. Value-based 与 Policy-based 的根本差异

表面上，一个学价值，一个学策略。更深层区别在于：

- 是否把策略选择显式嵌入优化变量；
- 是否更依赖 bootstrapping；
- 是否更容易处理连续动作；
- 是否更便于加入安全约束、信任域或熵项。

## 12. 关键工程组件

- replay buffer；
- target network；
- advantage estimation；
- entropy regularization；
- trust region / clipping；
- exploration noise；
- normalization 与 reward scaling。

## 13. 常见失败模式

- critic 不稳定拖累 actor；
- replay buffer 分布老化；
- 值函数过估计；
- continuous control 中策略崩塌；
- PPO clipping 过度保守；
- 奖励尺度不稳导致训练震荡。

## 14. 评测指标

- 平均回报；
- 成功率；
- 学习曲线面积；
- 训练方差；
- 约束违反率；
- 推理时延与控制频率；
- sim2real transfer 表现。

## 15. 研究切口

- actor-critic 中 critic 误差如何传播到策略；
- value-based 与 policy-based 在 offline / safe / multi-agent 场景的边界；
- 熵正则、自适应温度与探索质量之间的关系；
- 深度 RL 表征学习与 world model 的接口。

## 联读

- [Bellman 方程、动态规划与时序差分学习](../01-foundations/bellman-equations-dynamic-programming-and-temporal-difference-learning.md)
- [强化学习基础：探索、信用分配、离线强化学习与模型化方法](../01-foundations/reinforcement-learning-foundations-exploration-credit-assignment-and-offline-rl.md)
- [从 MDP 到深度强化学习：强化学习主线总论](../02-paradigms/reinforcement-learning-from-mdp-to-deep-rl.md)
- [深度强化学习进阶算法：TRPO、PPO、DDPG、TD3、SAC、A2C、A3C、MARL 与 MRL](./advanced-reinforcement-learning-algorithms-trpo-ppo-ddpg-td3-sac-a2c-a3c-and-marl.md)
- [多智能体强化学习与信用分配](../04-systems-engineering/multi-agent-reinforcement-learning-and-credit-assignment.md)

## 参考文献

[1] Sutton, R. S. & Barto, A. G. *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press, 2018.
[2] Mnih, V. et al. *Human-Level Control Through Deep Reinforcement Learning*. Nature, 2015.
[3] Schulman, J. et al. *Proximal Policy Optimization Algorithms*. arXiv:1707.06347, 2017.
