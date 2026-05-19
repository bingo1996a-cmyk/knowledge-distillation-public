# Pontryagin 最大值原理 (Pontryagin's Maximum Principle, PMP)

## 定位

Pontryagin 最大值原理（PMP）提供最优控制的**必要条件**（而非 HJB 的充分条件），通过引入协态变量（costate）将约束优化转化为 Hamiltonian 系统的两点边值问题（Two-Point Boundary Value Problem, TPBVP）。PMP 特别适合处理有输入约束和控制量受限的最优控制问题——当控制量出现在约束边界上时，PMP 自然给出 Bang-Bang 控制结构。

由俄罗斯数学家 Lev Pontryagin 及其学生在 1950 年代建立，PMP 与 Bellman 动态规划共同构成最优控制理论的两大支柱。

## 核心问题

**核心问题**：给定系统动力学和代价函数，如何求解最优控制输入的必要条件？

PMP 回答的是：**如果 $u^*(t)$ 是最优控制，那么它必须满足什么条件？** 它与 HJB 的根本区别在于：
- HJB 给出充分条件（如果找到了解，它一定是最优的）；
- PMP 给出必要条件（如果是最优的，它必须满足这些条件）；
- PMP 比 HJB 更容易在数值上求解，特别是存在输入约束时。

## 基本模型

### 问题表述（Bolza 型）

考虑系统 $\dot{x} = f(x, u, t)$，代价函数：

$$
J = \int_{t_0}^{t_f} \ell(x(t), u(t), t) dt + \phi(x(t_f))
$$

### Hamiltonian 与 PMP 条件

定义 Hamiltonian 函数：

$$
H(x, u, \lambda, \lambda_0) = \lambda_0 \ell(x, u) + \lambda^T f(x, u)
$$

其中 $\lambda(t) \in \mathbb{R}^n$ 为协态变量（costate），$\lambda_0 \geq 0$ 为常数。

PMP 的必要条件为：

1. **状态方程**：$\dot{x} = \frac{\partial H}{\partial \lambda} = f(x, u)$
2. **协态方程**：$\dot{\lambda} = -\frac{\partial H}{\partial x} = -\frac{\partial f}{\partial x}^T \lambda - \lambda_0 \frac{\partial \ell}{\partial x}^T$
3. **横截条件**（自由终端状态）：$\lambda(t_f) = \lambda_0 \frac{\partial \phi}{\partial x}\big|_{t_f}$
4. **Hamiltonian 最小化条件**：$H(x^*, u^*, \lambda, \lambda_0) \leq H(x^*, u, \lambda, \lambda_0)$ 对所有允许的 $u$ 成立

### 正则形式与边值问题

状态和协态方程构成 Hamiltonian 系统的正则方程（canonical equations）：

$$
\dot{x} = \frac{\partial H}{\partial \lambda}, \quad \dot{\lambda} = -\frac{\partial H}{\partial x}
$$

加上边界条件（初始状态固定 $x(t_0)=x_0$，终端条件来自横截条件），构成两点边值问题。

## 重要推论：Bang-Bang 控制与奇异弧

### Bang-Bang 控制

当 Hamiltonian 对控制 $u$ 是线性的（即 $H = H_0 + \psi^T u$，其中 $\psi$ 为切换函数），最小化条件导致：

$$
u^*_i = \begin{cases}
u_{i,\min} & \text{if } \psi_i > 0 \\
u_{i,\max} & \text{if } \psi_i < 0
\end{cases}
$$

即最优控制总是在边界上切换——这就是 Bang-Bang 控制。切换函数 $\psi_i$ 过零点决定了切换时间。

### 奇异弧 (Singular Arc)

当切换函数在某段时间区间内恒为零（$\psi_i(t) \equiv 0$），PMP 不提供 $u$ 的显式信息。此时需要计算 $\psi$ 的各阶时间导数来隐含确定控制——此段称为奇异弧，对应的控制称为奇异控制。

奇异弧在能量最优问题（如最小燃料消耗）中常见，需要额外的条件（广义 Legendre-Clebsch 条件）来保证最优性。

## 关键概念

### 协态变量的含义

协态 $\lambda(t)$ 具有"影子价格"的解释——它表示状态变化对最优代价的边际影响。具体地：

$$
\lambda_i(t) = \frac{\partial J^*}{\partial x_i(t)}
$$

即如果 $x_i(t)$ 增加一个微小量，最优代价 $J^*$ 会变化多少。这一解释与经济学中的 Lagrange 乘子完全一致。

### PMP 与 HJB 的关系

PMP 可以从 HJB 方程推导出来：假设价值函数 $V(x,t)$ 光滑，定义 $\lambda = \partial V/\partial x$，则协态方程和 Hamiltonian 最小化条件都可以从 HJB 导出。因此：

- HJB 是充分条件（需要 $V$ 光滑可微）；
- PMP 是必要条件（允许 $V$ 非光滑，但要求极值轨线存在）；
- PMP 比 HJB 适用范围更广（可处理状态约束、非光滑价值函数）；
- 两者在光滑情形下等价。

### 切换函数与切换结构

切换函数 $\psi(t) = \lambda^T(t) g(x(t))$（其中 $g$ 为控制系数矩阵）决定了最优控制的切换结构。切换次数和切换时间点需要通过数值求解 TPBVP 来确定。

## 工程判断

### PMP 主要通过数值方法求解

PMP 的自然求解框架是间接法（indirect method）：
- **打靶法（Shooting Method）**：猜测初始协态 $\lambda(0)$，正向积分状态和协态方程，检查终端条件是否满足，迭代修正；
- **多点边值问题**：存在状态约束或切换结构时，需在切换点拼接，解决多点边值问题。

数值困难：对初始猜测敏感、对刚性系统不稳定、协态初值无物理意义。

### 直接配点法 vs. PMP 间接法

现代轨迹优化中，直接配点法（direct collocation）将最优控制问题离散化为非线性规划（NLP），比间接法更鲁棒且不需要推导协态方程。但 PMP 提供的结构洞察（切换结构、奇异弧分析）对理解问题本质仍有不可替代的价值。

### PMP 不适合在线控制

PMP 求解给出的是开环最优解（open-loop optimal control），需要对未来整体规划。在反馈控制中通常结合 MPC（滚动时域 + PMP 结构）或使用 PMP 离线求解参考轨迹后搭配跟踪控制器。

## 常见误区

### "PMP 是设计闭环控制器的实用方法"
PMP 给出开环最优解（给定 $t_0$ 和 $x_0$ 下的最优轨迹），不是反馈律。要从 PMP 得到反馈控制需要额外技巧（如状态相关 Riccati 方程 SDRE）。

### "PMP 和 HJB 相互独立"
HJB 是充分条件（解存在则全局最优），PMP 是必要条件（最优轨线必须满足）。两者在光滑情形下等价，PMP 可从 HJB 导出。

### "PMP 对所有最优控制问题都给出完整的控制律"
PMP 是必要条件而非充分条件。满足 PMP 条件的解可能是局部最优、全局最优或鞍点。奇异弧情形下 PMP 不直接给出控制，需要额外分析。

## 回链

- [动态规划与 Bellman 方程](./动态规划与Bellman方程.md)
- [模型预测控制 (MPC)](./模型预测控制.md)
- [状态反馈与极点配置](../03-现代控制/状态反馈与极点配置.md)
- [LQR 线性二次型调节器](../03-现代控制/LQR线性二次型调节器.md)
