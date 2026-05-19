# 最优控制与 Pontryagin 极大值原理

## 作用

最优控制（Optimal Control）研究如何为动态系统选择控制输入，使性能指标达到最优。  
Pontryagin 极大值原理（Pontryagin Maximum Principle, PMP）是连续时间最优控制中的基础必要条件。

## 基本问题

考虑连续时间系统

$$
\dot x(t)=f(x(t),u(t),t),\qquad x(0)=x_0
$$

目标是最小化代价泛函

$$
J = \phi(x(T)) + \int_0^T L(x(t),u(t),t)\,dt
$$

其中 $u(t)$ 是控制函数，$L$ 是运行代价，$\phi$ 是终端代价。

## Hamiltonian 构造

定义 Hamiltonian：

$$
H(x,u,\lambda,t)=L(x,u,t)+\lambda^\top f(x,u,t)
$$

其中 $\lambda(t)$ 是伴随变量（costate / adjoint variable）。

## Pontryagin 极大值原理的基本形式

若 $u^\ast(t)$ 是最优控制，则在适当正则条件下，存在伴随变量 $\lambda(t)$ 使得：

### 1. 状态方程

$$
\dot x^\ast(t)=\frac{\partial H}{\partial \lambda}(x^\ast,u^\ast,\lambda,t)
$$

### 2. 伴随方程

$$
\dot \lambda(t)=-\frac{\partial H}{\partial x}(x^\ast,u^\ast,\lambda,t)
$$

### 3. 最优性条件

最优控制应在允许集合上使 Hamiltonian 取极小或极大（取决于问题约定）。常见最小化形式为

$$
u^\ast(t) \in \arg\min_{u\in \mathcal{U}} H(x^\ast(t),u,\lambda(t),t)
$$

### 4. 终端条件

若终端状态自由，则常有

$$
\lambda(T)=\nabla_x \phi(x(T))
$$

## 直观理解

- 状态方程描述“系统如何走”
- 伴随方程描述“代价敏感度如何反传”
- Hamiltonian 最优性条件描述“当前控制应如何平衡即时成本与未来影响”

这与现代最优控制、变分法、模型预测控制和策略梯度中的敏感度分析都有深层联系。

## 与动态规划的关系

- PMP 给出必要条件，偏局部轨迹视角
- 动态规划给出 Bellman 方程，偏全局值函数视角

在足够光滑条件下，两者可通过 Hamilton-Jacobi-Bellman（HJB）理论联系起来。

## 一个典型二次型问题

若系统线性、代价二次，则进入线性二次调节（Linear Quadratic Regulator, LQR）框架。  
这类问题常能导出 Riccati 方程并得到反馈控制律。

## 为什么重要

- 它是连续时间控制优化的标准必要条件
- 它帮助理解伴随变量、协态变量与梯度反传之间的统一性
- 它是航迹优化、能量管理、模型预测控制和微分博弈的重要入口

## 关键假设与前提检查

1. 状态方程是否可微并满足存在唯一解
2. 控制约束是否明确
3. 终端条件与性能指标是否定义清楚
4. 问题是否存在异常极值或奇异弧

## 最小例子

### 例 1：一阶系统的能量最优控制

**问题陈述**：系统 $\dot x=u$，$x(0)=0$，$T=1$，$x(1)=1$。代价 $J=\int_0^1\frac12u^2dt$。

**数学表达**：Hamiltonian $H=\frac12u^2+\lambda u$。PMP: $\dot\lambda=-\partial H/\partial x=0$，$u^*=\arg\min_u H$。

**计算步骤**：

- 伴随方程：$\dot\lambda=0\Rightarrow\lambda(t)\equiv c$（常数）
- 最优条件：$\partial H/\partial u=u+\lambda=0\Rightarrow u^*(t)=-\lambda(t)=-c$
- 状态：$\dot x=-c$，$x(t)=-c t+d$。由 $x(0)=0$ 得 $d=0$；$x(1)=1$ 得 $-c=1\Rightarrow c=-1$
- 最优控制：$u^*(t)=1$，最优轨迹 $x^*(t)=t$，最小代价 $J^*=0.5$

**结果解读**：PMP 将最优控制问题归结为两点边值问题。本例中，常数控制 $u=1$ 是最优的——以恒定功率推进最小化能量，满足终端约束。

### 例 2：含状态阻尼的 LQ 问题

**问题陈述**：系统 $\dot x=-x+u$，$x(0)=2$，$T=1$，代价 $J=\int_0^1(x^2+u^2)dt$，终端代价 $\phi(x(1))=0$。

**数学表达**：$H=x^2+u^2+\lambda(-x+u)$。PMP 伴随方程 $\dot\lambda=-\partial H/\partial x=-2x+\lambda$，最优控制 $u^*=-\frac12\lambda$。

**计算步骤**：

- 最优控制代入：$u=-\lambda/2$，得 $\dot x=-x-\lambda/2$
- 伴随-状态系统：
  $\begin{cases}\dot x=-x-\lambda/2,\quad x(0)=2\\ \dot\lambda=\lambda-2x,\quad \lambda(1)=0\end{cases}$
- 猜解 $x$ 和 $\lambda$ 的线性组合。试 $x(t)=ae^{rt}$，$\lambda(t)=be^{rt}$：
  $r a=-a-b/2$，$r b=b-2a$。解得 $r=\pm\sqrt3$
- 由边界条件确定系数，得 $x(t)\approx2.154e^{\sqrt3 t}+0.122e^{-\sqrt3 t}$，$u^*(t)=-\lambda(t)/2\approx-1.038e^{\sqrt3 t}+0.372e^{-\sqrt3 t}$

**结果解读**：含阻尼的 LQ 问题展示了 PMP 的完整求解流程——Hamiltonian 最小化 + 伴随方程 + 边界条件构成两点边值问题。其解包含正指数成分（系统需要主动控制对抗阻尼），与例 1 的纯驱动机理不同。

## 风险与约束

- PMP 常提供必要而非充分条件
- 非凸约束下可能出现多个驻值轨迹
- 连续时间解析推导可行，不代表数值求解容易

## 与其他条目的关系

- 前置： [导数](../../02-核心概念/导数.md)、[状态空间模型](../../02-核心概念/状态空间模型.md)、[凸性](../../02-核心概念/凸性.md)
- 前序： [拉格朗日乘子法](../05-优化与控制/Lagrange乘子.md)、[KKT 条件](../05-优化与控制/KKT条件.md)、[动态规划与递推方法](../05-优化与控制/动态规划与递推.md)
- 后续：LQR、HJB 方程、模型预测控制、随机控制
- 应用： [控制与优化中的数学](../../04-应用/控制与优化中的数学.md)、[最优控制中的数学](../../04-应用/最优控制中的数学.md)

## 推荐教材与延伸阅读

- Kirk, D. E. (2004). *Optimal Control Theory: An Introduction*. Dover. — 入门经典，直观且有大量工程实例，特别适合自学。
- Bryson, A. E. & Ho, Y.-C. (1975). *Applied Optimal Control: Optimization, Estimation and Control*. Taylor & Francis. — 应用导向的经典，PMP 与 LQR 的工程细节丰富。
- Liberzon, D. (2012). *Calculus of Variations and Optimal Control Theory: A Concise Introduction*. Princeton University Press. — 简明现代的教材，从变分法到 PMP 再到 HJB 过渡自然。
