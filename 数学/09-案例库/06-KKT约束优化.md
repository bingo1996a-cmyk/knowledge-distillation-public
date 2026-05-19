# 案例 06：KKT 条件下的小规模约束优化

## 问题陈述

在资源有限的情况下分配生产计划：生产两种产品 A 和 B，单位利润分别为 3 和 4。每单位 A 耗 2 小时人工和 1 单位原料，每单位 B 耗 1 小时人工和 2 单位原料。总人工 ≤ 8 小时，总原料 ≤ 6 单位。求最大化利润的生产方案。

## 数学建模

**决策变量**：$x_1$（产品A数量），$x_2$（产品B数量）

**优化问题**：
$$
\begin{aligned}
\max_{x_1,x_2} & \quad 3x_1 + 4x_2 \\
\text{s.t.} & \quad 2x_1 + x_2 \le 8 \quad \text{(人工)} \\
& \quad x_1 + 2x_2 \le 6 \quad \text{(原料)} \\
& \quad x_1,x_2 \ge 0
\end{aligned}
$$

**标准化为最小化形式**：
$$
\begin{aligned}
\min_{x} & \quad f(x) = -3x_1 -4x_2 \\
\text{s.t.} & \quad g_1(x) = 2x_1+x_2-8 \le 0 \\
& \quad g_2(x) = x_1+2x_2-6 \le 0 \\
& \quad x_1,x_2 \ge 0
\end{aligned}
$$

## 方法选择：KKT 条件

对于不等式约束优化，KKT 条件是局部最优解的必要条件：

**Lagrange 函数**：$\mathcal{L}(x,\mu)=f(x)+\mu_1 g_1(x)+\mu_2 g_2(x)$

**KKT 条件**：
1. 平稳性：$\nabla_x\mathcal{L}=0$
2. 原始可行性：$g_i(x)\le0$
3. 对偶可行性：$\mu_i\ge0$
4. 互补松弛：$\mu_i g_i(x)=0$

## 求解步骤

**步 1**：写出 KKT 条件
$$
\begin{aligned}
\frac{\partial\mathcal{L}}{\partial x_1} &= -3 + 2\mu_1 + \mu_2 - \nu_1 = 0 \\
\frac{\partial\mathcal{L}}{\partial x_2} &= -4 + \mu_1 + 2\mu_2 - \nu_2 = 0 \\
\mu_1(2x_1+x_2-8) &= 0, \quad \mu_2(x_1+2x_2-6) = 0 \\
\nu_1 x_1 &= 0, \quad \nu_2 x_2 = 0
\end{aligned}
$$

**步 2**：分析互补松弛条件。假设两个约束都束紧（$x$ 在交点取最优）：
$$
\begin{cases}2x_1+x_2=8\\x_1+2x_2=6\end{cases}
\Rightarrow x_1=\frac{10}{3},\; x_2=\frac{4}{3}
$$

$x_1,x_2>0$，故 $\nu_1=\nu_2=0$。解平稳方程：
$$
\begin{cases}2\mu_1+\mu_2=3\\\mu_1+2\mu_2=4\end{cases}
\Rightarrow \mu_1=\frac{2}{3},\; \mu_2=\frac{5}{3}
$$

$\mu_1,\mu_2>0$，KKT 条件满足。最优解：$x^*=(\frac{10}{3},\frac{4}{3})$。

**步 3**：计算最优值和影子价格
- 利润：$3\times\frac{10}{3}+4\times\frac{4}{3}=10+\frac{16}{3}=\frac{46}{3}\approx15.33$
- $\mu_1=\frac23$：多 1 小时人工可增利约 0.67
- $\mu_2=\frac53$：多 1 单位原料可增利约 1.67——原料更紧缺

## 数值实现（伪代码）

```python
import numpy as np
from scipy.optimize import minimize

# 定义目标函数和约束
def objective(x):
    return -3*x[0] - 4*x[1]  # 负号因为minimize做最小化

constraints = [
    {'type': 'ineq', 'fun': lambda x: 8 - 2*x[0] - x[1]},   # 人工
    {'type': 'ineq', 'fun': lambda x: 6 - x[0] - 2*x[1]},   # 原料
]
bounds = [(0, None), (0, None)]

result = minimize(objective, [0, 0], bounds=bounds,
                  constraints=constraints, method='SLSQP')

print(f"最优生产方案: A={result.x[0]:.2f}, B={result.x[1]:.2f}")
print(f"最大利润: {-result.fun:.2f}")

# 输出:
# 最优生产方案: A=3.33, B=1.33
# 最大利润: 15.33
```

## 结果解释

- **束紧约束**：两个约束都在边界上——人工和原料都已耗尽。若任一资源有剩余，说明该资源不是瓶颈。
- **影子价格**：KKT 乘子直接给出每种资源的边际价值。原料的边际价值（1.67）高于人工（0.67），优先增加原料供应。
- **互补松弛**：若某个 $\mu_i=0$，说明该约束不束紧，可安全放宽而不改善目标。

## 局限性

- 仅适用于光滑约束（非光滑需次梯度方法）
- 非凸问题中 KKT 仅是必要条件
- 约束过多时组合分析不可行——需数值 QP 求解器

## 关联知识库入口

- 方法：[KKT 条件](../03-定理与方法/05-优化与控制/KKT条件.md)
- 方法：[优化中的对偶理论](../03-定理与方法/05-优化与控制/优化中的对偶.md)
- 方法：[线性规划](../03-定理与方法/05-优化与控制/线性规划.md)
