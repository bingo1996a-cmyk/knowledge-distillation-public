# 随机近似与 Robbins-Monro 方法

## 作用

随机近似（Stochastic Approximation）研究如何在只能观测带噪声信息时逼近方程根、极值点或固定点。

它是在线学习、强化学习、随机优化与自适应算法的底层方法之一。

## 经典形式

Robbins-Monro 迭代常写成

$$
\theta_{k+1}=\theta_k-a_k\,H(\theta_k,\xi_k)
$$

其中 $H$ 是带噪声的观测，$a_k$ 是步长序列。

## 为什么重要

### 1. 它适合不能精确求梯度或期望的场景

### 2. 它能解释很多在线算法为什么收敛

### 3. 它是 TD 学习、策略梯度、随机逼近控制器调参的理论基础之一

## 常见条件

常见分析会要求

$$
\sum_{k=1}^{\infty} a_k=\infty,\qquad \sum_{k=1}^{\infty} a_k^2<\infty
$$

以平衡探索和噪声平均。

## 最小例子

### 问题陈述
用 Robbins-Monro 算法求方程 $g(x) = x^3 - 2 = 0$ 的根（即 $\sqrt[3]{2} \approx 1.26$）。观测为 $Y_n = g(X_n) + \varepsilon_n$，其中 $\varepsilon_n \sim \mathcal{N}(0, 1)$。取步长 $\alpha_n = 1/n$，初始 $X_0 = 0$。

### 数学表达
Robbins-Monro 迭代：$X_{n+1} = X_n - \alpha_n Y_n$，其中 $Y_n = X_n^3 - 2 + \varepsilon_n$。理论条件：(1) $\sum \alpha_n = \infty$（保证走足够远），(2) $\sum \alpha_n^2 < \infty$（抑制噪声积累）。

### 计算/推理步骤
1. 第一次迭代：$X_0 = 0$，$\alpha_1 = 1$，$Y_1 = 0^3 - 2 + \varepsilon_1 = -2 + \varepsilon_1$。$\varepsilon_1$ 随机，若取 $\varepsilon_1 = 0.5$，则 $X_1 = 0 - 1 \cdot (-1.5) = 1.5$。
2. 第二次迭代：$\alpha_2 = 0.5$，$Y_2 = 1.5^3 - 2 + \varepsilon_2 = 3.375 - 2 + \varepsilon_2 = 1.375 + \varepsilon_2$。若 $\varepsilon_2 = -0.3$，则 $X_2 = 1.5 - 0.5 \cdot 1.075 = 0.9625$。
3. 第三次迭代：$\alpha_3 = 1/3$，$Y_3 = 0.9625^3 - 2 + \varepsilon_3 = 0.892 - 2 + \varepsilon_3$。若 $\varepsilon_3 = 0.1$，则 $X_3 = 0.9625 - (1/3)(-1.008) = 1.298$。
4. 继续迭代，$X_n$ 逐渐向 $\sqrt[3]{2} \approx 1.26$ 收敛，但收敛路径受噪声随机性影响而振荡。

### 结果解读
Robbins-Monro 算法的核心是步长 $\alpha_n = 1/n$ 的衰减设计：足够慢（调和级数发散）以保证可以到达真根，同时足够快（平方收敛）以压制噪声累积。本例中只需约 10-20 步即可接近 $\sqrt[3]{2}$，体现了随机逼近"在噪声中渐进寻根"的基本能力。

## 风险与约束

- 步长过大可能发散，过小则过慢
- 噪声若不满足基本矩条件，分析会失效
- 非凸目标下只能保证弱形式结论或局部结果

## 与其他条目的关系

- 前置： [梯度下降](../05-优化与控制/梯度下降.md)、[鞅与停时](../01-分析与测度/鞅与停时.md)
- 相关： [镜像下降与自然梯度](../05-优化与控制/镜像下降与自然梯度.md)、[近似动态规划与策略梯度](../05-优化与控制/近似动态规划与策略梯度.md)
- 应用： [强化学习中的数学](../../04-应用/强化学习中的数学.md)

## 推荐教材与延伸阅读

- Kushner, H. J. & Yin, G. G. (2003). *Stochastic Approximation and Recursive Algorithms and Applications*, 2nd ed. Springer. — 随机近似的权威理论著作，O. D. E. 方法与收敛分析。
- Borkar, V. S. (2008). *Stochastic Approximation: A Dynamical Systems Viewpoint*. Hindustan Book Agency. — 从动力系统视角理解随机近似的简洁专著。
- Bertsekas, D. P. & Tsitsiklis, J. N. (1996). *Neuro-Dynamic Programming*. Athena Scientific. — 第 3 章从强化学习角度讨论随机近似与 TD 学习。
