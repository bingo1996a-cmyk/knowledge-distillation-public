# 案例 19：PageRank——网页排名算法

## 问题陈述

互联网有数十亿个网页通过超链接相连。给定网页间的链接结构，如何对每个网页赋予一个"重要性"分数，使搜索结果能按重要性排序？Google 的 PageRank 用 Markov 链的稳态分布给出了优雅答案。

## 数学建模

**网页图**：网页为节点，超链接为有向边。邻接矩阵 $A_{ij}=1$ 若网页 $i$ 链接到网页 $j$。

**随机浏览者模型**：浏览者以概率 $\alpha$（阻尼因子，通常 0.85）沿当前页面的随机出链跳转，以 $1-\alpha$ 随机跳到任意页面。

**转移矩阵**：
$$
P = \alpha D^{-1}A + (1-\alpha)\frac{1}{n}\mathbf{1}\mathbf{1}^\top
$$

其中 $D=\operatorname{diag}(d_1,\dots,d_n)$，$d_i$ 为页面 $i$ 的出度（若无出链则指向所有页面）。

**PageRank 向量** $\pi$ 是 $P$ 的稳态分布：
$$
\pi = \pi P,\quad \sum_i\pi_i = 1
$$

## 方法：幂迭代

由于 $n$ 极大（数十亿），直接求解特征向量不可行。用幂迭代：
$$
\pi^{(k+1)} = \pi^{(k)}P = \alpha\pi^{(k)}D^{-1}A + (1-\alpha)\frac{1}{n}\mathbf{1}^\top
$$

迭代保证收敛：$P$ 是随机不可约非周期矩阵 → $\pi^{(k)}$ 以 $|\lambda_2|^k\approx\alpha^k$ 的速率收敛（$\lambda_2$ 是第二特征值）。50-100 次迭代足以达到机器精度（$\alpha^{50}\approx3\times10^{-4}$）。

## 数值实现（伪代码）

```python
import numpy as np

# 小型网页图示例（6页面）
A = np.array([
    [0,1,1,0,0,0],  # 页面0链接到1,2
    [0,0,0,1,0,0],  # 页面1链接到3
    [0,0,0,1,0,0],  # 页面2链接到3
    [0,0,0,0,1,1],  # 页面3链接到4,5
    [0,0,0,0,0,1],  # 页面4链接到5
    [1,0,0,0,0,0],  # 页面5链接到0（形成环）
], dtype=float)

n = len(A)
alpha = 0.85

# 构造转移矩阵：对有出链和无出链的页面分别处理
out_degree = A.sum(axis=1)
P = np.zeros((n, n))
for i in range(n):
    if out_degree[i] > 0:
        P[i,:] = alpha * A[i,:] / out_degree[i]
    else:
        P[i,:] = alpha / n  # dangling node
    P[i,:] += (1-alpha) / n  # 随机跳转

# 幂迭代
pi = np.ones(n) / n
for k in range(100):
    pi_new = pi @ P
    if np.linalg.norm(pi_new - pi, 1) < 1e-10:
        print(f"Converged at iteration {k}")
        break
    pi = pi_new

# 输出排名
ranking = np.argsort(pi)[::-1]
for rank, idx in enumerate(ranking):
    print(f"Rank {rank+1}: Page {idx}, PR={pi[idx]:.4f}")
```

## 结果解释

- **稳态分布**：$\pi_3\approx0.21$（最高），$\pi_5\approx0.18$。页面 3 被 1 和 2 链接而获得高 PageRank
- **阻尼因子效应**：$\alpha\to1$ → 几乎只沿链接走，可能困在死胡同；$\alpha\to0$ → 几乎完全随机，各页面等权重。$\alpha=0.85$ 是平衡
- **Dangling Node 处理**：无出链的页面（悬垂节点）将 PageRank 均匀分配给所有页面——防止"流失"
- **收敛速率**：$|\lambda_2|\le\alpha<1$。50 次迭代后精度约 $10^{-4}$，100 次可达 $10^{-8}$

## 局限性

- **链接作弊**：创建大量指向目标页面的链接可人为提升 PageRank（Google 用 spam detection 对抗）
- **冷启动**：新页面没有入链时 PageRank 极低
- **个性化**：标准 PageRank 不考虑用户兴趣——个性化 PageRank 将随机跳转限于用户偏好页面

## 关联知识库入口

- 案例：[Markov 链稳态与混合时间](./10-Markov链稳态与混合时间.md)
- 概念：[特征值](../02-核心概念/特征值.md)
- 方法：[Markov 链与随机过程](../03-定理与方法/04-概率与统计/Markov链与随机过程.md)
