---
title: 经典统计学习模型：SVM、树模型、集成学习、高斯过程与进化方法
layer: 03-model-families
tags:
  - machine-learning
prerequisites: []
see-also: []
status: stable
last-updated: 2026-05-08
---
# 经典统计学习模型：SVM、树模型、集成学习、高斯过程与进化方法

## 1. 这页的定位

这一页补的是“神经网络之外”的经典主线，尤其是：

- 支持向量机（support vector machine, SVM）；
- 决策树、随机森林、梯度提升树；
- 高斯过程（Gaussian process, GP）；
- 进化算法与群体优化。

## 2. SVM

SVM 的基本思想是最大间隔分类。在线性可分时，可写成：

$$
\min_{w,b} \frac{1}{2}\|w\|^2
\quad
\text{s.t. } y_i(w^\top x_i + b) \ge 1.
$$

加入软间隔后，目标变为

$$
\min_{w,b,\xi} \frac12\|w\|^2 + C\sum_i \xi_i.
$$

SVM 的根本思想不是“一个分类器”，而是：

- 用间隔控制复杂度；
- 用核方法处理非线性；
- 在小样本、中等维度下通常表现稳健。

## 3. 树模型与集成学习

决策树通过递归划分特征空间构造分段常数近似。其优点是可解释、能处理混合型特征；缺点是高方差。

因此，随机森林通过 bagging 降方差，梯度提升树通过逐步拟合残差降偏差。

## 4. 高斯过程

高斯过程从函数分布角度定义回归：

$$
f \sim \mathcal{GP}(m(x), k(x,x')).
$$

它的优势是：

- 预测时自带不确定性；
- 对小样本问题尤其有效；
- 核函数可编码先验结构。

## 5. 进化方法

进化算法、遗传算法、粒子群优化并不依赖梯度，适合：

- 黑盒优化；
- 离散结构搜索；
- 多峰非凸目标；
- 神经架构搜索与超参数搜索。

## 6. 与神经方法的关系

这些方法不是“旧算法”，而是现代 AI 的基线、对照组和组合部件：

- GBDT 在表格数据上长期强势；
- GP 在小样本与不确定性任务上仍重要；
- SVM 是理解核方法与间隔理论的关键；
- 进化方法在 NAS、机器人策略搜索、黑盒优化中仍活跃。

## 联读

- [经典学习算法：回归、分类、聚类、降维与贝叶斯学习](./classical-learning-algorithms-regression-classification-clustering-dimensionality-reduction-and-bayesian-learning.md)
- [机器学习模型族：核方法、树模型、集成学习与神经模型](./machine-learning-models-kernel-methods-tree-ensembles-and-neural-models.md)
- [搜索、优化与群体智能](../01-foundations/search-optimization-and-swarm-intelligence.md)

## 参考文献

[1] Cortes, C. & Vapnik, V. *Support-Vector Networks*. Machine Learning, 1995.
[2] Breiman, L. *Random Forests*. Machine Learning, 2001.
[3] Chen, T. & Guestrin, C. *XGBoost: A Scalable Tree Boosting System*. KDD, 2016.
