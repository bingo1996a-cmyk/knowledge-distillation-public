# 凸共轭与 Fenchel 对偶

## 作用

凸共轭（Convex Conjugate）与 Fenchel 对偶（Fenchel Duality）是凸分析的核心工具。  
它把“原函数上的优化问题”转换为“对偶变量上的优化问题”，比基本拉格朗日对偶更一般，也更适合处理正则化、稀疏估计、分布匹配与变分推断。

## 凸共轭的定义

给定函数 $f: \mathbb{R}^n \to (-\infty,+\infty]$，其凸共轭定义为

$$
f^\ast(y)=\sup_{x\in\mathbb{R}^n}\{\langle y,x\rangle - f(x)\}
$$

这里 $\langle y,x\rangle$ 是内积。  
直观上，$f^\ast$ 描述的是函数 $f$ 在对偶空间中的“支撑超平面斜率成本”。

## 几何直观

若把 $f(x)$ 看作一张凸曲面，则 $f^\ast(y)$ 刻画的是斜率为 $y$ 的线性函数与该曲面之间最优贴合后的剩余量。  
因此，凸共轭本质上是原函数的“斜率视角表达”。

## Fenchel-Young 不等式

对任意 $x,y$，都有

$$
f(x)+f^\ast(y)\ge \langle x,y\rangle
$$

当且仅当 $y\in \partial f(x)$ 时取等号，这里 $\partial f(x)$ 是次梯度（subdifferential）。

## 双共轭

在适当条件下，闭凸函数满足

$$
f^{\ast\ast}=f
$$

这称为 Fenchel-Moreau 定理（Fenchel-Moreau Theorem）。  
它说明：闭凸函数可以由其所有支撑超平面完全恢复。

## Fenchel 对偶的基本形式

考虑原问题

$$
\inf_x \{f(x)+g(Ax)\}
$$

其 Fenchel 对偶问题常写为

$$
\sup_y \{-f^\ast(-A^\top y)-g^\ast(y)\}
$$

这个形式在信号处理、机器学习和变分问题中非常常见。

## 为什么重要

### 1. 统一很多正则化模型

例如 Lasso、支持向量机、最大熵模型、变分推断、最优传输等问题，都可以通过共轭与对偶重写。

### 2. 连接原始变量与对偶变量

原问题有时难以直接解，但对偶问题可能更低维、更易并行、或更适合分解算法。

### 3. 帮助理解近端方法

许多近端算法（proximal methods）和 Moreau 分解都建立在共轭理论上。

## 一个典型例子

设

$$
f(x)=\frac{1}{2}\|x\|_2^2
$$

则其共轭仍为

$$
f^\ast(y)=\frac{1}{2}\|y\|_2^2
$$

这说明二次函数在共轭变换下具有自对偶性。

又如指示函数 $\iota_C(x)$ 的共轭是集合 $C$ 的支撑函数（support function）。

## 与拉格朗日对偶的关系

- [优化中的对偶理论](../05-优化与控制/优化中的对偶.md) 更强调约束优化下的乘子结构
- Fenchel 对偶更强调函数分解、线性映射与共轭变换
- 两者都属于“通过对偶变量重写原问题”的大框架

## 在机器学习中的常见位置

- 正则化风险最小化
- 稀疏优化与 $\ell_1$ 惩罚
- 变分下界与 KL 项重写
- 对偶坐标上升法
- 分布鲁棒优化与 Wasserstein 球约束

## 与其他条目的关系

- 前置： [凸性](../../02-核心概念/凸性.md)、[内积](../../02-核心概念/内积.md)
- 前序： [优化中的对偶理论](../05-优化与控制/优化中的对偶.md)
- 后续：内点法、近端方法、分布鲁棒优化
- 应用： [机器学习中的数学](../../04-应用/机器学习中的数学.md)、[最优控制中的数学](../../04-应用/最优控制中的数学.md)

## 最小例子

### 例 1：$\ell_1$ 范数的凸共轭

- **问题陈述**：求 $f(x) = \|x\|_1$ 的凸共轭 $f^*(y)$。
- **数学表达**：$f^*(y) = \sup_{x\in\mathbb{R}^n} \{\langle y,x\rangle - \|x\|_1\}$。
- **计算/推理步骤**：对每个分量，$\langle y,x\rangle - |x_i| = y_i x_i - |x_i|$。若 $|y_i|>1$，取 $x_i \to \infty$ 得无穷大。若 $|y_i|\leq 1$，最大值在 $x_i=0$ 处取 0。故 $f^*(y) = \begin{cases} 0 & \|y\|_\infty \leq 1 \\ +\infty & \text{otherwise} \end{cases}$，即 $\ell_\infty$ 单位球的指示函数。
- **结果解读**：$\ell_1$ 范数的共轭是 $\ell_\infty$ 单位球的指示函数，这解释了 $\ell_1$ 正则化与对偶变量有界性之间的对偶关系。

### 例 2：Fenchel 对偶——最小二乘与 $\ell_1$ 正则化

- **问题陈述**：把 Lasso 问题 $\min_x \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$ 写成 Fenchel 对偶形式。
- **数学表达**：设 $f(x)=\frac{1}{2}\|Ax-b\|^2$，$g(x)=\lambda\|x\|_1$。Fenchel 对偶为 $\sup_y \{-f^*(-A^\top y) - g^*(y)\}$。
- **计算/推理步骤**：$f$ 的共轭：$f^*(z)=\frac{1}{2}\|z\|^2 + \langle z,b\rangle$（平方后平移性质）。$g^*(y)=\iota_{\|\cdot\|_\infty \leq \lambda}(y)$（由例 1 缩放得）。故对偶问题为 $\sup_y \{-\frac{1}{2}\|A^\top y\|^2 + \langle A^\top y, b\rangle\}$ s.t. $\|y\|_\infty \leq \lambda$。
- **结果解读**：Fenchel 对偶把 Lasso 转化为一个约束在 $\ell_\infty$ 球上的二次规划，对偶变量 $y$ 的维度等于样本数，而非变量数。

## 风险提示

- 非凸问题中直接照搬共轭与对偶结论常会失效
- 若不区分闭包、适当函数、可微与不可微条件，公式容易写对但结论用错

## 推荐教材与延伸阅读

- Rockafellar, R. T. (1970). *Convex Analysis*. Princeton University Press. — 凸分析的经典，第 12—13 章深入处理共轭与 Fenchel 对偶。
- Boyd, S. & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press. — 第 3 章以优化视角介绍共轭，第 5 章介绍对偶。
- Bauschke, H. H. & Combettes, P. L. (2017). *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd ed. Springer. — 更严格的泛函分析处理，适合深入理论。
