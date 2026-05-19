---
title: 风险敏感强化学习（Risk-Sensitive Reinforcement Learning）、条件风险价值（CVaR）、熵正则化与鲁棒强化学习
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 风险敏感强化学习（Risk-Sensitive Reinforcement Learning）、条件风险价值（CVaR）、熵正则化与鲁棒强化学习

## 1. 为什么标准 RL 不够

经典强化学习通常优化期望回报：

$$
J(\pi)=\mathbb{E}[G].
$$

但在航天、自动驾驶、工业控制等高风险系统中，只看期望值不够，因为低概率高损失事件也很重要。

## 2. 风险敏感 RL

### 2.1 方差惩罚

一种简单做法是：

$$
J_{risk}(\pi)=\mathbb{E}[G]-\eta\,\mathrm{Var}(G).
$$

它能抑制高波动策略，但无法直接刻画尾部风险。

### 2.2 CVaR

条件风险价值（Conditional Value-at-Risk, CVaR）关注最差一小部分结果的平均损失。若损失变量为 $L$，则

$$
\mathrm{CVaR}_{\alpha}(L)=\mathbb{E}[L\mid L\ge \mathrm{VaR}_{\alpha}(L)].
$$

这非常适合表达“最坏的 5% 轨迹不能太差”。

## 3. 熵正则化 RL

熵正则化在目标中加入策略熵：

$$
J_{entropy}(\pi)=\mathbb{E}\Big[\sum_t \gamma^t\big(r_t+\alpha\mathcal H(\pi(\cdot\mid s_t))\big)\Big].
$$

它既提高探索性，也往往让策略更平滑。SAC 就是这一思想的代表。

## 4. 鲁棒强化学习

鲁棒 RL 不假设环境模型精确，而是假设转移动态属于某个不确定集 $\mathcal P$。优化目标变成：

$$
\max_{\pi}\min_{P\in\mathcal P} V^{\pi}(P).
$$

它更适合应对模型误差、环境扰动和部署偏移。

## 5. 三者的联系与区别

- **风险敏感 RL**：强调回报分布本身的风险；
- **CVaR RL**：强调尾部最坏情况；
- **熵正则化 RL**：强调探索与策略平滑；
- **鲁棒 RL**：强调环境不确定性下的最坏情况性能。

它们都不是简单追求“平均分更高”，而是要让策略在不确定条件下更可靠。

## 6. 应用场景

- 航天任务：燃料约束、失效容错、任务安全边界；
- 工业控制：安全阈值不能被突破；
- 推荐/调度：必须限制最差用户体验或极端拥塞。

## 7. 与知识库现有页的关系

- `分布式、风险敏感与约束强化学习`
- `风险敏感、安全与约束强化学习：面向高风险系统`
- `强化学习评估、离策略估计与安全部署`

## 8. 代表性论文

1. Tamar 等关于 policy gradients for coherent risk measures。
2. Chow 等关于 constrained / CVaR RL。
3. Haarnoja 等关于 SAC。
4. Iyengar、Nilim & El Ghaoui 关于 robust MDP。
