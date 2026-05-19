---
title: 离策略评估：FQE、WIS 与 Doubly Robust 比较
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 离策略评估：FQE、WIS 与 Doubly Robust 比较

## 重定向说明

本页与 [离策略评估：双重稳健估计与 OPE 基准](./off-policy-evaluation-doubly-robust-estimators-and-ope-benchmarks.md) 之间曾存在循环引用。现已修正。

OPE（Off-Policy Evaluation）方法（WIS、FQE、DR 等）的完整内容分布在以下文件中：

- **离策略算法实现**：详见 [连续控制与离策略 Actor-Critic](./continuous-control-ddpg-td3-sac-and-off-policy-actor-critic.md)；
- **强化学习评估框架**：详见 [强化学习算法族系](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md) 中的评估与基准讨论；
- **价值函数方法**：详见 [基于价值的强化学习](./value-based-reinforcement-learning-dp-td-sarsa-q-learning-dqn-and-double-dqn.md)。

### 快速对照

- WIS（加权重要采样）：更偏重要采样稳定化；
- FQE（拟合 Q 迭代）：更偏拟合价值函数；
- DR（双重稳健）：试图同时利用模型估计与重要采样，降低偏差与方差。

## 保留本页的原因

保留旧链接，避免外部或历史内部引用失效。
