# 近端方法、ADMM 与算子分裂

## 作用

近端方法（Proximal Methods）处理的是“目标函数可分解，但其中一部分不光滑或不适合直接求梯度”的优化问题。  
ADMM（Alternating Direction Method of Multipliers）则是在可分结构与约束耦合存在时非常常用的一类分裂算法。

它们在稀疏优化、Lasso、约束学习、分布式优化、MPC 与大规模机器学习中都非常重要。

## 为什么普通梯度法不够

很多问题可写为

$$
\min_x\ f(x)+g(x)
$$

其中：

- $f$ 光滑，可求梯度
- $g$ 可能不光滑，但结构简单，例如 $\ell_1$ 范数、指标函数、核范数等

这类问题上，直接梯度下降往往不适用或收敛很差。

## 近端算子

近端方法的核心对象是近端算子（proximal operator）：

$$
\operatorname{prox}_{\lambda g}(v)=\arg\min_x \left\{g(x)+\frac{1}{2\lambda}\|x-v\|_2^2\right\}
$$

它可理解为：在保持靠近 $v$ 的同时，向满足 $g$ 结构的方向做一步“受控投影”。

## 近端梯度法

若问题为 $f+g$ 型，则一个标准更新是

$$
x^{k+1}=\operatorname{prox}_{\lambda g}\bigl(x^k-\lambda\nabla f(x^k)\bigr)
$$

这也称为前向-后向分裂（forward-backward splitting）。

### 典型例子：软阈值

当

$$
g(x)=\|x\|_1
$$

其近端映射对应软阈值（soft-thresholding）算子。

## ADMM 的标准形式

考虑带耦合约束的问题：

$$
\min_{x,z} f(x)+g(z)
\quad \text{s.t.}\quad Ax+Bz=c
$$

其增广拉格朗日函数可写为

$$
\mathcal L_\rho(x,z,y)=f(x)+g(z)+y^\top(Ax+Bz-c)+\frac\rho2\|Ax+Bz-c\|_2^2
$$

ADMM 交替更新：

$$
x^{k+1}=\arg\min_x \mathcal L_\rho(x,z^k,y^k)
$$

$$
z^{k+1}=\arg\min_z \mathcal L_\rho(x^{k+1},z,y^k)
$$

$$
y^{k+1}=y^k+\rho\bigl(Ax^{k+1}+Bz^{k+1}-c\bigr)
$$

## 为什么重要

### 1. 它擅长处理结构化大问题

很多问题整体难，但分块后每一步都容易。

### 2. 它天然适合约束优化与分布式求解

因此在网络优化、MPC、图学习、联邦与分布式训练中很常见。

### 3. 它把对偶思想和数值算法结合起来

ADMM 不是纯粹启发式，而是增广拉格朗日与算子分裂思想的实现。

## 关键假设与前提检查

1. 问题是否具有可分结构
2. 每个子问题是否容易解或近似解
3. 是否更关心高精度解，还是更关心可扩展与工程可用
4. 参数 $\rho$ 与步长是否有合理调节策略

## 最小例子

### 例 1：Lasso 问题的近端梯度求解

**问题陈述**：Lasso 回归 $\min_x \frac12 \|Ax - b\|_2^2 + \lambda \|x\|_1$，其中 $A = \begin{bmatrix}2 & 0 \\ 0 & 1\end{bmatrix}$，$b = \begin{bmatrix}4 \\ 1\end{bmatrix}$，$\lambda = 0.5$。用近端梯度法求解。

**数学表达**：目标 $f(x) = \frac12 \|Ax-b\|_2^2$，$g(x) = \lambda \|x\|_1$。近端梯度更新：$x^{k+1} = \operatorname{prox}_{\alpha \lambda \|\cdot\|_1}(x^k - \alpha \nabla f(x^k))$。

**计算/推理步骤**：
1. $\nabla f(x) = A^T(Ax - b) = \begin{bmatrix}4x_1 - 8 \\ x_2 - 1\end{bmatrix}$。
2. 软阈值算子：$\operatorname{prox}_{\alpha \lambda \|\cdot\|_1}(v) = \operatorname{sign}(v) \cdot \max(|v| - \alpha\lambda, 0)$。
3. 设置 $\alpha = 0.2$（满足 $\alpha \le 1/\|A^T A\| = 1/4$），从 $x^0 = (0, 0)$ 出发。
4. 第一步：$\nabla f(x^0) = (-8, -1)$。梯度步：$x^0 - \alpha \nabla f = (0, 0) - 0.2(-8, -1) = (1.6, 0.2)$。软阈值：$\operatorname{prox}_{0.1}(1.6) = \max(|1.6|-0.1, 0) \cdot \operatorname{sign}(1.6) = 1.5$；$\operatorname{prox}_{0.1}(0.2) = \max(0.2-0.1, 0) = 0.1$。$x^1 = (1.5, 0.1)$。
5. 迭代至收敛（约 30 步）：$x^* \approx (1.82, 0.80)$。

**结果解读**：近端梯度法将 Lasso 的 $\ell_1$ 正则项转化为每步计算软阈值操作，实现简单且收敛快。软阈值将小于 $\alpha\lambda$ 的系数直接置零（产生稀疏解），这正是 $\ell_1$ 正则化的稀疏诱导特性。

### 例 2：ADMM 求解等式约束二次规划

**问题陈述**：$\min_{x,z} (x-1)^2 + (z+1)^2$，约束 $x + z = 0$。用 ADMM 求解。

**数学表达**：增广拉格朗日 $\mathcal{L}_\rho(x, z, y) = (x-1)^2 + (z+1)^2 + y(x+z) + (\rho/2)(x+z)^2$。

**计算/推理步骤**：
1. 设置 $\rho = 1$，初始化 $x^0 = 0$，$z^0 = 0$，$y^0 = 0$。
2. $x$ 更新（固定 $z^k, y^k$）：$\min_x (x-1)^2 + y^k x + (\rho/2)(x+z^k)^2$。对 $x$ 求导得 $2(x-1) + y + (x+z) = 0 \Rightarrow 3x = 2 - y - z$。代入 $y^0=0, z^0=0$：$3x = 2 \Rightarrow x^1 = 2/3$。
3. $z$ 更新（固定 $x^{k+1}, y^k$）：$\min_z (z+1)^2 + y^k z + (\rho/2)(x^{k+1}+z)^2$。求导得 $2(z+1) + y + (x+z) = 0 \Rightarrow 3z = -2 - y - x$。代入 $x^1=2/3, y^0=0$：$3z = -2 - 0 - 2/3 = -8/3 \Rightarrow z^1 = -8/9$。
4. 对偶更新：$y^1 = y^0 + \rho(x^1 + z^1) = 0 + (2/3 - 8/9) = -2/9$。
5. 第 2 步：$x^2$ 用 $y^1, z^1$ 更新：$3x = 2 - (-2/9) - (-8/9) = 2 + 2/9 + 8/9 = 28/9 \Rightarrow x^2 = 28/27$。
   $z^2$ 用 $x^2, y^1$ 更新：$3z = -2 - (-2/9) - 28/27 = -2 + 2/9 - 28/27 = (-54 + 6 - 28)/27 = -76/27 \Rightarrow z^2 = -76/81$。
6. 真解：$x^* = -z^* = 1$（检查：$(1-1)^2 + (-1+1)^2 = 0$，$1 + (-1) = 0$）。ADMM 迭代趋近此值。

**结果解读**：ADMM 通过交替更新原始变量和对偶变量来求解含约束优化。增广拉格朗日中的 $\rho$ 控制约束违反的惩罚力度，对偶变量 $y$ 累积约束误差信息。本例收敛速度由 $\rho$ 和问题条件数共同决定。

## 在资源受限条件下的可行最优路径

1. 先掌握投影、近端映射与次梯度直觉
2. 先从 Lasso、约束二次规划等标准问题上实现近端梯度与 ADMM
3. 再迁移到 MPC、分布式优化与稀疏学习
4. 需要高精度与中等规模时，再与内点法比较

## 与其他条目的关系

- 前置： [凸性](../../02-核心概念/凸性.md)、[优化中的对偶理论](../05-优化与控制/优化中的对偶.md)、[凸共轭与 Fenchel 对偶](../05-优化与控制/凸共轭与Fenchel对偶.md)
- 前序： [梯度下降](../05-优化与控制/梯度下降.md)、[内点法](../05-优化与控制/内点法.md)
- 应用： 稀疏建模、约束学习、MPC、分布式优化

## 推荐教材与延伸阅读

- Parikh, N. & Boyd, S. (2014). "Proximal Algorithms". *Foundations and Trends in Optimization*, 1(3), 127–239. — 近端方法的系统综述，理论与算法兼顾。
- Boyd, S., Parikh, N., Chu, E., Peleato, B. & Eckstein, J. (2011). "Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers". *Foundations and Trends in Machine Learning*, 3(1), 1–122. — ADMM 的最权威综述与入门文献。
- Beck, A. (2017). *First-Order Methods in Optimization*. SIAM. — 第 6—10 章覆盖近端梯度、近端算子与分裂方法的严格理论。
