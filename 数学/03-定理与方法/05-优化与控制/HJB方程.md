# HJB 方程

## 作用

Hamilton-Jacobi-Bellman 方程（HJB Equation）是连续时间最优控制与随机控制中的核心最优性方程。  
它把“从当前状态出发的最优代价”写成一个值函数（value function）满足的偏微分方程。

离散时间中的 Bellman 最优方程，是 HJB 在连续时间下的对应物。

## 基本对象

设系统状态为 $x(t)$，控制为 $u(t)$，动力学写成

$$
\dot x(t)=f\bigl(x(t),u(t),t\bigr)
$$

若性能指标取为

$$
J_{t,x}(u)=\phi\bigl(x(T)\bigr)+\int_t^T l\bigl(x(s),u(s),s\bigr)\,ds
$$

则值函数定义为

$$
V(t,x)=\inf_{u(\cdot)} J_{t,x}(u)
$$

## 确定性 HJB 方程

在适当光滑条件下，值函数满足

$$
-\partial_t V(t,x)=\inf_u\Bigl\{l(x,u,t)+\nabla_x V(t,x)^\top f(x,u,t)\Bigr\}
$$

终端条件为

$$
V(T,x)=\phi(x)
$$

这表示：最优值函数在无穷小时间推进下，必须与“即时成本 + 未来最优成本”保持一致。

## 随机控制中的 HJB

若状态满足 It\^o 随机微分方程（stochastic differential equation, SDE）

$$
dX_t=f(X_t,u_t,t)\,dt+\sigma(X_t,u_t,t)\,dW_t
$$

则 HJB 方程会多出扩散项：

$$
-\partial_t V=\inf_u\left\{l+\nabla_x V^\top f+\frac12\operatorname{tr}\bigl(\sigma\sigma^\top \nabla_x^2 V\bigr)\right\}
$$

这里 $\nabla_x^2 V$ 是 Hessian 矩阵（Hessian matrix）。

## 几何与决策含义

HJB 的核心不是单纯一个偏微分方程，而是一个“局部最优性条件”。

- $V(t,x)$ 表示从当前时刻、当前状态出发的最优剩余代价
- $\nabla_x V$ 衡量状态微小变化对未来总代价的敏感度
- 最优控制由 Hamiltonian 最小化给出

定义 Hamiltonian 为

$$
H(x,u,p,t)=l(x,u,t)+p^\top f(x,u,t)
$$

则确定性 HJB 可写成

$$
-\partial_t V(t,x)=\inf_u H\bigl(x,u,\nabla_x V(t,x),t\bigr)
$$

## 为什么重要

### 1. 它把最优控制问题转成值函数方程

这使“求最优控制律”与“求 PDE 解”之间建立了直接对应。

### 2. 它是 Bellman 思想的连续时间表达

因此它同时连接：

- 最优控制
- 动态规划
- 随机控制
- 强化学习中的连续时间极限视角

### 3. 它能导出反馈控制律

一旦值函数已知，最优控制常可通过点态最小化获得。

## 最小例子

### 例 1：LQR 的 HJB 验证

考虑标量系统 $\dot x = ax + bu$，成本 $J = \int_0^\infty (x^2 + u^2) dt$。

- **问题陈述**：假设最优值函数为 $V(x)=px^2$，由 HJB 方程确定 $p$。
- **数学表达**：HJB：$0 = \inf_u \{ x^2 + u^2 + V'(x)(ax+bu) \}$。代入 $V'=2px$。
- **计算/推理步骤**：最小化 $u^2 + 2pxbu$ 得 $u^* = -pbx$。代入 HJB：$0 = x^2 + p^2b^2x^2 + 2px(ax - pb^2x) = x^2 + p^2b^2x^2 + 2apx^2 - 2p^2b^2x^2 = x^2 + 2apx^2 - p^2b^2x^2$。消 $x^2$ 得 $1 + 2ap - p^2b^2 = 0$。解二次方程：$p = \frac{a + \sqrt{a^2+b^2}}{b^2}$（取正根保证稳定）。
- **结果解读**：HJB 在 LQR 问题中退化为代数 Riccati 方程，给出闭式最优解 $u=-pbx$。

### 例 2：一维驱动系统的 HJB 数值求解思路

- **问题陈述**：$\dot x = u$，$|u|\leq 1$，成本 $J = \int_0^1 (x^2 + u^2) dt$，终端成本 $\phi(x)=x^2$。在 $(t,x)=(0.5,1)$ 处手工估计值函数。
- **数学表达**：HJB：$-\partial_t V = \min_{|u|\leq 1} \{ x^2 + u^2 + \partial_x V \cdot u \}$，终端 $V(1,x)=x^2$。
- **计算/推理步骤**：在 $(t,x)=(1,1)$ 处 $V=1$。逆向一步：时间步 $\Delta t=0.5$，假设在 $x$ 附近二次形式 $V\approx p(t)x^2$，则 $\partial_t V \approx \dot p x^2$，$\partial_x V \approx 2p x$，最优控制 $u^* = -\text{sat}(p x)$（饱和约束）。粗略估算值函数从 $V(1,1)=1$ 按时间反向扩散到 $V(0.5,1)\approx 0.7$。
- **结果解读**：HJB 方程将最优控制转化为 PDE 求解，其终端条件从最终成本出发逆向构造值函数。

## 关键假设与前提检查

1. 状态是否能合理写成 Markov 状态
2. 成本函数是否真正对应任务目标
3. 值函数是否具备足够正则性，或是否需要转向粘性解（viscosity solution）框架
4. 维度是否允许直接求解 PDE

## 风险与约束

- 高维 HJB 会遭遇维数灾难（curse of dimensionality）
- 值函数可能不可微，经典解框架失效
- 即使有理论最优性，数值求解也可能无法满足实时性
- 模型误差会使由 HJB 导出的控制律偏离可部署最优解

## 在资源受限条件下的可行最优路径

1. 先从离散时间 Bellman 方程与 MDP 理解值函数思想
2. 再学习确定性 HJB
3. 只在低维问题中直接数值求解 HJB
4. 高维问题优先转向 LQR、MPC、近似动态规划或函数逼近方法

## 与其他条目的关系

- 前置： [状态空间模型](../../02-核心概念/状态空间模型.md)、[随机过程](../../02-核心概念/随机过程.md)、[最优控制与 Pontryagin 极大值原理](../05-优化与控制/最优控制与Pontryagin原理.md)
- 前序： [动态规划与递推方法](../05-优化与控制/动态规划与递推.md)、[马尔可夫决策过程](../05-优化与控制/Markov决策过程.md)
- 后续： [Riccati 方程、LQR 与 LQG](../05-优化与控制/Riccati方程与LQR-LQG.md)、[模型预测控制](../05-优化与控制/模型预测控制.md)、连续时间强化学习

## 推荐教材与延伸阅读

1. Fleming, W. H. & Soner, H. M. (2006). *Controlled Markov Processes and Viscosity Solutions* (2nd ed.). Springer. — HJB 方程与粘性解框架的权威专著
2. Øksendal, B. (2003). *Stochastic Differential Equations* (6th ed.). Springer. — 第 11 章系统覆盖随机控制中的 HJB 方程
3. Bertsekas, D. P. (2012). *Dynamic Programming and Optimal Control* (Vol. 2, 4th ed.). Athena Scientific. — 离散与连续时间最优控制的互补视角
