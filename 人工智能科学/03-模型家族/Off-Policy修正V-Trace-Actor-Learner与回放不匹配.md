---
title: 离策略修正、V-trace、Actor-Learner 与重放失配
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 离策略修正、V-trace、Actor-Learner 与重放失配

## 重定向说明

本页在 V32 中收窄后与 [离策略修正：重要采样与 Retrace](./off-policy-correction-importance-sampling-and-retrace.md) 之间曾存在互指的循环引用。现已修正：离策略修正的通用内容分散在以下文件中，按主题选择查阅：

- **离策略算法实现**：详见 [连续控制与离策略 Actor-Critic](./continuous-control-ddpg-td3-sac-and-off-policy-actor-critic.md)，涵盖 DDPG、TD3、SAC 等主流离策略方法及其实现细节；
- **离策略数据流与回放机制**：详见 [强化学习算法族系](./reinforcement-learning-algorithm-family-dp-mc-td-sarsa-q-learning-dqn-actor-critic-and-ppo.md)，讨论 off-policy 与 on-policy 的根本差异及其工程影响；
- **本页历史内容（V-trace）**：V-trace 现在作为分布式 actor-learner 架构的离策略修正技术，在 IMPALA 和类似系统的相关资料中介绍。

## 保留本页的原因

保留旧链接，避免外部或历史内部引用失效。
