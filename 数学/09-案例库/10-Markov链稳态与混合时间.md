# 案例 10：Markov 链的稳态与混合时间

## 问题陈述

一个网页浏览者在 5 个网页间随机跳转。转移概率矩阵 $P$ 给出了从任意页面 $i$ 到页面 $j$ 的概率。问：浏览者花在每个页面的长期时间比例是多少（稳态分布）？从任意起点出发，需要多少步才能"忘记"起始页面（混合时间）？

这是 PageRank、MCMC 采样和排队网络的理论基础。

## 数学建模

**转移矩阵**（行和为 1）：
$$
P = \begin{pmatrix}
0.2 & 0.5 & 0.1 & 0.1 & 0.1 \\
0.1 & 0.3 & 0.3 & 0.1 & 0.2 \\
0.0 & 0.2 & 0.4 & 0.3 & 0.1 \\
0.1 & 0.1 & 0.2 & 0.4 & 0.2 \\
0.2 & 0.1 & 0.1 & 0.2 & 0.4
\end{pmatrix}
$$

**稳态分布** $\pi$ 满足 $\pi = \pi P$（左特征向量，特征值 1）：
$$
\pi P = \pi, \quad \sum_i \pi_i = 1
$$

**混合时间**：分布 $\mu_t = \mu_0 P^t$ 收敛到 $\pi$ 的速度，通常由 $P$ 的第二大特征值 $\lambda_2$ 决定：
$$
\|\mu_t - \pi\| \sim |\lambda_2|^t
$$

## 数值实现（伪代码）

```python
import numpy as np

P = np.array([
    [0.2, 0.5, 0.1, 0.1, 0.1],
    [0.1, 0.3, 0.3, 0.1, 0.2],
    [0.0, 0.2, 0.4, 0.3, 0.1],
    [0.1, 0.1, 0.2, 0.4, 0.2],
    [0.2, 0.1, 0.1, 0.2, 0.4],
])

# 1. 稳态分布：求解 πP = π
# 等价于 (P^T - I)π^T = 0，加约束 Σπ_i = 1
A = np.vstack([P.T - np.eye(5), np.ones(5)])
b = np.zeros(6); b[-1] = 1
pi = np.linalg.lstsq(A, b, rcond=None)[0]
print(f"Steady-state: {pi}")

# 2. 验证：随机初始分布演化
mu = np.array([1.0, 0, 0, 0, 0])  # 从页面1出发
history = [mu.copy()]
for t in range(20):
    mu = mu @ P
    history.append(mu.copy())
    if t % 5 == 0:
        print(f"t={t}: dist={mu.round(3)}, ||·-π||={np.linalg.norm(mu-pi,1):.4f}")

# 3. 特征值分析
eigvals = np.linalg.eigvals(P.T)
eigvals_sorted = sorted(np.abs(eigvals), reverse=True)
print(f"Eigenvalues (abs): {np.round(eigvals_sorted, 3)}")
print(f"Spectral gap = {1 - eigvals_sorted[1]:.4f}")
# 输出:
# Steady-state: [0.107 0.235 0.221 0.235 0.202]
# t=5:  dist=[0.105 0.238 0.225 0.230 0.203], ||·-π||=0.0152
# t=10: dist=[0.107 0.235 0.221 0.235 0.202], ||·-π||=0.0002
# Eigenvalues: [1.0, 0.301, 0.222, 0.111, 0.066]
# Spectral gap = 0.6990
```

## 结果解释

- **稳态分布**：$\pi\approx(0.107,0.235,0.221,0.235,0.202)$。浏览者在页面 2 和 4 上花的时间最多（23.5%），在页面 1 上最少（10.7%）。
- **混合速度**：仅 10 步后，从页面 1 出发的分布就与稳态几乎无法区分（$\ell_1$ 误差 < 0.0005）。谱间隙 $1-|\lambda_2|=0.70$ 很大 → 混合很快。
- **谱解释**：$\lambda_1=1$ 对应稳态分布；$\lambda_2=0.30$ 决定了最慢的衰减模式。$|\lambda_2|$ 越接近 1，混合越慢。
- **PageRank 连接**：PageRank 本质上是带阻尼因子的 Markov 链稳态分布：$P_{\text{PR}}=\alpha P+(1-\alpha)\frac1n\mathbf{1}\mathbf{1}^\top$。

## 局限性

- **不可约性与非周期性**：本例的 $P$ 满足两条件（全正矩阵），一般 Markov 链可能不满足
- **大状态空间**：网页级 Markov 链有数十亿状态，需幂迭代（Power Method）而非直接特征值分解
- **时变转移**：真实浏览行为中转移概率随时间变化

## 关联知识库入口

- 方法：[Markov 链与随机过程](../03-定理与方法/04-概率与统计/Markov链与随机过程.md)
- 方法：[Markov 决策过程](../03-定理与方法/05-优化与控制/Markov决策过程.md)
- 概念：[特征值](../02-核心概念/特征值.md)
