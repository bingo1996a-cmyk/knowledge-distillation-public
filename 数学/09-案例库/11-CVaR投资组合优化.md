# 案例 11：CVaR 投资组合优化

## 问题陈述

一个投资者在 3 种资产间分配资金。历史日收益率数据显示资产间有相关性。如何在给定置信水平 $\alpha=95\%$ 下，最小化条件风险价值（CVaR）——即最坏 5% 情景下的平均损失？这是风险管理中取代方差的最常用方法。

## 数学建模

设 $x=(x_1,x_2,x_3)^\top$ 为资产权重（$\sum x_i=1$，$x_i\ge0$），$r\in\mathbb{R}^3$ 为随机收益率向量。损失为 $L(x,r)=-r^\top x$。

**CVaR 定义**（Rockafellar-Uryasev 公式）：
$$
\text{CVaR}_\alpha(x) = \min_{\gamma\in\mathbb{R}} \left\{\gamma + \frac{1}{1-\alpha}\mathbb{E}\left[\max(L(x,r)-\gamma, 0)\right]\right\}
$$

其中 $\gamma$ 是 VaR（Value-at-Risk）的辅助变量。此公式将 CVaR 最小化化为线性规划！

**样本近似**（历史数据的经验分布，$S$ 个情景）：
$$
\begin{aligned}
\min_{x,\gamma,z} &\quad \gamma + \frac{1}{(1-\alpha)S}\sum_{s=1}^S z_s \\
\text{s.t.} &\quad z_s \ge -r_s^\top x - \gamma \quad \forall s \\
&\quad z_s \ge 0, \quad \sum_i x_i = 1, \quad x_i \ge 0
\end{aligned}
$$

## 方法：线性规划

目标函数和约束均为线性——这是一个标准的线性规划，可用单纯形法或内点法求解。

## 数值实现（伪代码）

```python
import numpy as np
from scipy.optimize import linprog

# 3资产，100天历史日收益率（百分比）
np.random.seed(42)
n_assets, n_scenarios = 3, 100
returns = np.random.randn(n_scenarios, n_assets) * 1.5 + np.array([0.05, 0.08, 0.03])

alpha = 0.95

# LP变量: [x1, x2, x3, gamma, z1, ..., zS]
c = np.zeros(3 + 1 + n_scenarios)
c[3] = 1.0                              # gamma的系数
c[4:] = 1.0 / ((1 - alpha) * n_scenarios)  # z_s的系数

# 约束矩阵
A_ub = np.zeros((n_scenarios, 3 + 1 + n_scenarios))
b_ub = np.zeros(n_scenarios)
for s in range(n_scenarios):
    A_ub[s, :3] = returns[s, :]          # -(-r_s^T x) = r_s^T x
    A_ub[s, 3] = 1.0                     # gamma
    A_ub[s, 4+s] = -1.0                  # -z_s
    # 即: returns[s]·x + gamma - z_s <= 0  <==>  z_s >= returns[s]·x + gamma

A_eq = np.zeros((1, 3 + 1 + n_scenarios))
A_eq[0, :3] = 1.0
b_eq = np.array([1.0])

bounds = [(0, 1)] * 3 + [(None, None)] + [(0, None)] * n_scenarios

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                 bounds=bounds, method='highs')

x_opt = result.x[:3]
gamma_opt = result.x[3]
cvar_opt = result.fun

print(f"Optimal weights: {np.round(x_opt, 3)}")
print(f"VaR (gamma): {gamma_opt:.4f}")
print(f"CVaR (95%): {cvar_opt:.4f}")

# 对比等权重
x_equal = np.ones(3) / 3
losses = -returns @ x_equal
cvar_equal = np.mean(np.sort(losses)[-int(n_scenarios*(1-alpha)):])
print(f"Equal-weight CVaR: {cvar_equal:.4f}")
```

## 结果解释

- **最优权重**：LP 解将更多权重分配给损失分布左尾较薄的资产（更稳健的资产）
- **CVaR vs 方差**：方差对称惩罚正负偏离，CVaR 只惩罚左尾。对于非对称分布，CVaR 更合理
- **$\gamma$ 的解释**：最优 $\gamma$ 等于 VaR——即损失分布的 $1-\alpha=5\%$ 分位点
- **CVaR > VaR**：CVaR 是超过 VaR 的损失的条件均值，始终 $\ge$ VaR

## 局限性

- **历史情景依赖**：100 天历史未必覆盖极端尾部事件（需压力测试补充）
- **线性规划**：不含整数约束时可快速求解；含离散约束时需求解 MILP
- **单期模型**：未考虑多期动态再平衡

## 关联知识库入口

- 方法：[CVaR 约束与样本外压力测试](../03-定理与方法/05-优化与控制/CVaR风险约束与样本外压力测试.md)
- 方法：[分布鲁棒优化与风险度量](../03-定理与方法/05-优化与控制/分布鲁棒优化与风险度量.md)
- 概念：[风险度量](../02-核心概念/风险度量.md)
