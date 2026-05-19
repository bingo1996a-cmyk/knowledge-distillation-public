---
title: 模型化强化学习、世界模型与规划
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 模型化强化学习、世界模型与规划

## 定位

本页讨论 model-based RL（模型化强化学习）与 world model 之间的联系与差异。  
它关注一条重要主线：

`动力学模型 -> 预测 -> 想象轨迹 -> 规划 -> 控制`

## 一、概念边界

### 1. model-based RL

model-based RL 通过显式或隐式环境模型来提高学习效率或支持规划。  
模型可以是：

- 已知物理模型；
- 学习得到的转移模型；
- 潜空间动力学模型；
- 带不确定性的 ensemble model。

### 2. world model

world model 更强调学习环境中可压缩、可预测、可模拟的内部表示。  
它不只是为了控制，也常用于：

- 具身智能；
- 视频预测；
- imagined rollouts；
- agent memory 与 planning；
- long-horizon task decomposition。

## 二、主线结构

### 1. 动力学学习

核心问题是学习：

\[
p(s_{t+1} \mid s_t, a_t)
\]

或在潜空间中学习：

\[
z_{t+1} = f_\phi(z_t, a_t)
\]

### 2. 规划

一旦有模型，就可通过：

- MPC；
- shooting method；
- CEM；
- tree search；
- latent planning；
- policy improvement with imagination

来生成更优动作。

### 3. world model 与 RL 接口

world model 可以服务于：

- 表征学习；
- offline policy evaluation；
- uncertainty-aware planning；
- sim2real bridging；
- multi-agent prediction。

## 三、优势

- 更高样本效率；
- 更容易引入先验模型；
- 更自然地接入控制和规划；
- 有利于解释与诊断；
- 可用 imagined data 提高决策质量。

## 四、局限

- 模型偏差会在长规划中积累；
- 分布外状态预测容易失真；
- 规划成本可能较高；
- 在高维多模态场景下，模型学习本身就很难。

## 五、常见失败模式

- 学到的模型对一步预测准确，但长期滚动崩溃；
- reward model 或 dynamics model 存在 shortcut；
- planner 利用模型漏洞；
- world model 学到表面统计而非因果结构；
- sim2real gap 被 latent imagination 放大。

## 六、评测指标

- one-step / multi-step prediction error；
- planning return；
- data efficiency；
- uncertainty calibration；
- robustness to model bias；
- sim2real transfer performance。

## 七、研究切口

- world model 中表征、预测和规划能否统一；
- 如何把不确定性估计嵌入 planning；
- model-based RL 与 differentiable simulation / neural operator 的接口；
- multi-agent world model 如何支持协同控制与责任归因。

## 八、与知识库其他页面的关系

- 与 [世界模型](./world-models.md) 相接；
- 与 [持续交互智能体与世界建模](./interactive-agents-and-continual-world-modeling.md) 相接；
- 与 [从 MDP 到深度强化学习：强化学习主线总论](../02-paradigms/reinforcement-learning-from-mdp-to-deep-rl.md) 相接；
- 与 [人工智能在航天系统与航空航天中的应用](../06-applications/ai-in-space-systems-and-aerospace.md) 相接。
