# 拉格朗日乘子法

## 作用

拉格朗日乘子法（Lagrange Multiplier Method）用于处理带等式约束的极值问题，是优化中最经典的最优性条件之一。

## 基本问题

考虑约束优化问题：

$$
\min_x f(x) \quad \text{s.t.} \quad g(x)=0
$$

构造拉格朗日函数

$$
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x)
$$

必要条件通常写成

$$
\nabla_x \mathcal{L}(x,\lambda)=0, \quad g(x)=0
$$

## 几何直观

在最优点上，目标函数的梯度与约束面的法向方向对齐。对单约束问题，这可写为

$$
\nabla f(x^*) = -\lambda \nabla g(x^*)
$$

这表示在可行方向上，目标函数的一阶变化为零。

## 多约束情形

若存在多个约束 $g_i(x)=0$，则

$$
\mathcal{L}(x,\lambda)=f(x)+\sum_{i=1}^m \lambda_i g_i(x)
$$

## 为什么重要

- 它是约束优化的标准入口
- 它连接几何直观与代数计算
- 它是 KKT 条件、对偶理论、最优控制等更一般理论的前奏

## 典型例子

求约束 $x^2+y^2=1$ 下函数 $f(x,y)=x+y$ 的极值，可写成

$$
\mathcal{L}(x,y,\lambda)=x+y+\lambda(x^2+y^2-1)
$$

然后联立一阶条件求解。

## 与其他概念的关系

- 前置： [导数](../../02-核心概念/导数.md)、[函数](../../02-核心概念/函数.md)
- 分支关联： [优化](../../01-分支/优化.md)
- 后续：KKT 条件、凸优化、最优控制、对偶方法

## 最小例子

### 例 1：单位圆上的线性函数

- **问题陈述**：在约束 $x^2 + y^2 = 1$ 下求 $f(x,y) = x + y$ 的极值。
- **数学表达**：$\mathcal{L}(x,y,\lambda) = x+y + \lambda(x^2+y^2-1)$。
- **计算/推理步骤**：$\partial_x: 1 + 2\lambda x = 0 \Rightarrow x = -1/(2\lambda)$，$\partial_y: 1 + 2\lambda y = 0 \Rightarrow y = -1/(2\lambda)$。代入约束 $(-1/(2\lambda))^2 + (-1/(2\lambda))^2 = 1 \Rightarrow 1/(2\lambda^2) = 1 \Rightarrow \lambda = \pm 1/\sqrt{2}$。$\lambda = -1/\sqrt{2}$ 时 $x=y=1/\sqrt{2}$，$f=\sqrt{2}$（最大值）。$\lambda=1/\sqrt{2}$ 时 $x=y=-1/\sqrt{2}$，$f=-\sqrt{2}$（最小值）。
- **结果解读**：在最优点，$\nabla f=(1,1)$ 与 $\nabla g=(2x,2y)$ 共线（平行），比值 $\lambda$ 恰好是 $-1/\sqrt{2}$，这正是"梯度对齐"的几何直观。

### 例 2：矩形面积最大化

- **问题陈述**：用固定周长 $P$ 围成矩形，求最大面积。
- **数学表达**：$A=wh$，约束 $2w+2h=P$。$\mathcal{L}=wh + \lambda(2w+2h-P)$。
- **计算/推理步骤**：$\partial_w: h + 2\lambda = 0$，$\partial_h: w + 2\lambda = 0$，$h = w = -2\lambda$。由约束 $4w=P$，$w=h=P/4$，最大面积 $P^2/16$。
- **结果解读**：在周长固定下面积最大时矩形为正方形，拉格朗日乘子法自然得到这一结论。

## 注意事项

- 这是必要条件，不自动保证全局最优
- 还需结合二阶条件、凸性或几何结构判断极值性质
- 对不等式约束问题，通常应转入 KKT 框架

## 推荐教材与延伸阅读

1. Boyd & Vandenberghe, *Convex Optimization*（Cambridge University Press, 2004）——第5章讲解拉格朗日对偶与 KKT 条件，是此话题的现代标准参考。
2. Luenberger & Ye, *Linear and Nonlinear Programming*（4th ed., Springer, 2016）——第10-11章提供乘子法的经典数值视角。
3. Bertsekas, *Nonlinear Programming*（3rd ed., Athena Scientific, 2016）——对凸与非凸情形下乘子法的理论分析最为详尽。
