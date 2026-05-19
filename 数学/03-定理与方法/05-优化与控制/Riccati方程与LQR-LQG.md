# Riccati 方程、LQR 与 LQG

## 作用

Riccati 方程（Riccati Equation）是线性二次最优控制中的核心方程。  
它把一类原本动态耦合的最优控制问题，化成了矩阵递推或矩阵代数方程。

LQR（Linear Quadratic Regulator）和 LQG（Linear Quadratic Gaussian）都是控制理论中最重要的基线模型之一。

## LQR 问题设定

以离散时间系统为例：

$$
x_{k+1}=Ax_k+Bu_k
$$

考虑有限时域性能指标：

$$
J= x_N^\top Q_N x_N+\sum_{k=0}^{N-1}\left(x_k^\top Q x_k+u_k^\top R u_k\right)
$$

其中通常要求

$$
Q\succeq 0,\qquad Q_N\succeq 0,\qquad R\succ 0
$$

## 二次值函数假设

该问题的关键结构是：最优值函数保持二次型。

$$
V_k(x)=x^\top P_k x
$$

把它代入 Bellman 递推，可得到离散 Riccati 反向递推：

$$
P_k=Q+A^\top P_{k+1}A-A^\top P_{k+1}B\left(R+B^\top P_{k+1}B\right)^{-1}B^\top P_{k+1}A
$$

终端条件为

$$
P_N=Q_N
$$

## 最优反馈律

对应的最优控制律为线性状态反馈：

$$
u_k^*=-K_k x_k
$$

其中反馈增益

$$
K_k=\left(R+B^\top P_{k+1}B\right)^{-1}B^\top P_{k+1}A
$$

## 无限时域与代数 Riccati 方程

当系统与代价时不变，且考虑无限时域时，常得到离散代数 Riccati 方程（Discrete Algebraic Riccati Equation, DARE）：

$$
P=Q+A^\top P A-A^\top P B\left(R+B^\top P B\right)^{-1}B^\top P A
$$

若可稳定化（stabilizable）与可检测（detectable）等条件满足，则可得到稳定反馈律。

## LQG：控制与估计结合

LQG 在线性二次控制中再引入高斯噪声与部分可观测：

$$
x_{k+1}=Ax_k+Bu_k+w_k,
\qquad y_k=Cx_k+v_k
$$

其中 $w_k,v_k$ 常取零均值高斯噪声。此时：

- 用 Kalman Filter 估计状态
- 用 LQR 对估计状态设计控制律

这体现了分离原理（separation principle）：

> 在线性高斯与二次代价条件下，最优估计与最优控制可以分开设计，再组合成闭环。

## 为什么重要

### 1. 它是最优控制中少数可解析求解的大类问题

因此 LQR/LQG 常被当作基准控制器与局部近似工具。

### 2. 它把 Bellman、矩阵分析与稳定性连接起来

Riccati 方程同时体现：

- 值函数思想
- 反馈最优性
- 数值线性代数结构

### 3. 它是 MPC、轨迹优化与强化学习近似方法的重要起点

很多复杂控制器都在局部线性二次近似上建立。

## 最小例子

### 例 1：一阶系统的 LQR 设计

**问题陈述**：一阶系统 $x_{k+1}=x_k+u_k$，代价 $J=\sum_{k=0}^{\infty}(x_k^2+u_k^2)$。求无限时域最优反馈增益 $K$ 和代数 Riccati 方程的解 $P$。

**数学表达**：$A=1$，$B=1$，$Q=1$，$R=1$。离散代数 Riccati 方程：
$$
P = Q + A^\top P A - A^\top P B (R+B^\top P B)^{-1} B^\top P A.
$$

**计算/推理步骤**：

1. 代入数值：$P = 1 + 1\cdot P\cdot 1 - 1\cdot P\cdot1\cdot(1+1\cdot P\cdot1)^{-1}\cdot1\cdot P\cdot1$。
2. 化简：$P = 1 + P - P^2/(1+P)$。
3. 两边乘以 $(1+P)$：$P(1+P) = (1+P)(1+P) - P^2$。
   展开：$P+P^2 = 1+2P+P^2-P^2 = 1+2P$。
   整理得：$P+P^2 = 1+2P \Rightarrow P^2 - P - 1 = 0$。
4. 解得 $P = (1+\sqrt{5})/2 \approx 1.618$（正根）。
5. 反馈增益：$K = (R+B^\top P B)^{-1} B^\top P A = P/(1+P) = 1.618/2.618 \approx 0.618$。
6. 最优控制律：$u_k^\star = -0.618\,x_k$。闭环系统 $x_{k+1}=x_k-0.618x_k=0.382x_k$，稳定（极点 0.382 < 1）。

**结果解读**：一阶 LQR 的 Riccati 方程退化为二次方程，解析可解。$P\approx 1.618$（黄金比例）是值函数的二次系数，反馈 $K\approx 0.618$ 平衡了状态偏差与控制代价。闭环极点 0.382 比开环极点 1 有显著改善（从不稳定到快速衰减）。这个例子清晰展示了 Riccati 方程的完整求解流程和 LQR 设计从模型到反馈的路径。

### 例 2：二阶系统的有限时域 Riccati 递推

**问题陈述**：系统 $x_{k+1}=2x_k+u_k$（$A=2,B=1$），时域 $N=3$，终端代价 $Q_N=0$，步代价 $Q=1,R=1$。求反向 Riccati 递推 $P_3,P_2,P_1$ 和相应反馈增益。

**数学表达**：递推 $P_k=Q+A^\top P_{k+1}A - A^\top P_{k+1}B(R+B^\top P_{k+1}B)^{-1}B^\top P_{k+1}A$，$P_3=0$。

**计算/推理步骤**：

1. $k=3$（终端）：$P_3=0$。
2. $k=2$：$P_2 = 1 + 4\times0 - 2\times0\times(1+0)^{-1}\times2\times0 = 1$。$K_2 = (R+B^\top P_3B)^{-1}B^\top P_3A = 0$。
3. $k=1$：$P_1 = 1 + 4\times1 - 2\times1\times(1+1)^{-1}\times2\times1 = 1+4-4/2 = 3$。$K_1 = 1\times2/(1+1)=1$。即 $u_1^\star = -x_1$。
4. $k=0$：$P_0 = 1 + 4\times3 - 2\times3\times(1+3)^{-1}\times2\times3 = 1+12-36/4=13-9=4$。$K_0 = 3\times2/(1+3)=6/4=1.5$。即 $u_0^\star = -1.5x_0$。

**结果解读**：随着反向递推从终端向初始时刻推进，$P_k$ 从 0 增长到 4，反映了"剩余时间越多，对状态的惩罚越重"的直觉。$K_k$ 从 0（终端时刻无需控制）增加到 1.5（初始时刻需大力校正），体现了时变 LQR 的自然行为——距终端越远，反馈越激进。

## 关键假设与前提检查

1. 线性模型是否足够逼近真实系统
2. 二次代价是否能表达任务目标与控制成本
3. $R$ 是否正定，系统是否可稳定化
4. 部分可观测情形下，估计器误差是否可接受

## 风险与约束

- 强非线性系统上，LQR/LQG 只能作局部近似
- 二次代价可能无法表达硬约束与安全边界
- 噪声若明显非高斯，LQG 假设会变弱
- 只看理论闭环稳定，不等于工程实现就鲁棒

## 在资源受限条件下的可行最优路径

1. 先在局部平衡点附近线性化系统
2. 先设计 LQR 基线控制器
3. 有噪声且不可完全观测时，再接入 Kalman Filter 得到 LQG
4. 若存在显式约束，再转向 MPC

## 与其他条目的关系

- 前置： [矩阵](../../02-核心概念/矩阵.md)、[范数与正定性](../../02-核心概念/范数与正定性.md)、[状态空间模型](../../02-核心概念/状态空间模型.md)
- 前序： [动态规划与递推方法](../05-优化与控制/动态规划与递推.md)、[卡尔曼滤波](../06-数值与计算/Kalman滤波.md)、[HJB 方程](../05-优化与控制/HJB方程.md)
- 后续： [模型预测控制](../05-优化与控制/模型预测控制.md)、约束 LQR、鲁棒 LQG

## 推荐教材与延伸阅读

1. Lancaster, P. & Rodman, L. (1995). *Algebraic Riccati Equations*. Oxford University Press. — Riccati 方程理论的数学专著
2. Anderson, B. D. O. & Moore, J. B. (2007). *Optimal Control: Linear Quadratic Methods*. Dover Publications. — LQR/LQG 的经典系统性论述
3. Zhou, K., Doyle, J. C. & Glover, K. (1996). *Robust and Optimal Control*. Prentice Hall. — 从 LQR 延伸到鲁棒控制的综合教材
