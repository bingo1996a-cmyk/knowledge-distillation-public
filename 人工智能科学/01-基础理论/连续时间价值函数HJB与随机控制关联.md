---
title: 连续时间价值函数、HJB 方程与随机控制联系（Continuous-Time Value Functions, HJB Equations, and Stochastic Control Links）
layer: 01-foundations
tags:
  - ai-theory
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 连续时间价值函数、HJB 方程与随机控制联系（Continuous-Time Value Functions, HJB Equations, and Stochastic Control Links）

## 1. 这页解决什么问题

离散时间强化学习（Reinforcement Learning, RL）通常从 Bellman 方程出发，而控制理论中的很多经典结果却写成连续时间形式，例如 Hamilton–Jacobi–Bellman 方程（Hamilton–Jacobi–Bellman Equation, HJB）。本页的目标是把两者接起来：

- 解释连续时间价值函数的意义；
- 说明 HJB 方程如何看成 Bellman 最优方程的连续时间极限；
- 说明它与随机微积分、随机控制、模型预测控制（Model Predictive Control, MPC）和强化学习的关系。

## 2. 连续时间控制问题的基本形式

设状态过程满足随机微分方程（Stochastic Differential Equation, SDE）

$$
dX_t = f(X_t, u_t)\,dt + \sigma(X_t, u_t)\,dW_t,
$$

其中 $u_t$ 为控制输入，$W_t$ 为 Wiener 过程。给定运行代价 $c(x,u)$ 和终端代价 $g(x)$，目标是最小化

$$
J^{u}(t,x)=\mathbb{E}\left[\int_t^T c(X_s,u_s)\,ds + g(X_T)\mid X_t=x
\right].
$$

连续时间最优值函数定义为

$$
V(t,x)=\inf_u J^u(t,x).
$$

## 3. 从 Bellman 原理到 HJB 方程

Bellman 最优性原理在连续时间下可写成：从当前时刻开始，最优策略在任何更短的后续时间区间上仍然保持最优。

对一个足够小的时间步长 $\Delta t$，有近似递推

$$
V(t,x)=\inf_u \mathbb{E}\left[c(x,u)\Delta t + V(t+\Delta t, X_{t+\Delta t})
\right].
$$

对右侧做 Itô 展开并令 $\Delta \to 0$，可得 HJB 方程：

$$
-\partial_t V(t,x)=\inf_u \Big(c(x,u)+
abla_x V(t,x)^o p f(x,u)+\frac12 \mathrm{tr}(\sigma\sigma^\top 
\nabla_x^2 V(t,x))\Big),
$$

终端条件为

$$
V(T,x)=g(x).
$$

这就是连续时间最优控制问题的核心偏微分方程。

## 4. 与离散时间 Bellman 方程的关系

离散时间值函数通常写成

$$
V(s)=\min_a \left[r(s,a)+\gamma \sum_{s'}P(s'\mid s,a)V(s')
\right].
$$

若把时间步长缩小，并令折扣因子与连续时间贴现率对应，则可以把离散时间 Bellman 关系看成连续时间 HJB 的近似离散化版本。两者的共同结构是：

- 当前代价；
- 状态转移；
- 未来最优值；
- 对控制或动作求最优。

## 5. HJB 为什么重要

### 5.1 它是连续时间最优控制的“值函数母方程”

无论是确定性控制还是随机控制，只要目标是“最优决策”，值函数通常都落到 HJB 或其变体上。

### 5.2 它连接强化学习与控制理论

强化学习中学值函数，本质上是在学某种 Bellman 固定点；控制理论中求解 HJB，本质上是在求连续时间值函数。两者差异主要在：

- 模型是否已知；
- 时间是离散还是连续；
- 解法是解析、数值、近似动态规划还是神经近似。

### 5.3 它揭示“值函数—策略”双关系

一旦得到 $V(t,x)$，最优控制往往可以由

$$
u^*(t,x)=\arg\min_u \Big(c(x,u)+
abla_x V^\top f + \frac12 \mathrm{tr}(\sigma\sigma^\top\nabla^2_x V)\Big)
$$

给出。也就是说，值函数蕴含了策略。

## 6. LQR 例子：HJB 的闭式解

在线性二次调节（Linear Quadratic Regulator, LQR）中，系统为

$$
\dot x = Ax + Bu,
$$

代价为

$$
J = \int_0^T (x^\top Qx + u^\top Ru)\,dt + x(T)^\top Sx(T).
$$

猜测值函数形如

$$
V(t,x)=x^\top P(t)x,
$$

代入 HJB 可得 Riccati 微分方程。由此得到最优反馈控制

$$
u^*(t) = -R^{-1}B^\top P(t)x(t).
$$

这个例子说明：在某些特殊结构下，HJB 虽然看起来复杂，但可以转化为矩阵方程。

## 7. HJB 与现代强化学习的桥梁

### 7.1 连续控制强化学习

DDPG、TD3、SAC 等算法虽然通常写成离散时间迭代形式，但它们服务的典型任务是连续控制。若环境采样足够快，背后的物理系统本质上更接近连续时间动力学。

### 7.2 近似动态规划

当 HJB 无法解析求解时，可以用函数逼近学习值函数或策略，这就形成了近似动态规划（Approximate Dynamic Programming, ADP）与神经最优控制的路线。

### 7.3 模型预测控制与值函数近似

MPC 每次只解有限时域问题，值函数近似可以作为末端成本；而 RL 学到的值函数也可用来提高 MPC 的长时域效果。它们并不是完全对立，而是可以混合。

## 8. 计算困难与现实限制

### 8.1 维数灾难

HJB 是定义在状态空间上的偏微分方程，维数稍高就难以直接离散求解。

### 8.2 模型不确定性

若 $f$、$\sigma$ 不精确，直接解 HJB 的结果可能偏离真实控制需求。

### 8.3 采样噪声与函数逼近误差

用神经网络近似值函数时，会引入优化误差、采样误差和逼近误差。

## 9. 本页与知识库其他页面的关系

- 与“Bellman 方程、动态规划与时序差分学习”构成离散—连续时间桥；
- 与“随机微积分、扩散过程与连续时间控制”形成数学基础与控制应用的双页结构；
- 与“constrained RL、MPC bridge 与 shielded control”形成控制—强化学习—安全约束主线。

## 10. 参考资料

### 教材

1. Bertsekas. *Dynamic Programming and Optimal Control*.
2. Fleming, Soner. *Controlled Markov Processes and Viscosity Solutions*.
3. Yong, Zhou. *Stochastic Controls*.

### 论文与经典文献

1. Bellman. *Dynamic Programming*.
2. Kappen. *Path Integrals and Symmetry Breaking for Optimal Control Theory*.
3. Todorov. *Linearly-Solvable Markov Decision Problems*.
