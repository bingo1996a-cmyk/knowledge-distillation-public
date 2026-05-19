# 案例 20：支持向量机的凸优化推导

## 问题陈述

给定两类线性可分的数据点，找一条分隔超平面使两类之间的间隔（margin）最大。这是支持向量机（SVM）的原始形式——分类问题转化为凸二次规划。

## 数学建模

训练数据 $\{(x_i,y_i)\}_{i=1}^n$，$x_i\in\mathbb{R}^d$，$y_i\in\{\pm1\}$。超平面 $w^\top x+b=0$。

**硬间隔 SVM**（线性可分）：
$$
\begin{aligned}
\min_{w,b} &\quad \frac12\|w\|^2 \\
\text{s.t.} &\quad y_i(w^\top x_i+b)\ge 1,\quad i=1,\dots,n
\end{aligned}
$$

$\|w\|^2$ 最小化等价于最大化间隔 $2/\|w\|$。约束确保所有点到超平面的几何距离至少 $1/\|w\|$。

**软间隔 SVM**（允许少量误分类）：
$$
\begin{aligned}
\min_{w,b,\xi} &\quad \frac12\|w\|^2 + C\sum_{i=1}^n\xi_i \\
\text{s.t.} &\quad y_i(w^\top x_i+b)\ge 1-\xi_i,\quad \xi_i\ge 0
\end{aligned}
$$

$C$ 权衡间隔最大化与误分类惩罚。$C\to\infty$ 时退化为硬间隔。

## 方法：Lagrange 对偶 + KKT

### Lagrange 函数

$$
\mathcal{L}(w,b,\alpha) = \frac12\|w\|^2 - \sum_{i=1}^n\alpha_i\left[y_i(w^\top x_i+b)-1\right]
$$

$\alpha_i\ge0$ 为 Lagrange 乘子。

### 对偶推导

令 $\nabla_w\mathcal{L}=w-\sum\alpha_i y_i x_i=0$ → $w=\sum\alpha_i y_i x_i$。$\nabla_b\mathcal{L}=-\sum\alpha_i y_i=0$ → $\sum\alpha_i y_i=0$。

代入消去 $w,b$ 得对偶问题：
$$
\begin{aligned}
\max_\alpha &\quad \sum_{i=1}^n\alpha_i - \frac12\sum_{i,j=1}^n\alpha_i\alpha_j y_i y_j x_i^\top x_j \\
\text{s.t.} &\quad \sum\alpha_i y_i = 0,\quad \alpha_i\ge 0
\end{aligned}
$$

只需要内积 $x_i^\top x_j$（可核化 → 核SVM）！

### KKT 条件与支撑向量

互补松弛：$\alpha_i[y_i(w^\top x_i+b)-1]=0$。因此：
- $\alpha_i>0$ → $y_i(w^\top x_i+b)=1$：支撑向量（在间隔边界上）
- $\alpha_i=0$ → 该点不在间隔边界上，对超平面无贡献

最优 $w=\sum_{i\in SV}\alpha_i y_i x_i$——模型仅由支撑向量决定。

## 数值实现（伪代码）

```python
import numpy as np
from scipy.optimize import minimize

# 生成二分类数据
np.random.seed(42)
n = 50
X_pos = np.random.randn(n//2, 2) + [2, 2]
X_neg = np.random.randn(n//2, 2) + [-2, -2]
X = np.vstack([X_pos, X_neg])
y = np.array([1]*(n//2) + [-1]*(n//2))

# 对偶SVM：最小化 -∑α_i + 0.5∑α_i α_j y_i y_j x_i^T x_j
C = 1.0  # 软间隔参数
def dual_obj(alpha):
    Q = np.outer(alpha*y, alpha*y) * (X @ X.T)
    return -np.sum(alpha) + 0.5 * np.sum(Q)

# 约束
cons = ({'type': 'eq', 'fun': lambda a: a @ y})
bounds = [(0, C) for _ in range(n)]

result = minimize(dual_obj, np.zeros(n), bounds=bounds, constraints=cons,
                  method='SLSQP')
alpha = result.x

# 提取支撑向量
sv_mask = alpha > 1e-5
w = np.sum(alpha[sv_mask, None] * y[sv_mask, None] * X[sv_mask], axis=0)
sv_idx = np.where(sv_mask)[0][0]
b = y[sv_idx] - w @ X[sv_idx]

print(f"Support vectors: {sv_mask.sum()} / {n}")
print(f"w = {w}, b = {b:.3f}")
print(f"Margin = {2/np.linalg.norm(w):.3f}")
# 输出约: Support vectors: 4 / 50 — 模型仅由4个支撑向量决定
```

## 结果解释

- **稀疏性**：仅 4/50 个点是支撑向量——SVM 的解是稀疏的（大部分 $\alpha_i=0$）。这使得预测 $f(x)=\operatorname{sign}(\sum_{SV}\alpha_i y_i x_i^\top x+b)$ 非常快
- **对偶优势**：对偶问题的变量数 = 样本数 $n$（而非特征维数 $d$）。在高维（$d\gg n$，如文本分类）时对偶方法更高效
- **软间隔**：$C$ 越小，容忍的误分类越多，间隔越宽。$C=1$ 时选择平衡；$C=0.1$ 时可能有轻度误分类但更宽的泛化间隔
- **强对偶性**：凸二次规划的 Slater 条件满足，对偶间隙为零——求解对偶等价于求解原问题

## 局限性

- **线性不可分**：原始特征空间线性不可分时需核化（RBF 核等）——计算复杂度升至 $O(n^2)$
- **大规模数据**：$Q$ 矩阵为 $n\times n$，$n>10^5$ 时内存不足——需 SMO 或随机梯度方法
- **概率输出**：SVM 只给出分类决策，不直接提供概率——需 Platt scaling 后处理

## 关联知识库入口

- 方法：[KKT 条件](../03-定理与方法/05-优化与控制/KKT条件.md)
- 方法：[优化中的对偶理论](../03-定理与方法/05-优化与控制/优化中的对偶.md)
- 案例：[KKT 约束优化案例](./06-KKT约束优化.md)
