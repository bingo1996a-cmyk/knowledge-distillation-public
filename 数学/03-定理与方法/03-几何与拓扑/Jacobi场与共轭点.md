# Jacobi 场与共轭点

## 作用

Jacobi 场（Jacobi Field）是沿测地线的变分向量场，描述了一族"相邻"测地线如何偏离或聚集。它是连接曲率与测地线稳定性、共轭点与 Morse 理论的桥梁。在广义相对论中，Jacobi 场描述了引力潮汐力；在几何控制中，它用于分析路径最优性的二阶条件。

## 定义与方程

设 $\gamma(t)$ 是 Riemann 流形 $(M,g)$ 上的测地线。沿 $\gamma$ 的向量场 $J(t)$ 若满足 **Jacobi 方程**：

$$
\frac{D^2 J}{dt^2} + R(J,\dot\gamma)\dot\gamma = 0
$$

则称 $J$ 为 Jacobi 场。其中 $\frac{D}{dt}$ 是沿 $\gamma$ 的协变导数，$R$ 是曲率张量。

### Jacobi 方程的物理意义

- 在球面（正曲率 $K>0$）上：邻近测地线相互靠拢（汇聚）
- 在鞍面（负曲率 $K<0$）上：邻近测地线相互远离（发散）
- 在平直空间（$K=0$）上：邻近测地线保持平行

## 共轭点

若存在非零 Jacobi 场 $J$ 在 $t=0$ 和 $t=t_0$ 处均为零，则 $\gamma(t_0)$ 称为 $\gamma(0)$ 沿 $\gamma$ 的**共轭点**（Conjugate Point）。

**关键结论**：测地线在经过第一个共轭点之后不再是最短的。这推广了球面上"大圆弧超过半圆后不再最短"的经典事实。

## 最小例子

### 例 1：单位球面 $S^2$ 上的 Jacobi 场

球面 $S^2$ 上，Gauss 曲率 $K=1$。沿赤道测地线（大圆），取垂直于赤道的 Jacobi 场 $J(t)=(\sin t)N(t)$，其中 $N$ 是单位法向量。

Jacobi 方程：$\frac{D^2J}{dt^2} + R(J,\dot\gamma)\dot\gamma = \ddot{J} + J = 0$（因 $K=1$）。

$J(t)=\sin t$ 在 $t=0$ 和 $t=\pi$ 处为零。因此赤道上的对径点是共轭点——沿大圆走过半圆（$\pi$ 弧度）后，测地线失去最短性。

### 例 2：柱面上的 Jacobi 场

柱面 $\mathbb{R}\times S^1$ 的 Gauss 曲率 $K=0$。沿母线方向，Jacobi 场 $J(t)=at+b$ 是线性的——邻近测地线既不收敛也不发散，保持恒定距离。共轭点不存在。

### 例 3：负曲率与测地线偏离

双曲平面（$K=-1$）上，Jacobi 方程变为 $\ddot{J} - J = 0$，解为 $J(t)=Ae^t + Be^{-t}$——邻近测地线指数级发散。这是混沌动力系统对初值敏感依赖的几何根源。

## 与其他概念的关系

- 前置： [联络、曲率与测地线](./联络曲率与测地线.md)
- 前置： [曲线、曲面与流形的微分几何](./曲线曲面与流形的微分几何.md)
- 延伸：Morse 指数定理、Bonnet-Myers 定理（正曲率紧致性）
- 应用： [物理中的数学](../../04-应用/物理中的数学.md)（潮汐力、引力透镜）

## 推荐教材与延伸阅读

1. do Carmo, *Riemannian Geometry*（Birkhäuser）——第5章（Jacobi场）和第9章（比较定理）的论述清晰。
2. Lee, *Introduction to Riemannian Manifolds*（2nd ed., Springer GTM 176）——第10章Jacobi场的现代处理。
3. Cheeger & Ebin, *Comparison Theorems in Riemannian Geometry*（AMS Chelsea）——比较定理的经典专著，Jacobi场是核心工具。
