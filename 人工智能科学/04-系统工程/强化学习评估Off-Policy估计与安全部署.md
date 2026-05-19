---
title: 强化学习评估、离策略估计与安全部署
layer: 04-systems-engineering
tags:
  - systems-engineering
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 强化学习评估、离策略估计与安全部署

## 1. 为什么这页重要

强化学习的一个根本困难是：策略效果往往只能通过交互得到，而真实系统不允许任意试错。因此评估与部署不是训练之后的附属步骤，而是 RL 工程主线的一部分。

## 2. 在线评估与离线评估

- 在线评估：真实环境或高保真仿真中直接执行策略。
- 离线评估：基于历史日志估计新策略表现。

## 3. 离策略估计（OPE）

典型技术：

- importance sampling
- weighted importance sampling
- doubly robust estimation
- fitted Q evaluation

OPE 的难点在于分布偏移与支持覆盖不足。

## 4. 安全部署

安全部署通常需要：

- action shielding
- fallback policy
- runtime monitor
- uncertainty trigger
- human override

## 5. sim2real 与安全约束

RL 模型在仿真中有效，不等于在真实系统中可靠。部署前应额外验证：

- dynamics mismatch
- observation noise
- latency
- rare events
- reward hacking

## 6. 与高风险系统的关系

在机器人、工业控制、航天系统与跨组织高约束场景，RL 部署需要与 TEVV、assurance case、incident response 联动。
