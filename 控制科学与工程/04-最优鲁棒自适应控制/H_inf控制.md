# H∞ 控制 (H-Infinity Control)

## 定位

H∞ 控制是鲁棒控制理论的核心方法，将不确定性下的系统设计从"尝试保证稳定"提升到"在最坏情况扰动下定量优化性能"的层面。与 LQG 最小化平均性能不同，H∞ 最小化最坏情况增益——即对未知扰动具有最强的抑制保证。

由 Zames（1981）提出理论框架，Doyle、Glover、Khargonekar、Francis（1989，DGKF 论文）给出 Riccati 方程解法，H∞ 控制在 1980-1990 年代彻底改变了鲁棒控制的理论与工程实践。

## 核心问题

**核心问题**：给定含有建模不确定性的系统，如何设计控制器使其对最坏情况扰动具有最小增益？

即最小化从扰动 $w$ 到评价输出 $z$ 的 H∞ 范数：

$$
\|T_{zw}\|_\infty = \sup_{\omega} \bar{\sigma}(T_{zw}(j\omega))
$$

其中 $\bar{\sigma}$ 表示最大奇异值。

## 基本模型

### H∞ 范数

H∞ 范数衡量传递函数在所有频率上的最大增益——即系统对正弦输入的最坏情况放大倍数：

$$
\|G\|_\infty = \sup_{\omega} \bar{\sigma}(G(j\omega))
$$

物理含义：系统在最坏频率下的最大振幅放大比。

### 小增益定理 (Small Gain Theorem)

小增益定理是鲁棒稳定性分析的基础：

如果两个稳定系统 $G$ 和 $\Delta$ 互联，且 $\|G\|_\infty \cdot \|\Delta\|_\infty < 1$，则互联系统保持稳定。

对于鲁棒控制：若 $\|G\|_\infty < 1/\gamma$ 且不确定性 $\|\Delta\|_\infty < \gamma$，则系统对 $\Delta$ 鲁棒稳定。

### 标准 H∞ 问题

广义被控对象 $P(s)$ 连接控制器 $K(s)$：

$$
\begin{bmatrix} z \\ y \end{bmatrix} = P(s) \begin{bmatrix} w \\ u \end{bmatrix}, \quad u = K(s) y
$$

其中 $z$ 为评价输出，$y$ 为测量输出，$w$ 为外部扰动，$u$ 为控制输入。

闭环传递函数 $T_{zw} = \mathcal{F}_l(P, K)$（下线性分式变换, LFT）。H∞ 控制的目标是找到 $K$ 使 $\|T_{zw}\|_\infty < \gamma$ 且闭环内部稳定。

### 混合灵敏度 H∞ 问题

最常见的 H∞ 设计配置是加权混合灵敏度：

$$
\min_K \left\| \begin{bmatrix} W_p S \\ W_u K S \\ W_t T \end{bmatrix} \right\|_\infty
$$

其中 $S = (I + GK)^{-1}$ 为灵敏度函数（扰动抑制），$T = GK(I+GK)^{-1}$ 为补灵敏度函数（鲁棒性）。加权函数 $W_p, W_u, W_t$ 在各频段设定不同的性能/鲁棒目标。

## 关键概念

### H∞ 与 H2 (LQG) 的本质区别

| 维度 | H2 (LQG) | H∞ |
|:---|:---|:---|
| 优化目标 | 最小化均方根能量（平均情况） | 最小化最坏情况增益（峰值） |
| 噪声假设 | 高斯白噪声 | 有界能量扰动（无统计假设） |
| 鲁棒性 | 无固有保证（Doyle 反例） | 有小增益定理保证 |
| 范数 | $\|G\|_2 = \sqrt{\frac{1}{2\pi}\int \operatorname{tr}(G^*G)d\omega}$ | $\|G\|_\infty = \sup_\omega \bar{\sigma}(G)$ |

### Riccati 方程解法（DGKF 1989）

标准 H∞ 问题通过求解两个代数 Riccati 方程来获得 $K(s)$：

$$
X = \operatorname{Ric}\left( \begin{bmatrix} A & \gamma^{-2}B_1B_1^T - B_2B_2^T \\ -C_1^T C_1 & -A^T \end{bmatrix} \right)
$$
$$
Y = \operatorname{Ric}\left( \begin{bmatrix} A^T & \gamma^{-2}C_1^T C_1 - C_2^T C_2 \\ -B_1B_1^T & -A \end{bmatrix} \right)
$$

需满足 $\rho(XY) < \gamma^2$（谱半径条件）。控制器 $K(s)$ 的阶数不超过广义被控对象的阶数。

### LMI 解法

H∞ 问题也可以表述为线性矩阵不等式（LMI）：

$$
\begin{bmatrix} A^T P + P A & P B & C^T \\ B^T P & -\gamma I & D^T \\ C & D & -\gamma I \end{bmatrix} \prec 0
$$

LMI 公式的优势：可自然处理多目标设计（同时约束 H2 和 H∞ 性能）、结构约束、时变参数等。

### mu 综合 (Structured Singular Value)

标准 H∞ 假设不确定性为满块有界（full-block bounded），过于保守。mu 综合将不确定性分解为块对角结构 $\Delta = \operatorname{diag}(\Delta_1, \ldots, \Delta_n)$，结构化奇异值 $\mu$ 提供更紧致的鲁棒性分析。

$$
\mu_{\Delta}(M) = \frac{1}{\min\{\bar{\sigma}(\Delta) : \det(I - M\Delta) = 0, \Delta \in \boldsymbol{\Delta}\}}
$$

## 工程判断

### 加权函数的选择

加权函数是 H∞ 设计中最重要的工程判断——它们编码了设计规范：
- $W_p(s)$：在低频大增益（小 $S$ 保证跟踪/扰动抑制）；
- $W_t(s)$：在高频大增益（小 $T$ 保证传感器噪声抑制和鲁棒性）；
- $W_u(s)$：限制控制幅度。

### H∞ 控制器阶数

H∞ 控制器阶数等于广义被控对象阶数（包括加权函数）。工程中通常需要配合模型降阶（如平衡截断 balanced truncation）来获得可实现的低阶控制器。

### 优势与局限

优点：最坏情况保证、系统化的设计流程、成熟的计算工具（MATLAB Robust Control Toolbox）。
局限：设计保守（范数有界不确定性假设）、加权函数选择需经验、控制器阶数可能较高。

## 常见误区

### "H∞ 设计自动保证对所有不确定性稳定"
仅当不确定性被正确建模为范数有界且满足小增益条件时成立。

### "H∞ 控制器一定比 PID 好"
对于简单系统，PID 加足够裕度同样有效。H∞ 适合高要求复杂系统（柔性结构、飞行器、精密伺服）。

### "gamma 迭代总是收敛到全局最优"
H∞ 问题是凸的但求解算法可能受数值条件影响，高维度系统中的 Riccati 方程求解可能遇到数值困难。

## 回链

- [LQG 与分离原则](../03-现代控制/LQG与分离原则.md)
- [分布式与分散式控制](./分布式与分散式控制.md)
- [性能、约束与权衡](../01-基础理论/性能约束与权衡.md)
- [不确定性、扰动与噪声](../01-基础理论/不确定性扰动与噪声.md)
