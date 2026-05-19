---
title: 模仿学习（Imitation Learning）、逆强化学习（Inverse Reinforcement Learning）与奖励建模（Reward Modeling）
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 模仿学习（Imitation Learning）、逆强化学习（Inverse Reinforcement Learning）与奖励建模（Reward Modeling）

## 1. 三者为什么放在一起

强化学习的一条主线是“自己试错获得奖励”。但很多现实任务中，奖励函数难写、样本昂贵、探索危险，于是产生了另一条主线：

- **模仿学习**：直接学专家行为
- **逆强化学习**：从专家行为反推出潜在奖励函数
- **奖励建模**：用偏好或标注数据学习奖励信号

这三者共同回答：**当奖励无法直接给定时，如何让系统学会合理行为。**

## 2. 模仿学习的基本形式

### 2.1 行为克隆（Behavior Cloning, BC）

最直接的方法是把专家轨迹看作监督学习数据：

$$
\min_\pi \mathbb E_{(s,a)\sim \mathcal D_E}[\ell(\pi(s),a)].
$$

`\min_\pi \mathbb E_{(s,a)\sim \mathcal D_E}[\ell(\pi(s),a)]`

优点：

- 简单
- 稳定
- 适合大规模离线数据

缺点：

- covariate shift：模型一旦偏离专家分布，就会进入未见状态，误差累积

### 2.2 DAgger

Dataset Aggregation（DAgger）通过让当前策略与专家交互、持续收集专家纠正数据，缓解 covariate shift。

其思想是：训练集不能只来自专家自己访问的状态，还要包含学习者未来会访问的状态。

## 3. 逆强化学习（IRL）的基本思想

IRL 不直接模仿动作，而是寻找一个奖励函数 $r$，使得专家策略在该奖励下是最优或近似最优。

形式上，可写为：

$$
\pi_E \approx \arg\max_\pi \mathbb E_\pi\left[\sum_t \gamma^t r(s_t,a_t)\right].
$$

### 3.1 为什么 IRL 难

因为奖励函数并不唯一。很多不同的奖励都能解释同一个专家行为，这称为**不可辨识性**（identifiability problem）。

### 3.2 代表方法

- Maximum Margin Planning
- Maximum Entropy IRL
- Deep IRL
- Adversarial IRL

其中最大熵逆强化学习（MaxEnt IRL）很重要，因为它在所有匹配专家特征期望的策略中，选择熵最大的那一个，减少不必要偏置。

## 4. 奖励建模（Reward Modeling）

奖励建模比传统 IRL 更贴近现代大模型对齐。其核心不是从完整专家轨迹恢复奖励，而是从：

- 人类偏好比较
- 排序数据
- 审核反馈
- 对比选择

中学得一个奖励模型 $r_\phi$。

例如，对两个候选输出 $y^+$ 与 $y^-$，训练奖励模型使：

$$
P(y^+ \succ y^-) = \sigma\big(r_\phi(x,y^+) - r_\phi(x,y^-)\big).
$$

这是 RLHF（Reinforcement Learning from Human Feedback）和偏好优化主线中的基础部件。

## 5. 三者之间的关系

### 5.1 从监督到奖励再到策略

- BC：直接学策略
- IRL：先学奖励，再求策略
- Reward Modeling：先学偏好/奖励模型，再优化策略

### 5.2 抽象层次差异

- 模仿学习复制“做法”
- 逆强化学习推断“目标”
- 奖励建模学习“偏好信号”

### 5.3 与强化学习的关系

一旦有了奖励函数或奖励模型，就又回到了 RL 优化环路。因此，这三者不是 RL 的替代，而是 RL 的前端补充。

## 6. 在现代 AI 中的应用

### 6.1 机器人控制

- 行为克隆用于从示教轨迹学习控制器
- IRL 用于从专家演示中恢复任务意图

### 6.2 自动驾驶与高风险控制

- 不适合盲目探索
- 需要利用专家行为数据
- 可结合安全约束与 sim2real

### 6.3 大语言模型对齐

- 奖励建模与偏好优化成为后训练关键步骤
- DPO / RPO 一类方法虽不总显式训练奖励模型，但其思想仍与偏好信号建模紧密相关

## 7. 常见失败模式

1. 专家数据质量差 → 模仿学习上限低  
2. 分布偏移严重 → 行为克隆级联失效  
3. IRL 不可辨识 → 学得的奖励不可解释  
4. 奖励模型过拟合标注偏好 → reward hacking  
5. 偏好数据本身有偏差 → 目标错配

## 8. 关键联系图

可以把三者视为同一条“从示例中学习目标与行为”的链：

- 演示数据 → BC → 策略
- 演示数据 → IRL → 奖励 → RL → 策略
- 偏好数据 → Reward Model → RL / Preference Optimization → 策略

## 9. 建议阅读

- Ross et al., DAgger
- Ng and Russell, IRL
- Ziebart, Maximum Entropy IRL
- Christiano et al., preference-based reward learning
- RLHF / reward model 相关后训练论文
