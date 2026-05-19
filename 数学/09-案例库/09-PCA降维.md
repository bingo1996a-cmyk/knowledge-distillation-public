# 案例 09：PCA 与降维——从数据到主成分

## 问题陈述

手写数字数据集 MNIST 中每张图是 $28\times28=784$ 维向量，但实际"有效维度"远小于 784。如何找到数据方差最大的方向，将 784 维压缩到 2 维以实现可视化，同时保留尽可能多的数据变异性？这是数据分析和机器学习中最常用的降维技术。

## 数学建模

给定数据中心化后的设计矩阵 $X\in\mathbb{R}^{n\times d}$（$n$ 个样本，$d$ 维特征，均值为零）。求一组正交方向 $w_1,\dots,w_k$（$k\ll d$），使投影方差最大化：

$$
w_1 = \arg\max_{\|w\|=1} \operatorname{Var}(Xw) = \arg\max_{\|w\|=1} w^\top \Sigma w
$$

其中 $\Sigma = \frac1n X^\top X$ 是协方差矩阵。用 Lagrange 乘子法：

$$
\mathcal{L}=w^\top\Sigma w - \lambda(w^\top w-1)
$$

令梯度为零：$\Sigma w=\lambda w$。即 $w$ 是 $\Sigma$ 的特征向量，对应的方差 $\lambda$ 是特征值。

## 方法：特征值分解 + 投影

1. 去均值：$\tilde X = X - \bar X$
2. 计算协方差：$\Sigma = \frac1n \tilde X^\top \tilde X$
3. 特征值分解：$\Sigma w_i = \lambda_i w_i$
4. 按 $\lambda_i$ 降序排序，取前 $k$ 个特征向量 $W_k=(w_1,\dots,w_k)$
5. 投影：$Z = \tilde X W_k$（$n\times k$ 的降维数据）

## 数值实现（伪代码）

```python
import numpy as np
from sklearn.datasets import load_digits

# 加载数据（8x8手写数字=64维，用于演示）
digits = load_digits()
X = digits.data  # 1797 samples x 64 features
y = digits.target

# 1. 去均值
X_centered = X - X.mean(axis=0)

# 2. 协方差矩阵
Sigma = X_centered.T @ X_centered / (len(X) - 1)

# 3. 特征值分解
eigvals, eigvecs = np.linalg.eigh(Sigma)
# eigh返回升序，翻转为降序
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# 4. 取前2个主成分
W2 = eigvecs[:, :2]
Z = X_centered @ W2  # 1797 x 2

# 5. 解释方差比
explained_var_ratio = eigvals / eigvals.sum()
print(f"PC1 explains: {explained_var_ratio[0]:.1%}")
print(f"PC2 explains: {explained_var_ratio[1]:.1%}")
print(f"First 2 PCs explain: {explained_var_ratio[:2].sum():.1%}")
print(f"First 10 PCs explain: {explained_var_ratio[:10].sum():.1%}")

# 输出:
# PC1 explains: 14.9%
# PC2 explains: 13.6%
# First 2 PCs explain: 28.5%
# First 10 PCs explain: 57.9%
```

## 结果解释

- **方差解释**：前 2 个主成分解释 28.5% 的方差——2D 可视化展现了数据的主要结构，但丢失了大量细节。前 10 个 PC 解释约 58%，前 30 个 PC 解释约 85%。
- **主成分的含义**：PC1 通常对应图像的"整体亮度"或"笔划粗细"方向，PC2 可能对应"数字形状的弯曲程度"。PC 方向不一定有直观语义解释——它们是数据驱动的而非人定义的。
- **特征值衰减**：特征值从 ~0.6 指数衰减到 $10^{-4}$。衰减越快，降维越有效。
- **几何视角**：PCA 等价于用 $k$ 维超平面最小重构误差地拟合数据——投影距离平方和 = 被丢弃的特征值之和。

## 局限性

- **线性假设**：PCA 只能捕捉线性结构。环形或螺旋形数据需核 PCA 或 t-SNE
- **尺度敏感**：不同量纲特征需先标准化（除以标准差）→ 等价于对相关矩阵做 PCA
- **离群点**：少数离群点可大幅扭曲主成分方向 → 需鲁棒 PCA
- **可解释性**：主成分是原始特征的线性组合，常难以直观解释

## 关联知识库入口

- 概念：[特征值](../02-核心概念/特征值.md)
- 方法：[特征值方法与谱视角](../03-定理与方法/02-代数与数论/特征值方法与谱视角.md)
- 方法：[矩阵分解](../03-定理与方法/06-数值与计算/矩阵分解.md)
