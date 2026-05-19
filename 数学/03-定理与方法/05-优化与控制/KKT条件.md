# KKT 条件

## 作用

KKT 条件（Karush-Kuhn-Tucker Conditions）是带不等式约束优化问题的标准一阶最优性条件。  
它是拉格朗日乘子法在更一般约束情形下的扩展。

## 基本问题

考虑优化问题

$$
\min_x f(x)\quad \text{s.t.}\quad g_i(x)\le 0,\ i=1,\dots,m,\quad h_j(x)=0,\ j=1,\dots,p
$$

构造拉格朗日函数

$$
\mathcal{L}(x,\lambda,\nu)=f(x)+\sum_{i=1}^m \lambda_i g_i(x)+\sum_{j=1}^p \nu_j h_j(x)
$$

其中不等式约束乘子满足 $\lambda_i\ge 0$。

## KKT 条件的四个部分

在适当约束资格条件下，局部最优点常满足：

### 1. 原始可行性（Primal Feasibility）

$$
g_i(x^\star)\le 0,\qquad h_j(x^\star)=0
$$

### 2. 对偶可行性（Dual Feasibility）

$$
\lambda_i^\star \ge 0
$$

### 3. 驻点条件（Stationarity）

$$
\nabla_x \mathcal{L}(x^\star,\lambda^\star,\nu^\star)=0
$$

### 4. 互补松弛（Complementary Slackness）

$$
\lambda_i^\star g_i(x^\star)=0,\quad i=1,\dots,m
$$

## 互补松弛的直观意义

若某个不等式约束没有“卡住”最优点，即 $g_i(x^\star)<0$，则对应乘子必须为零。  
若某个乘子大于零，则对应约束一定在边界上激活。

## 为什么重要

KKT 条件把几何边界、代数方程与对偶思想统一起来，是现代优化理论的核心接口。

它的重要性体现在：

- 统一处理等式与不等式约束
- 为算法提供停止准则
- 为对偶理论提供结构支点
- 在凸优化中常能给出全局最优判据

## 与凸优化的关系

若问题是凸优化问题，并满足适当正则条件，例如 Slater 条件（Slater Condition），则 KKT 条件通常不仅是必要条件，也是充分条件。

这意味着：  
只要找到满足 KKT 的点，就可确认其为全局最优解。

## 最小例子

### 例 1：不等式约束二次优化

**问题陈述**：求解 $\min_x x^2$ 满足 $x \ge 1$（即约束 $g(x)=1-x\le 0$），并用 KKT 条件验证最优性。

**数学表达**：拉格朗日函数 $\mathcal{L}(x,\lambda)=x^2+\lambda(1-x)$，KKT 条件为：
- 原始可行：$1-x^\star\le 0$
- 对偶可行：$\lambda^\star\ge 0$
- 驻点：$2x^\star-\lambda^\star=0$
- 互补松弛：$\lambda^\star(1-x^\star)=0$

**计算/推理步骤**：

1. 由互补松弛：若 $1-x^\star<0$，则 $\lambda^\star=0$，驻点得 $x^\star=0$，但不满足 $x^\star\ge 1$。所以必有 $1-x^\star=0$，即 $x^\star=1$。
2. 代入驻点：$2\times1-\lambda^\star=0 \Rightarrow \lambda^\star=2$。
3. 检查所有条件：$x^\star=1\ge 1$ ✓，$\lambda^\star=2\ge 0$ ✓，$2-\lambda^\star=0$ ✓，$\lambda^\star(1-1)=0$ ✓。

**结果解读**：通过 KKT 条件，我们从代数角度找到了约束边界上的最优点。$\lambda^\star=2$ 可解释为：约束 $x\ge 1$ 每放松一个单位，目标最优值 $x^2$ 会下降约 $2\Delta x$（即影子价格）。这个一维例子虽然简单，却展示了 KKT 所有四个成分如何协同工作以确定最优解。

### 例 2：二维约束优化

**问题陈述**：求解 $\min_{(x_1,x_2)} (x_1-2)^2 + (x_2-1)^2$ 满足 $x_1^2+x_2^2\le 1$。

**数学表达**：约束 $g(x)=x_1^2+x_2^2-1\le 0$。拉格朗日函数 $\mathcal{L}=(x_1-2)^2+(x_2-1)^2 + \lambda(x_1^2+x_2^2-1)$。

**计算/推理步骤**：

1. 驻点条件：$\partial\mathcal{L}/\partial x_1 = 2(x_1-2)+2\lambda x_1=0$，$\partial\mathcal{L}/\partial x_2 = 2(x_2-1)+2\lambda x_2=0$。
2. 整理得 $x_1=2/(1+\lambda)$，$x_2=1/(1+\lambda)$。
3. 由互补松弛：若 $g(x^\star)<0$，则 $\lambda^\star=0$，得 $(2,1)$，但 $g(2,1)=4+1-1=4>0$，不可行。故 $g(x^\star)=0$。
4. 代入约束：$(2/(1+\lambda))^2 + (1/(1+\lambda))^2 = 1 \Rightarrow 4+1=(1+\lambda)^2 \Rightarrow \lambda = \sqrt{5}-1\approx 1.236$。
5. $x_1^\star=2/2.236\approx 0.894$，$x_2^\star=1/2.236\approx 0.447$，目标值 $\approx (0.894-2)^2+(0.447-1)^2\approx 1.528$。

**结果解读**：这个例子展示了 KKT 条件在更实际的场景中如何运作——无约束最优点 $(2,1)$ 被圆约束"推回"可行域边界，$\lambda^\star\approx 1.236$ 量化了这个约束的"紧度"。约束曲面的法线与目标梯度在最优解处方向相反，这正是 KKT 驻点条件的几何解释。

## 与拉格朗日乘子法的关系

- [拉格朗日乘子法](../05-优化与控制/Lagrange乘子.md) 主要针对等式约束
- KKT 条件扩展到不等式约束
- 两者本质都依赖“可行方向上无下降方向”的一阶思想

## 典型例子

考虑一维问题

$$
\min_x x^2 \quad \text{s.t.}\quad x\ge 1
$$

可写为约束 $g(x)=1-x\le 0$，则

$$
\mathcal{L}(x,\lambda)=x^2+\lambda(1-x)
$$

驻点条件给出

$$
2x-\lambda=0
$$

结合原始可行性与互补松弛，可得最优解为 $x^\star=1$。

## 与其他概念的关系

- 前置： [导数](../../02-核心概念/导数.md)、[凸性](../../02-核心概念/凸性.md)、[范数与正定性](../../02-核心概念/范数与正定性.md)
- 分支层： [优化](../../01-分支/优化.md)
- 后续：对偶理论、内点法、二次规划、最优控制

## 风险提示

- 没有约束资格条件时，KKT 可能失效
- 在非凸问题中，满足 KKT 不保证全局最优
- 数值算法中通常只能近似满足 KKT 残差为零

## 推荐教材与延伸阅读

- Boyd, S. & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press. — 第 5 章对 KKT 与对偶有极清晰的处理。
- Nocedal, J. & Wright, S. J. (2006). *Numerical Optimization*, 2nd ed. Springer. — 第 12 章从数值角度讨论 KKT 条件与约束优化算法。
- Luenberger, D. G. & Ye, Y. (2008). *Linear and Nonlinear Programming*, 4th ed. Springer. — 经典教材，第 11—14 章覆盖约束最优性与 KKT。
